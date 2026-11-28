# HTML・PDFの生成と共存公開計画

2026-11-28：場の量子論と同じQuarto方式を採用。論理学のビルドは既存の build_logic_book.yml で実施し、logic-book 成果物にHTMLとA5 PDFを保存する。第1〜2章はビルド成功。未執筆章は登録しない。

## 共存公開構成（初回公開成功）

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

2026-11-28：build_qft_book.yml を共通ビルド・公開workflowに変更。build_logic_book.yml は再利用workflowと手動ビルドに限定。両書籍の生成物を assemble で合体し、mainのみ公開・版マーカーの確認・書籍別Releaseを実行する。旧QFT単独公開は同じworkflow内で置き換えた。PRでは組立まで検査し公開しない。論理学のローカルリンク・画像・PDF署名の検査を追加。QFTも同じコミットから再ビルドするため、論理学だけの更新でもQFTの新しい版タグを作る方式とした。初回CI・マージ・公開成功は未確認。実機検査や全ページ目視は別工程。

2026-11-28 13:46 JST：main run 46108611606のbuild/logic/assemble/deploy/release全成功。第1〜4章収録の [HTML](https://daysulab.github.io/Learning_with_Codex/logic/) と [PDF Release](https://github.com/daysUlab/Learning_with_Codex/releases/tag/logic-c4b43bd76a44) を確認。既存QFTも同時公開成功。第5章以降は最新CI成功後に公開。
