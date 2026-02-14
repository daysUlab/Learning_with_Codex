# basics（線形代数の基礎実践）

このページは、物理で必要な線形代数の「最小実戦セット」を身につけるための実践ノートです。  
目標は、次を手で再現できることです。

- 連立一次方程式の行列表現
- 逆行列と解の存在条件
- 固有値・固有ベクトル
- 対角化による計算の簡略化

---

## 1. 学習目標

1. 連立一次方程式を行列形式へ変換できる。
2. 行列式から可逆性と解の一意性を判定できる。
3. 固有値方程式を立てて固有値・固有ベクトルを求められる。
4. 対角化の意味を、反復計算・時間発展計算と結びつけて説明できる。
5. 計算結果を代入チェックと次元チェックで検証できる。

## 2. 前提知識

- [README.md](README.md) の内容
- 連立一次方程式
- 二次方程式

## 3. 記法・単位・符号規約

- ベクトル:

$$
\mathbf{x}=
\begin{pmatrix}
x_1 \\
\vdots \\
x_n
\end{pmatrix}
$$

- 行列:

$$
A=(a_{ij})
$$

- 線形系:

$$
A\mathbf{x}=\mathbf{b}
$$

- 単位行列:

$$
I
$$

- 行列式:

$$
\det A
$$

- 固有値問題:

$$
A\mathbf{v}=\lambda\mathbf{v}
$$

単位は成分ごとに持つ。和を取る場合は必ず同次元であることを確認する。

## 4. 本文（直観→導出→確認）

### 4.1 直観：多自由度系は行列で見る

物理の多自由度系では、状態変数が同時に結合します。  
行列は「結合の地図」です。

### 4.2 導出A：連立方程式と可逆性

次の連立を考える。

$$
\begin{cases}
2x+y=5 \\
3x-2y=4
\end{cases}
$$

行列形式:

$$
A=
\begin{pmatrix}
2 & 1 \\
3 & -2
\end{pmatrix},
\quad
\mathbf{x}=
\begin{pmatrix}
x \\
y
\end{pmatrix},
\quad
\mathbf{b}=
\begin{pmatrix}
5 \\
4
\end{pmatrix}
$$

$$
A\mathbf{x}=\mathbf{b}
$$

行列式:

$$
\det A=2\cdot(-2)-1\cdot3=-7\neq0
$$

よって可逆で、解は一意。

逆行列:

$$
A^{-1}=\frac{1}{-7}
\begin{pmatrix}
-2 & -1 \\
-3 & 2
\end{pmatrix}
$$

$$
\mathbf{x}=A^{-1}\mathbf{b}
$$

計算:

$$
\mathbf{x}=
\frac{1}{-7}
\begin{pmatrix}
-2 & -1 \\
-3 & 2
\end{pmatrix}
\begin{pmatrix}
5 \\
4
\end{pmatrix}=
\frac{1}{-7}
\begin{pmatrix}
-14 \\
-7
\end{pmatrix}=
\begin{pmatrix}
2 \\
1
\end{pmatrix}
$$

したがって

$$
x=2,
\quad
y=1
$$

### 4.3 導出B：固有値と固有ベクトル

行列

$$
A=
\begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix}
$$

の固有値を求める。

$$
\det(A-\lambda I)=0
$$

$$
\det
\begin{pmatrix}
4-\lambda & 1 \\
2 & 3-\lambda
\end{pmatrix}=(4-\lambda)(3-\lambda)-2
$$

$$
=\lambda^2-7\lambda+10
=(\lambda-5)(\lambda-2)=0
$$

よって

$$
\lambda_1=5,
\quad
\lambda_2=2
$$

固有ベクトルを求める。

#### 固有値 5

$$
(A-5I)\mathbf{v}=0
$$

$$
\begin{pmatrix}
-1 & 1 \\
2 & -2
\end{pmatrix}
\begin{pmatrix}
v_1 \\
v_2
\end{pmatrix}=0
$$

$$
v_1=v_2
$$

1つ選んで

$$
\mathbf{v}^{(1)}=
\begin{pmatrix}
1 \\
1
\end{pmatrix}
$$

#### 固有値 2

$$
(A-2I)\mathbf{v}=0
$$

$$
\begin{pmatrix}
2 & 1 \\
2 & 1
\end{pmatrix}
\begin{pmatrix}
v_1 \\
v_2
\end{pmatrix}=0
$$

$$
2v_1+v_2=0
$$

1つ選んで

$$
\mathbf{v}^{(2)}=
\begin{pmatrix}
1 \\
-2
\end{pmatrix}
$$

### 4.4 導出C：対角化

固有ベクトルを列に並べる。

$$
P=
\begin{pmatrix}
1 & 1 \\
1 & -2
\end{pmatrix}
$$

固有値を対角に置く。

$$
D=
\begin{pmatrix}
5 & 0 \\
0 & 2
\end{pmatrix}
$$

このとき

$$
A=PDP^{-1}
$$

よって

$$
A^n=PD^nP^{-1}
$$

となる。  
長時間発展や反復作用の計算で大幅に効率化できる。

### 4.5 確認

1. 求めた解を元の連立へ代入する。
2. 固有値・固有ベクトルは

