"""生成PDFの全ページ境界検査と代表ページの画像出力。
機械的な候補抽出であり、文字の重なり・改ページの妥当性の目視判定とは別。
"""
from pathlib import Path
import json
import re
import fitz

root=Path(__file__).resolve().parents[1]
out=root/"_quality"
out.mkdir(exist_ok=True)
doc=fitz.open(root/"_book/logic.pdf")
pages=[]
for i,page in enumerate(doc):
    rect=page.rect
    outside=[]
    chars=0
    replacement=0
    # 物理ページ境界を越える文字・画像を候補とする。
    # 柱、ノンブル、意図的な装飾は本文余白違反とは限らない。
    for block in page.get_text("dict",flags=fitz.TEXTFLAGS_DICT)["blocks"]:
        if block["type"]==1:
            items=[("image",block["bbox"],"")]
        else:
            items=[("text",s["bbox"],s["text"]) for line in block.get("lines",[]) for s in line["spans"]]
        for kind,box,txt in items:
            chars+=len(txt)
            replacement+=txt.count("\ufffd")
            if box[0]<rect.x0-2 or box[1]<rect.y0-2 or box[2]>rect.x1+2 or box[3]>rect.y1+2:
                outside.append({"kind":kind,"box":[round(x,1) for x in box],"text":txt[:100]})
    pages.append({"page":i+1,"size_pt":[round(rect.width,1),round(rect.height,1)],"chars":chars,"replacement_chars":replacement,"outside":outside})
# 目次・部扉・各章先頭、補章・索引をブックマークから抽出。
toc=doc.get_toc()
selected=set(range(min(6,len(doc))))
selected.update(row[2]-1 for row in toc if row[0]<=2 and 1<=row[2]<=len(doc))
selected.add(len(doc)-1)
for i in sorted(selected):
    doc[i].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out/f"pdf-{i+1:04d}.png")
log=(out/"render.log").read_text(errors="replace") if (out/"render.log").exists() else ""
warnings=[line.strip() for line in log.splitlines() if re.search(r"Overfull \\[hv]box|Missing character:",line)]
report={"page_count":len(doc),"bookmarks":toc,"sample_pages":[i+1 for i in sorted(selected)],"pages":pages,"tex_warnings":warnings}
(out/"pdf-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(f"PDF pages={len(doc)}, sampled={len(selected)}, outside_pages={sum(bool(p['outside']) for p in pages)}, replacement_chars={sum(p['replacement_chars'] for p in pages)}, TeX warnings={len(warnings)}")
