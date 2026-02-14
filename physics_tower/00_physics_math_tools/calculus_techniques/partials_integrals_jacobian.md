# partials_integrals_jacobian（偏微分・部分積分・ヤコビアン実践）

このページは、微積分テクニックの中でも物理で特に使用頻度が高い

- 偏微分
- 部分積分
- ヤコビアン

の3本柱を、**1つずつ手で再導出できる状態** にすることを目的にした実践ノートです。

---

## 1. 学習目標

1. 偏微分と全微分の使い分けを式で説明できる。
2. 部分積分を境界項の意味まで含めて使える。
3. 2変数・3変数のヤコビアンを計算し、積分変数変換に適用できる。
4. 次元解析・符号チェック・極限確認で導出を検算できる。
5. 力学・電磁気・統計の後続章で同手法を再利用できる。

## 2. 前提知識

- [README.md](README.md) の内容（連鎖律、基本積分、極座標）
- 1変数の積分計算
- 行列式 $2\times2$, $3\times3$ の計算

## 3. 記法・単位・符号規約

- 偏微分: $\partial_x f\equiv\dfrac{\partial f}{\partial x}$
- 全微分: $df=\sum_i \dfrac{\partial f}{\partial q_i}dq_i$
- ヤコビアン:
  $$
  J=\frac{\partial(x_1,\dots,x_n)}{\partial(u_1,\dots,u_n)}
  $$
- 変数変換の積分測度:
  $$
  d^n x = |J|\,d^n u
  $$
- 単位は SI 基準、最終結果で次元整合を確認する。

## 4. 本文（直観→導出→確認）

### 4.1 直観

- 偏微分は「他を固定した局所感度」。
- 部分積分は「微分を片方へ移して境界項を取り出す操作」。
- ヤコビアンは「座標変換で体積要素が何倍に伸縮するか」。

この3つは、実はすべて「何を固定し、どこを移すか」の管理問題です。

### 4.2 導出A：偏微分と全微分

状態関数 $f(x,y)=x^2y+\sin y$ を考える。

偏微分は

$$
\frac{\partial f}{\partial x}=2xy,
\qquad
\frac{\partial f}{\partial y}=x^2+\cos y
$$

全微分は

$$
df=\frac{\partial f}{\partial x}dx+\frac{\partial f}{\partial y}dy
=(2xy)dx+(x^2+\cos y)dy
$$

ここで $x=x(t),y=y(t)$ なら

$$
\frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}
$$

となる。

#### 確認

- $dy=0$ なら $df=(\partial f/\partial x)dx$ に戻る。
- $dx=0$ なら $df=(\partial f/\partial y)dy$ に戻る。

### 4.3 導出B：部分積分と境界項

まず積の微分式

$$
\frac{d}{dx}(uv)=u\frac{dv}{dx}+v\frac{du}{dx}
$$

を $[a,b]$ で積分:

$$
\int_a^b\frac{d}{dx}(uv)dx=\int_a^b u\,dv+\int_a^b v\,du
$$

左辺は

$$
[uv]_a^b
$$

なので

$$
\int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du
$$

#### 物理での意味

ラグランジュ形式の変分で

$$
\delta S=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}\delta q+\frac{\partial L}{\partial \dot q}\delta\dot q\right)dt
$$

第2項を部分積分すると

$$
\int_{t_1}^{t_2}\frac{\partial L}{\partial \dot q}\delta\dot q\,dt
=\left[\frac{\partial L}{\partial \dot q}\delta q\right]_{t_1}^{t_2}
-\int_{t_1}^{t_2}\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q}\right)\delta q\,dt
$$

端点固定 $\delta q(t_1)=\delta q(t_2)=0$ なら境界項が消え、オイラー・ラグランジュ方程式へ進める。

### 4.4 導出C：ヤコビアン

#### 2次元（極座標）

$$
x=r\cos\theta,\quad y=r\sin\theta
$$

なので

$$
J=\frac{\partial(x,y)}{\partial(r,\theta)}=
\begin{vmatrix}
\cos\theta & -r\sin\theta\\
\sin\theta & r\cos\theta
\end{vmatrix}=r
$$

よって

$$
dxdy=r\,drd\theta
$$

#### 3次元（球座標）

$$
x=r\sin\theta\cos\phi,
\ y=r\sin\theta\sin\phi,
\ z=r\cos\theta
$$

の行列式計算より

$$
\left|\frac{\partial(x,y,z)}{\partial(r,\theta,\phi)}\right|=r^2\sin\theta
$$

したがって

$$
dV=dx\,dy\,dz=r^2\sin\theta\,dr\,d\theta\,d\phi
$$

### 4.5 確認テンプレ

1. 固定する変数を先に書く。
2. 積分区間・境界条件を先に書く。
3. 変数変換で測度（$dxdy$ など）まで更新する。
4. 最後に次元を確認する。

## 5. 例題（3題）

