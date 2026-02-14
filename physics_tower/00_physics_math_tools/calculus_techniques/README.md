# calculus_techniques（物理で使う微積分テクニック）

この章は、物理で頻出する微積分操作を「計算手順」ではなく、
**何を保存し、何を変数として追跡しているか** の観点で整理する入口です。

微積分は道具ですが、使い方には定石があります。
本章では EMAN-Physics 風に、

- 直観（何を見たいのか）
- 導出（途中式を省略しない）
- 確認（次元・符号・極限）

の順で学びます。

---

## 1. 学習目標

1. 偏微分・全微分・連鎖律の違いを物理量の依存関係で説明できる。
2. 積分（不定積分・定積分・部分積分）が「仕事」「作用」「平均値」にどう現れるか説明できる。
3. ヤコビアンを使った変数変換の意味を、体積要素の変形として理解できる。
4. 1つの式変形をしたら、次元と符号で検算する習慣を持てる。
5. 後続の実践ページ [partials_integrals_jacobian.md](partials_integrals_jacobian.md) に入る準備を完了できる。

## 2. 前提知識（必要最小セット）

- 1変数の微分積分（$\frac{d}{dx}$, $\int f(x)dx$）
- 三角関数・指数関数の基本微分
- ベクトルの成分表示（最低限）

未習熟なら、先に [../00_overview.md](../00_overview.md) を復習してから進むことを推奨します。

## 3. 記法・単位・符号規約

- 関数依存: $f(x,t)$（変数が複数あることを明示）
- 偏微分: $\partial_x f = \dfrac{\partial f}{\partial x}$
- 全微分（1変数関数）: $\dfrac{df}{dt}$
- 全微分（多変数関数）:
  $$
  \frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}+\cdots
  $$
- 積分区間は必ず書く（例: $\int_{t_1}^{t_2}$）
- 体積要素: $dV=dx\,dy\,dz$（座標変換後はヤコビアンを掛ける）

## 4. 本文（直観→導出→確認）

### 4.1 直観：微分は「感度」、積分は「累積」

- 微分は「入力を少し変えたとき、出力がどれだけ変わるか」
- 積分は「小さな寄与を足し合わせた総量」

物理では、

- 速度 $v=\dfrac{dx}{dt}$ は位置の時間感度
- 仕事 $W=\int \vec{F}\cdot d\vec{r}$ は力の寄与の累積

という対応になります。

### 4.2 導出：連鎖律と全微分（途中式あり）

状態量 $U=U(S,V)$ を時間の関数 $S(t),V(t)$ を通じて追跡するとき、

$$
U(t)=U(S(t),V(t))
$$

です。時間微分を取ると、連鎖律より

$$
\frac{dU}{dt}
=\frac{\partial U}{\partial S}\frac{dS}{dt}
+\frac{\partial U}{\partial V}\frac{dV}{dt}
$$

ここで

$$
T\equiv\left(\frac{\partial U}{\partial S}\right)_V,
\qquad
p\equiv-\left(\frac{\partial U}{\partial V}\right)_S
$$

と定義すれば

$$
\frac{dU}{dt}=T\frac{dS}{dt}-p\frac{dV}{dt}
$$

さらに両辺に $dt$ を掛けて

$$
dU=T\,dS-p\,dV
$$

を得ます。これは熱力学第一法則の微分形の典型例です。

#### 次元確認

- $[dU]=\mathrm{J}$
- $[T\,dS]=\mathrm{K}\cdot(\mathrm{J/K})=\mathrm{J}$
- $[p\,dV]=\mathrm{Pa}\cdot\mathrm{m^3}=\mathrm{N/m^2}\cdot\mathrm{m^3}=\mathrm{J}$

すべてエネルギー次元で一致します。

### 4.3 導出：部分積分が物理で現れる理由

積の微分

$$
\frac{d}{dx}(uv)=u\frac{dv}{dx}+v\frac{du}{dx}
$$

を区間 $[a,b]$ で積分すると

$$
\int_a^b \frac{d}{dx}(uv)\,dx
=\int_a^b u\frac{dv}{dx}\,dx+\int_a^b v\frac{du}{dx}\,dx
$$

左辺は基本定理で

$$
[uv]_a^b=\int_a^b u\,dv+\int_a^b v\,du
$$

したがって

$$
\int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du
$$

を得ます。これが部分積分です。

物理では、作用積分の変分や、電磁気のエネルギー表示で頻出します。  
境界項 $[uv]_a^b$ の扱い（固定端か自由端か）が物理条件と直結する点が重要です。

### 4.4 導出：ヤコビアンによる変数変換

2変数変換 $(x,y)\leftrightarrow(u,v)$ で

$$
x=x(u,v),\qquad y=y(u,v)
$$

とすると、面積要素は

$$
dx\,dy = \left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv
$$

ここで

$$
J\equiv \frac{\partial(x,y)}{\partial(u,v)}
=\begin{vmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v}\\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{vmatrix}
$$

がヤコビアンです。

例として極座標

$$
x=r\cos\theta,\qquad y=r\sin\theta
$$

なら

$$
J=
\begin{vmatrix}
\cos\theta & -r\sin\theta\\
\sin\theta & r\cos\theta
\end{vmatrix}
=r(\cos^2\theta+\sin^2\theta)=r
$$

ゆえに

$$
dx\,dy=r\,dr\,d\theta
$$

となります。

### 4.5 確認：検算テンプレ

1. 変数依存を明示したか（$f(x,t)$ か $f(x)$ か）。
2. 微分記号を取り違えていないか（$d$ と $\partial$）。
3. 積分区間・初期条件を書いたか。
4. 変数変換時にヤコビアンを掛けたか。
5. 次元・符号・極限で最終式を確認したか。

