# 半導体を電磁気・量子・統計で分担する

```mermaid
flowchart LR
    Q["量子<br/>許されるstate・band"] --> S["統計<br/>どのstateを占有"]
    S --> E["電磁気・輸送<br/>電荷・電位・電流"]
    E --> D["device・回路"]
```

| 問い | 正本 |
|---|---|
| なぜband gapがあるか | 量子力学：周期potential・Bloch |
| Fermi levelで何個占有するか | 統計力学：FD・DOS |
| 空乏層の電位はどうなるか | 電磁気学：Poisson |
| gate voltageで電荷がどう変わるか | 電磁気学・統計 |
| oxideをどう透過するか | 量子力学：tunnel |
| 端子電流・RC・発熱 | 輸送・回路・熱 |

一つの理論でdevice全体を説明し切ろうとせず、出力を次modelの入力へ渡します。

## 演習と全解答

1. band gapをPoisson方程式から導けるか。
   **解答**：導けません。周期potentialの量子固有値問題が必要です。
2. band図だけでcarrier濃度を決められるか。
   **解答**：温度、chemical potential、DOS、占有統計が必要です。
3. tunnel currentに電磁気が不要か。
   **解答**：必要です。電場が障壁形状を作り、量子透過と供給carrierを組み合わせます。
4. holeはどの理論の対象か。
   **解答**：band欠損として量子、有効carrierの占有として統計、正電荷輸送として電磁気にまたがります。
5. LEDに必要な三概念を挙げよ。
   **解答**：band間遷移、electron・hole占有、pn接合の注入・電場です。
6. MOSFET微細化の限界を三理論から一つずつ挙げよ。
   **解答**：量子tunnel、統計的carrier・dopant揺らぎ、短channel electrostaticsです。

- 親：[横断README](README.md)
- 量子：[固体・半導体](../07_quantum_mechanics/part10_solid_state_semiconductors/README.md)
- 電磁気：[半導体bridge](../02_electromagnetism/part06_semiconductor_bridge/README.md)
- 統計：[carrier](../05_statistical_mechanics/part03_quantum_and_applications/02_semiconductor_carriers_and_einstein_relation.md)
