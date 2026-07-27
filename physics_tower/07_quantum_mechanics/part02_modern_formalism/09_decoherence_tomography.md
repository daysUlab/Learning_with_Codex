# decoherenceと状態tomography――見えないcoherenceをどう検証するか

## system–environment entanglement

systemの二経路stateとenvironmentが

$$
\frac{|0\rangle+|1\rangle}{\sqrt2}|e\rangle
\longrightarrow
\frac{|0\rangle|e_0\rangle+|1\rangle|e_1\rangle}{\sqrt2}
$$

とentangleしたとします。environmentを観測しないsystem stateは

$$
\rho_S=\frac12
\begin{pmatrix}
1&\langle e_1|e_0\rangle\\
\langle e_0|e_1\rangle&1
\end{pmatrix}.
$$

environment記録が区別可能になり

$$
\langle e_1|e_0\rangle\to0
$$

ならoff-diagonal成分が抑制されます。相互作用が特定basisの情報を安定にenvironmentへ複製すると、そのbasisがpreferred basisとして現れます。

## decoherenceが説明する範囲

decoherenceは、局所的な干渉が見えなくなりclassical mixtureのように振る舞う機構と、その時間scaleを説明します。全体系のunitary stateから単一結果を一意に選ぶことや、Born確率の解釈を、それだけで全立場に共通して解決するとは限りません。

## state tomography

状態は一回の測定で読み取れません。qubitなら

$$
\rho=\frac12(I+r_xX+r_yY+r_zZ)
$$

なので、同じ準備を多数回行い、x, y, z測定の平均

$$
r_i=\langle\sigma_i\rangle
$$

を推定します。有限標本では統計誤差があり、単純な線形反転が非正値matrixを返すこともあるため、maximum likelihoodやBayesian推定など物理制約付き再構成を使います。

## 演習と全解答

1. 上式で
   $$
   \langle e_1|e_0\rangle=1
   $$
   のpurityを求めよ。  
   **解答**：元の
   $$
   |+\rangle
   $$
   なのでpurityは1です。
2.
   $$
   \langle e_1|e_0\rangle=0
   $$
   のstateを求めよ。  
   **解答**：
   $$
   \rho_S=I/2
   $$
   でpurityは1/2です。
3. populationsがdecoherenceだけで必ず変わるか。  
   **解答**：pure dephasingでは対角成分は保たれ、off-diagonal成分だけが減衰します。energy relaxationは別channelです。
4. qubit tomographyにz測定だけでは足りない理由を述べよ。  
   **解答**：
   $$
   r_z
   $$
   しか得られず、
   $$
   r_x,r_y
   $$
   すなわちcoherenceが決まらないためです。
5.
   $$
   \langle X\rangle=0.6,\quad
   \langle Y\rangle=0,\quad
   \langle Z\rangle=0.8
   $$
   のdensity matrixを書け。  
   **解答**：
   $$
   \rho=\frac12
   \begin{pmatrix}
   1.8&0.6\\
   0.6&0.2
   \end{pmatrix}
   =
   \begin{pmatrix}
   0.9&0.3\\
   0.3&0.1
   \end{pmatrix}
   $$
   Bloch vector長は1なのでpureです。
6. 100回の二値測定と10000回では標準誤差が概ね何倍違うか。  
   **解答**：
   $$
   1/\sqrt N
   $$
   で減るため、10000回は100回の1/10です。

## 参考・ナビゲーション

- 参考：Schlosshauer, *Decoherence and the Quantum-to-Classical Transition*.
- 前：[合成系](08_composite_entanglement.md)
- 次：[波動関数への橋](10_to_wavefunction_schrodinger.md)
- 解釈：[標準形式側の解釈記事](../part11_standard_formalism/05_measurement_decoherence_interpretations.md)

