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
# 全章の冒頭に学習目的を明記する。内容の教育的妥当性は本文レビューで確認する。
for path in paths:
    s = (root/path).read_text()
    assert re.match(r'^# [^\n]+\n\n::: \{\.callout-note title="この章で学ぶ理由"\}\n[^\n]+\n:::\n', s), f"missing chapter purpose: {path}"
    assert "## 初読の到達目標" in s, f"missing first-read goal: {path}"
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
# 章間参照・引用・付録リンクの存在を確認する。
sources = [root/"index.qmd", *(root/p for p in paths), root/"glossary.qmd", root/"references.qmd"]
bib_keys = set(re.findall(r"@\w+\{([^,]+),", (root/"references.bib").read_text()))
for p in sources:
    s = p.read_text()
    for ref in re.findall(r"@((?:eq|fig)-[\w-]+)", s):
        assert ref in labels, f"unresolved cross-reference {ref}: {p}"
    for target in re.findall(r"\]\(([^)\s]+\.qmd)(?:#[^)]*)?\)", s):
        assert (p.parent/target).is_file(), f"missing qmd link {target}: {p}"
    for cite in re.findall(r"\[@([\w-]+)", s):
        assert cite in bib_keys, f"missing bibliography key {cite}: {p}"
    for chapter in re.findall(r"第(\d+)章", s):
        assert 1 <= int(chapter) <= 18, f"invalid chapter number: {p}"
print("18 chapters, chapter goals, cross-references, glossary and source links: OK")
# レビュー済み範囲の数値検査
import runpy
for test_path in sorted((root/"scripts").glob("check_review_*.py")):
    runpy.run_path(str(test_path), run_name="__main__")

