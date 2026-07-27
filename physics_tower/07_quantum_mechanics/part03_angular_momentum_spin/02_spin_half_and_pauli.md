# spin 1/2・Pauli行列・Stern–Gerlach

## 内部自由度

spin

$$
\frac12
$$

stateは

$$
|\chi\rangle=\alpha|+z\rangle+\beta|-z\rangle
$$

で表します。spin演算子は

$$
\hat{\mathbf S}=\frac{\hbar}{2}\boldsymbol\sigma
$$

です。

$$
\sigma_x=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},\quad
\sigma_y=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix},\quad
\sigma_z=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
$$

各軸での測定値は

$$
\pm\frac{\hbar}{2}
$$

です。

$$
|+x\rangle=\frac{|+z\rangle+|-z\rangle}{\sqrt2},\qquad
|-x\rangle=\frac{|+z\rangle-|-z\rangle}{\sqrt2}
$$

なのでz上向きをxで測ると各1/2です。

Bloch vector

$$
\mathbf n
$$

に沿うpure stateのdensity matrixは

$$
\rho=\frac12(I+\mathbf n\cdot\boldsymbol\sigma)
$$

です。球面上の向きは古典自転軸ではなく、全方向の測定確率をまとめるstate座標です。

## 演習と全解答

1. Pauli Xの固有値を求めよ。
   **解答**：
   $$
   \det(\sigma_x-\lambda I)=\lambda^2-1=0
   $$
   より
   $$
   \pm1
   $$
2.
   $$
   [S_x,S_y]
   $$
   を求めよ。
   **解答**：
   $$
   i\hbar S_z
   $$
3.
   $$
   |+x\rangle
   $$
   をzで測る確率を求めよ。
   **解答**：各
   $$
   1/2
   $$
4. z上向きをz下向きへ変える演算子を一つ挙げよ。
   **解答**：
   $$
   \sigma_x
   $$
   です。
5.
   $$
   S^2
   $$
   の固有値を求めよ。
   **解答**：
   $$
   s(s+1)\hbar^2=\frac34\hbar^2
   $$
6. spinを半径を持つ球の自転とすると何が問題か。
   **解答**：古典的表面速度・連続成分ではspinorの
   $$
   2\pi
   $$
   回転符号や軸ごとの二値測定を再現できません。

## ナビゲーション

- 前：[軌道角運動量](01_orbital_angular_momentum.md)
- 次：[合成と磁気moment](03_addition_magnetic_moments_atoms.md)
- 実験：[Stern–Gerlach](../part01_mysteries/03_single_particle_interference_and_spin.md)
