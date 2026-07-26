# SRAMとcache――双安定回路でbitを保持する

## 6T cell

典型的な6T SRAMは、二つのCMOS inverterを交差結合した4 transistorのlatchと、word lineで制御する2 access transistorから成ります。二つの安定状態が0と1です。

読み出しではbit lineの微小差を検出し、書込みでは外部driverがlatch状態を反転させます。DRAMのような定期refreshは不要ですが、電源を切れば消えます。

## cache hierarchy

on-chip SRAMは高速ですが、6Tと配線・sense回路を要し面積が大きいため容量は限られます。CPU・GPUは複数段cache、register file、shared/local memoryを組み合わせます。名称と管理方式はarchitectureごとに異なります。

## 数値例

32 MiB cacheを6T cellだけで見積もるとbit数は

$$
32\times2^{20}\times8\approx2.68\times10^8
$$

cell transistorだけで

$$
1.61\times10^9
$$

個です。周辺回路も必要です。

## 演習と全解答

1. 6Tの内訳を述べよ。  
   **解答**：交差結合inverterの4Tとaccessの2Tです。
2. SRAMがdynamicでない理由を述べよ。  
   **解答**：電源中は正帰還で状態を再生し続け、電荷を周期refreshしないためです。
3. 64 MiBならcell transistor数は約いくつか。  
   **解答**：上の2倍で約32.2億個です。
4. SRAMがDRAMより大容量化しにくい理由を述べよ。  
   **解答**：1 bit当たり複数transistorと配線を要しcell面積が大きいためです。
5. 読出しが状態を乱す可能性を述べよ。  
   **解答**：access transistor接続で内部node電圧が変化し、cell ratioが不適切だと反転し得ます。
6. cache missの物理的意味を述べよ。  
   **解答**：より遠く遅い階層からデータを搬送し、配線・interfaceのenergyとlatencyを払います。

## ナビゲーション

- 前：[CMOSとGPU](02_cmos_logic_and_gpu_switching.md)
- 次：[DRAM](04_dram_as_a_transistor_capacitor_cell.md)
