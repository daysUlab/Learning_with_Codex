# multiplicity・最頻状態・揺らぎ：Einstein solid

## energy quantumを数える

N個のoscillatorへq個のenergy quantumを分配するEinstein solidのmultiplicityはstars and barsから

$$
\Omega(N,q)=\binom{q+N-1}{q}
$$

です。二つのsolid A,Bがenergy quantumを交換し、total

$$
q=q_A+q_B
$$

固定なら

$$
\Omega_{\mathrm{tot}}(q_A)=\Omega_A(q_A)\Omega_B(q-q_A)
$$

が最大の分配が平衡です。

## なぜ平均が安定するか

独立な寄与をN個足すと典型的に平均はN、標準偏差は

$$
\sqrt N
$$

scaleなので相対揺らぎは

$$
\frac{\sigma}{\langle X\rangle}\sim\frac1{\sqrt N}
$$

です。

$$
N\sim10^{23}
$$

では巨視量が極めて安定します。microstateを知らなくても予測できる中心理由です。

## 演習と全解答

1.
   $$
   N=2,\ q=3
   $$
   のmultiplicityを求めよ。
   **解答**：
   $$
   \binom43=4
   $$
2.
   $$
   N=3,\ q=2
   $$
   はいくつか。
   **解答**：
   $$
   \binom42=6
   $$
3. total multiplicityを積にする理由は何か。
   **解答**：Aの各microstateとBの各microstateを独立に組み合わせるからです。
4. 平衡は必ず完全等分か。
   **解答**：同じ性質・同じNなら対称性から近いですが、異なる系ではtemperature一致が条件です。
5. Nを100倍にすると相対揺らぎはどうなるか。
   **解答**：10分の1です。
6. 小系で揺らぎを無視してよいか。
   **解答**：いいえ。nano・生体系では平均と同程度になり得ます。

## 限界・ナビゲーション

最頻状態の議論は確率が等しい条件を暗黙に使っています。次に孤立系ensembleとして明示します。

- 前：[小さな数え上げ](02_microstate_macrostate_small_counting.md)
- 次：[microcanonical](../part02_classical_ensembles/01_microcanonical_entropy_temperature.md)
- 親：[part01](README.md)
