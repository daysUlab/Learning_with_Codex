# 高速I/Oの信号品質と電力供給

## なぜMaxwellへ戻るか

立上り時間に対して配線遅延が無視できないと、配線は集中抵抗ではなく伝送線路です。特性impedance不整合は反射、隣接線の相互容量・相互inductanceはcrosstalkを生みます。

同時切替電流とpackage inductanceは

$$
V_L=L\frac{dI}{dt}
$$

の電圧変動を生み、ground bounceやsupply droopになります。decoupling capacitorは局所的に電荷を供給します。

## 数値例

package inductance 0.5 nHで1 nsに10 A変化すると

$$
V_L=0.5\times10^{-9}\frac{10}{10^{-9}}=5\ \mathrm V
$$

です。これは単純一経路の極端な値で、実装では多数のpower/ground接続、低inductance化、decouplingで抑えます。

## eye diagramへの入口

多数bitの波形を重ねたeyeは、timing margin、noise margin、jitter、intersymbol interferenceを可視化します。開口が小さいほど判定余裕が少ないことを示します。

## 演習と全解答

1. 同じ電流変化を2 nsにすると上の誘導電圧はいくらか。  
   **解答**：2.5 Vです。
2. 終端の役割を述べよ。  
   **解答**：負荷を特性impedanceへ近づけ反射を抑えます。
3. decoupling容量100 nFから10 Aを1 ns供給した電圧降下を求めよ。  
   **解答**：
   $$
   \Delta V=\frac{I\Delta t}{C}=0.1\ \mathrm V
   $$
4. crosstalkの二つの結合を述べよ。  
   **解答**：相互容量による電界結合と相互inductanceによる磁界結合です。
5. clock周波数だけで伝送線路判定できない理由を述べよ。  
   **解答**：高調波を決める立上り時間、配線長、媒質速度、要求精度が必要です。
6. PDNの意味を述べよ。  
   **解答**：regulatorからpackage・dieまで、必要な周波数帯で低impedanceに電力を供給するnetworkです。

## ナビゲーション

- 前：[GPUと帯域](08_gpu_memory_bandwidth_and_ai.md)
- 次：[packageと熱](10_packaging_tsv_chiplets_and_thermal_limits.md)
- 正本：[伝送線路](../part05_circuit_applications/11_transmission_lines_as_distributed_circuits.md)

## 参考資料

- H. W. Johnson and M. Graham, *High-Speed Digital Design*。
- E. Bogatin, *Signal and Power Integrity—Simplified*。
