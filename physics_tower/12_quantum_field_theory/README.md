# 高校数学から学ぶ場の量子論

原稿の正本は `.qmd`。HTMLと日本語PDFを同じ原稿から生成する独立したQuarto Bookです。既存Markdown教材は移行しません。

## ビルド
Quarto 1.x、Python 3、Matplotlib、NumPy、LuaLaTeX（日本語対応のTeX Live等）、luatexja-fontspec、Noto Serif/Sans CJK JP が必要です。

```sh
cd physics_tower/12_quantum_field_theory
python3 -m pip install -r requirements.txt
python3 scripts/check.py
quarto render
quarto preview --to html
```

CIではUbuntu 24.04の texlive-luatex、texlive-lang-japanese、texlive-latex-extra、texlive-fonts-recommended、texlive-fonts-extra、texlive-science、texlive-lang-english と日本語フォントを導入します。

生成物は `_book/`。HTMLの入口は `index.html`、PDFは `qft.pdf`。生成物はコミットしません。

GitHub Pages の Settings → Pages → Source を GitHub Actions に設定すると、mainへの更新で公開できます。公開先候補: https://daysulab.github.io/Learning_with_Codex/ 。未設定ならActionsのビルド成果物から閲覧してください。

## 執筆規約

- 各章で動機、直感、数学準備、導出、数値例、図、演習と解答、次章への接続を揃える。
- 数式は独立した `$$` ブロックを基本とし、参照する式には `#eq-...` を付ける。
- 記号、単位、仮定、計量符号、自然単位系の導入を明記する。数値例は検算する。
- 図は再生成可能なコードまたはSVGを正本にする。HTMLの操作教材には静的図・説明を併設。
- 参考文献は出典と実際に参照した範囲を明記し、既存書籍の文章・図を転載しない。
- 章追加時は `_quarto.yml`、`PROGRESS.md`、`scripts/check.py` の整合を確認する。
- PRではHTML/PDFビルドを確認する。実機表示未確認の状態を完成扱いにしない。


## iPhone・iPadで読む

GitHub Pages公開後は Safari で https://daysulab.github.io/Learning_with_Codex/ を開きます。PDFの直接URLは https://daysulab.github.io/Learning_with_Codex/qft.pdf です。ZIP成果物はバックアップ・オフライン用に残します。公開はリポジトリの Pages 設定と deploy ジョブ成功を前提とします。

## 成果物の保存と版管理

- 最新版HTML: https://daysulab.github.io/Learning_with_Codex/
- 最新版PDF: https://daysulab.github.io/Learning_with_Codex/qft.pdf
- 過去版PDF: https://github.com/daysUlab/Learning_with_Codex/releases （mainの公開成功ごとに qft-コミット短縮SHA のプレリリースを作成）。
- Actionsの qft-book ZIP はHTMLのオフライン利用・一時バックアップ用。生成物は原稿ブランチにコミットしない。

## 独立した学習設計と公開管理

本書は5部18章構成。初期の学習範囲の参考元は references.qmd に明記する。公開済み教材から本文や図を転載しない。新版のPages公開後、旧版のActions実行17件と成果物の削除成功を確認した（run 46026432817）。一時削除ジョブは除去済み。古いPR・キャッシュ・第三者の保存物までは完全消去を保証しない。
