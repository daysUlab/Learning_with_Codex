"""章登録・数式ブロックの基本検査（TeX構文はPDFビルドで検査）。"""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
config = (root/"_quarto.yml").read_text()
paths = re.findall(r"^\s*- (chapters/[^\s]+\.qmd)\s*$", config, re.M)
assert len(paths) == 21 and len(set(paths)) == 21, paths
assert [int(Path(p).name[:2]) for p in paths] == list(range(1,22))
assert set(paths) == {str(p.relative_to(root)) for p in (root/"chapters").glob("*.qmd")}
for p in [root/"index.qmd", *(root/p for p in paths)]:
    s = p.read_text()
    assert s.startswith("# "), p
    assert len(re.findall(r"^\s*\$\$(?:\s+\{#eq-[^}]+\})?\s*$", s, re.M)) % 2 == 0, p
print("21 chapters: OK")

