# 電磁場中の荷電粒子：canonical momentumとgauge

## 問い

Lorentz力

$$
m\ddot{\mathbf r}=q(\mathbf E+\dot{\mathbf r}\times\mathbf B)
$$

を、scalar potentialとvector potentialを使うLagrangianから再現します。

$$
\mathbf E=-\nabla\phi-\partial_t\mathbf A,\qquad
\mathbf B=\nabla\times\mathbf A
$$

に対して

$$
L=\frac12m\dot{\mathbf r}^2+q\dot{\mathbf r}\cdot\mathbf A-q\phi
$$

と置きます。Euler–Lagrange式を成分で展開するとLorentz力が得られます。

## 二つのmomentum

mechanical momentumは

$$
m\dot{\mathbf r}
$$

canonical momentumは

$$
\mathbf p=\frac{\partial L}{\partial\dot{\mathbf r}}
=m\dot{\mathbf r}+q\mathbf A
$$

です。Hamiltonianは

$$
H=\frac{(\mathbf p-q\mathbf A)^2}{2m}+q\phi
$$

です。

gauge変換

$$
\mathbf A\to\mathbf A+\nabla\chi,\qquad
\phi\to\phi-\partial_t\chi
$$

でLは

$$
q\frac{d\chi}{dt}
$$

だけ変わるため運動方程式は不変です。

## 演習と全解答

1. 磁場だけなら速さは変わるか。
   **解答**：
   $$
   q\mathbf v\cdot(\mathbf v\times\mathbf B)=0
   $$
   なので変わりません。
2. canonicalとmechanical momentumはいつ一致するか。
   **解答**：
   $$
   q\mathbf A=0
   $$
   と選べる場合です。
3. uniform磁場中のcyclotron角周波数を答えよ。
   **解答**：
   $$
   \omega_c=\frac{|q|B}{m}
   $$
4. gauge変換で場は変わるか。
   **解答**：curl gradientと混合偏微分の相殺により変わりません。
5. 電子の電荷を明記せよ。
   **解答**：
   $$
   q_e=-e
   $$
6. vector potentialは不要な冗長量か。
   **解答**：gauge冗長性はありますが、作用・canonical構造・量子phaseに自然に現れます。

## 比較と限界

Newton形式はLorentz力の軌道直観に強く、Lagrange形式はgauge・canonical momentum・量子への接続に強い。放射反作用や相対論的速度ではmodelを拡張します。

- 前：[場への拡張](../part05_infinite_dof/01_from_particles_to_fields.md)
- 関連：[電磁気学](../../02_electromagnetism/00_overview.md)
- 次：[拘束とrobotics](../part07_constraints/01_constraints_robotics_and_simulation.md)
