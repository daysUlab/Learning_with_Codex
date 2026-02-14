# 00_physics_math_tools（物理数学ツール概観）

物理を学ぶときに必要な数学は、**「難しい順」ではなく「使う順」** で整理すると理解が速くなります。  
この章では、後続の力学・電磁気・量子で共通に使う道具を、

- 直観（なぜ要るのか）
- 式（どう書くのか）
- 確認（どこを検算するか）

の順に揃えます。

---

## 1. 学習目標

この章を読み終えると、次ができるようになります。

1. 物理で使う数学分野（微積・線形代数・ベクトル解析・微分方程式・誤差解析）の役割を説明できる。
2. どの現象にどの道具を選ぶべきかを、方程式の形から判断できる。
3. 次元解析とオーダー評価（桁見積もり）で式の妥当性を素早くチェックできる。
4. 「微分方程式を解く→初期条件を入れる→極限で確認する」という共通手順を実行できる。
5. 後続章への準備として、最低限の記法・単位・符号規約を統一できる。

## 2. 前提知識（最小セット）

最低限、以下が分かっていれば読み進められます。

- 高校数学の関数・三角関数・指数対数
- 1変数微分積分（$\frac{d}{dx}$, $\int dx$）
- ベクトルの成分表示（$\vec{a}=(a_x,a_y,a_z)$）

不安がある場合は、先に次を併読してください。

- [calculus_techniques/README.md](calculus_techniques/README.md)
- [linear_algebra/README.md](linear_algebra/README.md)
- [vector_analysis/README.md](vector_analysis/README.md)
- [differential_equations/README.md](differential_equations/README.md)
- [experiment/README.md](experiment/README.md)

## 3. 記法・単位・符号規約

### 3.1 記法

- スカラー: $m, t, E, T, p$
- ベクトル: $\vec{r}, \vec{v}, \vec{F}, \vec{E}, \vec{B}$
- 行列: $A, M$
- 転置: $A^\mathsf{T}$
- 内積: $\vec{a}\cdot\vec{b}$
- 外積: $\vec{a}\times\vec{b}$
- 偏微分: $\partial_i f = \frac{\partial f}{\partial x_i}$
- ナブラ: $\nabla=(\partial_x,\partial_y,\partial_z)$

### 3.2 単位系

基本は SI 単位系を採用します。

$$
[\text{長さ}] = \mathrm{m},\quad
[\text{質量}] = \mathrm{kg},\quad
[\text{時間}] = \mathrm{s}
$$

必要に応じて派生単位を使います。

$$
1\ \mathrm{N}=1\ \mathrm{kg\,m/s^2},\qquad
1\ \mathrm{J}=1\ \mathrm{kg\,m^2/s^2}
$$

### 3.3 符号規約

- 座標軸の正方向は最初に宣言する。
- ポテンシャルと力の関係は
  $$\vec{F}=-\nabla U$$
  を基本とする。
- フーリエ変換の符号は章ごとに明示（量子・電磁気で差が出るため）。

## 4. 本文（直観→導出→確認）

### 4.1 直観：道具の対応表を持つ

物理では、現象に応じて「道具」を切り替えます。

- 変化率を見る → 微分
- 累積量を見る → 積分
- 多成分の連立を見る → 線形代数
- 場の性質を見る → ベクトル解析
- 時間発展を求める → 微分方程式
- 実験値の信頼性を見る → 誤差解析

この対応表を先に頭に置くと、式変形が「目的を失った計算」になりません。

### 4.2 導出：物理で最頻出の最小チェーン

物理の導出で最も頻出する流れを、1自由度の運動方程式で確認します。

$$
m\ddot{x}+\gamma\dot{x}+kx=0
$$

ここで、

- $m$ は質量
- $\gamma$ は粘性減衰係数
- $k$ はばね定数

です。

#### (i) 次元チェック

各項の次元を揃えます。

$$
[m\ddot{x}] = \mathrm{kg\cdot m/s^2}=\mathrm{N}
$$
$$
[\gamma\dot{x}] = [\gamma]\,\mathrm{m/s}
$$

よって $[\gamma]=\mathrm{kg/s}$ であれば第2項も N になります。さらに

$$
[kx]=[k]\,\mathrm{m}
$$

より $[k]=\mathrm{kg/s^2}$（=N/m）で整合。

#### (ii) 特性方程式

試行解 $x=e^{rt}$ を代入すると

$$
m r^2 e^{rt}+\gamma r e^{rt}+k e^{rt}=0
$$

