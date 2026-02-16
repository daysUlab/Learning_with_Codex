# ポインティングベクトルとエネルギー保存

## 学習目標
- 電磁場のエネルギー密度を式で書き、各項の物理的意味を説明できる。
- ポインティング定理を導出し、エネルギー保存則として読める。
- 平面波や回路近似で、エネルギー流束とジュール熱の収支を計算できる。

---

## 0. 導入

電磁気学では、場そのものがエネルギーを持ち、空間を通してエネルギーを運びます。
この「運ばれる向きと量」を表すのがポインティングベクトルです。

$$
\mathbf{S}=\frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}
$$

さらに、場のエネルギー密度

$$
u
$$

を導入すると、ポインティング定理

$$
\frac{\partial u}{\partial t}+\nabla\cdot\mathbf{S}+\mathbf{J}\cdot\mathbf{E}=0
$$

が得られます。
これは「場のエネルギー変化 + 流出 + 物質への供給 = 0」という局所保存則です。

---

## 1. 場のエネルギー密度

真空中での電場・磁場のエネルギー密度は

$$
u_E=\frac{\varepsilon_0}{2}E^2
$$

$$
u_B=\frac{1}{2\mu_0}B^2
$$

です。
合計を

$$
u=u_E+u_B=\frac{\varepsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2
$$

と置きます。

---

## 2. ポインティング定理の導出

出発点は次の 2 式です。

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

ベクトル恒等式

$$
\nabla\cdot(\mathbf{E}\times\mathbf{B})=\mathbf{B}\cdot(\nabla\times\mathbf{E})-\mathbf{E}\cdot(\nabla\times\mathbf{B})
$$

に代入すると

$$
\nabla\cdot(\mathbf{E}\times\mathbf{B})=-\mathbf{B}\cdot\frac{\partial\mathbf{B}}{\partial t}-\mu_0\mathbf{E}\cdot\mathbf{J}-\mu_0\varepsilon_0\mathbf{E}\cdot\frac{\partial\mathbf{E}}{\partial t}
$$

ここで

$$
\mathbf{B}\cdot\frac{\partial\mathbf{B}}{\partial t}=\frac{1}{2}\frac{\partial B^2}{\partial t}
$$

$$
\mathbf{E}\cdot\frac{\partial\mathbf{E}}{\partial t}=\frac{1}{2}\frac{\partial E^2}{\partial t}
$$

を使い、

$$
\mathbf{S}=\frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}
$$

を定義すると

$$
\frac{\partial}{\partial t}\left(\frac{\varepsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2\right)+\nabla\cdot\mathbf{S}+\mathbf{J}\cdot\mathbf{E}=0
$$

すなわち

$$
\frac{\partial u}{\partial t}+\nabla\cdot\mathbf{S}+\mathbf{J}\cdot\mathbf{E}=0
$$

を得ます。

---

## 3. 各項の物理的意味

式

$$
\frac{\partial u}{\partial t}+\nabla\cdot\mathbf{S}+\mathbf{J}\cdot\mathbf{E}=0
$$

の意味は次の通りです。

- $$
\frac{\partial u}{\partial t}
$$
  その点の場エネルギーの時間変化。
- $$
\nabla\cdot\mathbf{S}
$$
  その点からのエネルギー流出率。
- $$
\mathbf{J}\cdot\mathbf{E}
$$
  場から荷電粒子系へ渡る単位体積あたりの仕事率。

導体では

$$
\mathbf{J}\cdot\mathbf{E}
$$

がジュール熱の発生率に対応します。

---

## 4. 平面波でのエネルギー流

真空中平面波では

$$
B=\frac{E}{c}
$$

なので

$$
S=\frac{1}{\mu_0}EB=\frac{E^2}{\mu_0 c}=\varepsilon_0 c E^2
$$

です。

時間平均を取ると（

$$
E(t)=E_0\cos(\omega t)
$$

）

$$
\langle S\rangle=\frac{1}{2}\varepsilon_0 c E_0^2
$$

となります。

この量は波の強度です。

---

## 5. 例題

## 5.1 平面波の平均強度

振幅

$$
E_0
$$

の平面波の平均ポインティング流束は

$$
\langle S\rangle=\frac{1}{2}\varepsilon_0 c E_0^2
$$

です。

## 5.2 抵抗体へのエネルギー流入

定常直流回路で抵抗体まわりに閉曲面

$$
S
$$

を取ると、定常なので

$$
\frac{d}{dt}\int_V u\,dV=0
$$

です。
ポインティング定理の体積積分形

$$
\frac{d}{dt}\int_V u\,dV+\oint_S \mathbf{S}\cdot d\mathbf{A}+\int_V \mathbf{J}\cdot\mathbf{E}\,dV=0
$$

より

$$
\oint_S \mathbf{S}\cdot d\mathbf{A}=-\int_V \mathbf{J}\cdot\mathbf{E}\,dV
$$

となり、外部から流入する電磁エネルギーが抵抗内の発熱と一致します。

---

## 6. よくある誤解

- 電力は導線内の電子だけが運ぶと考える。
  - 実際には場が空間を通してエネルギーを運びます。
- $$
\mathbf{S}
$$
  の向きだけを見て大きさの時間平均を忘れる。
  - 交流・波動問題では平均値が観測量になることが多いです。
- $$
\mathbf{J}\cdot\mathbf{E}
$$
  の符号を常に正と決めつける。
  - 系によっては場へエネルギーを返す場合もあります。

---

## 7. 演習問題

1. 真空平面波で

$$
E_0=1.0\times10^3\,\mathrm{V/m}
$$

のとき、平均強度

$$
\langle S\rangle
$$

を求めよ。

2. ポインティング定理の各項が何を表すか、文章で説明せよ。

3. 定常状態で

$$
\partial u/\partial t=0
$$

のとき、体積積分形のエネルギー収支を示せ。

4. なぜ抵抗加熱が

$$
\mathbf{J}\cdot\mathbf{E}
$$

で表せるかを説明せよ。

---

## 8. 演習解答

1.

$$
\langle S\rangle=\frac{1}{2}\varepsilon_0 c E_0^2
$$

$$
=\frac{1}{2}\times 8.85\times10^{-12}\times 3.0\times10^8\times(1.0\times10^3)^2
$$

$$
\approx 1.33\times10^3\,\mathrm{W/m^2}
$$

です。

2.

$$
\partial u/\partial t
$$

は場エネルギーの蓄積変化、

$$
\nabla\cdot\mathbf{S}
$$

は流出入、

$$
\mathbf{J}\cdot\mathbf{E}
$$

は物質への仕事率を表します。

3. 体積

$$
V
$$

で積分すると

$$
\oint_S \mathbf{S}\cdot d\mathbf{A}+\int_V \mathbf{J}\cdot\mathbf{E}\,dV=0
$$

です。流入エネルギーが消費電力に一致します。

4. 電荷が電場から受ける力は

$$
q\mathbf{E}
$$

で、単位体積あたりの仕事率に直すと

$$
\mathbf{J}\cdot\mathbf{E}
$$

になります。

---

## まとめ

- ポインティングベクトル

$$
\mathbf{S}=\frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}
$$

は電磁エネルギー流束を表す。
- ポインティング定理は場と物質を含む局所エネルギー保存則である。
- 波動問題・回路問題ともに、エネルギー収支の検算軸として有効である。
