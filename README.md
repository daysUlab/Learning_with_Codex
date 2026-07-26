# Learning with Codex 教科書プロジェクト

このリポジトリは、複数分野を横断する教科書プロジェクトです。
各タワーはスケルトンから始め、`PROGRESS.md` のキューに沿って本文・演習・図解を段階的に整備します。

`logic_tower` は本線と発展・応用68記事を本文化済みです。ほかのタワーの状態は各 `PROGRESS.md` を正本として確認します。

`physics_tower` の電磁気学章は、Maxwell方程式から回路、半導体デバイス、DRAM・NAND・HBM・GPU・SSD、AI計算基盤への入口まで本文化済みです。
解析力学・熱力学・統計力学も、Newton力学から巨視的状態量、微視的確率、量子統計へ進む一続きの本線として本文化済みです。

## トップレベル目次
- [logic_tower](logic_tower/README.md)
- [math_tower](math_tower/README.md)
- [physics_tower](physics_tower/README.md)
- [db_tower](db_tower/README.md)

## 進め方
- 基本は overview から読み始めます。
- 各章は基礎ノートを順に追加します。
- 演習や補足は `templates/` のテンプレートを利用します。
- 進捗管理は `*/PROGRESS.md` と `PROGRESS.md` を併用して確認します。
