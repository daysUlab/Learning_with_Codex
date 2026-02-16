# アンペール・マクスウェルの法則

## 学習目標
- アンペールの法則を積分形で使い、対称性のある系の磁場を求められる。
- 変位電流項が必要になる理由を、連続の式との整合で説明できる。
- 積分形と微分形を往復して、場の局所方程式として理解できる。

---

## 0. 導入

静磁場では、電流が磁場の渦を作ります。
その関係はアンペールの法則で

$$
\oint_C \mathbf{B}\cdot d\mathbf{l}=\mu_0 I_{\mathrm{enc}}
$$

と書けます。

しかし時間変化する電場を含む状況では、この式のままでは矛盾が出ます。
それを解消して理論を閉じるのがアンペール・マクスウェルの法則です。

$$
\oint_C \mathbf{B}\cdot d\mathbf{l}=\mu_0 I_{\mathrm{cond}}+\mu_0\varepsilon_0\frac{d\Phi_E}{dt}
$$

---

## 1. 静磁場でのアンペールの法則

円筒対称の電流分布では、アンペール積分路を円に取ると計算が簡単になります。
半径

$$
r
$$

の円周上で

$$
\mathbf{B}
$$

の大きさが一定なら

$$
\oint_C \mathbf{B}\cdot d\mathbf{l}=B(r)\,2\pi r
$$

です。

例えば無限直線電流

$$
I
$$

に対して

$$
B(r)\,2\pi r=\mu_0 I
$$

$$
B(r)=\frac{\mu_0 I}{2\pi r}
$$

を得ます。

---

## 2. 変位電流が必要になる理由

コンデンサの充電を考えると、同じ積分路

$$
C
$$

に対して、張る面の取り方で貫く伝導電流が変わって見える問題が起きます。

- 導線を貫く面を取ると

$$
I_{\mathrm{cond}}=I
$$

- 極板間をふくらませた面を取ると、電荷は真空を横切らないため

$$
I_{\mathrm{cond}}=0
$$

になります。

左辺

$$
\oint_C \mathbf{B}\cdot d\mathbf{l}
$$

は同じなのに右辺が一致しないと困るため、電場変化による項を加えます。

$$
I_{\mathrm{disp}}=\varepsilon_0\frac{d\Phi_E}{dt}
$$

これで

$$
I_{\mathrm{cond}}+I_{\mathrm{disp}}
$$

が面の取り方によらず同じになり、法則が一貫します。

---

## 3. 連続の式との整合

電荷保存は連続の式

$$
\frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{J}=0
$$

で与えられます。

もし微分形を古い形

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}
$$

のままにすると、両辺の発散を取って

$$
0=\mu_0\nabla\cdot\mathbf{J}
$$

となり、一般には

$$
\nabla\cdot\mathbf{J}=0
$$

を強制してしまいます。これは時間変化する電荷密度と両立しません。

そこで

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

とすると、発散を取って

$$
0=\mu_0\nabla\cdot\mathbf{J}+\mu_0\varepsilon_0\frac{\partial}{\partial t}(\nabla\cdot\mathbf{E})
$$

さらに

$$
\nabla\cdot\mathbf{E}=\frac{\rho}{\varepsilon_0}
$$

を使えば

$$
\nabla\cdot\mathbf{J}+\frac{\partial\rho}{\partial t}=0
$$

が再現され、電荷保存と整合します。

---

## 4. 積分形と微分形

アンペール・マクスウェルの積分形は

$$
\oint_C \mathbf{B}\cdot d\mathbf{l}=\mu_0\int_S \mathbf{J}\cdot d\mathbf{S}+\mu_0\varepsilon_0\frac{d}{dt}\int_S \mathbf{E}\cdot d\mathbf{S}
$$

です。

ストークスの定理を使うと

$$
\int_S (\nabla\times\mathbf{B})\cdot d\mathbf{S}=\mu_0\int_S \mathbf{J}\cdot d\mathbf{S}+\mu_0\varepsilon_0\int_S \frac{\partial\mathbf{E}}{\partial t}\cdot d\mathbf{S}
$$

任意の面で成立するので

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

を得ます。

---

## 5. 例題

## 5.1 無限直線電流

電流

$$
I
$$

が z 軸に沿って流れるとき、半径

$$
r
$$

の円周を積分路に取ると

$$
B(r)\,2\pi r=\mu_0 I
$$

$$
B(r)=\frac{\mu_0 I}{2\pi r}
$$

となります。

## 5.2 平行板コンデンサ充電時の磁場（極板間）

半径

$$
R
$$

の平行板コンデンサを充電中とし、極板間で

$$
\mathbf{E}(t)
$$

がほぼ一様とします。半径

$$
r<R
$$

の円周を積分路に取ると、貫く伝導電流は 0 なので

$$
\oint_C \mathbf{B}\cdot d\mathbf{l}=\mu_0\varepsilon_0\frac{d\Phi_E}{dt}
$$

$$
B(r)\,2\pi r=\mu_0\varepsilon_0\frac{d}{dt}\left(E\pi r^2\right)
$$

$$
B(r)=\frac{\mu_0\varepsilon_0 r}{2}\frac{dE}{dt}
$$

を得ます。

---

## 6. よくある誤解

- 変位電流を「電子が真空を流れる電流」と同一視する。
  - 実体は電場の時間変化項です。
- アンペール則は静磁場でしか使えないと考える。
  - マクスウェル補正付きで一般状況へ拡張されます。
- 積分路だけ決めれば十分で、面の選び方は無関係だと思う。
  - 法則が正しいかは、面の選び方に依存しない形であることが本質です。

---

## 7. 演習問題

1. 無限直線電流

$$
I
$$

に対し、半径

$$
2r
$$

での磁場

$$
B(2r)
$$

を求めよ。

2. 充電中コンデンサで、極板間の電場が

$$
E(t)=\beta t
$$

と増加するとき、

$$
r<R
$$

での磁場

$$
B(r)
$$

を求めよ。

3. 変位電流密度

$$
\mathbf{J}_{\mathrm{disp}}=\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

の単位が

$$
\mathbf{J}
$$

と同じであることを示せ。

4. なぜ変位電流項がないと連続の式と矛盾するか、発散を取る手順で説明せよ。

---

## 8. 演習解答

1.

$$
B(2r)=\frac{\mu_0 I}{2\pi(2r)}=\frac{\mu_0 I}{4\pi r}
$$

です。

2.

$$
\frac{dE}{dt}=\beta
$$

より

$$
B(r)=\frac{\mu_0\varepsilon_0 r}{2}\beta
$$

です。

3.

$$
\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

の単位は

$$
\frac{\mathrm{C}}{\mathrm{V\,m}}\cdot\frac{\mathrm{V}}{\mathrm{m\,s}}=\frac{\mathrm{C}}{\mathrm{m}^2\mathrm{s}}=\frac{\mathrm{A}}{\mathrm{m}^2}
$$

で、電流密度と一致します。

4. 補正なしでは

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}
$$

から

$$
0=\mu_0\nabla\cdot\mathbf{J}
$$

となり

$$
\nabla\cdot\mathbf{J}=0
$$

を強制します。これは一般の

$$
\frac{\partial\rho}{\partial t}\neq 0
$$

の状況と整合しないため、

$$
\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

が必要です。

---

## まとめ

- アンペール・マクスウェルの法則は、磁場の循環を電流と電場変化で統一して記述する。
- 変位電流項は、コンデンサ問題の面依存性を解消し、連続の式と理論を整合させる。
- 積分形と微分形を往復できると、対称性計算と局所方程式の両方を一貫して扱える。
