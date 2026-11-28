"""公開する論理学書籍のローカルリンク・画像・生成PDFを検査する。"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
root=Path(__file__).resolve().parents[1]
book=root/"_book"
chapters=re.findall(r"^\s*- (chapters/\S+\.qmd)\s*$",(root/"_quarto.yml").read_text(),re.M)
pages=[book/"index.html",*(book/Path(p).with_suffix(".html") for p in chapters),book/"references.html"]
class Doc(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="img" and a.get("src"):
            self.urls.append(("image",a["src"]))
        if tag=="a" and a.get("href"):
            self.urls.append(("link",a["href"]))
errors=[]
for page in pages:
    assert page.is_file() and page.stat().st_size>0, page
    d=Doc()
    d.feed(page.read_text(encoding="utf-8"))
    for kind,url in d.urls:
        u=urlsplit(url)
        if u.scheme or u.netloc or not u.path or u.path.startswith("/"):
            continue
        target=page.parent/unquote(u.path)
        if kind=="image" or target.suffix in (".html",".pdf",".qmd"):
            if not target.is_file():
                errors.append(f"{page.name}: {url}")
pdf=book/"logic.pdf"
assert pdf.is_file() and pdf.stat().st_size>0
with pdf.open("rb") as f:
    assert f.read(5)==b"%PDF-"
assert not errors, errors
print(f"logic: {len(pages)} HTML pages, local links/images and PDF signature OK")