$e^{rt}\neq 0$ より

$$
mr^2+\gamma r+k=0
$$

二次方程式の解は

$$
r=\frac{-\gamma\pm\sqrt{\gamma^2-4mk}}{2m}
$$

#### (iii) 場合分け

判別式 $\Delta=\gamma^2-4mk$ で挙動が分かれる。

- $\Delta>0$: 過減衰（指数2本）
- $\Delta=0$: 臨界減衰（重解）
- $\Delta<0$: 不足減衰（振動しながら減衰）

不足減衰では

$$
r=-\frac{\gamma}{2m}\pm i\omega_d,
\qquad
\omega_d=\sqrt{\frac{k}{m}-\left(\frac{\gamma}{2m}\right)^2}
$$

したがって

$$
x(t)=e^{-\gamma t/(2m)}\left(C_1\cos\omega_d t + C_2\sin\omega_d t\right)
$$

を得る。

### 4.3 確認：極限で物理に戻る

- 減衰なし極限 $\gamma\to 0$:
  $$x(t)=C_1\cos\sqrt{k/m}\,t + C_2\sin\sqrt{k/m}\,t$$
  となり、単振動に一致。
- ばねなし極限 $k\to 0$:
  速度が指数的に落ちる運動に移行し、粘性抵抗だけの直観と一致。
- 次元確認: $\omega_d$ の次元は $\mathrm{s^{-1}}$。

このように、**極限確認は導出の最終検算** です。

## 5. 例題（少なくとも3つ）

### 例題1（易）：次元解析で係数の単位を求める

式

$$
F = c v^2
$$

で $c$ の単位を求めよ。

**解法**

$$
[c] = \frac{[F]}{[v]^2}
=\frac{\mathrm{kg\,m/s^2}}{(\mathrm{m/s})^2}
=\mathrm{kg/m}
$$

**確認**: 抵抗力モデルで現れる密度や断面積の組合せと同じ次元になり妥当。

### 例題2（中）：連立一次方程式を行列で解く

未知数 $x,y$ について

$$
\begin{cases}
2x+y=5\\
x- y=1
\end{cases}
$$

を解け。

**解法**

$$
\begin{pmatrix}
2 & 1\\
1 & -1
\end{pmatrix}
\begin{pmatrix}
x\\y
\end{pmatrix}
=
\begin{pmatrix}
5\\1
\end{pmatrix}
$$

第2式より $x=1+y$。第1式に代入:

$$
2(1+y)+y=5 \Rightarrow 3y=3 \Rightarrow y=1,
$$
$$
x=2
$$

### 例題3（中〜難）：単純な常微分方程式

$$
\frac{dN}{dt}=-\lambda N,\qquad N(0)=N_0
$$

を解け。

**解法**

変数分離すると

$$
\frac{dN}{N}=-\lambda dt
$$

積分して

$$
\ln|N|=-\lambda t + C
$$

指数を取り

$$
N=C' e^{-\lambda t}
$$

初期条件 $N(0)=N_0$ より $C'=N_0$:

$$
N(t)=N_0 e^{-\lambda t}
$$

**確認**: $t=0$ で $N_0$、$\lambda>0$ なら時間とともに減少。

## 6. よくある誤解・落とし穴

1. **「微分方程式を解けば終わり」**  
   → 物理では初期条件・境界条件を入れて初めて解が確定する。
2. **次元が違う項を足してしまう**  
   → 和の各項は必ず同じ次元でなければならない。
3. **ベクトルをスカラー扱いする**  
   → 方向情報を落とすと符号ミスではなく概念ミスになる。
4. **検算を数値代入だけで済ませる**  
   → 極限（$t\to0$, パラメータ$\to0$）確認を入れると強い。

## 7. 章末まとめ

- 物理数学は「難しさ」より「使いどころ」で整理する。
- 微分・積分は変化率と累積量を結ぶ基本ペアである。
- 線形代数は連立方程式と固有値問題を統一的に扱える。
- ベクトル解析は場の方程式（電磁気・流体）の共通言語である。
- 微分方程式は初期条件とセットで物理予測を与える。
- 次元解析と極限確認は、式の健全性チェックとして必須。
- 実験データでは誤差評価が理論式と同じくらい重要。

## 8. 演習（8〜15問）＋解答

難易度配分: 易4・中4・難2

### 問題

