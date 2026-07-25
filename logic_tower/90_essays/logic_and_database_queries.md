# logic_and_database_queries

SQLの問い合わせは、単なる文字列操作ではありません。各行や行の組が条件を満たすかを判定する、論理式の評価として読めます。

この見方を身につけると、`AND` と `OR` の括弧、`EXISTS`、全称条件、NULLによる想定外の結果を、暗記ではなく論理から説明できます。

---

## 1. このページの到達目標

- WHERE句を命題論理・述語論理の式として読める。
- `EXISTS` と存在量化の対応を説明できる。
- 全称条件を反例の不存在としてSQLへ翻訳できる。
- SQLのNULLと3値論理を説明できる。
- 重複や空集合など、論理とSQLの差を点検できる。

---

## 2. 問い合わせを集合として考える

テーブルの各行を対象 $x$ とし、条件を満たすことを述語 $P(x)$ とします。

```sql
SELECT *
FROM employees
WHERE department = 'Data';
```

は、直観的には

$$
\{x\mid \mathrm{Employee}(x)\land
\mathrm{Department}(x)=\mathrm{Data}\}
$$

という集合を求めています。

SQLは重複を持つバッグ意味論を標準とするなど、純粋な集合論とは違いますが、検索条件の設計にはこの見方が有効です。

---

## 3. 論理式からSQLへの流れ

次の図は、日本語の要求をSQLへ変換する手順です。読み取るポイントは、いきなり構文を書くのではなく、対象・量化・否定を論理式で確定してから実装することです。

```mermaid
flowchart LR
    A["日本語の要求"] --> B["対象と述語"]
    B --> C["量化と否定"]
    C --> D["EXISTSなどへ翻訳"]
    D --> E["NULLと重複を確認"]
```

---

## 4. AND・OR・NOT

基本対応は次のとおりです。

| 論理 | SQL |
|---|---|
| $P\land Q$ | `P AND Q` |
| $P\lor Q$ | `P OR Q` |
| $\lnot P$ | `NOT P` |

たとえば「データ部門に所属し、かつ有効な社員」は

$$
\mathrm{Data}(x)\land\mathrm{Active}(x)
$$

です。

```sql
WHERE department = 'Data'
  AND status = 'active'
```

`AND` は `OR` より優先されますが、仕様のまとまりを明確にするため、混在時は括弧を付けます。

```sql
WHERE status = 'active'
  AND (department = 'Data' OR department = 'AI')
```

---

## 5. EXISTSは存在量化

「少なくとも1件の未払い請求がある顧客」を考えます。

$$
\exists i\,
(\mathrm{InvoiceOf}(i,c)\land\mathrm{Unpaid}(i))
$$

SQLでは相関サブクエリを使えます。

```sql
SELECT c.customer_id
FROM customers AS c
WHERE EXISTS (
  SELECT 1
  FROM invoices AS i
  WHERE i.customer_id = c.customer_id
    AND i.status = 'unpaid'
);
```

`EXISTS` が見るのは、サブクエリが1行以上返すかです。`SELECT 1` の1という値そのものは判定に使われません。

---

## 6. 全称量化は反例が存在しないこと

SQLには通常 `FOR ALL` がありません。「顧客の請求がすべて支払済み」を直接書く代わりに、

$$
\forall i\,
(\mathrm{InvoiceOf}(i,c)\to\mathrm{Paid}(i))
$$

を

$$
\lnot\exists i\,
(\mathrm{InvoiceOf}(i,c)\land\lnot\mathrm{Paid}(i))
$$

へ変形します。

```sql
SELECT c.customer_id
FROM customers AS c
WHERE NOT EXISTS (
  SELECT 1
  FROM invoices AS i
  WHERE i.customer_id = c.customer_id
    AND (i.status <> 'paid' OR i.status IS NULL)
);
```

考え方は「すべて成功した顧客を探す」ではなく、「失敗した反例を1件も持たない顧客を探す」です。

---

## 7. 空集合と空虚真

請求が1件もない顧客について、上の `NOT EXISTS` はTRUEになります。未払いの反例が存在しないからです。

論理学でも、対象が空なら

$$
\forall x\in\varnothing\,P(x)
$$

は真です。これを空虚真と呼びます。

業務要件が「請求が1件以上あり、かつすべて支払済み」なら、存在条件を追加します。

```sql
WHERE EXISTS (
  SELECT 1
  FROM invoices AS i
  WHERE i.customer_id = c.customer_id
)
AND NOT EXISTS (
  SELECT 1
  FROM invoices AS i
  WHERE i.customer_id = c.customer_id
    AND (i.status <> 'paid' OR i.status IS NULL)
)
```

---

## 8. NULLと3値論理

標準SQLの条件評価には

$$
\mathrm{TRUE},\quad\mathrm{FALSE},\quad\mathrm{UNKNOWN}
$$

があります。

NULLは未知または欠損を表すマーカーであり、通常の値ではありません。

```sql
salary = NULL
```

ではなく

```sql
salary IS NULL
```

を使います。

`salary > 500000` は、salaryがNULLならUNKNOWNです。WHERE句に残るのはTRUEの行だけなので、FALSEとUNKNOWNの行はともに除外されます。

