# qa（電磁気Q&A）

このページは、電磁気でつまずきやすいポイントを短く確認する補助ノートです。

## 1. よくある質問

### Q1. 電場と磁場は別物か

静的には別に扱うことが多いですが、時間変化を含めるとマクスウェル方程式で相互に結合します。

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

### Q2. 変位電流は「実際の電流」か

導体中の伝導電流とは区別される項ですが、磁場を作る源として方程式に同等に現れます。

$$
\mathbf{J}_{\text{disp}}=\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

### Q3. 境界条件はなぜ必要か

微分方程式の解は定数を含むため、物理境界で値や不連続を与えて解を一意化します。

## 2. ミニチェック

1. 使う式の前提（静電・定常・時間変化あり）を書いたか。
2. 積分面や積分経路の向きを定義したか。
3. 単位系を SI で揃えたか。

## 3. ナビゲーション

- 親: [../00_overview.md](../00_overview.md)
- 関連: [../part01_build_maxwell/README.md](../part01_build_maxwell/README.md)
- 関連: [../part02_use_maxwell/README.md](../part02_use_maxwell/README.md)
- 関連: [../part03_phenomenology/README.md](../part03_phenomenology/README.md)
