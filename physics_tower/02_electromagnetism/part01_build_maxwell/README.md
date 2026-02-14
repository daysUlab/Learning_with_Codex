# part01_build_maxwell（マクスウェル方程式を組み立てる）

このパートでは、実験法則からマクスウェル方程式へ到達する流れを確認します。

## 1. 学習目標

1. ガウス法則とアンペール法則の意味を説明できる。
2. ファラデーの法則と変位電流項の必要性を説明できる。
3. 微分形と積分形の対応を示せる。

## 2. 構築の流れ

### ステップ1：電荷から電場

$$
\nabla\cdot\mathbf{E}=\frac{\rho}{\varepsilon_0}
$$

### ステップ2：磁荷がない

$$
\nabla\cdot\mathbf{B}=0
$$

### ステップ3：電磁誘導

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

### ステップ4：アンペール法則の拡張

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

## 3. 変位電流項が必要な理由

連続の式

$$
\frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{J}=0
$$

と整合させるため、

$$
\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

が不可欠です。

## 4. 演習（3問）

1. 積分形のガウス法則を書け。
2. 連続の式から変位電流項の必要性を説明せよ。
3. ファラデーの法則の積分形を書け。

## 5. ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 次: [../part02_use_maxwell/README.md](../part02_use_maxwell/README.md)
