# 合成系・partial trace・entanglement

## 合成系

system

$$
A,\ B
$$

のHilbert空間を

$$
\mathcal H_A,\quad\mathcal H_B
$$

とすると、標準量子論では合成系を

$$
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B
$$

で表します。product stateは

$$
\rho_{AB}=\rho_A\otimes\rho_B
$$

です。確率

$$
p_i
$$

でproduct stateを混ぜた

$$
\rho_{AB}=\sum_ip_i\rho_A^{(i)}\otimes\rho_B^{(i)}
$$

はseparableで、classical correlationを持ち得ます。

## entangled state

pure state

$$
|\Psi\rangle_{AB}
$$

が

$$
|\psi\rangle_A\otimes|\phi\rangle_B
$$

へ因数分解できなければentangledです。代表例は

$$
|\Phi^+\rangle
=\frac{|00\rangle+|11\rangle}{\sqrt2}.
$$

全体density operatorからAのlocal stateを得るpartial traceは

$$
\rho_A=\operatorname{Tr}_B\rho_{AB}.
$$

Bell stateでは

$$
\rho_A=\rho_B=\frac12I
$$

です。全体はpureでも部分系はmixedになります。

## local measurementとcorrelation

A側effect

$$
E_a
$$

とB側effect

$$
F_b
$$

の同時確率は

$$
p(a,b)=\operatorname{Tr}[
\rho_{AB}(E_a\otimes F_b)]
$$

です。entanglementは強い相関を生みますが、それだけで超光速通信はできません。相手がどの測定を選んでも、結果を伝えない限り自分のreduced stateは変わらないno-signallingを満たします。

## tensor product再構成の注意

独立に操作できる部分系とlocal measurementの組合せからtensor productを理解できますが、これは標準量子論の構造を説明する再構成です。一般確率論では合成則は一意でなく、物理的入力が必要です。

## 演習と全解答

1.
   $$
   |0\rangle\otimes|1\rangle
   $$
   を計算basisで書け。  
   **解答**：
   $$
   |01\rangle=(0,1,0,0)^\mathsf T
   $$
2.
   $$
   |\Phi^+\rangle
   $$
   がproduct stateでない理由を述べよ。  
   **解答**：係数行列
   $$
   \operatorname{diag}(1/\sqrt2,1/\sqrt2)
   $$
   のrankが2で、rank-oneの外積へ分解できません。
3. Bell stateのA側reduced stateを計算せよ。  
   **解答**：
   $$
   \operatorname{Tr}_B|\Phi^+\rangle\langle\Phi^+|
   =\frac12(|0\rangle\langle0|+|1\rangle\langle1|)
   =I/2
   $$
4. classical correlated state
   $$
   \rho_c=\frac12(|00\rangle\langle00|+|11\rangle\langle11|)
   $$
   のA側stateを求めよ。  
   **解答**：
   $$
   \rho_A=I/2
   $$
   でBell stateと同じlocal stateです。
5. 上二状態を区別する測定を述べよ。  
   **解答**：両側をx基底で測るとBell stateは同じ符号だけを返しますが、
   $$
   \rho_c
   $$
   は4組を各1/4で返します。
6. entanglementが通信にならない理由を述べよ。  
   **解答**：相手のsettingを平均した自分側のmarginal
   $$
   p(a)=\operatorname{Tr}(\rho_AE_a)
   $$
   は相手の選択に依存せず、相関の照合には古典通信が要るためです。

## 参考・ナビゲーション

- 参考：[合成系と量子もつれ（qm大学物理）](https://qmcharge.com/article-quantum-entanglement-1)（確認日：2026-07-27）
- 前：[量子channel](07_channels_unitary.md)
- 次：[decoherenceとtomography](09_decoherence_tomography.md)
- 発展：[同種粒子・多体系](../part05_many_body/README.md)

