# 量子状態・波動関数・Born則

## 現代量子論から見ると

このページでは一般状態

$$
\rho
$$

のうちpure state

$$
\rho=|\psi\rangle\langle\psi|
$$

へ限定し、position basisを選びます。wavefunctionはpure stateのposition representationで、一般のquantum stateそのものではありません。以下のBorn則は一般化Born則をideal position PVMへ特殊化したものです。現実の有限分解能detectorは一般にPOVMです。

## 何を状態として残すか

古典一粒子のstateは位相空間の一点

$$
(x,p)
$$

です。この節ではpure stateに限定し、同じ準備操作が将来の各測定結果へ与える確率振幅を一つのray

$$
|\psi\rangle
$$

で表します。全体phase

$$
e^{i\chi}|\psi\rangle
$$

は同じ物理状態です。

位置表示は

$$
\psi(x,t)=\langle x|\psi(t)\rangle
$$

で、Born則は

$$
P(x\in[a,b])=\int_a^b|\psi(x,t)|^2\,dx
$$

です。従って規格化条件は

$$
\int_{-\infty}^{\infty}|\psi(x,t)|^2\,dx=1
$$

です。一次元波動関数の次元は

$$
[\psi]=\mathrm{m^{-1/2}}
$$

です。

## 規格化と期待値

$$
\psi(x)=Ae^{-\kappa|x|},\qquad\kappa>0
$$

なら

$$
1=2|A|^2\int_0^\infty e^{-2\kappa x}dx
=\frac{|A|^2}{\kappa}
$$

より

$$
|A|=\sqrt{\kappa}
$$

です。位置の期待値は

$$
\langle x\rangle=\int x|\psi(x)|^2dx=0
$$

で、対称性だけでも分かります。

波動関数は物質密度そのものではありません。電荷を持つ一粒子の期待電荷密度として

$$
q|\psi|^2
$$

が現れる場合はありますが、spinや多粒子stateは一つの三次元scalar fieldでは表せません。

## 演習と全解答

1. 区間
   $$
   0<x<L
   $$
   で一定の波動関数
   $$
   \psi=A
   $$
   を規格化せよ。
   **解答**：
   $$
   |A|^2L=1\Rightarrow |A|=L^{-1/2}
   $$
2. 規格化済みstateを
   $$
   2|\psi\rangle
   $$
   としてよいか。
   **解答**：同じrayですが、確率計算前にnorm 1へ規格化します。
3.
   $$
   e^{i\chi}\psi
   $$
   で位置確率が変わらないことを示せ。
   **解答**：
   $$
   |e^{i\chi}\psi|^2=|\psi|^2
   $$
4.
   $$
   \psi=Ae^{-\kappa|x|}
   $$
   で
   $$
   P(x>0)
   $$
   を求めよ。
   **解答**：evenな確率密度なので
   $$
   1/2
   $$
   です。
5. 一回の位置測定から波動関数を決定できるか。
   **解答**：できません。同じ準備を多数回行い、複数の測定basisを使うstate tomographyが必要です。
6. 二粒子波動関数の引数を述べよ。
   **解答**：spinなし位置表示なら
   $$
   \psi(\mathbf r_1,\mathbf r_2,t)
   $$
   で、通常は六次元configuration space上です。

## 参考・ナビゲーション

Sakurai & Napolitano, *Modern Quantum Mechanics*, Ch.1.

- 前：[一般形式からwavefunctionへ](../part02_modern_formalism/10_to_wavefunction_schrodinger.md)
- 次：[重ね合わせと位相](02_superposition_phase_quantum_probability.md)
- 補習：[数学診断](../remedial_room/README.md)
