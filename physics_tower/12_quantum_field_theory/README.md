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

本書は序章（第0章）と5部18章構成。初期の学習範囲の参考元は references.qmd に明記する。公開済み教材から本文や図を転載しない。新版のPages公開後、旧版のActions実行17件と成果物の削除成功を確認した（run 46026432817）。一時削除ジョブは除去済み。古いPR・キャッシュ・第三者の保存物までは完全消去を保証しない。

## 全章の横断検査と表示診断

第0章の発見・学習ロードマップと用語・記号索引を参照してください。CIでは数式・図の参照、引用キー、章リンク、初読の到達目標を検査します。ビルド後に scripts/check_rendered.py でHTMLのローカル画像・リンク、PDFのページ数と抽出文字の座標を確認します。scripts/check_browser.py はChromeの幅390/820/1280pxで全ページの表示を診断します。Chromeとplaywrightが必要です。CI成果物 qft-quality にJSON、ビルドログ、サンプルPNGを保存します。ブラウザ診断の失敗は報告用でありビルドを止めません。PDFの抽出座標・警告やスクリーンショットは目視・Safari実機試験の代わりではありません。

## 制作手順の再利用

[教科書制作の進め方](../../TEXTBOOK_WORKFLOW.md) に、今回の設計・執筆・3章単位レビュー・横断点検・公開の手順をまとめています。詳細なレビュー記録は [REVIEW.md](REVIEW.md)、現在の状態は [PROGRESS.md](PROGRESS.md) を参照してください。


## 高校数学からの橋渡し（第1〜6章）

各節・小節の冒頭の「高校数学からの橋渡し」は、既習の計算と新しい考え方をつなぐ初読用の補足です。具体例、物理的入力・定義と導出結果の区別、初読では厳密な証明を保留できる事項を、必要に応じて記述します。本文の数式や演習の代替ではありません。HTML/PDFとも同じ原稿から生成し、節ごとの配置は scripts/check.py で検査します。

### 外部画像の扱い

はじめに・第0章の外部画像は `external_images.json` に出典・著作者・ライセンス・変更有無を記録し、各図注からも参照できます。画像は個別ライセンスのまま扱い、本書の独自部分のライセンスで上書きしません。Quartoのpre-renderで取得・形式検証を行います。取得できない場合はビルドを失敗させ、無断の代替画像を使用しません。
