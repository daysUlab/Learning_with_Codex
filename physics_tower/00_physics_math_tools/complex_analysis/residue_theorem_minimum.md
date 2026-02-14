# residue_theorem_minimum（留数定理ミニマム実装）

このページは、複素解析の中でも物理で最も実用的な **留数定理** を、最小構成で「使える形」にするための実践ページです。  
狙いは暗記ではなく、次の1本を毎回再現できることです。

$$
\text{実積分} \longrightarrow \text{複素積分} \longrightarrow \text{極の留数和}
$$

---

## 1. 学習目標

1. 留数定理の適用手順（積分路選択→極抽出→留数計算→実部/虚部取得）を再現できる。
2. 1位極と2位極の留数計算式を使い分けできる。
3. $e^{iaz}$ 型積分で、上半平面/下半平面のどちらに閉じるべきか判断できる。
4. 計算後に極限と偶奇性で答えを検算できる。
5. 力学・電磁気・統計で頻出する有理関数積分の最小ケースを自力で解ける。

## 2. 前提知識

- [README.md](README.md) の内容（複素数・積分路・留数の基本）
- 有理関数の分母因数分解
- 実関数の偶奇性

## 3. 記法・単位・符号規約

- 留数: $\operatorname{Res}(f,z_0)$
- 反時計回り閉曲線: 正向き
- 留数定理:
  $$
  \oint_C f(z)dz = 2\pi i\sum_{z_k\in \mathrm{Int}(C)}\operatorname{Res}(f,z_k)
  $$
- 1位極:
  $$
  \operatorname{Res}(f,z_0)=\lim_{z\to z_0}(z-z_0)f(z)
  $$
- $m$ 位極:
  $$
  \operatorname{Res}(f,z_0)=\frac{1}{(m-1)!}\lim_{z\to z_0}\frac{d^{m-1}}{dz^{m-1}}\left[(z-z_0)^m f(z)\right]
  $$

## 4. 本文（直観→導出→確認）

### 4.1 直観：全体積分を局所情報へ圧縮する

実軸上の積分は「全区間の足し合わせ」です。しかし複素解析では、閉曲線積分を **特異点の局所係数（留数）** だけで決められます。  
つまり、面倒な積分を「極の情報」へ圧縮できるのが留数定理の本質です。

### 4.2 導出：代表例を途中式で解く

次を計算します。

$$
I=\int_{-\infty}^{\infty}\frac{dx}{x^2+1}
$$

#### Step 1: 複素関数へ拡張

$$
f(z)=\frac{1}{z^2+1}=\frac{1}{(z-i)(z+i)}
$$

極は $z=\pm i$。

#### Step 2: 積分路の選択

上半平面の半円で閉じると、内部の極は $z=i$ のみ。半円弧半径 $R\to\infty$ で弧積分は 0 に収束（有理関数で分母次数が十分高い場合の標準結果）。

#### Step 3: 留数計算

$$
\operatorname{Res}(f,i)
=\lim_{z\to i}\frac{z-i}{(z-i)(z+i)}
=\frac{1}{2i}
$$

#### Step 4: 留数定理適用

$$
\oint_C f(z)dz = 2\pi i\cdot\frac{1}{2i}=\pi
$$

弧積分が 0 なので、実軸積分そのものが

$$
I=\pi
$$

となる。

### 4.3 導出：$\cos$ 積分の最小パターン

$$
I(a)=\int_{-\infty}^{\infty}\frac{\cos(ax)}{x^2+1}dx,\quad a>0
$$

とする。複素版

$$
J(a)=\int_{-\infty}^{\infty}\frac{e^{iaz}}{z^2+1}dz
$$

を考える。$z=x+iy$ に対し

$$
e^{iaz}=e^{iax-ay}
$$

なので、$a>0$ では上半平面（$y>0$）で減衰。よって上半平面で閉じる。

極 $z=i$ で

$$
\operatorname{Res}\left(\frac{e^{iaz}}{z^2+1},i\right)
=\lim_{z\to i}\frac{e^{iaz}}{z+i}
=\frac{e^{-a}}{2i}
$$

したがって

$$
J(a)=2\pi i\cdot\frac{e^{-a}}{2i}=\pi e^{-a}
$$

求める積分は実部なので

$$
I(a)=\Re J(a)=\pi e^{-a}
$$

### 4.4 確認：最終検算

- $a\to0^+$ で $I(a)\to\pi$（前節の基本積分に一致）。
- $a\to\infty$ で $I(a)\to0$（高速振動の平均化と一致）。
- 被積分関数は偶関数なので、結果が正であることとも整合。

## 5. 例題（3題）

### 例題1（易）

$$
\int_{-\infty}^{\infty}\frac{dx}{x^2+4}
$$

を求めよ。

**解答**

上半平面の極は $z=2i$。

$$
\operatorname{Res}\left(\frac{1}{z^2+4},2i\right)=\frac{1}{4i}
$$

よって

$$
\int_{-\infty}^{\infty}\frac{dx}{x^2+4}=2\pi i\cdot\frac{1}{4i}=\frac{\pi}{2}
$$

