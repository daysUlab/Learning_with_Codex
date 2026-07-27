# 自由粒子――古典軌道・平面波・波束

## 同じ問題を比較する

| 軸 | 古典 | 量子 |
|---|---|---|
| 状態 | $$x_0,p_0$$ | $$\psi(x,0)$$ |
| 運動方程式 | $$\dot x=p/m,\ \dot p=0$$ | $$i\hbar\partial_t\psi=-(\hbar^2/2m)\partial_x^2\psi$$ |
| 予測 | 一本の軌道 | 測定結果の分布 |
| energy | $$p^2/2m$$ | 同じ固有値だがstateは重ね合わせ可能 |

平面波

$$
\psi=Ae^{i(kx-\omega t)}
$$

を代入すると

$$
p=\hbar k,\qquad E=\hbar\omega=\frac{\hbar^2k^2}{2m}
$$

です。phase velocityは

$$
v_{\mathrm p}=\frac{\omega}{k}=\frac{\hbar k}{2m}
$$

group velocityは

$$
v_{\mathrm g}=\frac{d\omega}{dk}=\frac{\hbar k}{m}=\frac{p}{m}
$$

で古典速度と一致します。

localized particleは平面波の重ね合わせで作ります。自由Gaussian wave packetは中心がgroup velocityで動き、幅は時間とともに広がります。古典点粒子にはないdispersionです。

## 演習と全解答

1.
   $$
   k=1.0\times10^{10}\ \mathrm{m^{-1}}
   $$
   のelectron momentumを求めよ。
   **解答**：
   $$
   p=\hbar k\simeq1.05\times10^{-24}\ \mathrm{kg\,m/s}
   $$
2. 上のgroup velocityを求めよ。
   **解答**：
   $$
   v_g=p/m_e\simeq1.16\times10^6\ \mathrm{m/s}
   $$
3. 平面波の位置確率密度は何か。
   **解答**：全空間で一定で、位置がlocalizedしていません。
4. wave packetを狭くすると運動量幅はどうなるか。
   **解答**：Fourier関係により広がります。
5. group velocityとphase velocityのどちらがpacket中心の移動に対応するか。
   **解答**：group velocityです。
6. 古典極限でpacketが古典軌道に見える条件を述べよ。
   **解答**：packet幅と広がりが観測scaleに比べ小さく、potentialが幅の範囲で滑らかで、decoherenceも位置を局在化する条件です。

## ナビゲーション

- 前：[Schrödinger方程式](01_schrodinger_hamiltonian_continuity.md)
- 次：[井戸と障壁](03_wells_barriers_tunneling.md)
- 横断：[Newton・Hamilton・Schrödinger](../../cross_connections/09_newton_hamilton_schrodinger.md)
