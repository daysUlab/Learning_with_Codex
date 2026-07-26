# 第2法則・entropy・Carnot機関

## なぜ第1法則だけでは足りないか

energy保存は、熱が低温から高温へ自発移動しない理由や、吸収した熱をcycleですべて仕事へ変えられない理由を示しません。第2法則が過程の向きを制約します。

可逆過程でentropy差を

$$
dS=\frac{\delta Q_{\mathrm{rev}}}{T}
$$

と定義します。孤立系では

$$
\Delta S\ge0
$$

です。

## Carnot cycle

高温熱浴

$$
T_h
$$

から

$$
Q_h
$$

を吸収し、低温熱浴

$$
T_c
$$

へ

$$
Q_c
$$

を捨てる可逆機関では

$$
\frac{Q_h}{T_h}=\frac{Q_c}{T_c}
$$

効率は

$$
\eta=\frac{W}{Q_h}=1-\frac{T_c}{T_h}
$$

です。作動物質によらない最大効率です。

## 数値例

$$
T_h=600\ \mathrm{K},\qquad T_c=300\ \mathrm{K}
$$

なら

$$
\eta_{\max}=0.50
$$

です。

## 演習と全解答

1. 一つの熱浴から熱を取り全て仕事にするcycleは可能か。
   **解答**：Kelvin–Planck表現に反し不可能です。
2. 可逆過程で宇宙全体のentropy変化はいくらか。
   **解答**：ゼロです。
3. 不可逆過程ではどうか。
   **解答**：正です。
4.
   $$
   T_h=500\ \mathrm{K},\ T_c=300\ \mathrm{K}
   $$
   の最大効率を求めよ。
   **解答**：
   $$
   \eta=1-\frac35=0.40
   $$
5. 冷蔵庫の仕事が必要な理由は何か。
   **解答**：低温から高温への熱移送を起こすためです。
6. entropyは「乱雑さ」だけで定義すべきか。
   **解答**：いいえ。熱力学では状態量と可逆熱から定義し、状態数との関係は統計力学で導きます。

## 限界・ナビゲーション

可逆processは無限にゆっくりな理想限界で、有限出力には不可逆性が伴います。

- 前：[状態方程式](03_equations_of_state_heat_capacity_enthalpy.md)
- 次：[不可逆性](../part02_phenomenology/01_reversible_irreversible_and_entropy_generation.md)
- 親：[part01](README.md)

## 参考資料

Carnot (1824); Clausius (1865).
