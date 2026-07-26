# 半導体製造の概観――材料と形状へ電場設計を刻む

## 工程と物理的役割

| 工程 | 作るもの |
|---|---|
| oxidation | 絶縁膜・界面 |
| deposition | 導体・誘電体・半導体薄膜 |
| lithography | 平面pattern |
| etching | patternの形状転写 |
| implantation | dopantの導入 |
| diffusion・annealing | 濃度分布、結晶損傷回復、活性化 |
| metallization | contact・配線 |
| planarization | 次層の平坦面 |
| wafer test | 不良die選別 |
| packaging・final test | 外部接続と製品保証 |

工程は「物質を載せる」だけではありません。誘電率、導電率、仕事関数、固定電荷、dopant分布、寸法、界面粗さを作り込み、Poisson方程式の係数・源・境界を実物へ実装します。

## 寸法ばらつき

平行板近似では

$$
C=\frac{\varepsilon A}{t}
$$

なので膜厚1%の変化は他を固定すれば容量約1%の逆方向変化です。しきい値や漏れは指数的・非線形に敏感な場合があります。

## 演習と全解答

1. implantationとannealingの役割差を述べよ。  
   **解答**：前者はionを導入し、後者は損傷回復・dopant活性化・分布変化を行います。
2. planarizationが必要な理由を述べよ。  
   **解答**：多層形成で段差が累積するとlithography焦点・膜厚・接続が不安定になるためです。
3. 酸化膜厚が2%増えた容量比を一次近似で求めよ。  
   **解答**：約2%減少です。正確には1/1.02で約0.9804倍です。
4. metallizationが単なる理想導線でない理由を述べよ。  
   **解答**：抵抗、容量、inductance、electromigration、contact抵抗を持つためです。
5. wafer testとfinal testを分ける理由を述べよ。  
   **解答**：package前に不良dieを除き、assembly後の接続・熱・機能も最終確認するためです。
6. 製造工程を電磁気学へ結びつける一文を書け。  
   **解答**：工程は電荷・材料定数・境界形状を作り、望む電場と電流経路を実装します。

## ナビゲーション

- 前：[package](10_packaging_tsv_chiplets_and_thermal_limits.md)
- 次：[企業マップ](12_company_map_kioxia_micron_skhynix_nvidia.md)
- 関連：[化学](../../11_chemistry/00_overview.md)

## 参考資料

- J. D. Plummer, M. Deal, and P. Griffin, *Silicon VLSI Technology*。
- S. M. Sze, *VLSI Technology*。