### 例題2（中）

$$
\int_{-\infty}^{\infty}\frac{\cos(2x)}{x^2+1}dx
$$

を求めよ。

**解答**

公式 $\int_{-\infty}^{\infty}\dfrac{\cos(ax)}{x^2+1}dx=\pi e^{-a}$ に $a=2$ を代入:

$$
\pi e^{-2}
$$

### 例題3（やや難）

$$
\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+1}dx
$$

を求めよ。

**解答**

$x\sin x$ は偶関数なので積分は 0 ではない。  
$\Im\int_{-\infty}^{\infty}\dfrac{x e^{ix}}{x^2+1}dx$ を考える。

$$
f(z)=\frac{z e^{iz}}{z^2+1}
$$

上半平面の極 $z=i$ の留数は

$$
\operatorname{Res}(f,i)=\lim_{z\to i}\frac{z e^{iz}}{z+i}=\frac{i e^{-1}}{2i}=\frac{e^{-1}}{2}
$$

ゆえに

$$
\int_{-\infty}^{\infty}\frac{z e^{iz}}{z^2+1}dz=2\pi i\cdot\frac{e^{-1}}{2}=\pi i e^{-1}
$$

虚部を取って

$$
\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+1}dx=\pi e^{-1}
$$

## 6. よくある誤解・落とし穴

1. $e^{iaz}$ の符号に応じた半平面選択を逆にする。
2. 積分路内部にない極まで足してしまう。
3. 留数の式で $2\pi i$ だけ掛けて、実部・虚部の取り出しを忘れる。
4. 偶奇性チェックをせず、符号ミスに気づかない。

## 7. 章末まとめ

- 留数定理は「閉曲線積分 = 内部極の留数和」である。
- 実積分の多くは $e^{iaz}$ を使うと機械的に解ける。
- 1位極の留数は極限1本で求まる。
- 積分路選択は減衰因子 $e^{-ay}$ の符号で決まる。
- 計算後は極限・偶奇性で必ず検算する。
- 最小手順を固定すれば、応用問題でも迷いにくい。

## 8. 演習（10問）＋解答

難易度: 易4・中4・難2

### 問題

1. **易**: $\operatorname{Res}(1/(z-3),3)$ を求めよ。  
2. **易**: $\int_{-\infty}^{\infty}\dfrac{dx}{x^2+9}$ を求めよ。  
3. **易**: $\int_{-\infty}^{\infty}\dfrac{dx}{x^2+16}$ を求めよ。  
4. **易**: $\int_{-\infty}^{\infty}\dfrac{\cos x}{x^2+1}dx$ を求めよ。  
5. **中**: $\operatorname{Res}\left(\dfrac{1}{(z-1)(z+1)},1\right)$ を求めよ。  
6. **中**: $\int_{-\infty}^{\infty}\dfrac{\cos(3x)}{x^2+1}dx$ を求めよ。  
7. **中**: 時計回り積分路での留数定理の係数を書け。  
8. **中**: $\int_{-\infty}^{\infty}\dfrac{x\sin(2x)}{x^2+1}dx$ を求めよ。  
9. **難**: $\int_{-\infty}^{\infty}\dfrac{\cos(ax)}{x^2+b^2}dx\ (a,b>0)$ を導け。  
10. **難**: $\int_{-\infty}^{\infty}\dfrac{x\sin(ax)}{x^2+b^2}dx\ (a,b>0)$ を導け。  

### 解答

1. **解答**:  
   $$\operatorname{Res}\left(\frac{1}{z-3},3\right)=1$$

2. **解答**:  
   $$\int_{-\infty}^{\infty}\frac{dx}{x^2+9}=\frac{\pi}{3}$$

3. **解答**:  
   $$\int_{-\infty}^{\infty}\frac{dx}{x^2+16}=\frac{\pi}{4}$$

4. **解答**:  
   $$\int_{-\infty}^{\infty}\frac{\cos x}{x^2+1}dx=\pi e^{-1}$$

5. **解答**:  
   $$\operatorname{Res}\left(\frac{1}{(z-1)(z+1)},1\right)=\lim_{z\to1}\frac{1}{z+1}=\frac12$$

6. **解答**:  
   $$\int_{-\infty}^{\infty}\frac{\cos(3x)}{x^2+1}dx=\pi e^{-3}$$

7. **解答**:  
   $$\oint_C f(z)dz=-2\pi i\sum\operatorname{Res}$$

8. **解答**:  
   一般結果より
   $$\int_{-\infty}^{\infty}\frac{x\sin(2x)}{x^2+1}dx=\pi e^{-2}$$

9. **解答**:  
   上半平面の極 $ib$ を使って
   $$\int_{-\infty}^{\infty}\frac{\cos(ax)}{x^2+b^2}dx=\frac{\pi}{b}e^{-ab}$$

10. **解答**:  
    同様に
    $$\int_{-\infty}^{\infty}\frac{x\sin(ax)}{x^2+b^2}dx=\pi e^{-ab}$$

---

## ナビゲーション

- 親: [README.md](README.md)