1. **易**: $x=v_0t+\frac12at^2$ の各項の次元を示せ。  
2. **易**: $E=\frac12mv^2$ の次元がジュールと一致することを示せ。  
3. **易**: $\vec{a}=(1,2,3),\ \vec{b}=(2,0,-1)$ の内積 $\vec{a}\cdot\vec{b}$ を求めよ。  
4. **易**: $\frac{dy}{dx}=3x^2$ を積分して一般解を求めよ。  
5. **中**: $\frac{dT}{dt}=-k(T-T_\mathrm{env})$ を解け（$T(0)=T_0$）。  
6. **中**: 行列
   $$A=\begin{pmatrix}2&0\\0&5\end{pmatrix}$$
   の固有値を求めよ。  
7. **中**: $x''+4x=0$ の一般解を求めよ。  
8. **中**: $\nabla\cdot\vec{F}$ を、$\vec{F}=(x^2,xy,z)$ に対して求めよ。  
9. **難**: 減衰振動 $m\ddot{x}+\gamma\dot{x}+kx=0$ の臨界減衰条件を導け。  
10. **難**: $\omega_d=\sqrt{k/m-(\gamma/2m)^2}$ の次元が $\mathrm{s^{-1}}$ であることを示せ。  

### 解答

1. **解答**:  
   $[x]=\mathrm{L}$、$[v_0t]=\mathrm{(L/T)T}=\mathrm{L}$、$[at^2]=\mathrm{(L/T^2)T^2}=\mathrm{L}$。

2. **解答**:  
   $$\left[\frac12mv^2\right]=\mathrm{kg}(\mathrm{m/s})^2=\mathrm{kg\,m^2/s^2}=\mathrm{J}$$

3. **解答**:  
   $$\vec{a}\cdot\vec{b}=1\cdot2+2\cdot0+3\cdot(-1)=-1$$

4. **解答**:  
   $$y=\int 3x^2dx=x^3+C$$

5. **解答**:  
   $\theta=T-T_\mathrm{env}$ と置くと $\dot\theta=-k\theta$。  
   $$\theta(t)=\theta_0e^{-kt}=(T_0-T_\mathrm{env})e^{-kt}$$
   よって
   $$T(t)=T_\mathrm{env}+(T_0-T_\mathrm{env})e^{-kt}$$

6. **解答**:  
   対角行列なので固有値は対角成分そのもの。  
   $$\lambda_1=2,\ \lambda_2=5$$

7. **解答**:  
   特性方程式 $r^2+4=0\Rightarrow r=\pm2i$。  
   $$x(t)=C_1\cos 2t + C_2\sin 2t$$

8. **解答**:  
   $$\nabla\cdot\vec{F}=\frac{\partial x^2}{\partial x}+\frac{\partial (xy)}{\partial y}+\frac{\partial z}{\partial z}=2x+x+1=3x+1$$

9. **解答**:  
   特性方程式 $mr^2+\gamma r+k=0$ が重解になる条件は判別式0。  
   $$\gamma^2-4mk=0\Rightarrow \gamma=2\sqrt{mk}$$
   （$\gamma>0$ を採用）。

10. **解答**:  
    $$\left[\frac{k}{m}\right]=\frac{\mathrm{kg/s^2}}{\mathrm{kg}}=\mathrm{s^{-2}},\quad
    \left[\left(\frac{\gamma}{2m}\right)^2\right]=\left(\frac{\mathrm{kg/s}}{\mathrm{kg}}\right)^2=\mathrm{s^{-2}}$$
    したがって平方根を取って
    $$[\omega_d]=\mathrm{s^{-1}}$$

---

## ナビゲーション

- 親: [../README.md](../README.md)
- 子:
  - [calculus_techniques/README.md](calculus_techniques/README.md)
  - [calculus_techniques/partials_integrals_jacobian.md](calculus_techniques/partials_integrals_jacobian.md)
  - [complex_analysis/README.md](complex_analysis/README.md)
  - [complex_analysis/residue_theorem_minimum.md](complex_analysis/residue_theorem_minimum.md)
  - [differential_equations/README.md](differential_equations/README.md)
  - [differential_equations/ode_methods.md](differential_equations/ode_methods.md)
  - [experiment/README.md](experiment/README.md)
  - [experiment/errors_significant_digits.md](experiment/errors_significant_digits.md)
  - [linear_algebra/README.md](linear_algebra/README.md)
  - [linear_algebra/basics.md](linear_algebra/basics.md)
  - [vector_analysis/README.md](vector_analysis/README.md)
  - [vector_analysis/nabla_identities.md](vector_analysis/nabla_identities.md)