## 5. 例題（段階別）

### 例題1（易）：連鎖律

$f(x)=x^2,\ x(t)=3t+1$ のとき $\dfrac{df}{dt}$ を求めよ。

**解法**

$$
\frac{df}{dt}=\frac{df}{dx}\frac{dx}{dt}=2x\cdot 3=6x
$$

$x=3t+1$ を代入して

$$
\frac{df}{dt}=18t+6
$$

### 例題2（中）：部分積分

$$
I=\int_0^1 x e^x\,dx
$$

を求めよ。

**解法**  
$u=x,\ dv=e^x dx$ と置くと $du=dx,\ v=e^x$。

$$
I=[xe^x]_0^1-\int_0^1 e^x dx
=(e-0)-(e-1)=1
$$

### 例題3（やや難）：極座標での積分

単位円盤 $D: x^2+y^2\le1$ で

$$
\iint_D (x^2+y^2)\,dxdy
$$

を求めよ。

**解法**  
極座標で $x^2+y^2=r^2$, $dxdy=rdrd\theta$:

$$
\iint_D (x^2+y^2)dxdy
=\int_0^{2\pi}\int_0^1 r^2\cdot r\,drd\theta
=\int_0^{2\pi}\left[\frac{r^4}{4}\right]_0^1 d\theta
=\int_0^{2\pi}\frac14 d\theta
=\frac{\pi}{2}
$$

## 6. よくある誤解・落とし穴

1. **偏微分と全微分を混同する**  
   → 依存変数を明示してから微分する。
2. **部分積分で境界項を落とす**  
   → 境界条件がゼロにするのか、まず確認する。
3. **ヤコビアンを忘れる**  
   → 変数変換のときは「体積要素も変わる」が原則。
4. **計算だけ合っていて物理次元が崩れている**  
   → 最後に次元を必ず検算する。

## 7. 章末まとめ

- 微分は感度、積分は累積という直観を保持する。
- 多変数関数の時間変化は連鎖律で記述する。
- 部分積分は「境界項 + 内部積分」の分離操作である。
- 変数変換ではヤコビアンが面積・体積の伸縮を担う。
- 物理式では次元一致が最初の妥当性チェックになる。
- 計算ルールと物理条件（境界・初期条件）を同時に扱う。

## 8. 演習（10問）＋解答

難易度目安: 易4・中4・難2

### 問題

1. **易**: $y=x^3,\ x=2t$ のとき $dy/dt$ を求めよ。  
2. **易**: $f(x,t)=x^2t$ の $\partial f/\partial x$ と $\partial f/\partial t$ を求めよ。  
3. **易**: $\int_0^2 (3x+1)dx$ を計算せよ。  
4. **易**: $\int x\cos x\,dx$ を部分積分で求めよ。  
5. **中**: $U(S,V)=aS^2/V$（$a$定数）について $dU$ を求めよ。  
6. **中**: $I=\int_0^\pi x\sin x\,dx$ を求めよ。  
7. **中**: 極座標変換のヤコビアンを計算せよ。  
8. **中**: 円盤 $x^2+y^2\le R^2$ で $\iint 1\,dxdy$ を求めよ。  
9. **難**: $f(x,y)=x^2+y^2,\ x=u-v,\ y=u+v$ のとき $\partial(f)/\partial(u)$ を連鎖律で求めよ。  
10. **難**: 体積要素変換を用いて球座標の
   $$dV=r^2\sin\theta\,dr\,d\theta\,d\phi$$
   を示せ（概略で可）。

### 解答

1. **解答**:  
   $$\frac{dy}{dt}=\frac{dy}{dx}\frac{dx}{dt}=3x^2\cdot2=6x^2=24t^2$$

2. **解答**:  
   $$\frac{\partial f}{\partial x}=2xt,\qquad \frac{\partial f}{\partial t}=x^2$$

3. **解答**:  
   $$\int_0^2 (3x+1)dx=\left[\frac32x^2+x\right]_0^2=6+2=8$$

4. **解答**:  
   $u=x,\ dv=\cos xdx$ とすると
   $$\int x\cos xdx=x\sin x-\int\sin xdx=x\sin x+\cos x+C$$

5. **解答**:  
   $$dU=\frac{\partial U}{\partial S}dS+\frac{\partial U}{\partial V}dV
   =\frac{2aS}{V}dS-\frac{aS^2}{V^2}dV$$

6. **解答**:  
   $u=x,\ dv=\sin xdx$ として $v=-\cos x$:
   $$I=[-x\cos x]_0^\pi+\int_0^\pi \cos xdx=\pi+0=\pi$$

7. **解答**:  
   $$x=r\cos\theta,\ y=r\sin\theta\Rightarrow
   J=\begin{vmatrix}
   \cos\theta & -r\sin\theta\\
   \sin\theta & r\cos\theta
   \end{vmatrix}=r$$

8. **解答**:  
   面積そのものなので
   $$\iint_{x^2+y^2\le R^2}1\,dxdy=\pi R^2$$

9. **解答**:  
   まず $f=(u-v)^2+(u+v)^2=2u^2+2v^2$ なので
   $$\frac{\partial f}{\partial u}=4u$$
   （連鎖律で計算しても同じ）。

10. **解答（概略）**:  
    球座標
    $$x=r\sin\theta\cos\phi,\ y=r\sin\theta\sin\phi,\ z=r\cos\theta$$
    のヤコビアン行列の行列式を計算すると
    $$\left|\frac{\partial(x,y,z)}{\partial(r,\theta,\phi)}\right|=r^2\sin\theta$$
    よって
    $$dV=r^2\sin\theta\,dr\,d\theta\,d\phi$$

---

## ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 子:
  - [partials_integrals_jacobian.md](partials_integrals_jacobian.md)
