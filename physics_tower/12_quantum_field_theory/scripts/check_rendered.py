"""生成HTML/PDFの機械的な検査。目視・実機検査の代替ではない。"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re
import subprocess
import xml.etree.ElementTree as ET
root = Path(__file__).resolve().parents[1]
book = root/"_book"
out = root/"_quality"
out.mkdir(exist_ok=True)
paths = re.findall(r"^\s*- (chapters/[^\s]+\.qmd)\s*$", (root/"_quarto.yml").read_text(), re.M)
pages = [book/"index.html", *(book/Path(p).with_suffix(".html") for p in paths), book/"glossary.html", book/"references.html"]

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "img" and a.get("src"):
            self.images.append(a["src"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])

def target(page, url):
    u = urlsplit(url)
    if u.scheme or u.netloc or u.path.startswith("/"):
        return None, ""
    return (page.parent/unquote(u.path)).resolve() if u.path else page.resolve(), unquote(u.fragment)

docs = {}
for page in pages:
    assert page.is_file() and page.stat().st_size > 0, f"missing HTML: {page}"
    doc = Document()
    doc.feed(page.read_text(encoding="utf-8"))
    docs[page.resolve()] = doc
errors, warnings = [], []
for page, doc in docs.items():
    for url in doc.images:
        t, _ = target(page, url)
        if t is not None and not t.is_file():
            errors.append(f"missing image: {page.name}: {url}")
    for url in doc.links:
        t, frag = target(page, url)
        if t is None:
            continue
        if t.suffix in (".html", ".pdf", ".qmd") and not t.is_file():
            errors.append(f"missing local link: {page.name}: {url}")
        if t in docs and frag and frag not in docs[t].ids:
            warnings.append(f"unresolved HTML anchor: {page.name}: {url}")
pdf = book/"qft.pdf"
assert pdf.is_file() and pdf.stat().st_size > 0
info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
(out/"pdfinfo.txt").write_text(info)
xml = subprocess.check_output(["pdftotext", "-bbox", str(pdf), "-"], text=True)
tree = ET.fromstring(xml)
def tag(e):
    return e.tag.split("}")[-1]
pdfpages = [e for e in tree.iter() if tag(e) == "page"]
assert pdfpages, "PDF has no pages"
assert len(pdfpages) >= 18, "unexpectedly short PDF"
blank = []
for i, page in enumerate(pdfpages, 1):
    width, height = float(page.get("width")), float(page.get("height"))
    words = [e for e in page.iter() if tag(e) == "word"]
    if not words:
        blank.append(i)
    for word in words:
        x0,y0,x1,y1 = (float(word.get(k)) for k in ("xMin","yMin","xMax","yMax"))
        if x0 < -2 or y0 < -2 or x1 > width+2 or y1 > height+2:
            warnings.append(f"PDF page {i}: text box beyond page bounds: {word.text!r}")
        if "\ufffd" in (word.text or ""):
            warnings.append(f"PDF page {i}: replacement character")
# Sample cover and evenly spaced pages; retain PNGs for later human inspection.
sample = sorted(set([1, 2, *[round(1+(len(pdfpages)-1)*j/12) for j in range(1,13)]]))
for i in sample:
    subprocess.run(["pdftoppm","-f",str(i),"-l",str(i),"-r","120","-png","-singlefile",str(pdf),str(out/f"pdf-page-{i:04d}")],check=True)
log = out/"render.log"
if log.exists():
    for line in log.read_text(errors="replace").splitlines():
        if re.search(r"Overfull \\[hv]box|Missing character:|undefined references",line):
            warnings.append(line[:500])
report = {"html_pages":len(docs),"image_references":sum(len(d.images) for d in docs.values()),"pdf_pages":len(pdfpages),"pdf_sample_pages":sample,"pdf_pages_without_extracted_words":blank,"errors":errors,"warnings":warnings}
(out/"render-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
assert not errors, "rendered local links or images broken"
