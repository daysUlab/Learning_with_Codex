"""原稿構造と第1章の代表的な意味論の検算（形式証明の機械検証ではない）。"""
from pathlib import Path
from itertools import product
import re
root=Path(__file__).resolve().parents[1]
paths=re.findall(r"^\s*- (chapters/\S+\.qmd)\s*$",(root/"_quarto.yml").read_text(),re.M)
assert paths
for i,p in enumerate(paths,1):
    assert Path(p).name.startswith(f"{i:02d}_")
    s=(root/p).read_text()
    assert "未執筆スケルトン" not in s
    for title in ["この章で学ぶ理由","## 初読の到達目標","## 演習","## 解答"]:
        assert title in s,(p,title)
    assert len(re.findall(r"^\$\$\s*$",s,re.M))%2==0
    for name in re.findall(r"\]\(\.\./figures/([^)]*)\)",s):
        assert name in (root/"scripts/figures.py").read_text(),name
imp=lambda p,q:max(1-p,q)
rows=list(product([0,1],repeat=2))
assert [imp(p,q) for p,q in rows]==[1,1,0,1]
assert [imp(p,min(p,q)) for p,q in rows]==[1,1,0,1]
assert all(not(imp(p,q) and p) or q for p,q in rows)
assert any(imp(p,q) and q and not p for p,q in rows)
assert all(1-min(p,q)==max(1-p,1-q) for p,q in rows)
assert all(imp(min(p,q),p) for p,q in rows)
assert all(not(max(p,q) and not p) or q for p,q in rows)
assert 2**3-1==7
print(f"{len(paths)} published chapter(s); introductory truth-table checks OK")
