# canonical ensemble・Boltzmann因子・partition function

## 熱浴と接する小系

total energy一定の大きな熱浴Rと小系Sを考えます。Sがenergy

$$
E_i
$$

を持つ確率は、熱浴の状態数を一次展開して

$$
P_i\propto\Omega_R(E_{\mathrm{tot}}-E_i)
\propto e^{-E_i/(k_BT)}
$$

です。

$$
\beta=\frac1{k_BT}
$$

とし、正規化すると

$$
P_i=\frac{e^{-\beta E_i}}{Z},\qquad
Z=\sum_i e^{-\beta E_i}
$$

です。

## 熱力学量を取り出す

$$
F=-k_BT\ln Z
$$

$$
U=-\frac{\partial\ln Z}{\partial\beta}
$$

$$
\operatorname{Var}(E)=\frac{\partial^2\ln Z}{\partial\beta^2}
=k_BT^2C_V
$$

partition functionは状態を重み付けし、微分で平均と揺らぎを生成します。

## 二準位系

energy

$$
0,\varepsilon
$$

なら

$$
Z=1+e^{-\beta\varepsilon}
$$

$$
U=\frac{\varepsilon}{e^{\beta\varepsilon}+1}
$$

です。

## 演習と全解答

1. 高温で二状態の確率はどうなるか。
   **解答**：
   $$
   \beta\to0\Rightarrow P_0=P_1=\frac12
   $$
2. 低温でexcited state確率はどうなるか。
   **解答**：指数的にゼロへ近づきます。
3. 全energyへ定数Cを足すと確率は変わるか。
   **解答**：共通因子がZで相殺し変わりません。
4. 平均energyを定義から書け。
   **解答**：
   $$
   U=\sum_iP_iE_i
   $$
5. negative energyがあるとBoltzmann因子は不正か。
   **解答**：energy zeroは任意で、Zが有限なら問題ありません。
6. canonicalでenergyは固定か。
   **解答**：固定でなく揺らぎ、平均がUです。

## ナビゲーション

- 前：[microcanonical](01_microcanonical_entropy_temperature.md)
- 次：[grand canonical](03_grand_canonical_and_chemical_potential.md)
- 親：[part02](README.md)
