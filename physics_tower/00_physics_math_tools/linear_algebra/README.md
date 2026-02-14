# linear_algebra（物理で使う線形代数の入口）

線形代数は、物理で出てくる「連立」「変換」「固有モード」を1つの言語で扱う道具です。  
力学の正準変換、量子力学の状態ベクトル、電磁気のテンソル表現まで、基礎は同じ構造にあります。

この章では、

- 直観
- 導出
- 確認

の順に、物理で再利用しやすい最小セットを整理します。

---

## 1. 学習目標

1. ベクトル・行列・線形写像の関係を説明できる。
2. 連立一次方程式を行列形式で表し、解の存在性を判定できる。
3. 固有値問題の物理的意味（固有モード）を説明できる。
4. 直交行列と対角化の役割を、計算簡略化の観点で理解できる。
5. 後続ページ

$$
\texttt{basics.md}
$$

へ進む準備を整えられる。

## 2. 前提知識（必要最小セット）

- 四則演算
- 連立一次方程式
- ベクトルの成分表示

復習リンク:

- [../00_overview.md](../00_overview.md)
- [../calculus_techniques/README.md](../calculus_techniques/README.md)

## 3. 記法・単位・符号規約

- ベクトル:

$$
\mathbf{x}=(x_1,x_2,\dots,x_n)^\mathsf{T}
$$

- 行列:

$$
A=(a_{ij})
$$

- 線形方程式:

$$
A\mathbf{x}=\mathbf{b}
$$

- 内積:

$$
\mathbf{u}\cdot\mathbf{v}=\mathbf{u}^\mathsf{T}\mathbf{v}
$$

- 直交行列:

$$
Q^\mathsf{T}Q=I
$$

単位は、各成分の物理量に依存するため、和や積の次元整合をその都度確認する。

## 4. 本文（直観→導出→確認）

### 4.1 直観：線形代数は「同時に動く量」の圧縮表現

連立方程式を1本ずつ追うより、行列でまとめると構造が見える。  
特に物理では、自由度が多い系の振動や状態遷移を一括で扱える。

### 4.2 導出A：連立一次方程式の行列表現

方程式系

$$
\begin{cases}
2x+y=5 \\
x-y=1
\end{cases}
$$

は

$$
\begin{pmatrix}
2 & 1 \\
1 & -1
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
5 \\
1
\end{pmatrix}
$$

と書ける。

逆行列が存在すれば

$$
\mathbf{x}=A^{-1}\mathbf{b}
$$

で解ける。判定は行列式。

$$
\det A=2\cdot(-1)-1\cdot1=-3\neq0
$$

よって解は一意。

### 4.3 導出B：固有値問題

線形変換で方向が変わらないベクトルを考える。

$$
A\mathbf{v}=\lambda\mathbf{v}
$$

非自明解

$$
\mathbf{v}\neq\mathbf{0}
$$

が存在する条件は

$$
\det(A-\lambda I)=0
$$

#### 例

$$
A=
\begin{pmatrix}
2 & 0 \\
0 & 5
\end{pmatrix}
$$

なら

$$
\det(A-\lambda I)=(2-\lambda)(5-\lambda)=0
$$

したがって

$$
\lambda_1=2,
\quad
\lambda_2=5
$$

物理では、固有値が固有振動数やエネルギー準位に対応する場面が多い。

### 4.4 導出C：対角化の利点

対角化可能なとき

$$
A=PDP^{-1}
$$

ここで

$$
D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)
$$

なら

$$
A^k=PD^kP^{-1}
$$

となり、累乗計算が簡単になる。  
時間発展演算子の計算で特に有効。

### 4.5 確認：検算テンプレ

1. 連立解は元の式へ代入して確認。
2. 固有ベクトルは

$$
A\mathbf{v}
$$

と

$$
\lambda\mathbf{v}
$$

が一致するか確認。
3. 次元が混ざっていないか確認。

## 5. 例題（3題）

### 例題1（易）

$$
\mathbf{u}=(1,2),
\quad
\mathbf{v}=(3,4)
$$

の内積を求めよ。

**解答**

$$
\mathbf{u}\cdot\mathbf{v}=1\cdot3+2\cdot4=11
$$

### 例題2（中）

$$
\begin{cases}
3x+2y=7 \\
x-y=1
\end{cases}
$$

を解け。

**解答**

第2式より

$$
x=1+y
$$

第1式へ代入:

