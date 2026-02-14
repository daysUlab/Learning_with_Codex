# 02_electromagnetism（電磁気学の全体像）

この章では、電場・磁場・電磁波をマクスウェル方程式で統一的に扱う視点を身につけます。

## 1. 学習目標

1. 電場と磁場の基本量を定義できる。
2. マクスウェル方程式の微分形と積分形を対応づけられる。
3. 静電場・静磁場・電磁誘導の典型問題を解ける。
4. 境界条件と保存則の関係を説明できる。

## 2. 前提知識

- ベクトル解析（勾配・発散・回転）
- 力学の保存則
- 微分方程式の初歩

## 3. 基本記号

真空の誘電率

$$
\varepsilon_0
$$

真空の透磁率

$$
\mu_0
$$

電場

$$
\mathbf{E}
$$

磁場

$$
\mathbf{B}
$$

電荷密度

$$
\rho
$$

電流密度

$$
\mathbf{J}
$$

## 4. マクスウェル方程式（微分形）

$$
\nabla\cdot\mathbf{E}=\frac{\rho}{\varepsilon_0}
$$

$$
\nabla\cdot\mathbf{B}=0
$$

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

## 5. 章の進み方

- `part01_build_maxwell`: 方程式の構築と意味
- `part02_use_maxwell`: 方程式を解く手順
- `part03_phenomenology`: 誘導・波動・放射の現象論
- `qa`: よくある疑問の整理

## 6. 例題（1題）

真空中で

$$
\rho=0
$$

かつ

$$
\mathbf{J}=0
$$

のとき、電場に対する波動方程式を書け。

**解答**

$$
\nabla^2\mathbf{E}-\mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}=\mathbf{0}
$$

## 7. ナビゲーション

- 親: [../README.md](../README.md)
- 次: [part01_build_maxwell/README.md](part01_build_maxwell/README.md)
- 関連: [part02_use_maxwell/README.md](part02_use_maxwell/README.md)
- 関連: [part03_phenomenology/README.md](part03_phenomenology/README.md)
- 補助: [qa/README.md](qa/README.md)
