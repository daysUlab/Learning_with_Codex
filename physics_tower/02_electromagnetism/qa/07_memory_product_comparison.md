# memory製品比較――どの階層を選ぶか

## 選択表

| 要求 | 第一候補 | 理由 |
|---|---|---|
| 演算器直結・最小latency | register / SRAM | on-chip |
| GPU近傍・大bandwidth | HBM | 広幅・積層DRAM |
| CPU主記憶・容量 | DDR DRAM | moduleで拡張 |
| 永続・高速storage | NAND SSD | 不揮発＋controller |
| 最大容量・archive | SSD / HDD | workloadと費用で選択 |

## 判断問題と全解答

1. 100 GB modelを推論中に毎step読む場所としてSSDだけでよいか。  
   **解答**：通常は不十分です。実行working setはHBM/DRAMへ置き、cache再利用します。
2. 電源断後もcheckpointを残す層はどこか。  
   **解答**：NAND SSDやnetwork storageです。
3. HBMとDDRはcell物理が根本的に別か。  
   **解答**：どちらもDRAMで、主差はinterface、積層、package、channel構成です。
4. SRAMを1 TB主記憶にしにくい理由を述べよ。  
   **解答**：6T cellの面積・電力・費用が大きいためです。
5. QLCをwrite-heavy用途へ使う際の注意を述べよ。  
   **解答**：endurance、write amplification、sustained性能、over-provisioningを確認します。
6. 「速い」の意味を分解せよ。  
   **解答**：latency、sequential throughput、random IOPS、tail latency、read/write別に分けます。
7. HBM容量不足時の対策を三つ挙げよ。  
   **解答**：model分割、precision低減、recomputation/offload、batch調整などです。
8. memory階層が必要な根本理由を述べよ。  
   **解答**：速度・容量・energy・面積・不揮発性・費用を一種類で同時最適化できないためです。

## ナビゲーション

- 前：[半導体の誤解](06_semiconductor_common_misconceptions.md)
- 本文：[ロジック・memory・storage](../part07_semiconductor_products/01_logic_memory_and_storage.md)
- 次：[企業value chain](08_semiconductor_company_value_chain.md)
