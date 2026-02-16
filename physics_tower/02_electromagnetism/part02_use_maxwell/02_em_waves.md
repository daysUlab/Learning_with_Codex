# マクスウェル方程式から電磁波へ

## 学習目標
- 真空中マクスウェル方程式から、電場と磁場の波動方程式を導出できる。
- 波の速度

$$
c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$

の意味を説明できる。
- 平面波での

$$
\mathbf{E},\mathbf{B},\mathbf{k}
$$

の直交関係と、エネルギー流の向きを説明できる。

---

## 0. 導入

マクスウェル方程式の重要な結論の 1 つは、電場と磁場が自律的に伝搬できることです。

- 時間変化する電場が磁場を生む。
- 時間変化する磁場が電場を生む。

この相互作用が連鎖すると、波として空間を伝わります。
これが電磁波です。

---

## 1. 真空中の出発式

真空中（

$$
\rho=0,\mathbf{J}=0
$$

）では、方程式は次の形になります。

$$
\nabla\cdot\mathbf{E}=0
$$

$$
\nabla\cdot\mathbf{B}=0
$$

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

$$
\nabla\times\mathbf{B}=\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

---

## 2. 電場の波動方程式導出

ファラデーの式

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

の両辺に回転を取り

$$
\nabla\times(\nabla\times\mathbf{E})=-\frac{\partial}{\partial t}(\nabla\times\mathbf{B})
$$

とします。

ベクトル恒等式

$$
\nabla\times(\nabla\times\mathbf{E})=\nabla(\nabla\cdot\mathbf{E})-\nabla^2\mathbf{E}
$$

と

$$
\nabla\cdot\mathbf{E}=0
$$

より

$$
-\nabla^2\mathbf{E}=-\mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}
$$

したがって

$$
\nabla^2\mathbf{E}=\mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}
$$

を得ます。

同様に

$$
\mathbf{B}
$$

についても

$$
\nabla^2\mathbf{B}=\mu_0\varepsilon_0\frac{\partial^2\mathbf{B}}{\partial t^2}
$$

が成立します。

---

## 3. 波の速度

一般の波動方程式

$$
\nabla^2\mathbf{F}=\frac{1}{v^2}\frac{\partial^2\mathbf{F}}{\partial t^2}
$$

と比較すると

$$
v=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$

です。
真空ではこの

$$
v
$$

が光速

$$
c
$$

に一致します。

$$
c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$

この一致が、光が電磁波であることを示す決定的な結果です。

---

## 4. 平面波の基本関係

平面波解を

$$
\mathbf{E}(\mathbf{r},t)=\mathbf{E}_0\cos(\mathbf{k}\cdot\mathbf{r}-\omega t)
$$

$$
\mathbf{B}(\mathbf{r},t)=\mathbf{B}_0\cos(\mathbf{k}\cdot\mathbf{r}-\omega t)
$$

とします。

真空条件

$$
\nabla\cdot\mathbf{E}=0,\nabla\cdot\mathbf{B}=0
$$

から

$$
\mathbf{k}\cdot\mathbf{E}_0=0
$$

$$
\mathbf{k}\cdot\mathbf{B}_0=0
$$

であり、

$$
\mathbf{E},\mathbf{B}
$$

は伝搬方向

$$
\mathbf{k}
$$

に垂直です。

さらに回転方程式から

$$
\mathbf{B}=\frac{1}{\omega}\mathbf{k}\times\mathbf{E}
$$

となり、

$$
B=\frac{E}{c}
$$

が得られます。

---

## 5. エネルギー流との関係

ポインティングベクトル

$$
\mathbf{S}=\frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}
$$

は単位面積あたりのエネルギー流束です。

平面波では

$$
\mathbf{S}
$$

の向きは

$$
\mathbf{k}
$$

と同じです。
したがって、波の進行方向とエネルギー輸送方向は一致します。

---

## 6. 例題

## 6.1 周波数と波長から波数を求める

真空中で周波数

$$
f
$$

の電磁波の角周波数は

$$
\omega=2\pi f
$$

波数は

$$
k=\frac{\omega}{c}=\frac{2\pi}{\lambda}
$$

です。

## 6.2 電場振幅から磁場振幅を求める

平面波で電場振幅が

$$
E_0
$$

のとき

$$
B_0=\frac{E_0}{c}
$$

です。

---

## 7. よくある誤解

- 電場だけが波として伝わると考える。
  - 実際は

$$
\mathbf{E},\mathbf{B}
$$

が結合して同時に伝わります。
-

$$
\mathbf{E}
$$

と

$$
\mathbf{B}
$$

の向きを任意に取ってしまう。
  - 3 つのベクトル

$$
\mathbf{E},\mathbf{B},\mathbf{k}
$$

は右手系を作ります。
- 媒質中でも常に速度が

$$
c
$$

だと思う。
  - 一般には媒質パラメータに依存します。

---

## 8. 演習問題

1. 真空中マクスウェル方程式から

$$
\mathbf{E}
$$

の波動方程式を導出せよ。

2. 真空中の平面波で

$$
E_0=3.0\times 10^2\,\mathrm{V/m}
$$

のとき

$$
B_0
$$

を求めよ。

3. 波長

$$
\lambda=600\,\mathrm{nm}
$$

の光について、周波数

$$
f
$$

を求めよ。

4. なぜ

$$
\mathbf{S}
$$

の向きが波の進行方向と一致するか、

$$
\mathbf{E}\times\mathbf{B}
$$

の向きで説明せよ。

---

## 9. 演習解答

1.

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

に回転を取り、

$$
\nabla\times\mathbf{B}=\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

を代入し、

$$
\nabla\cdot\mathbf{E}=0
$$

を使うと

$$
\nabla^2\mathbf{E}=\mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}
$$

を得ます。

2.

$$
B_0=\frac{E_0}{c}=\frac{3.0\times10^2}{3.0\times10^8}=1.0\times10^{-6}\,\mathrm{T}
$$

です。

3.

$$
f=\frac{c}{\lambda}=\frac{3.0\times10^8}{600\times10^{-9}}=5.0\times10^{14}\,\mathrm{Hz}
$$

です。

4. 平面波で

$$
\mathbf{E}\perp\mathbf{B}
$$

かつ

$$
\mathbf{E},\mathbf{B},\mathbf{k}
$$

が右手系を作るため、

$$
\mathbf{E}\times\mathbf{B}
$$

は

$$
\mathbf{k}
$$

方向を向きます。

---

## まとめ

- 真空中マクスウェル方程式から、

$$
\mathbf{E},\mathbf{B}
$$

の波動方程式が導かれる。
- 伝搬速度は

$$
c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$

で与えられ、光の本質が電磁波であることを示す。
- 平面波では

$$
\mathbf{E},\mathbf{B},\mathbf{k}
$$

が直交し、エネルギー流は

$$
\mathbf{S}=\frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}
$$

で表される。
