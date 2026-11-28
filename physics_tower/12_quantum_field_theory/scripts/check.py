"""章登録・数式ブロックの基本検査（TeX構文はPDFビルドで検査）。"""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
config = (root/"_quarto.yml").read_text()
paths = re.findall(r"^\s*- (chapters/[^\s]+\.qmd)\s*$", config, re.M)
assert len(paths) == 19 and len(set(paths)) == 19, paths
assert [int(Path(p).name[:2]) for p in paths] == list(range(0,19))
assert set(paths) == {str(p.relative_to(root)) for p in (root/"chapters").glob("*.qmd")}
for p in [root/"index.qmd", *(root/p for p in paths)]:
    s = p.read_text()
    assert not re.search(r"^\$(?:[ \t]+\{#eq-[^}]+\})?[ \t]*$", s, re.M), f"single dollar delimiter: {p}"
    assert not re.search(r"\\(?:rm|bf|it|tt|sf|sl|sc)\b", s), f"obsolete TeX font command: {p}"
    assert s.startswith("# "), p
    assert len(re.findall(r"^\s*\$\$(?:\s+\{#eq-[^}]+\})?\s*$", s, re.M)) % 2 == 0, p
assert paths[0] == "chapters/00_physical_discoveries.qmd"
assert (root/paths[0]).read_text().splitlines()[0].endswith("{.unnumbered}"), "chapter zero must not consume a chapter number"
assert all("{.unnumbered}" not in (root/path).read_text().splitlines()[0] for path in paths[1:])
assert config.index("    - index.qmd") < config.index("    - chapters/00_physical_discoveries.qmd") < config.index("    - part:")
# 全章の冒頭に学習目的を明記する。内容の教育的妥当性は本文レビューで確認する。
for path in paths:
    s = (root/path).read_text()
    assert re.match(r'^# [^\n]+\n\n::: \{\.callout-note title="この章で学ぶ理由"\}\n[^\n]+\n:::\n', s), f"missing chapter purpose: {path}"
    assert "## 初読の到達目標" in s, f"missing first-read goal: {path}"
    # callout の開始・終了が独立した行にあることを確認。
    depth = 0
    for line in s.splitlines():
        if line.startswith("::: {"):
            depth += 1
        elif line.strip() == ":::":
            depth -= 1
            assert depth >= 0, f"unmatched callout end: {path}"
        elif ":::" in line:
            raise AssertionError(f"malformed callout: {path}: {line}")
    assert depth == 0, f"unclosed callout: {path}"
# 図参照・ラベルの重複は全章で検査する。
figure_source = (root/"scripts/figures.py").read_text()
labels = set()
for p in [root/"index.qmd", *(root/p for p in paths)]:
    s = p.read_text()
    for label in re.findall(r"\{#((?:eq|fig)-[^}\s]+)\}", s):
        assert label not in labels, f"duplicate cross-reference label: {label} ({p})"
        labels.add(label)
    for name in re.findall(r"\]\(\.\./figures/([^)\s]+)\)", s):
        if not name.startswith("external/"):
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
        assert 0 <= int(chapter) <= 18, f"invalid chapter number: {p}"
print("chapter 0 and 18 numbered chapters, chapter goals, cross-references, glossary and source links: OK")
# レビュー済み範囲の数値検査
import runpy
for test_path in sorted((root/"scripts").glob("check_review_*.py")):
    runpy.run_path(str(test_path), run_name="__main__")


# 第1〜6章：各節・小節の直後に初読者向けの橋渡しを置く。
for path in paths[1:7]:
    s = (root/path).read_text()
    headings = re.findall(r"^#{2,3} .+$", s, re.M)
    bridges = re.findall(r'^#{2,3} .+\n\n::: \{\.callout-tip title="高校数学からの橋渡し"\}\n[^\n]+\n:::$', s, re.M)
    assert len(headings) == len(bridges), f"missing section bridge: {path} ({len(bridges)}/{len(headings)})"
print("chapter 1–6 section bridges: OK")

# 外部画像は個別の出典・ライセンスを持つものだけを許可する。
import json
assets = json.loads((root/"external_images.json").read_text())["assets"]
assert len({a["file"] for a in assets}) == len(assets)
assert all(a["license"] in {"CC BY 4.0", "CC BY-SA 4.0", "CC BY-SA 3.0"} for a in assets)
for asset in assets:
    source = (root/asset["placement"]).read_text()
    assert source.count("figures/external/"+asset["file"]) == 1, asset
    assert all(value in source for value in (asset["source"], asset["author"], asset["license_url"], asset["change"])), asset
for p in sources:
    for name in re.findall(r"figures/external/([^\s)]+)", p.read_text()):
        assert name in {a["file"] for a in assets}, (p, name)
print("external images: attribution, license, placement OK")