### NOTを付けても戻らない

$$
\lnot\mathrm{UNKNOWN}
=
\mathrm{UNKNOWN}
$$

したがって

```sql
WHERE NOT (salary > 500000)
```

にもNULLの行は含まれません。含めたいなら明示します。

```sql
WHERE salary <= 500000
   OR salary IS NULL
```

---

## 9. NOT INの落とし穴

次の条件を考えます。

```sql
WHERE customer_id NOT IN (
  SELECT customer_id
  FROM blocked_customers
)
```

サブクエリ結果にNULLが1つでもあると、多くの比較がUNKNOWNになり、期待した行が返らない場合があります。

存在しないことを表したいなら、NULLの扱いを確認したうえで `NOT EXISTS` を使う方が意図を明確にしやすいです。

```sql
WHERE NOT EXISTS (
  SELECT 1
  FROM blocked_customers AS b
  WHERE b.customer_id = c.customer_id
)
```

---

## 10. JOINと存在

INNER JOINは、結合条件を満たす行の組を作ります。

$$
\{(x,y)\mid R(x)\land S(y)\land J(x,y)\}
$$

一方、「関連行が存在するか」だけが必要なら、JOINによって行数を増やすより `EXISTS` の方が要求を直接表します。

顧客に請求が3件あればJOINは顧客を3行へ増やす可能性があります。`DISTINCT` で消す前に、求めたいものが「行の組」か「存在判定」かを確認します。

---

## 11. 例題：全商品を購入した顧客

「商品マスタにあるすべての商品を購入した顧客」を考えます。

$$
\forall p\,
(\mathrm{Product}(p)\to\mathrm{Purchased}(c,p))
$$

反例の不存在へ変形すると、

$$
\lnot\exists p\,
(\mathrm{Product}(p)\land\lnot\mathrm{Purchased}(c,p))
$$

です。

```sql
SELECT c.customer_id
FROM customers AS c
WHERE NOT EXISTS (
  SELECT 1
  FROM products AS p
  WHERE NOT EXISTS (
    SELECT 1
    FROM purchases AS x
    WHERE x.customer_id = c.customer_id
      AND x.product_id = p.product_id
  )
);
```

外側の `NOT EXISTS` は「未購入の商品がない」、内側は「その商品の購入記録がない」を表します。

---

## 12. つまずきやすい点

### つまずき1：NULLを1つの値だと思う

NULLとの通常比較はUNKNOWNになります。`IS NULL` を使います。

### つまずき2：全称条件に1つのEXISTSを使う

全称は通常、「反例が存在しない」という `NOT EXISTS` へ変換します。

### つまずき3：空集合を忘れる

`NOT EXISTS` による全称条件は、対象が0件でも成立します。業務要件と一致するか確認します。

### つまずき4：JOIN後の重複を論理の重複と混同する

SQLは標準ではバッグ意味論です。射影しても重複が自動で消えるとは限りません。

### つまずき5：DB製品差を無視する

NULL、型変換、照合順序、最適化などの詳細は製品で異なります。実行環境の仕様も確認します。

---

## 13. 演習問題

### 問1

「有効で、東京または大阪に住む顧客」を論理式とWHERE条件で表しなさい。

### 問2

「少なくとも1回購入した顧客」を `EXISTS` で表しなさい。

### 問3

「すべての課題を提出した学生」を、反例の不存在として日本語で言い換えなさい。

### 問4

`NOT (x = 10)` で $x$ がNULLの場合、評価結果を答えなさい。

### 問5

請求が0件の顧客が「すべて支払済み」に含まれる理由を説明しなさい。

### 問6

存在だけを確認したい場合、JOINより `EXISTS` が意図を表しやすい理由を説明しなさい。

---

## 14. 演習問題の解答

### 解答1

$$
\mathrm{Active}(x)\land
(\mathrm{Tokyo}(x)\lor\mathrm{Osaka}(x))
$$

```sql
WHERE status = 'active'
  AND (city = 'Tokyo' OR city = 'Osaka')
```

### 解答2

```sql
WHERE EXISTS (
  SELECT 1
  FROM purchases AS p
  WHERE p.customer_id = c.customer_id
)
```

### 解答3

「未提出の課題が1件も存在しない学生」です。

### 解答4

UNKNOWNです。`x = 10` がUNKNOWNであり、その否定もUNKNOWNです。

### 解答5

未払い請求という反例が1件も存在しないためです。これは空虚真に対応します。

### 解答6

JOINは関連行の数だけ元の行を増やし得ます。`EXISTS` は関連行が1件以上あるかだけを直接判定します。

---

## 学習チェック（自己確認）

- WHERE句を論理式へ戻せる。
- 存在と全称を `EXISTS` / `NOT EXISTS` で表せる。
- 空虚真が業務要件に合うか確認できる。
- TRUE・FALSE・UNKNOWNを区別できる。
- JOIN、重複、存在判定を区別できる。

---

## ナビゲーション

- 親: [README.md](README.md)
- 前: [README.md](README.md)
- 次: [modal_logic_and_computation.md](modal_logic_and_computation.md)
