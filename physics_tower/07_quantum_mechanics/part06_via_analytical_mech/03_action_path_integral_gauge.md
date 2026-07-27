# 作用・経路積分・gauge――一つの古典経路から全経路へ

## 停留作用の再登場

古典力学では

$$
S[q]=\int L(q,\dot q,t)\,dt
$$

が停留する経路を選びました。量子のpath integralでは、始点から終点へのamplitudeを概念的に

$$
K(q_f,t_f;q_i,t_i)
=\int\mathcal Dq\ e^{iS[q]/\hbar}
$$

と表します。

各経路を古典確率で足すのではなく、複素phaseを足します。

$$
S\gg\hbar
$$

では停留経路近傍以外のphaseが激しくcancelし、stationary phaseとして古典軌道が残ります。これは古典極限の一つの見方です。

## 二重slitとの接続

経路を二群に粗視化すれば

$$
K=K_1+K_2
$$

で、Born則

$$
P=|K|^2
$$

から干渉項が出ます。

## gaugeとphase

電磁potentialのgauge変換

$$
\mathbf A'=\mathbf A+\nabla\chi,\qquad
\phi'=\phi-\frac{\partial\chi}{\partial t}
$$

に対して波動関数は

$$
\psi'=\exp\left(\frac{iq\chi}{\hbar}\right)\psi
$$

と変換します。観測確率は不変です。Aharonov–Bohm効果は、場がzeroの経路領域でも囲んだmagnetic fluxがrelative phaseへ影響し得ることを示します。

## 適用限界

path integralのmeasureは有限次元積分ほど自明ではありません。場の量子論・gauge固定・renormalizationは[素粒子](../../08_elementary_particle/00_overview.md)へ保留します。

## 演習と全解答

1. path weightの指数が無次元であることを確認せよ。
   **解答**：
   $$
   [S]=[\hbar]=\mathrm{J\,s}
   $$
   です。
2. action差
   $$
   \Delta S=2\pi\hbar
   $$
   の二経路のrelative phaseを求めよ。
   **解答**：
   $$
   e^{i\Delta S/\hbar}=e^{i2\pi}=1
   $$
3.
   $$
   \Delta S=\pi\hbar
   $$
   なら等振幅二経路はどうなるか。
   **解答**：relative phaseが
   $$
   -1
   $$
   で完全なcancelが可能です。
4. classical limitで一経路だけが「存在する」と直ちに言えるか。
   **解答**：path integralでは全経路を含みますが、粗いobservableでは非停留phaseがcancelし、古典経路近傍が支配します。
5. gauge変換で
   $$
   |\psi|^2
   $$
   が不変なことを示せ。
   **解答**：掛かる因子の絶対値が1だからです。
6. Aharonov–Bohm効果が「potentialは一意」と意味しない理由を述べよ。
   **解答**：gauge関連なpotentialは同じ物理を表し、observableは閉路phaseまたはfluxというgauge不変量です。

## ナビゲーション

- 前：[正準量子化](02_poisson_commutator_quantization.md)
- 次：[角運動量](../part03_angular_momentum_spin/README.md)
- 古典正本：[停留作用](../../03_analytical_mechanics/part03_variational/01_stationary_action.md)
