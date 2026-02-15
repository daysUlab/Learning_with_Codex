# トルクと角運動量の基本式

## 学習目標
- 角運動量とトルクをベクトルとして定義し、向き・大きさ・符号規約を説明できる。
- ニュートン方程式から
  $$
  \frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}
  $$
  を導出できる。
- 外力トルクゼロ条件から角運動量保存を判定し、回転問題へ適用できる。

## 0. 導入：なぜ運動量だけでは不十分か

直線運動では

$$
\frac{d\mathbf{p}}{dt}=\mathbf{F}
$$

が主役だが、回転を伴う問題では「どこを中心に回っているか」が本質になる。

同じ力でも、作用点が変われば回しやすさが変わる。この幾何学情報を含む量が

- 角運動量
- トルク

である。

力学を統一的に見ると、

$$
\text{力} \leftrightarrow \text{運動量変化}
$$

の回転版として

$$
\text{トルク} \leftrightarrow \text{角運動量変化}
$$

が立つ。

---

## 1. 定義

位置ベクトル

$$
\mathbf{r}
$$

運動量

$$
\mathbf{p}=m\mathbf{v}
$$

に対し、ある原点まわりの角運動量は

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

で定義される。

力

$$
\mathbf{F}
$$

が同じ原点に対して作るトルクは

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}
$$

である。

## 1.1 向きの規約

向きは右ねじ則で決まる。

- 反時計回りを正に取る平面運動では
  $$
  +\hat{\mathbf{z}}
  $$
  方向が正トルク。
- 時計回りは
  $$
  -\hat{\mathbf{z}}
  $$
  方向。

## 1.2 大きさ

外積の大きさより

$$
L=r p\sin\phi
$$

$$
\tau=rF\sin\theta
$$

となる。

ここで

$$
\phi
$$

は

$$
\mathbf{r}
$$

と

$$
\mathbf{p}
$$

のなす角、

$$
\theta
$$

は

$$
\mathbf{r}
$$

と

$$
\mathbf{F}
$$

のなす角である。

---

## 2. 基本方程式の導出

角運動量を時間微分する。

$$
\frac{d\mathbf{L}}{dt}=\frac{d}{dt}(\mathbf{r}\times\mathbf{p})
$$

積の微分則により

$$
\frac{d\mathbf{L}}{dt}=\frac{d\mathbf{r}}{dt}\times\mathbf{p}+\mathbf{r}\times\frac{d\mathbf{p}}{dt}
$$

第1項は

$$
\mathbf{v}\times m\mathbf{v}=\mathbf{0}
$$

なので消える。第2項で

$$
\frac{d\mathbf{p}}{dt}=\mathbf{F}
$$

を使うと

$$
\frac{d\mathbf{L}}{dt}=\mathbf{r}\times\mathbf{F}
$$

よって

$$
\frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}
$$

を得る。

これは回転運動の第一原理である。

---

## 3. 多粒子系への拡張

粒子

$$
i
$$

の角運動量を

$$
\mathbf{L}_i=\mathbf{r}_i\times\mathbf{p}_i
$$

とし、全角運動量を

$$
\mathbf{L}_{\mathrm{tot}}=\sum_i\mathbf{L}_i
$$

と置く。

時間微分すると

$$
\frac{d\mathbf{L}_{\mathrm{tot}}}{dt}=\sum_i\mathbf{r}_i\times\mathbf{F}_i
$$

力を外力と内力に分けると、中心力型の内力対は互いに打ち消し合い

$$
\frac{d\mathbf{L}_{\mathrm{tot}}}{dt}=\boldsymbol{\tau}_{\mathrm{ext}}
$$

となる。

したがって外力トルクがゼロなら

$$
\mathbf{L}_{\mathrm{tot}}=\text{const.}
$$

が成立する。

---

## 4. 原点依存性と注意

角運動量もトルクも原点に依存する。

- 保存判定をする前に、どの点まわりかを明示する。
- 外力トルクゼロは、その原点についての条件。

特に重力下の問題では、接地点・支点・重心のどれを原点に取るかで式の簡潔さが変わる。

---

## 5. 剛体近似との接続

剛体が固定軸まわりに回るとき

$$
L=I\omega
$$

$$
\tau=I\alpha
$$

が成り立つ。

これは一般式

$$
\frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}
$$

を固定軸へ射影した特別形である。

ここで

$$
I
$$

は慣性モーメント、

$$
\alpha
$$

は角加速度。

---

## 6. 例題

## 6.1 例題1：質点の瞬間角運動量

質点が

$$
\mathbf{r}=(a,0,0)
$$

にあり、速度

$$
\mathbf{v}=(0,v,0)
$$

で運動している。

$$
\mathbf{p}=m\mathbf{v}
$$

より

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

$$
\mathbf{L}=(a,0,0)\times(0,mv,0)=(0,0,amv)
$$

したがって

$$
L_z=amv
$$

である。

## 6.2 例題2：一定トルクでの角運動量変化

固定軸まわりで一定トルク

$$
\tau_0
$$

が時間

$$
\Delta t
$$

作用すると

$$
\Delta L=\int \tau\,dt=\tau_0\Delta t
$$

となる。これは回転版の力積・運動量関係である。

## 6.3 例題3：中心力での保存

中心力では

$$
\mathbf{F}\parallel\mathbf{r}
$$

なので

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}=\mathbf{0}
$$

ゆえに

$$
\frac{d\mathbf{L}}{dt}=\mathbf{0}
$$

すなわち

$$
\mathbf{L}=\text{const.}
$$

となる。これが軌道が1平面内に閉じる基礎理由になる。

---

## 7. よくある誤り

1. 角運動量をスカラーとして扱い、向きを落とす。
2. 原点を明示せずに保存判定する。
3. トルクゼロ条件を「力ゼロ」と混同する。
   - 力があっても作用線が原点を通ればトルクはゼロ。
4. 固定軸公式
   $$
   \tau=I\alpha
   $$
   を一般ベクトル式の代わりに無条件で使う。

---

## 8. まとめ

- 基本式は

$$
\frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}
$$

である。

- 外力トルクがゼロなら

$$
\mathbf{L}=\text{const.}
$$

が成立する。

- 実戦では「原点選択」と「トルクの向き判定」を先に行うと、回転問題の立式が大幅に安定する。
