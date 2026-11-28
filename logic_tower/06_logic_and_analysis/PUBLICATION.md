# HTML・PDFの生成と共存公開計画

2026-11-28：場の量子論と同じQuarto方式を採用。論理学のビルドは既存の build_logic_book.yml で実施し、logic-book 成果物にHTMLとA5 PDFを保存する。第1〜2章はビルド成功。未執筆章は登録しない。

## 公開構成案（未実装）

| 内容 | 予定URL（https://daysulab.github.io/Learning_with_Codex/ 以下） |
|---|---|
| 場の量子論 | 既存のルートと qft.pdf を維持 |
| 数理論理学 | logic/ |
| 数理論理学PDF | logic/logic.pdf |

1. QFTと論理学を別々にビルド・検査する。
2. main用の共通公開workflowで両方の生成物を同一の原稿コミットから組み立てる。QFTの生成物をルート、論理学の生成物を logic/ に配置。
3. Pagesへのアップロード・deployは共通workflowだけが担当する。旧QFT単独deployを無効化して、片方の更新で他方が消えることを防ぐ。
4. QFTのルートURL・qft.pdf・章リンクを維持し、二冊の相互リンクを追加する。既存リリースを削除しない。
5. PDFは書籍別のタグ（qft-<SHA> / logic-<SHA>）でGitHub Releasesへ保存。未完成版はprereleaseとして明記する。
6. PRではビルドだけ行い、mainへの統合後に公開する。両書籍の画像・ローカルリンク・PDFの存在、スマートフォン幅、公開URLの応答を確認する。

現在は公開処理の競合を避けるため論理学のPages公開・Releaseを実行していない。共存公開を実装する際は既存QFTの公開CIとPages設定を再確認する。実機検査や全ページ目視は別工程。