$$
3(1+y)+2y=7
$$

$$
5y=4
$$

$$
y=\frac{4}{5}
$$

$$
x=\frac{9}{5}
$$

### 例題3（やや難）

$$
A=
\begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix}
$$

の固有値を求めよ。

**解答**

$$
\det(A-\lambda I)=
\begin{vmatrix}
4-\lambda & 1 \\
2 & 3-\lambda
\end{vmatrix}
=(4-\lambda)(3-\lambda)-2
$$

$$
=\lambda^2-7\lambda+10
=(\lambda-5)(\lambda-2)
$$

よって

$$
\lambda_1=5,
\quad
\lambda_2=2
$$

## 6. よくある誤解・落とし穴

1. 行列積の順序を交換してしまう。
2. 成分ごとの単位差を無視して加算してしまう。
3. 固有値を求めて満足し、固有ベクトル確認をしない。
4. 逆行列がない場合に同じ手順を機械的に適用する。

## 7. 章末まとめ

- 線形代数は多自由度系を圧縮して扱う基盤。
- 連立一次方程式は

$$
A\mathbf{x}=\mathbf{b}
$$

で統一できる。
- 固有値問題はモード分解の入口。
- 対角化は反復計算と時間発展計算を軽くする。
- 検算は代入と次元整合で行う。
- 物理応用では「意味のある基底選択」が計算効率を左右する。

## 8. 演習（10問）＋解答

難易度配分: 易4・中4・難2

### 問題

1. **易**: 

$$
\mathbf{a}=(2,-1),
\quad
\mathbf{b}=(1,3)
$$

の内積を求めよ。  
2. **易**: 

$$
\begin{cases}
x+y=4 \\
x-y=2
\end{cases}
$$

を解け。  
3. **易**: 次の行列式を求めよ。  

$$
\begin{vmatrix}
1 & 2 \\
3 & 4
\end{vmatrix}
$$

4. **易**: 

$$
A=
\begin{pmatrix}
7 & 0 \\
0 & -2
\end{pmatrix}
$$

の固有値を求めよ。  
5. **中**: 

$$
A=
\begin{pmatrix}
1 & 2 \\
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
2x+3y=8 \\
4x+6y=16
\end{cases}
$$

の解の個数を判定せよ。  
7. **中**: 

$$
A=
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
$$

が直交行列であることを示せ。  
8. **中**: 

$$
A=
\begin{pmatrix}
3 & 1 \\
0 & 2
\end{pmatrix}
$$

の固有値を求めよ。  
9. **難**: 

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 2
\end{pmatrix}
$$

を対角化せよ（固有値のみでも可）。  
10. **難**: 

$$
A\mathbf{x}=\mathbf{0}
$$

で

$$
\det A=0
$$

のとき非自明解が存在し得る理由を説明せよ。  

### 解答

1. **解答**:  

$$
\mathbf{a}\cdot\mathbf{b}=2\cdot1+(-1)\cdot3=-1
$$

2. **解答**:  

$$
2x=6
\Rightarrow x=3,
\quad
y=1
$$

3. **解答**:  

$$
1\cdot4-2\cdot3=-2
$$

4. **解答**:  
対角成分より

$$
7,
\quad
-2
$$

5. **解答**:  

$$
A^2=
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
=
\begin{pmatrix}
1 & 4 \\
0 & 1
\end{pmatrix}
$$

6. **解答**:  
第2式は第1式の2倍なので独立式は1本。  
解は無限個。

7. **解答**:  

$$
A^\mathsf{T}=
\begin{pmatrix}
0 & 1 \\
-1 & 0
\end{pmatrix}
$$

$$
A^\mathsf{T}A=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}=I
$$

よって直交行列。

8. **解答**:  
上三角行列なので固有値は対角成分。

$$
3,
\quad
2
$$

9. **解答**:  

$$
\det(A-\lambda I)=
\begin{vmatrix}
2-\lambda & 1 \\
1 & 2-\lambda
\end{vmatrix}
=(2-\lambda)^2-1
$$

$$
=(\lambda-3)(\lambda-1)
$$

したがって固有値は

$$
3,
\quad
1
$$

10. **解答**:  

$$
\det A=0
$$

は列ベクトルが一次従属であることを意味し、線形写像が可逆でない。  
そのため核が自明でない場合があり

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

- 親: [../00_overview.md](../00_overview.md)
- 子:
  - [basics.md](basics.md)
