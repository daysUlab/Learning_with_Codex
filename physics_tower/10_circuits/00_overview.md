# 10_circuits――回路解析を独立した工学体系として深める

電磁気学章で、Maxwell方程式から電圧・電流・RLC・Kirchhoff則が生まれる由来と近似条件を学んだ後、回路解析そのものを詳しく扱う章です。

## 電磁気学章との役割分担

- [電磁気学のpart04](../02_electromagnetism/part04_from_fields_to_circuits/README.md)：場から端子量への縮約、R・C・Lの由来、Kirchhoff則、Poynting流束、集中定数近似。
- [電磁気学のpart05](../02_electromagnetism/part05_circuit_applications/README.md)：大学受験から工学初歩までの直流・過渡・交流・機器・伝送への橋渡し。
- [電磁気学のpart06](../02_electromagnetism/part06_semiconductor_bridge/README.md)：Poisson方程式、pn接合、MOS capacitor、MOSFETの場と電荷の由来。
- [電磁気学のpart07](../02_electromagnetism/part07_semiconductor_products/README.md)：SRAM・DRAM・NAND・HBM・GPU・SSDを物理deviceからsystemへ接続。
- 本章：Thévenin・Norton、節点・網目解析、フィルタ、二端子対、オペアンプ、ダイオード、トランジスタ、半導体回路、実装・計測。

同じ導出を複製せず、本章では場の自由度を縮約済みの端子モデルから開始します。高周波でその近似が崩れる場合は、電磁気学章の伝送線路・アンテナへ戻ります。

## この章で扱うこと
- 回路網の体系的な解析
- 線形回路の等価化と周波数応答
- 能動素子・半導体回路
- 実装、計測、モデル誤差

半導体回路では、本章はdiode・transistorの端子model、bias、増幅、switching回路を扱います。材料のbandやcarrier統計は量子・統計力学、MOS内部の電位・電荷分布は電磁気学part06を正本とし、重複導出しません。

## ナビゲーション
- 親: [../README.md](../README.md)
- 子:
  - [part01_basics/](part01_basics/)
  - [part02_dc/](part02_dc/)
  - [part03_ac/](part03_ac/)
  - [part04_semiconductors/](part04_semiconductors/)
