# ロジック・メモリ・ストレージを区別する

## 比較

| 層 | 代表 | 揮発性 | 速さ・容量の傾向 | 主な役割 |
|---|---|---:|---|---|
| 演算状態 | register | 揮発 | 最速・最小 | 演算中の値 |
| on-chip memory | SRAM cache | 揮発 | 非常に速い・小 | 再利用データ |
| 主記憶 | DDR DRAM | 揮発 | 中間 | CPU主記憶 |
| accelerator近傍 | HBM | 揮発 | 広帯域 | GPUへ並列供給 |
| 永続記憶 | NAND SSD | 不揮発 | 大容量 | model・dataset・checkpoint |
| 磁気記憶 | HDD | 不揮発 | 大容量・低単価 | archive、容量重視 |

logicはデータを変換し、memoryは状態を保持します。HBMはDRAMの実装方式、SSDはNAND dieにcontroller・firmware・interfaceを加えたシステムです。

```mermaid
flowchart LR
  R["register"] --> C["SRAM cache"]
  C --> H["HBM / DRAM"]
  H --> S["NAND SSD"]
  S --> D["HDD / archive"]
```

右へ行くほど一般に容量は増え、遅延は大きくなります。ただし製品世代とaccess patternに依存します。

## 数値例

1 TB/sのメモリ帯域で100 GBを一度読む理想下限は

$$
t=\frac{100\ \mathrm{GB}}{1000\ \mathrm{GB/s}}=0.10\ \mathrm s
$$

です。演算が速くてもデータ供給時間は消えません。

## 演習と全解答

1. HBMとNANDの最大の役割差を述べよ。  
   **解答**：HBMは揮発性作業メモリ、NANDは不揮発性保存です。
2. SSDとNAND dieは同義か。  
   **解答**：違います。SSDはcontroller、ECC、firmware、interfaceを含みます。
3. registerとcacheの違いを述べよ。  
   **解答**：registerは命令が直接扱う演算状態、cacheは再利用データを自動または明示的に近傍保持します。
4. 2 TB/sで100 GBを読む理想時間を求めよ。  
   **解答**：0.05 sです。
5. TLCとQLCの一般的トレードオフを述べよ。  
   **解答**：QLCはセル当たり容量を増やす一方、電圧窓が狭まり耐久・速度・保持・ECC要求が厳しくなります。
6. 価格順位を固定できない理由を述べよ。  
   **解答**：世代、容量、契約、市況、性能・耐久クラスで変わるためです。

## ナビゲーション

- 前：[part07入口](README.md)
- 次：[CMOSとGPU](02_cmos_logic_and_gpu_switching.md)
