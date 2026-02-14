# vector_analysis（物理で使うベクトル解析の入口）

ベクトル解析は、電磁気学・流体力学・連続体力学を読むための共通言語です。  
「場」を扱う物理では、次の3演算が中核になります。

$$
\nabla f,
\quad
\nabla\cdotF,
\quad
\nabla\timesF
$$

この章では、直観から式へ、式から検算へという順で、後続章にそのまま持ち込める形へ整理します。

---

## 1. 学習目標

1. 勾配・発散・回転の幾何学的意味を説明できる。
2. ナブラ演算を成分で計算できる。
3. ガウスの発散定理とストークスの定理を式で書き、物理的に解釈できる。
4. 単位・符号・座標系の取り方で誤らない計算手順を実行できる。
5. 後続ページ

$$
\texttt{nabla\_identities.md}
$$

で恒等式を使った展開に進める。

## 2. 前提知識（必要最小セット）

- ベクトルの成分表示
- 偏微分
- 2重積分・3重積分の初歩

復習リンク:

- [../00_overview.md](../00_overview.md)
- [../calculus_techniques/README.md](../calculus_techniques/README.md)

## 3. 記法・単位・符号規約

直交座標系

$$
(x,y,z)
$$

を基本に、ナブラを

$$
\nabla=
\left(
\frac{\partial}{\partial x},
\frac{\partial}{\partial y},
\frac{\partial}{\partial z}
\right)
$$

と定義する。

- スカラー場:

$$
f(x,y,z)
$$

- ベクトル場:

$$
F=(F_x,F_y,F_z)
$$

- 勾配:

$$
\nabla f=
\left(
\frac{\partial f}{\partial x},
\frac{\partial f}{\partial y},
\frac{\partial f}{\partial z}
\right)
$$

- 発散:

$$
\nabla\cdotF
=
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}
$$

- 回転:

$$
\nabla\timesF
=
[[\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}; \frac{\partial F_x}{\partial z}-\frac{\partial F_z}{\partial x}; \frac{\partial F_y}{\partial x}-\frac{\partial F_x}{\partial y}]]
$$

## 4. 本文（直観→導出→確認）

### 4.1 直観：場の「湧き出し」と「渦」を分ける

- 発散は、その点での湧き出し（源）や吸い込み（sink）の強さ。
- 回転は、その点まわりの渦の強さと向き。

電磁気で言えば、

$$
\nabla\cdotE
$$

は電荷密度と結びつき、

$$
\nabla\timesE
$$

は時間変化する磁場と結びつく。

### 4.2 導出A：成分計算の基本

ベクトル場

$$
F=(x^2,xy,z)
$$

に対して発散を計算する。

$$
\nabla\cdotF
=
\frac{\partial x^2}{\partial x}
+
\frac{\partial (xy)}{\partial y}
+
\frac{\partial z}{\partial z}
$$

$$
=2x+x+1
=3x+1
$$

次に回転を計算する。

$$
\nabla\timesF
=
[[\frac{\partial z}{\partial y}-\frac{\partial (xy)}{\partial z}; \frac{\partial x^2}{\partial z}-\frac{\partial z}{\partial x}; \frac{\partial (xy)}{\partial x}-\frac{\partial x^2}{\partial y}]]
=
[[0-0; 0-0; y-0]]
=
[[0; 0; y]]
$$

### 4.3 導出B：発散定理

体積領域

$$
V
$$

とその境界面

$$
S=\partial V
$$

に対して

$$
\iiint_V (\nabla\cdotF)\,dV
=
\iint_S F\cdot dS
$$

が成り立つ。  
左辺は内部での総湧き出し、右辺は境界面から外へ出る総流束で、保存則の幾何学表現になっている。

### 4.4 導出C：ストークスの定理

曲面

$$
S
$$

とその境界曲線

$$
C=\partial S
$$

に対して

$$
\iint_S (\nabla\timesF)\cdot dS
=
\oint_C F\cdot dl
$$

が成り立つ。  
左辺は面全体の回転の総和、右辺は境界に沿った循環。

### 4.5 確認テンプレ

1. 成分の偏微分先を取り違えていないか。
2. 面・曲線の向き（法線と周回方向）の整合を取ったか。
3. 次元整合が成立しているか。
4. 簡単な対称場で極限確認したか。