### 例題1（易）

$f(x,y)=x^3y^2$ の $\partial f/\partial x$, $\partial f/\partial y$ を求めよ。

**解答**

$$
\frac{\partial f}{\partial x}=3x^2y^2,
\qquad
\frac{\partial f}{\partial y}=2x^3y
$$

### 例題2（中）

$$
I=\int_0^1 x\ln x\,dx
$$

を求めよ。

**解答**  
$u=\ln x,\ dv=x\,dx$ とすると $du=dx/x,\ v=x^2/2$。

$$
I=\left[\frac{x^2}{2}\ln x\right]_0^1-\int_0^1\frac{x^2}{2}\cdot\frac{1}{x}dx
=0-\frac12\int_0^1 xdx=-\frac14
$$

### 例題3（やや難）

$$
\iint_{x^2+y^2\le a^2}(x^2+y^2)\,dxdy
$$

を求めよ。

**解答**  
極座標で $x^2+y^2=r^2$, $dxdy=rdrd\theta$。

$$
\int_0^{2\pi}\int_0^a r^2\cdot r\,drd\theta
=2\pi\left[\frac{r^4}{4}\right]_0^a
=\frac{\pi a^4}{2}
$$

## 6. よくある誤解・落とし穴

1. 偏微分なのに暗黙に他変数を時間依存で扱ってしまう。
2. 部分積分で境界項の評価を省略する。
3. ヤコビアンの絶対値を忘れる（向き反転変換で符号を誤る）。
4. $dxdy$ をそのまま残して変数だけ $r,\theta$ に変える。

## 7. 章末まとめ

- 偏微分は固定条件を明示して初めて意味が定まる。
- 全微分は連鎖律の圧縮表現。
- 部分積分は「内部項」と「境界項」を分離する道具。
- 物理では境界項が条件設定そのものになる。
- ヤコビアンは積分測度のスケール因子である。
- 変数変換では被積分関数と測度の両方を変換する。

## 8. 演習（10問）＋解答

難易度比: 易4・中4・難2

### 問題

1. **易**: $f(x,y)=x^2+xy$ の $\partial f/\partial x,\partial f/\partial y$。  
2. **易**: $f(x,y)=e^{xy}$ の $\partial f/\partial x$。  
3. **易**: $\int_0^1 x^2dx$ を求めよ。  
4. **易**: $\int_0^1 xe^x dx$ を部分積分で求めよ。  
5. **中**: $f(x,y)=x^2y$ の全微分 $df$ を書け。  
6. **中**: $\int_0^{\pi} x\cos x\,dx$ を計算せよ。  
7. **中**: $x=r\cos\theta,y=r\sin\theta$ でヤコビアンを求めよ。  
8. **中**: $\iint_{x^2+y^2\le1}1\,dxdy$ を極座標で求めよ。  
9. **難**: $x=u+v,y=u-v$ のヤコビアンを求め、$dxdy$ を $dudv$ で表せ。  
10. **難**: $I=\int_0^1 x(\ln x)^2dx$ を部分積分2回で求めよ。  

### 解答

1. **解答**:  
   $$\frac{\partial f}{\partial x}=2x+y,\quad \frac{\partial f}{\partial y}=x$$

2. **解答**:  
   $$\frac{\partial}{\partial x}e^{xy}=ye^{xy}$$

3. **解答**:  
   $$\int_0^1x^2dx=\left[\frac{x^3}{3}\right]_0^1=\frac13$$

4. **解答**:  
   $$\int_0^1xe^xdx=[xe^x]_0^1-\int_0^1e^xdx=e-(e-1)=1$$

5. **解答**:  
   $$df=\frac{\partial f}{\partial x}dx+\frac{\partial f}{\partial y}dy=2xy\,dx+x^2\,dy$$

6. **解答**:  
   $$\int_0^{\pi}x\cos xdx=[x\sin x]_0^{\pi}-\int_0^{\pi}\sin xdx=-2$$

7. **解答**:  
   $$J=\begin{vmatrix}\cos\theta&-r\sin\theta\\\sin\theta&r\cos\theta\end{vmatrix}=r$$

8. **解答**:  
   $$\int_0^{2\pi}\int_0^1 r\,drd\theta=2\pi\cdot\frac12=\pi$$

9. **解答**:  
   $$\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}1&1\\1&-1\end{vmatrix}=-2$$
   よって
   $$dxdy=|{-2}|dudv=2dudv$$

10. **解答**:  
    $u=(\ln x)^2,\ dv=xdx$ として積分すると
    $$I=\left[\frac{x^2}{2}(\ln x)^2\right]_0^1-\int_0^1x\ln x\,dx=-\int_0^1x\ln x\,dx$$
    さらに既知の
    $$\int_0^1x\ln x\,dx=-\frac14$$
    より
    $$I=\frac14$$

---

## ナビゲーション

- 親: [README.md](README.md)
