# 状態方程式・熱容量・enthalpy

## 状態方程式

理想気体では

$$
pV=Nk_BT=nRT
$$

です。これはenergy保存だけからは出ず、物質のconstitutive relationです。低密度・相互作用が弱い範囲で有効です。

## 熱容量

定積・定圧熱容量を

$$
C_V=\left(\frac{\partial U}{\partial T}\right)_V,\qquad
C_p=\left(\frac{\partial H}{\partial T}\right)_p
$$

と定義します。enthalpy

$$
H=U+pV
$$

はflow systemや定圧加熱で便利です。理想気体では

$$
C_p-C_V=nR
$$

です。

## 断熱変化

理想気体、可逆、一定熱容量なら

$$
pV^\gamma=\text{const.},\qquad
TV^{\gamma-1}=\text{const.}
$$

$$
\gamma=\frac{C_p}{C_V}
$$

です。急速圧縮でも断熱に近い場合がありますが、可逆とは限りません。

## 数値例

$$
n=1.0\ \mathrm{mol},\ T=300\ \mathrm{K},\ p=1.0\times10^5\ \mathrm{Pa}
$$

なら

$$
V=\frac{nRT}{p}=2.49\times10^{-2}\ \mathrm{m^3}
$$

です。

## 演習と全解答

1. 温度を一定にして体積を二倍にすると圧力はどうなるか。
   **解答**：理想気体では半分です。
2. enthalpyの単位は何か。
   **解答**：
   $$
   [pV]=\mathrm{Pa\,m^3}=\mathrm{J}
   $$
   なのでJです。
3. monatomic ideal gasのmolar
   $$
   C_V
   $$
   を古典結果で答えよ。
   **解答**：
   $$
   C_V=\frac32R
   $$
4.
   $$
   C_p
   $$
   が大きい理由を述べよ。
   **解答**：定圧加熱では内部energy増加に加え膨張仕事が必要です。
5. 断熱膨張で理想気体の温度はどうなるか。
   **解答**：
   $$
   TV^{\gamma-1}=\text{const.}
   $$
   より下がります。
6. 比熱の物質差を熱力学だけで予測できるか。
   **解答**：測定値として使えますが、微視的理由と値の計算は統計・量子が担当します。

## ナビゲーション

- 前：[第1法則](02_first_law_heat_and_work.md)
- 次：[第2法則](04_second_law_entropy_and_engines.md)
- 親：[part01](README.md)