$$
A\mathbf{v}=\lambda\mathbf{v}
$$

を直接確認する。
3. 物理量成分の次元整合を確認する。

## 5. 例題（3題）

### 例題1（易）

$$
\begin{cases}
x+y=3 \\
2x-y=0
\end{cases}
$$

を解け。

**解答**

2式を加えて

$$
3x=3
$$

$$
x=1
$$

$$
y=2
$$

### 例題2（中）

$$
A=
\begin{pmatrix}
1 & 2 \\
0 & 3
\end{pmatrix}
$$

の固有値を求めよ。

**解答**

上三角行列なので対角成分が固有値。

$$
\lambda_1=1,
\quad
\lambda_2=3
$$

### 例題3（やや難）

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 2
\end{pmatrix}
$$

の固有値を求めよ。

**解答**

$$
\det(A-\lambda I)=
\begin{vmatrix}
2-\lambda & 1 \\
1 & 2-\lambda
\end{vmatrix}=(2-\lambda)^2-1
$$

$$
=\lambda^2-4\lambda+3
=(\lambda-1)(\lambda-3)
$$

$$
\lambda_1=1,
\quad
\lambda_2=3
$$

## 6. よくある誤解・落とし穴

1. 行列積を可換だと思って順序を入れ替える。
2. 固有値だけ求めて固有ベクトル確認を省略する。
3. 行列式 0 のときに逆行列法を使い続ける。
4. 次元の異なる成分を同じベクトルで足してしまう。

## 7. 章末まとめ

- 連立一次方程式は

$$
A\mathbf{x}=\mathbf{b}
$$

で統一できる。
- 可逆性判定は

$$
\det A\neq0
$$

で行う。
- 固有値問題は

$$
\det(A-\lambda I)=0
$$

から始める。
- 対角化は反復計算を軽くする。
- 計算後は必ず代入確認する。
- 物理では固有値がモード・準位に対応する。

## 8. 演習（10問）＋解答

難易度配分: 易4・中4・難2

### 問題

1. **易**: 

$$
\begin{cases}
x+2y=5 \\
x-y=2
\end{cases}
$$

を解け。  
2. **易**: 

$$
\det
\begin{pmatrix}
2 & 3 \\
1 & 4
\end{pmatrix}
$$

を求めよ。  
3. **易**: 

$$
\mathbf{u}=
\begin{pmatrix}
1 \\
2
\end{pmatrix},
\quad
\mathbf{v}=
\begin{pmatrix}
3 \\
-1
\end{pmatrix}
$$

の内積を求めよ。  
4. **易**: 対角行列

$$
\begin{pmatrix}
6 & 0 \\
0 & -1
\end{pmatrix}
$$

の固有値を求めよ。  
5. **中**: 

$$
A=
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
$$

について

$$
A^2
$$

を求めよ。  
6. **中**: 

$$
\begin{cases}
2x+4y=6 \\
x+2y=3
\end{cases}
$$

の解の個数を判定せよ。  
7. **中**: 

$$
A=
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
$$

の固有値を求めよ。  
8. **中**: 

$$
A=
\begin{pmatrix}
3 & 0 \\
4 & 2
\end{pmatrix}
$$

の固有値を求めよ。  
9. **難**: 

$$
A=
\begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix}
$$

の固有値を求めよ。  
10. **難**: 

$$
\det A=0
$$

のとき

$$
A\mathbf{x}=\mathbf{0}
$$

が非自明解を持ち得る理由を述べよ。  

### 解答

1. **解答**:  
2式より

$$
x=2+y
$$

1式へ代入:

$$
2+y+2y=5
$$

$$
y=1,
\quad
x=3
$$

2. **解答**:  

$$
2\cdot4-3\cdot1=5
$$

3. **解答**:  

$$
\mathbf{u}\cdot\mathbf{v}=1\cdot3+2\cdot(-1)=1
$$

4. **解答**:  

$$
6,
\quad
-1
$$

5. **解答**:  

$$
A^2=
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}=
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
$$

6. **解答**:  
2本は同じ式なので独立方程式は1本。  
解は無限個。

7. **解答**:  

$$
\det(A-\lambda I)=
\begin{vmatrix}
-\lambda & 1 \\
1 & -\lambda
\end{vmatrix}=\lambda^2-1
$$

$$
\lambda=\pm1
$$

8. **解答**:  
下三角行列なので対角成分。

$$
3,
\quad
2
$$

9. **解答**:  

$$
\det(A-\lambda I)=
\begin{vmatrix}
1-\lambda & 2 \\
2 & 1-\lambda
\end{vmatrix}=(1-\lambda)^2-4
$$

$$
=\lambda^2-2\lambda-3
=(\lambda-3)(\lambda+1)
$$

$$
\lambda_1=3,
\quad
\lambda_2=-1
$$

10. **解答**:  

$$
\det A=0
$$

は列（または行）が一次従属で可逆でないことを意味する。  
したがって核が非自明になり得るため

$$
A\mathbf{x}=\mathbf{0}
$$

に

$$
\mathbf{x}\neq\mathbf{0}
$$

が存在し得る。

---

## ナビゲーション

- 親: [README.md](README.md)
