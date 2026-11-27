"""章登録・数式ブロックの基本検査（TeX構文はPDFビルドで検査）。"""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
config = (root/"_quarto.yml").read_text()
paths = re.findall(r"^\s*- (chapters/[^\s]+\.qmd)\s*$", config, re.M)
assert len(paths) == 18 and len(set(paths)) == 18, paths
assert [int(Path(p).name[:2]) for p in paths] == list(range(1,19))
assert set(paths) == {str(p.relative_to(root)) for p in (root/"chapters").glob("*.qmd")}
for p in [root/"index.qmd", *(root/p for p in paths)]:
    s = p.read_text()
    assert not re.search(r"^\$(?:[ \t]+\{#eq-[^}]+\})?[ \t]*$", s, re.M), f"single dollar delimiter: {p}"
    assert s.startswith("# "), p
    assert len(re.findall(r"^\s*\$\$(?:\s+\{#eq-[^}]+\})?\s*$", s, re.M)) % 2 == 0, p
# 図参照・ラベルの重複は全章で検査する。
figure_source = (root/"scripts/figures.py").read_text()
labels = set()
for p in [root/"index.qmd", *(root/p for p in paths)]:
    s = p.read_text()
    for label in re.findall(r"\{#((?:eq|fig)-[^}\s]+)\}", s):
        assert label not in labels, f"duplicate cross-reference label: {label} ({p})"
        labels.add(label)
    for name in re.findall(r"\]\(\.\./figures/([^)\s]+)\)", s):
        assert f'"{name}"' in figure_source or f"'{name}'" in figure_source, f"missing figure generator: {name} ({p})"
print("18 chapters: OK")
# レビュー済み範囲の数値検査
import runpy
runpy.run_path(str(root/"scripts/check_review_01_03.py"), run_name="__main__")

