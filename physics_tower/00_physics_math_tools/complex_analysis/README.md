# complex_analysis（物理で使う複素解析の入口）

複素解析は「難しい積分テクニック」ではなく、**対称性と解析性を使って実積分を整理する道具**です。  
量子力学・電磁気学・統計力学では、振動・減衰・応答関数を扱うときに複素数表示がほぼ標準になります。

この章では、

- 直観（なぜ複素数を使うのか）
- 導出（コーシー積分公式→留数定理）
- 確認（極限・次元・向きの符号）

の順で、最小限だけど手を動かせる形に整理します。

---

## 1. 学習目標

1. 複素関数の解析性（正則性）の意味を、実部・虚部の連立条件として説明できる。
2. 閉曲線積分と留数定理を使って、実積分の値を求められる。
3. 極（pole）の位数と留数の計算を、1位極・2位極で使い分けできる。
4. 物理で頻出の $e^{i\omega t}$ 表示とコサイン/サイン表示の対応を扱える。
5. 後続ページ [residue_theorem_minimum.md](residue_theorem_minimum.md) での計算を自力で再現できる。

## 2. 前提知識（必要最小セット）

- 実関数の微積分
- 三角関数とオイラー公式
  $$e^{i\theta}=\cos\theta+i\sin\theta$$
- 有理関数の部分分数分解

補助的に以下を参照:

- [../calculus_techniques/README.md](../calculus_techniques/README.md)
- [../00_overview.md](../00_overview.md)

## 3. 記法・単位・符号規約

- 複素数: $z=x+iy$（$x,y\in\mathbb{R}$）
- 共役: $\bar z=x-iy$
- 絶対値: $|z|=\sqrt{x^2+y^2}$
- 正則関数: $f(z)$ が領域内で複素微分可能
- 閉曲線積分: $\oint_C f(z)dz$
- 留数: $\operatorname{Res}(f,z_0)$
- 積分路の向き: 反時計回りを正向き（標準）

物理での時間依存は多くの場合

$$
e^{-i\omega t}
$$

規約も使うので、章ごとに必ず符号を明示します（本章では $e^{+i\omega t}$ 側で説明）。

## 4. 本文（直観→導出→確認）

### 4.1 直観：なぜ実積分を複素平面へ拡張するか

例えば実積分

$$
I=\int_{-\infty}^{\infty}\frac{\cos ax}{x^2+1}dx
$$

を直接計算するのは面倒です。そこで

$$
\cos ax = \Re\left(e^{iax}\right)
$$

を使って、まず

$$
J=\int_{-\infty}^{\infty}\frac{e^{iaz}}{z^2+1}dz
$$

を複素平面で計算し、最後に実部を取ると効率が良い。  
要するに「実関数の積分を、極の情報（局所情報）に圧縮する」のが複素解析の強みです。

### 4.2 導出A：コーシー積分公式から留数定理へ

正則関数 $g(z)$ と単純閉曲線 $C$ に対して、内部点 $z_0$ について

$$
g(z_0)=\frac{1}{2\pi i}\oint_C\frac{g(z)}{z-z_0}dz
$$

が成立（コーシー積分公式）。

有理関数 $f(z)$ が有限個の孤立特異点 $z_k$ を持つとき、各点の主部係数（$1/(z-z_k)$ の係数）が留数。したがって

$$
\oint_C f(z)dz = 2\pi i\sum_{z_k\in\mathrm{Int}(C)}\operatorname{Res}(f,z_k)
$$

を得ます。これが留数定理。

#### 1位極の留数

$$
\operatorname{Res}(f,z_0)=\lim_{z\to z_0}(z-z_0)f(z)
$$

#### 2位極（一般 $m$ 位極）

$$
\operatorname{Res}(f,z_0)=\frac{1}{(m-1)!}\lim_{z\to z_0}\frac{d^{m-1}}{dz^{m-1}}\left[(z-z_0)^m f(z)\right]
$$

### 4.3 導出B：代表積分を実際に計算

$$
I(a)=\int_{-\infty}^{\infty}\frac{\cos ax}{x^2+1}dx\qquad(a>0)
$$

を計算する。

複素積分

$$
J(a)=\int_{-\infty}^{\infty}\frac{e^{iaz}}{z^2+1}dz
$$

を上半平面半円で閉じる。$a>0$ では $e^{iaz}=e^{ia(x+iy)}=e^{iax}e^{-ay}$ なので上半平面で減衰し、半円弧寄与は 0（Jordan の補題の典型）とみなせる。

上半平面内の極は $z=i$ のみ。

$$
\operatorname{Res}\left(\frac{e^{iaz}}{z^2+1},i\right)
=\lim_{z\to i}\frac{e^{iaz}}{z+i}
=\frac{e^{iai}}{2i}
=\frac{e^{-a}}{2i}
$$

よって

$$
J(a)=2\pi i\cdot\frac{e^{-a}}{2i}=\pi e^{-a}
$$

$J(a)$ は実数なので

$$
I(a)=\Re J(a)=\pi e^{-a}
$$

を得る。

### 4.4 確認：符号・極限・次元

- $a\to 0^+$ で
  $$I(0)=\int_{-\infty}^{\infty}\frac{dx}{x^2+1}=\pi$$
  と一致。
