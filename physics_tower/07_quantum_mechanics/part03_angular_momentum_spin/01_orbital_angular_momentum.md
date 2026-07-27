# 軌道角運動量・回転代数・球面調和関数

## 古典円運動から何が変わるか

古典では

$$
\mathbf L=\mathbf r\times\mathbf p
$$

です。量子でも形式を保ちますが、成分は

$$
[\hat L_i,\hat L_j]=i\hbar\varepsilon_{ijk}\hat L_k
$$

を満たし、三成分を同時に確定できません。

共通に測れる組は

$$
\hat L^2,\quad\hat L_z
$$

で、

$$
\hat L^2|l,m\rangle=\hbar^2l(l+1)|l,m\rangle
$$

$$
\hat L_z|l,m\rangle=\hbar m|l,m\rangle
$$

$$
l=0,1,2,\ldots,\qquad m=-l,\ldots,l
$$

です。

ladder operator

$$
\hat L_\pm=\hat L_x\pm i\hat L_y
$$

は

$$
\hat L_\pm|l,m\rangle
=\hbar\sqrt{l(l+1)-m(m\pm1)}|l,m\pm1\rangle
$$

と作用します。

位置表示の角度部分は球面調和関数

$$
Y_l^m(\theta,\varphi)
$$

です。これは原子orbitalの角度依存を表し、electronの周回trajectoryではありません。

## 演習と全解答

1.
   $$
   l=2
   $$
   の
   $$
   m
   $$
   を列挙せよ。
   **解答**：
   $$
   -2,-1,0,1,2
   $$
2.
   $$
   l=1
   $$
   の
   $$
   L^2
   $$
   固有値を求めよ。
   **解答**：
   $$
   2\hbar^2
   $$
3.
   $$
   |1,1\rangle
   $$
   へ
   $$
   L_+
   $$
   を作用させよ。
   **解答**：
   $$
   0
   $$
4.
   $$
   L_x,L_y
   $$
   を同時に鋭く測れる一般stateがない理由を述べよ。
   **解答**：
   $$
   [L_x,L_y]=i\hbar L_z
   $$
   で非可換だからです。
5. 古典角運動量の大きさを
   $$
   l\hbar
   $$
   としてよいか。
   **解答**：固有値の平方根は
   $$
   \hbar\sqrt{l(l+1)}
   $$
   です。
6. 回転対称なHamiltonianで保存される量を述べよ。
   **解答**：完全な球対称なら
   $$
   [H,L_i]=0
   $$
   で
   $$
   \mathbf L
   $$
   と
   $$
   L^2
   $$
   が保存されます。

## ナビゲーション

- 前：[part03](README.md)
- 次：[spin 1/2](02_spin_half_and_pauli.md)
- 古典正本：[角運動量](../../01_dynamics/00_overview.md)
