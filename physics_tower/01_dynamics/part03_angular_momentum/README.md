# part03_angular_momentum（角運動量保存）

角運動量保存は、回転運動を理解するための中核です。
直線運動での運動量保存に対応する「回転版の保存則」として、

- 中心力運動
- 剛体回転
- 慣性モーメント変化

を一本の見方でつなげられるのが強みです。

## 1. 学習目標

1. 角運動量

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

とトルク

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}
$$

の関係を説明できる。
2. 外トルクゼロ条件から角運動量保存を導出できる。
3. 中心力運動で面積速度一定と結びつけて理解できる。
4. 回転体で

$$
I\omega=\text{const.}
$$

を正しく使える。

## 2. 基本式

角運動量

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

トルク

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}
$$

運動方程式

$$
\frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}
$$

外トルクゼロなら

$$
\mathbf{L}=\text{const.}
$$

剛体回転（固定軸）

$$
L=I\omega
$$

## 3. 直観：なぜ保存されるのか

角運動量保存は「回転に対する外からのねじりの総量」がゼロなら成り立ちます。
直線運動での「外力ゼロなら運動量保存」と完全に平行な構造です。

- 外力があっても、その作用線が回転中心を通ればトルクはゼロ。
- 力の大きさより「腕の長さ（モーメントアーム）」が効く。

という点が、初学者がつまずきやすいポイントです。

## 4. 中心力との接続

中心力では

$$
\mathbf{F}\parallel\mathbf{r}
$$

なので

$$
\mathbf{r}\times\mathbf{F}=\mathbf{0}
$$

よって

$$
\mathbf{L}=\text{const.}
$$

さらに面積速度

$$
\frac{dA}{dt}=\frac{L}{2m}
$$

が一定となり、ケプラー第2法則に接続します。

## 5. 例題（2題）

### 例題1（中心力）

質量

$$
m
$$

の質点が中心力場で運動する。角運動量保存が成り立つことを示せ。

**解答**

$$
\frac{d\mathbf{L}}{dt}=\mathbf{r}\times\mathbf{F}
$$

中心力より

$$
\mathbf{r}\times\mathbf{F}=\mathbf{0}
$$

したがって

$$
\frac{d\mathbf{L}}{dt}=\mathbf{0}
$$

ゆえに

$$
\mathbf{L}=\text{const.}
$$

### 例題2（慣性モーメント変化）

外トルクが働かない回転体で、慣性モーメントが

$$
I_1
$$

から

$$
I_2
$$

へ変化した。角速度比を求めよ。

**解答**

$$
I_1\omega_1=I_2\omega_2
$$

$$
\frac{\omega_2}{\omega_1}=\frac{I_1}{I_2}
$$

## 6. よくある誤り

1. 力があるから保存しない、と即断してしまう。
   → 判定すべきは力そのものではなくトルク。
2. 回転中心の取り方を曖昧にして符号を誤る。
3. ベクトル量を大きさだけで扱って向きの情報を捨てる。

## 7. 子mdの学習導線

- [01_torque_and_L.md](01_torque_and_L.md)
  定義と最小導出を確認。
- [02_central_force.md](02_central_force.md)
  中心力での保存と面積速度へ接続。
- [03_inertia_change.md](03_inertia_change.md)
  回転体での実用式へ展開。

## 8. ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 前: [../part02_energy_conservation/README.md](../part02_energy_conservation/README.md)
- 次: [../part04_applications/README.md](../part04_applications/README.md)

## 9. 参考（学習補助）

- EMANの物理学（力学）: https://eman-physics.net/mechanics/
