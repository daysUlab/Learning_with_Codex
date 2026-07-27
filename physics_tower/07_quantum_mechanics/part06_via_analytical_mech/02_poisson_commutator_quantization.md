# Poisson括弧・commutator・正準量子化

## 形式的対応

古典の正準関係

$$
\{q_i,p_j\}=\delta_{ij}
$$

に対し、量子では

$$
[\hat q_i,\hat p_j]=i\hbar\delta_{ij}
$$

です。観測量の運動も

$$
\{A,H\}
\quad\longleftrightarrow\quad
\frac{1}{i\hbar}[\hat A,\hat H]
$$

と対応します。

自由粒子なら

$$
H=\frac{p^2}{2m}
\quad\to\quad
\hat H=-\frac{\hbar^2}{2m}\nabla^2
$$

となり、Schrödinger方程式を得ます。

## 単純置換では済まない

古典変数は可換なので

$$
qp=pq
$$

ですが、演算子は

$$
\hat q\hat p\neq\hat p\hat q
$$

です。例えば古典式

$$
qp
$$

に

$$
\frac12(\hat q\hat p+\hat p\hat q)
$$

を対応させるsymmetrizationは候補ですが、一般に一意ではありません。

さらに拘束系、特異Lagrangian、曲がったconfiguration space、gauge theoryではdomain・measure・constraint処理が必要です。Groenewold–van Hove obstructionにより、すべてのPoisson代数をcommutatorへ完全に保つ量子化は一般にできません。

## 荷電粒子

古典のcanonical momentum

$$
\mathbf p=m\mathbf v+q\mathbf A
$$

を受け、

$$
\hat H=\frac{1}{2m}(\hat{\mathbf p}-q\mathbf A)^2+q\phi
$$

とします。canonical momentumとmechanical momentumを区別します。

## 演習と全解答

1.
   $$
   [\hat x,\hat p^2]
   $$
   を使い自由粒子の
   $$
   d\hat x/dt
   $$
   を求めよ。
   **解答**：
   $$
   \frac{i}{\hbar}[H,x]=\frac{\hat p}{m}
   $$
2.
   $$
   [\hat p,V(\hat x)]
   $$
   を求めよ。
   **解答**：
   $$
   -i\hbar V'(\hat x)
   $$
3.
   $$
   qp
   $$
   のHermitian量子化候補を書け。
   **解答**：
   $$
   \frac12(\hat q\hat p+\hat p\hat q)
   $$
4. 正準量子化がrecipeであって普遍的導出でない理由を述べよ。
   **解答**：順序・domain・constraint・topologyにより複数の非同値な選択が生じ得るためです。
5. vector potentialがzeroでもmagnetic fieldが必ずzeroか。
   **解答**：はい、単連結な局所領域で
   $$
   \mathbf B=\nabla\times\mathbf A
   $$
   なので
   $$
   \mathbf A=0
   $$
   ならzeroです。逆はgaugeにより必ずしも成り立ちません。
6. 古典Poisson括弧の極限が期待されるscaleを述べよ。
   **解答**：observableとstateが
   $$
   \hbar
   $$
   scaleの細かな非可換構造を分解せず、actionが十分大きい領域です。

## ナビゲーション

- 前：[基底と表示](01_basis_matrices_and_pictures.md)
- 次：[作用と経路積分](03_action_path_integral_gauge.md)
- 古典正本：[荷電粒子とgauge](../../03_analytical_mechanics/part06_canonical_em/01_charged_particle_and_gauge.md)
