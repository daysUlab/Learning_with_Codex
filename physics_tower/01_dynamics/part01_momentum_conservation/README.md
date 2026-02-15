# part01_momentum_conservation（運動量保存）

運動量保存は、力学の中でも「短時間の相互作用」を扱う場面で特に強力です。
衝突・反跳・爆発のように、力の時間変化を細かく追うのが難しいときでも、系全体の見方を適切に選べば問題を短く解けます。

## 1. 学習目標

1. 運動量保存則を運動方程式から導出できる。
2. 弾性衝突・非弾性衝突の式を正しく使い分けられる。
3. 重心系を使って計算を簡略化できる。
4. 解答後に、次元と極限で妥当性を点検できる。

## 2. 基本式

運動量の定義

$$
\mathbf{p}=m\mathbf{v}
$$

系全体の運動量

$$
\mathbf{P}=\sum_i \mathbf{p}_i
$$

時間変化

$$
\frac{d\mathbf{P}}{dt}=\mathbf{F}_{\text{ext}}
$$

外力和がゼロのとき

$$
\mathbf{P}=\text{const.}
$$

## 3. 直観：なぜ衝突で効くのか

衝突中の接触力は非常に大きく、時間変化も急激です。個々の力を時間積分する代わりに、

- 系を2物体まとめて取る
- 外力が無視できる短時間区間に限定する

ことで、運動量保存を直接使えます。これは「力の詳細を捨てても、積分された効果は保存則で押さえられる」という見方です。

## 4. 典型パターン

### 4.1 弾性衝突

$$
\mathbf{P}_{\text{before}}=\mathbf{P}_{\text{after}}
$$

$$
K_{\text{before}}=K_{\text{after}}
$$

### 4.2 完全非弾性衝突

$$
\mathbf{P}_{\text{before}}=\mathbf{P}_{\text{after}}
$$

$$
K_{\text{before}}>K_{\text{after}}
$$

### 4.3 爆発・分裂

初期静止なら

$$
\sum_i \mathbf{p}_i=\mathbf{0}
$$

で、各破片の運動量はベクトル和で打ち消し合います。

## 5. 例題（2題）

### 例題1（1次元・完全非弾性）

質量

$$
m
$$

の物体が速度

$$
u
$$

で進み、静止していた質量

$$
2m
$$

と衝突して合体する。合体後速度を求めよ。

**解答**

$$
mu=(m+2m)V
$$

$$
V=\frac{u}{3}
$$

### 例題2（爆発）

初期静止の物体が2つに分裂し、片方（質量

$$
2m
$$

）が速度

$$
\mathbf{v}
$$

で飛び出した。もう片方（質量

$$
m
$$

）の速度を求めよ。

**解答**

$$
2m\mathbf{v}+m\mathbf{v}_2=\mathbf{0}
$$

$$
\mathbf{v}_2=-2\mathbf{v}
$$

## 6. 学習の落とし穴

1. 外力を無視できない時間区間まで保存則を適用してしまう。
2. ベクトル式を成分式に落とさず符号を誤る。
3. 「弾性衝突」と「運動量保存」を混同し、エネルギー保存を常に使ってしまう。

## 7. 子mdの学習導線

- [01_derivation.md](01_derivation.md)
  導出の最小骨格を確認。
- [02_collision_patterns.md](02_collision_patterns.md)
  衝突の型を比較。
- [03_center_of_mass.md](03_center_of_mass.md)
  重心系での見通し改善を確認。

## 8. ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 前: [../columns_and_qa/README.md](../columns_and_qa/README.md)
- 次: [../part02_energy_conservation/README.md](../part02_energy_conservation/README.md)

## 9. 参考（学習補助）

- EMANの物理学（力学）: https://eman-physics.net/mechanics/
