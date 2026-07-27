# 調和振動子――Newton・Lagrange・Hamilton・量子

## 四つの表現

| 軸 | Newton | Lagrange | Hamilton | 量子 |
|---|---|---|---|---|
| 状態 | $$x,\dot x$$ | $$x,\dot x$$ | $$x,p$$ | $$|\psi\rangle$$ |
| 中心式 | $$m\ddot x=-kx$$ | Euler–Lagrange | 正準方程式 | Schrödinger |
| energy | 連続 | 連続 | 連続 | $$E_n=\hbar\omega(n+1/2)$$ |
| 初期条件 | $$x_0,\dot x_0$$ | 同左 | $$x_0,p_0$$ | 規格化state |

$$
\omega=\sqrt{\frac{k}{m}}
$$

として

$$
\hat H=\frac{\hat p^2}{2m}+\frac12m\omega^2\hat x^2
$$

です。ladder operator

$$
\hat a=\sqrt{\frac{m\omega}{2\hbar}}\hat x+
\frac{i}{\sqrt{2m\hbar\omega}}\hat p
$$

を定義すると

$$
[\hat a,\hat a^\dagger]=1
$$

$$
\hat H=\hbar\omega\left(\hat a^\dagger\hat a+\frac12\right)
$$

です。従って

$$
E_n=\hbar\omega\left(n+\frac12\right)
$$

を得ます。

zero-point energy

$$
E_0=\frac12\hbar\omega
$$

は

$$
\Delta x=\Delta p=0
$$

を許さないことと整合します。

古典極限では

$$
n\gg1
$$

で隣接準位差

$$
\hbar\omega
$$

が全energyに比べ小さくなり、coherent stateの期待値は古典軌道を描きます。

## 演習と全解答

1.
   $$
   k=4.0\ \mathrm{N/m},\quad m=1.0\ \mathrm{kg}
   $$
   の角振動数を求めよ。
   **解答**：
   $$
   \omega=2.0\ \mathrm{s^{-1}}
   $$
2. 隣接energy差を求めよ。
   **解答**：
   $$
   E_{n+1}-E_n=\hbar\omega
   $$
3.
   $$
   \hat a|0\rangle
   $$
   は何か。
   **解答**：
   $$
   0
   $$
   です。
4. 基底state energyを古典的静止energy 0にできない理由を述べよ。
   **解答**：位置と運動量を同時に確定すると不確定性関係に反するためです。
5. Hamilton形式から古典運動方程式を出せ。
   **解答**：
   $$
   \dot x=p/m,\quad\dot p=-m\omega^2x
   $$
   より
   $$
   \ddot x+\omega^2x=0
   $$
6. 量子振動子が分子振動・phonon・場のmodeへ再利用される理由を述べよ。
   **解答**：安定平衡点近傍のpotentialは二次近似でき、線形化した各normal modeが独立振動子になるためです。

## ナビゲーション

- 前：[井戸とtunnel](03_wells_barriers_tunneling.md)
- 次：[古典極限](05_ehrenfest_wkb_classical_limit.md)
- 古典正本：[三形式比較](../../03_analytical_mechanics/part01_supplements/01_newton_lagrange_hamilton_comparison.md)
