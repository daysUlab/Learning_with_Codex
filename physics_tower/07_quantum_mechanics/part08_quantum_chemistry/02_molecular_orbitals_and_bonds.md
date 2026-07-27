# 分子軌道・化学結合・Born–Oppenheimer近似

## 核とelectronのscaleを分ける

分子の完全Hamiltonianには核・electronの運動とCoulomb相互作用が入ります。核が重く遅いことを使い、まず核位置

$$
\{\mathbf R_A\}
$$

を固定して電子状態を解くのがBorn–Oppenheimer近似です。そのenergy面上で核運動を扱います。avoided crossingや強いnonadiabatic couplingでは破綻します。

## 最小例

二つの原子軌道

$$
\phi_A,\quad\phi_B
$$

から

$$
\psi_+=N_+(\phi_A+\phi_B)
$$

$$
\psi_-=N_-(\phi_A-\phi_B)
$$

を作ります。前者は核間で振幅が強め合うbonding orbital、後者はnodeを持つantibonding orbitalです。

$$
\mathrm{H_2^+}
$$

では一electronが

$$
\psi_+
$$

を占めて結合を作ります。

$$
\mathrm H_2
$$

では逆spinの二electronが同じ空間orbitalを占められます。Pauli原理は「同じ場所にいられない」ではなく、同じone-particle stateを同じspinのfermionが共有できない規則です。

## 演習と全解答

1. bonding combinationで核間密度が増える理由を述べよ。
   **解答**：二軌道の振幅が同符号で加わり、cross termが正になるためです。
2. antibonding orbitalにnodeができる理由を述べよ。
   **解答**：核間で二振幅が逆符号にcancelするためです。
3. Born–Oppenheimerで固定するものは何か。
   **解答**：電子問題を解く段階の核位置です。
4. 同一空間orbitalへ二electronを入れるspin条件を述べよ。
   **解答**：全一粒子stateが異なるよう、spinは反対向きにします。
5. 分子軌道はelectronの軌道trajectoryか。
   **解答**：いいえ。分子全体に広がる一electron stateの振幅です。
6. 振動・回転spectraへ進むのに必要な追加自由度を述べよ。
   **解答**：Born–Oppenheimer energy面上の核間距離・分子姿勢の量子運動です。

## ナビゲーション

- 前：[水素原子](01_hydrogen_atom_and_spectra.md)
- 次：[多電子と近似](03_many_electron_quantum_chemistry.md)
- 後続：[同種粒子](../part05_many_body/README.md)
