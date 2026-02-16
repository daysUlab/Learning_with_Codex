# logic_and_database_queries

このページは、命題論理・述語論理とデータベース問い合わせ（関係代数・SQL）の接点を、
初学者向けに整理するためのノートです。

「WHERE句は何をしているのか」を論理式として読めるようになると、
クエリのバグ（条件漏れ・否定ミス・NULL起因の誤判定）を大きく減らせます。

## この章で扱うこと
- 論理式と問い合わせ条件の対応
- 全称・存在量化と `EXISTS` / `NOT EXISTS` の直観
- 実務で誤りやすい「否定」と「NULL」の扱い

## まず押さえる対応表
- 連言（`A ∧ B`）: SQL の `A AND B`
- 選言（`A ∨ B`）: SQL の `A OR B`
- 否定（`¬A`）: SQL の `NOT A`
- 存在量化（`∃x P(x)`）: SQL の `EXISTS (subquery)`
- 全称量化（`∀x P(x)`）: SQL ではしばしば `NOT EXISTS (x s.t. NOT P(x))` で表す

## 例1: 存在量化（EXISTS）
「1件でも未提出課題がある学生」を探すとき、
論理としては `∃ assignment, not_submitted(student, assignment)` を見ています。

```sql
SELECT s.student_id
FROM students s
WHERE EXISTS (
  SELECT 1
  FROM assignments a
  LEFT JOIN submissions sub
    ON sub.student_id = s.student_id
   AND sub.assignment_id = a.assignment_id
  WHERE sub.submission_id IS NULL
);
```

## 例2: 全称量化（すべて提出済み）
「すべての課題を提出済み」は、
`∀ assignment, submitted(student, assignment)` です。
SQLでは直接 `FOR ALL` がないため、次の同値変形を使います。

- 全称: `∀x P(x)`
- 同値変形: `¬∃x ¬P(x)`

```sql
SELECT s.student_id
FROM students s
WHERE NOT EXISTS (
  SELECT 1
  FROM assignments a
  LEFT JOIN submissions sub
    ON sub.student_id = s.student_id
   AND sub.assignment_id = a.assignment_id
  WHERE sub.submission_id IS NULL
);
```

## つまずきやすい点
- `NOT IN` と `NULL` の組み合わせで、期待と異なる結果になりやすい。
- 否定条件は「何を否定しているか」を括弧レベルで確認する。
- 先に自然言語で「存在なのか、全称なのか」を決めてからSQL化する。

## 学習チェックリスト
- 日本語仕様を `∃` / `∀` を使って論理式に書ける。
- その論理式を `EXISTS` / `NOT EXISTS` ベースでSQLに落とせる。
- クエリ結果が意図とズレたとき、否定の位置とNULL評価を点検できる。

## ナビゲーション
- 親: [README.md](README.md)
- 兄弟:
  - [modal_logic_and_computation.md](modal_logic_and_computation.md)
  - [proof_assistants_and_logic.md](proof_assistants_and_logic.md)
