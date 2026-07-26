# NAND flash――絶縁された電荷でしきい値を記憶する

## cell

floating gateまたはcharge trapへ電荷を蓄え、MOSFETのしきい値電圧を変えます。readは選択gate電圧でchannelが導通するかをsenseします。program・eraseでは高電場とトンネルまたはhot-carrier機構を利用します。

電荷としきい値の単純関係は

$$
\Delta V_T\approx-\frac{\Delta Q_{\mathrm{store}}}{C_{\mathrm{couple}}}
$$

です。符号は蓄積電荷と定義に依存します。

## 多値化

| 方式 | bit/cell | 状態数 |
|---|---:|---:|
| SLC | 1 | 2 |
| MLC | 2 | 4 |
| TLC | 3 | 8 |
| QLC | 4 | 16 |

状態数が増えるほど各しきい値窓が狭くなり、program制御、read reference、ECC、retention、enduranceが厳しくなります。

## 3D NAND

cellを垂直方向へ積層し、面積当たり容量を増やします。word line積層、縦channel、string選択、深い孔の加工、層間ばらつきが重要です。「層数だけ」で性能や歩留まりは決まりません。

## 古典と量子の境界

電荷蓄積による電位・しきい値変化、容量結合、string RCは電磁気学で読めます。障壁透過率、trap準位、保持時間の微視的起源は量子・統計・欠陥物理が必要です。

## 演習と全解答

1. 3 bit/cellの状態数を求めよ。  
   **解答**：
   $$
   2^3=8
   $$
2. 結合容量2 fFへ電子1万個を追加した電圧変化の大きさを求めよ。  
   **解答**：
   $$
   |\Delta V|=\frac{10^4e}{2\ \mathrm{fF}}\approx0.80\ \mathrm V
   $$
3. QLCが16状態を必要とする理由を述べよ。  
   **解答**：4 bitの組合せが16通りだからです。
4. NANDが不揮発である理由を述べよ。  
   **解答**：絶縁されたfloating gateまたはtrapに電荷を保持し、電源なしでもしきい値差が残るためです。
5. enduranceが有限な理由を述べよ。  
   **解答**：高電場program/eraseの反復で絶縁膜・trap分布が劣化するためです。
6. 3D化と微細化を同義としない理由を述べよ。  
   **解答**：垂直積層でcell数を増やす軸と、横寸法を縮める軸は別だからです。
7. トンネルを古典Poissonだけで計算できるか。  
   **解答**：障壁形状は求められても透過率には量子力学が必要です。
8. DRAMとの保持差を述べよ。  
   **解答**：DRAMは漏れをrefreshし続ける揮発容量、NANDは絶縁電荷を長時間保持する不揮発cellです。

## ナビゲーション

- 前：[DRAM](04_dram_as_a_transistor_capacitor_cell.md)
- 次：[SSD](06_ssd_controller_and_nand_system.md)

## 参考資料

- [KIOXIA: NAND flash / memory products](https://www.kioxia.com/en-jp/business/memory.html)（確認日：2026-07-26）。
- [Micron: NAND flash](https://www.micron.com/products/storage/nand-flash)（確認日：2026-07-26）。