## 5. 例題（3題）

### 例題1（易）

$$
f=x^2+y^2+z^2
$$

の勾配を求めよ。

**解答**

$$
\nabla f=(2x,2y,2z)
$$

### 例題2（中）

$$
F=(-y,x,0)
$$

の回転を求めよ。

**解答**

$$
\nabla\timesF
=
[[0; 0; \frac{\partial x}{\partial x}-\frac{\partial(-y)}{\partial y}]]
=
[[0; 0; 1-(-1)]]
=
[[0; 0; 2]]
$$

### 例題3（やや難）

$$
F=(x,y,z)
$$

について、半径

$$
R
$$

の球面での流束を求めよ。

**解答**

発散は

$$
\nabla\cdotF=1+1+1=3
$$

発散定理より

$$
\iint_S F\cdot dS
=
\iiint_V 3\,dV
=3\cdot\frac{4}{3}\pi R^3
=4\pi R^3
$$

## 6. よくある誤解・落とし穴

1. 発散と回転をどちらも「変化率」とだけ覚えて区別しない。
2. 回転の成分順序（x,y,z）を入れ替える。
3. 面素ベクトルの向きを固定せずに符号が反転する。
4. 定理の適用前提（滑らかさ・向き）を確認しない。

## 7. 章末まとめ

- ナブラ演算は場の局所構造を記述する。
- 発散は源・吸い込み、回転は渦を測る。
- 発散定理は体積積分と面積分を橋渡しする。
- ストークスの定理は面積分と線積分を橋渡しする。
- 向きと符号規約は結果の正負を決める。
- 物理法則の微分形と積分形の往復に必須。

## 8. 演習（10問）＋解答

難易度配分: 易4・中4・難2

### 問題

1. **易**: 

$$
f=x^2y
$$

の

$$
\nabla f
$$

を求めよ。  
2. **易**: 

$$
F=(x,0,0)
$$

の発散を求めよ。  
3. **易**: 

$$
F=(0,0,z)
$$

の発散を求めよ。  
4. **易**: 

$$
F=(0,x,0)
$$

の回転を求めよ。  
5. **中**: 

$$
F=(-y,x,0)
$$

の発散を求めよ。  
6. **中**: 

$$
F=(x^2,y^2,z^2)
$$

の発散を求めよ。  
7. **中**: 

$$
F=(yz,zx,xy)
$$

の回転を求めよ。  
8. **中**: 

$$
F=(x,y,z)
$$

の発散を求めよ。  
9. **難**: 半径

$$
R
$$

球で

$$
F=(x,y,z)
$$

の流束を発散定理で求めよ。  
10. **難**: 

$$
F=(-y,x,0)
$$

について、単位円

$$
x^2+y^2=1
$$

上の線積分

$$
\oint_C F\cdot dl
$$

を求めよ。  

### 解答

1. **解答**:  

$$
\nabla f=
\left(
2xy,
\ x^2,
\ 0
\right)
$$

2. **解答**:  

$$
\nabla\cdotF=1
$$

3. **解答**:  

$$
\nabla\cdotF=1
$$

4. **解答**:  

$$
\nabla\timesF=
[[0; 0; 1]]
$$

5. **解答**:  

$$
\nabla\cdotF=0
$$

6. **解答**:  

$$
\nabla\cdotF=2x+2y+2z
$$

7. **解答**:  

$$
\nabla\timesF=
[[0; 0; 0]]
$$

8. **解答**:  

$$
\nabla\cdotF=3
$$

9. **解答**:  

$$
\iint_S F\cdot dS
=
\iiint_V 3\,dV
=4\pi R^3
$$

10. **解答**:  
単位円を

$$
r(\theta)=(\cos\theta,\sin\theta,0)
$$

で表す。

$$
dl=(-\sin\theta,\cos\theta,0)d\theta
$$

$$
F(r(\theta))=(-\sin\theta,\cos\theta,0)
$$

$$
F\cdot dl=1\cdot d\theta
$$

$$
\oint_C F\cdot dl=
\int_0^{2\pi}d\theta
=2\pi
$$

---

## ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 子:
  - [nabla_identities.md](nabla_identities.md)
