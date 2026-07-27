# 可換性・不確定性・位置／運動量表示

## 非可換性は測定器の粗さではない

位置表示で

$$
\hat x=x,\qquad
\hat p=-i\hbar\frac{d}{dx}
$$

です。任意の十分滑らかな関数へ作用させると

$$
[\hat x,\hat p]\psi
=-i\hbar x\psi'+i\hbar(x\psi)'=i\hbar\psi
$$

ゆえに

$$
[\hat x,\hat p]=i\hbar
$$

です。

Cauchy–Schwarz不等式からRobertson関係

$$
\Delta A\,\Delta B\geq\frac12
\left|\langle[\hat A,\hat B]\rangle\right|
$$

を得ます。従って

$$
\Delta x\,\Delta p\geq\frac{\hbar}{2}
$$

です。これはstate内の分散の下限であり、単なる装置誤差ではありません。

## Fourier変換

本章の規約では

$$
\phi(p)=\frac{1}{\sqrt{2\pi\hbar}}
\int_{-\infty}^{\infty}e^{-ipx/\hbar}\psi(x)\,dx
$$

$$
\psi(x)=\frac{1}{\sqrt{2\pi\hbar}}
\int_{-\infty}^{\infty}e^{ipx/\hbar}\phi(p)\,dp
$$

です。狭い位置波束には広い運動量成分が必要で、不確定性をwave packetの幅としても理解できます。

可換な観測量は共通固有basisを持てる条件を満たし、同時に鋭い値を持つstateを作れます。ただし縮退やdomainには注意が必要です。

## 演習と全解答

1.
   $$
   [\hat p,\hat x]
   $$
   を求めよ。
   **解答**：
   $$
   [\hat p,\hat x]=-[\hat x,\hat p]=-i\hbar
   $$
2.
   $$
   [\hat x,\hat p^2]
   $$
   を求めよ。
   **解答**：
   $$
   [x,p^2]=[x,p]p+p[x,p]=2i\hbar p
   $$
3.
   $$
   \Delta x=1.0\ \mathrm{nm}
   $$
   のとき最小
   $$
   \Delta p
   $$
   を概算せよ。
   **解答**：
   $$
   \Delta p\geq\frac{1.055\times10^{-34}}{2.0\times10^{-9}}
   \simeq5.3\times10^{-26}\ \mathrm{kg\,m/s}
   $$
4. momentum eigenfunctionを位置表示で書け。
   **解答**：
   $$
   \psi_p(x)\propto e^{ipx/\hbar}
   $$
5. 平面波が通常の意味で規格化できない理由を述べよ。
   **解答**：
   $$
   |\psi|^2
   $$
   が全空間で一定で積分が発散するため、delta規格化またはwave packetを使います。
6. 非可換なら任意のstateで両分散が大きいか。
   **解答**：下限はcommutatorの期待値で決まります。一方の固有stateでは他方の分散が増えるなど、state依存です。

## ナビゲーション

- 前：[演算子](03_hilbert_operators_eigenvalues.md)
- 次：[測定と解釈](05_measurement_decoherence_interpretations.md)
- 後続：[自由粒子](../part09_schrodinger_dynamics/02_free_particle_wave_packets.md)
