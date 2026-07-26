# Lagrange未定乗数・robotics・数値simulation

## 拘束力を回収する

拘束

$$
f_a(q,t)=0
$$

を座標に組み込まない場合

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}
-\frac{\partial L}{\partial q_i}
=\sum_a\lambda_a\frac{\partial f_a}{\partial q_i}
$$

とします。未定乗数

$$
\lambda_a
$$

は拘束反力に対応します。

## robotics

multi-link機構は一般に

$$
M(q)\ddot q+C(q,\dot q)\dot q+g(q)=\tau
$$

と整理できます。mass matrix

$$
M
$$

はkinetic energy、gravity vector

$$
g
$$

はpotential、入力torque

$$
\tau
$$

は一般化力から得られます。部品ごとに力を描くより、linkが増えても組織的に導出できます。

## simulation

explicit Euler法は

$$
q_{n+1}=q_n+\Delta t\,\dot q_n,\qquad
p_{n+1}=p_n-\Delta t\,\partial_qH_n
$$

ですが、長時間でenergy driftしやすい。symplectic Eulerでは更新順序をずらし、phase-space構造を保ちやすくします。

## 演習と全解答

1. 円拘束を書け。
   **解答**：
   $$
   f=x^2+y^2-R^2=0
   $$
2. その拘束力の向きは何か。
   **解答**：
   $$
   \nabla f=(2x,2y)
   $$
   なので半径方向です。
3. mass matrixの次元を一様にkgと言えるか。
   **解答**：角座標を含むと成分の次元は座標の組に依存します。全体として
   $$
   \frac12\dot q^\mathsf{T}M\dot q
   $$
   がenergyです。
4. robot入力はforceだけか。
   **解答**：一般化座標が角度ならtorqueです。
5. Euler法で時間刻みを半分にする効果は何か。
   **解答**：局所誤差は減りますが構造非保存そのものは残ります。
6. 接触が切れる場合、等式拘束だけで十分か。
   **解答**：いいえ。非貫通の不等式、衝撃、摩擦、complementarityが必要です。

## 章の限界と次章

解析力学で多粒子の軌道は書けますが、

$$
10^{23}
$$

個を追うのは現実的でなく、不可逆な熱化も軌道一本からは見えにくい。次は[熱力学](../../04_thermodynamics/00_overview.md)で巨視的状態量へ圧縮します。

- 前：[荷電粒子](../part06_canonical_em/01_charged_particle_and_gauge.md)
- 親：[part07](README.md)

## 参考資料

Spong et al., *Robot Modeling and Control*.
