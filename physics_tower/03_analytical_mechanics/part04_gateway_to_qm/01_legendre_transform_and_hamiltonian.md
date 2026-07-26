# Legendre変換とHamiltonian

## 問い

速度を独立変数から外し、座標と運動量で時間発展を書くにはどうするでしょうか。

凸な関数

$$
f(v)
$$

について傾き

$$
p=f'(v)
$$

を新変数とし

$$
g(p)=pv-f(v)
$$

とするのがLegendre変換です。力学では

$$
p_i=\frac{\partial L}{\partial\dot q_i},\qquad
H(q,p,t)=\sum_i p_i\dot q_i-L
$$

です。全微分を比べると

$$
dH=\sum_i\dot q_i\,dp_i-\sum_i\dot p_i\,dq_i-\frac{\partial L}{\partial t}dt
$$

からHamilton方程式

$$
\dot q_i=\frac{\partial H}{\partial p_i},\qquad
\dot p_i=-\frac{\partial H}{\partial q_i}
$$

を得ます。

## 例：調和振動子

$$
L=\frac12m\dot x^2-\frac12kx^2,\qquad p=m\dot x
$$

$$
H=\frac{p^2}{2m}+\frac12kx^2
$$

位相空間の軌道はenergy一定のellipseです。

## Hamiltonianとenergy

標準的な時間非依存の自然系では一致します。しかし速度依存potential、時間依存座標、特異Lagrangianでは単純な

$$
T+V
$$

と同一視できません。

## 演習と全解答

1. 自由粒子のHを求めよ。
   **解答**：
   $$
   H=\frac{p^2}{2m}
   $$
2. Hamilton方程式からNewton式を出せ。
   **解答**：
   $$
   \dot x=\frac pm,\quad\dot p=-V'(x)\Rightarrow m\ddot x=-V'(x)
   $$
3. Hが時間に陽に依存しないと何が言えるか。
   **解答**：軌道上でHが保存されます。
4. Legendre変換が失敗する条件は何か。
   **解答**：速度Hessianが特異で、速度を運動量から一意に戻せない場合です。
5. ばねのphase curveを書け。
   **解答**：
   $$
   \frac{p^2}{2mE}+\frac{kx^2}{2E}=1
   $$
6. 熱力学でも何を交換するか。
   **解答**：例えば
   $$
   U(S,V)
   $$
   から
   $$
   F(T,V)=U-TS
   $$
   へ自然変数を交換します。

## ナビゲーション

- 前：[Noether](../part03_variational/02_symmetry_cyclic_noether.md)
- 次：[phase space](02_phase_space_and_poisson_brackets.md)
- 親：[part04](README.md)