- $a\to\infty$ で $I(a)\to0$。振動平均の直観と一致。
- 被積分関数が偶関数であること（実積分側）とも整合。

## 5. 例題（段階別）

### 例題1（易）: オイラー公式の実部・虚部

$e^{i\theta}$ の実部と虚部を答えよ。

**解答**

$$
\Re(e^{i\theta})=\cos\theta,
\qquad
\Im(e^{i\theta})=\sin\theta
$$

### 例題2（中）: 単純極の留数

$$
f(z)=\frac{1}{(z-1)(z+2)}
$$

の $z=1$ における留数を求めよ。

**解答**

$$
\operatorname{Res}(f,1)=\lim_{z\to1}\frac{z-1}{(z-1)(z+2)}=\frac{1}{3}
$$

### 例題3（やや難）: 実積分

$$
\int_{-\infty}^{\infty}\frac{dx}{x^2+4}
$$

を留数定理で求めよ。

**解答**  
$f(z)=1/(z^2+4)=1/[(z-2i)(z+2i)]$。上半平面の極は $z=2i$。

$$
\operatorname{Res}(f,2i)=\lim_{z\to2i}\frac{1}{z+2i}=\frac{1}{4i}
$$

したがって

$$
\int_{-\infty}^{\infty}\frac{dx}{x^2+4}
=2\pi i\cdot\frac{1}{4i}=\frac{\pi}{2}
$$

## 6. よくある誤解・落とし穴

1. **積分路の向きを逆にして $2\pi i$ の符号を間違える**。
2. **閉じる半平面の選択を $e^{iaz}$ の符号と逆にする**。
3. **極の内外判定をせず全留数を足してしまう**。
4. **実部を取る問題で最後に虚部まで持ち込んで混乱する**。

## 7. 章末まとめ

- 複素解析は実積分を局所情報（極と留数）へ圧縮する方法である。
- 留数定理はコーシー積分公式の自然な拡張として理解できる。
- $e^{iaz}$ の減衰方向で積分路を選ぶのが実践上のコア。
- 検算は極限（$a\to0,\infty$）で行うと強い。
- 物理では振動現象・グリーン関数・応答関数で頻出する。
- 次ページで最低限の手順をさらに反復する。

## 8. 演習（10問）＋解答

難易度配分: 易4・中4・難2

### 問題

1. **易**: $z=3-4i$ の共役 $\bar z$ と $|z|$ を求めよ。  
2. **易**: $e^{i\pi/3}$ の実部・虚部を求めよ。  
3. **易**: $f(z)=1/(z-2)$ の $z=2$ における留数を求めよ。  
4. **易**: $\int_{-\infty}^{\infty}\frac{dx}{x^2+1}$ の値を答えよ。  
5. **中**: $f(z)=\frac{z+1}{z(z-1)}$ の $z=0,1$ の留数を求めよ。  
6. **中**: $\int_{-\infty}^{\infty}\frac{dx}{x^2+9}$ を求めよ。  
7. **中**: $a>0$ として $\int_{-\infty}^{\infty}\frac{\cos ax}{x^2+1}dx$ の結果を答えよ。  
8. **中**: 積分路を時計回りに取ったとき、留数定理の係数がどう変わるか述べよ。  
9. **難**: $\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+1}dx$ を求めよ。  
10. **難**: $\int_{-\infty}^{\infty}\frac{\cos ax}{x^2+b^2}dx\ (a,b>0)$ の結果を導け。  

### 解答

1. **解答**:  
   $$\bar z=3+4i,\qquad |z|=\sqrt{3^2+(-4)^2}=5$$

2. **解答**:  
   $$e^{i\pi/3}=\cos\frac{\pi}{3}+i\sin\frac{\pi}{3}=\frac12+i\frac{\sqrt3}{2}$$

3. **解答**:  
   1位極なので
   $$\operatorname{Res}\left(\frac{1}{z-2},2\right)=1$$

4. **解答**:  
   $$\int_{-\infty}^{\infty}\frac{dx}{x^2+1}=\pi$$

5. **解答**:  
   $$\operatorname{Res}(f,0)=\lim_{z\to0}\frac{z+1}{z-1}=-1$$
   $$\operatorname{Res}(f,1)=\lim_{z\to1}\frac{z+1}{z}=2$$

6. **解答**:  
   一般式 $\int_{-\infty}^{\infty}\frac{dx}{x^2+a^2}=\frac{\pi}{a}$ より
   $$\frac{\pi}{3}$$

7. **解答**:  
   $$\int_{-\infty}^{\infty}\frac{\cos ax}{x^2+1}dx=\pi e^{-a}$$

8. **解答**:  
   向きが逆なので
   $$\oint_C f(z)dz=-2\pi i\sum\operatorname{Res}$$

9. **解答**:  
   被積分関数は偶関数（$x\sin x$ は偶）なので 0 ではない。既知積分より
   $$\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+1}dx=\pi e^{-1}$$

10. **解答**:  
    極は $\pm ib$、上半平面の極 $ib$ を使って
    $$\int_{-\infty}^{\infty}\frac{\cos ax}{x^2+b^2}dx=\frac{\pi}{b}e^{-ab}$$

---

## ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 子:
  - [residue_theorem_minimum.md](residue_theorem_minimum.md)
