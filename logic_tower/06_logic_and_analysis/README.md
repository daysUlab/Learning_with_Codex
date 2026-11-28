# 高校数学から学ぶ数理論理学と超準解析

完全性からモデルを構成する数学へ進み、超実数・ブール値解析・強制法を具体例と証明で学ぶ独立Quarto書籍。既存Logic TowerのMarkdown教材は維持します。

- [全18章の設計](PLAN.md)
- [原稿の入口](index.qmd)
- [第1章](chapters/01_propositional_completeness.qmd)
- [第2章](chapters/02_boolean_algebras.qmd)
- [第3章](chapters/03_first_order.qmd)
- [第4章](chapters/04_model_existence.qmd)
- [第5章](chapters/05_sets_and_ordinals.qmd)
- [第6章](chapters/06_set_theories.qmd)
- [第7章](chapters/07_ultrafilters.qmd)
- [第8章](chapters/08_ultraproducts.qmd)
- [執筆進捗](PROGRESS.md)
- [レビュー記録](REVIEW.md)
- [制作手順](../../TEXTBOOK_WORKFLOW.md)

完成した章だけを _quarto.yml に登録し、未執筆スケルトンを公開物に混ぜません。日本語LuaLaTeXとMathJaxを使用。Pythonで図を生成し、代表例を検査します。

```sh
python3 -m pip install -r requirements.txt
python3 scripts/check.py
quarto render
```

GitHub Actionsは両書籍のHTML/PDFを生成・検査し、共通workflowで合体して公開する構成です。論理学の予定固定URLは https://daysulab.github.io/Learning_with_Codex/logic/ 、PDFは同配下の logic.pdf です。初回の共存公開はCI・main統合後に確認します。

HTML・PDFの共存公開案は [PUBLICATION.md](PUBLICATION.md) を参照してください。既存QFTのURLを維持する方針です。

初回公開成功（第1〜4章収録）：[HTML](https://daysulab.github.io/Learning_with_Codex/logic/)・[PDF](https://daysulab.github.io/Learning_with_Codex/logic/logic.pdf)。
