# 数式なしでわかる宇宙のロマン

前編は宇宙の成果を図表で味わい、後編は高校数学からそれを再現する二巻構成。前編26章、後編31章の暫定設計。

- [設計](DESIGN.md)
- [156テーマと全57章の目次](research/topics_catalog.md)
- [根拠台帳](research/evidence_registry.md)
- [進捗と次の作業](PROGRESS.md)
- [前編原稿](volume_1/index.qmd)
- [後編原稿](volume_2/index.qmd)

既存の[教科書制作手順](../../TEXTBOOK_WORKFLOW.md)に従う。Quartoと日本語LuaLaTeXがある環境で各巻のディレクトリから quarto render を実行する。前編の第1〜7章が初稿済み。公式観測画像の利用条件は[図版台帳](research/image_registry.md)に記載。ビルド前に Python 3 の取得スクリプトが公式画像をダウンロードするため、初回はインターネット接続が必要。第1〜6章のHTML/PDF共通ビルド成功（Actions run 46157728164）。全テーマの検証・目視レビューは未完了。

## 随時公開

mainへの統合時に共通Pagesワークフローで既存二冊と同時に公開する。初回デプロイ成功まで以下は予定URL。

- 前編HTML：https://daysulab.github.io/Learning_with_Codex/cosmic/
- 前編PDF：https://daysulab.github.io/Learning_with_Codex/cosmic/cosmic-romance.pdf
- 後編HTML：https://daysulab.github.io/Learning_with_Codex/cosmic-physics/
- 後編PDF：https://daysulab.github.io/Learning_with_Codex/cosmic-physics/cosmic-physics.pdf

PR時はビルド・組立のみ。Actionsの cosmic-romance-book / cosmic-physics-book から途中版を取得可能。既存QFT・論理学の公開先とRelease運用を変更しない。
