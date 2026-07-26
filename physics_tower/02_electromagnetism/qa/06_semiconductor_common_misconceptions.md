# 半導体の頻出誤解

| 誤解 | 修正 |
|---|---|
| 半導体は電磁気学だけで説明できる | 場・容量・電流は読めるが、bandとcarrier統計は量子・統計が必要 |
| 量子力学を終えるまでMOSFETを語れない | 巨視的なgate電場、反転、端子電流、RCは先に学べる |
| 空乏層には電荷がない | 移動carrierが乏しく、固定ionの空間電荷がある |
| gateには電流が流れない | 理想直流は小さいが、充放電電流と漏れがある |
| 電子の向きが電流の向き | 慣用電流は負電荷の移動と逆 |
| 高電位は電子の高energy | 電子の静電energyは電位と逆符号 |
| NAND gateとNAND flashは同じ | 論理関数とmemory string方式で別 |
| HBMは不揮発storage | HBMは積層DRAMで揮発 |

## 診断演習と全解答

1. 「空乏層は真空である」を直せ。  
   **解答**：結晶と固定ionは存在し、移動carrierだけが大幅に減っています。
2. 「gate currentがゼロなのでswitching energyもゼロ」を直せ。  
   **解答**：gate・配線容量の充放電にenergyが必要で、実物には漏れもあります。
3. 電子が右へ動くと慣用電流はどちらか。  
   **解答**：左です。
4. HBMとSSDを一文で区別せよ。  
   **解答**：HBMはGPU近傍の揮発作業memory、SSDはNANDを使う不揮発storageです。
5. Poisson方程式だけでband gapを求められるか。  
   **解答**：求められません。結晶の量子状態が必要です。
6. 短channel効果を全て量子効果と呼べるか。  
   **解答**：呼べません。二次元電場制御など古典静電学の効果も含みます。

## ナビゲーション

- 本文：[半導体への橋](../part06_semiconductor_bridge/README.md)
- 次：[memory製品比較](07_memory_product_comparison.md)
