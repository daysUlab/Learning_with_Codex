# Newton・Hamilton・Schrödingerの時間発展

| 軸 | Newton | Hamilton | Schrödinger |
|---|---|---|---|
| 状態 | $$q,\dot q$$ | $$q,p$$ | $$|\psi\rangle$$ |
| 中心式 | $$m\ddot q=F$$ | $$\dot q=\partial_pH,\ \dot p=-\partial_qH$$ | $$i\hbar\partial_t|\psi\rangle=H|\psi\rangle$$ |
| 初期条件 | 位置・速度 | phase-space point | 規格化state |
| 予測 | trajectory | phase-space flow | 各observableの確率 |
| 生成子 | force | Hamiltonian | Hamiltonian |

Hamiltonianという語が同じでも、古典ではphase-space上のflow、量子ではHilbert space上のunitary flowを生成します。

## 演習と全解答

1. 自由粒子の三形式のHamiltonian／方程式を書け。
   **解答**：
   $$
   m\ddot x=0,\quad H=p^2/(2m),\quad
   i\hbar\partial_t\psi=-(\hbar^2/2m)\partial_x^2\psi
   $$
2. 三形式で同じ初期条件をそのまま使えるか。
   **解答**：量子stateは位置・運動量分布とphaseを持ち、phase-space pointとは異なります。
3. Hamiltonianがenergyと一致しない古典系があるか。
   **解答**：時間依存座標や速度依存potentialなどで単純な
   $$
   T+V
   $$
   と一致しない場合があります。
4. 量子時間発展が確率を保存する条件を述べよ。
   **解答**：
   $$
   H=H^\dagger
   $$
   によるunitarityです。
5. Ehrenfest定理だけで完全な古典軌道を得るか。
   **解答**：非線形potentialではpacket幅の近似が必要です。
6. 三理論の選択を「新しいほどよい」で決めてよいか。
   **解答**：目的scale・精度・計算量で、古典modelが十分ならそれを使います。

- 親：[横断README](README.md)
- 解析力学：[三形式](../03_analytical_mechanics/part01_supplements/01_newton_lagrange_hamilton_comparison.md)
- 量子：[自由粒子](../07_quantum_mechanics/part09_schrodinger_dynamics/02_free_particle_wave_packets.md)
