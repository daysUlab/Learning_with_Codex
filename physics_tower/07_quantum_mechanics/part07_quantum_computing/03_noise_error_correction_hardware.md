# noise・量子誤り訂正・hardware・量子優位性

## open systemとしての量子computer

主なerrorはenergy relaxation、dephasing、gate・measurement error、leakage、crosstalkです。単純なbit flipだけでなくphase errorがあるため、classical redundancyをそのままcopyできません。

量子誤り訂正はlogical stateを多くのphysical qubitへentangleして符号化し、stateそのものを測らずsyndromeを測ります。threshold以下のlocal errorと十分なresourceがあれば、code distanceを増やしてlogical errorを抑えられるのがfault toleranceの考えです。

| modality | qubit例 | 主なtrade-off |
|---|---|---|
| superconducting circuit | Josephson level | fast gate・cryogenics |
| trapped ion | internal atomic level | high fidelity・slower operation |
| neutral atom | Rydberg state | array scalability・control |
| photon | path・polarization | networking・loss |
| semiconductor spin | electron/nuclear spin | integration・uniformity |

「量子優位性」は特定task・metric・classical baselineに対する実験結果です。全問題、実用価値、energy効率の包括的優位を自動的に意味しません。

本記事は特定vendorの将来roadmapを事実として採用しません。hardware分類とerror correctionの原理は、NIST Quantum Information Program、IBM Quantum Learning、Google Quantum AIの公式技術解説を2026-07-26に確認しました。

## 演習と全解答

1. dephasingが主に壊す情報は何か。
   **解答**：basis state間のrelative phaseと干渉です。
2. no-cloningがあるのに冗長符号化できる理由を述べよ。
   **解答**：未知stateを独立copyせず、ancillaとのunitaryで一つのlogical subspaceへentangleして写すためです。
3. syndrome測定でlogical amplitudeを直接読むか。
   **解答**：読みません。errorに対応するstabilizer情報を得ます。
4. physical qubit数とlogical qubit数を同一視できるか。
   **解答**：できません。誤り訂正では多数physical qubitで一logical qubitを作ります。
5. あるsampling taskでclassical計算を上回れば実用量子computer完成か。
   **解答**：taskの有用性、検証、精度、費用、classical algorithm更新を別に評価します。
6. hardware比較でqubit数だけを見てはいけない理由を述べよ。
   **解答**：connectivity、fidelity、coherence、gate speed、measurement、logical error、control資源が異なるためです。

## 参考・ナビゲーション

- [NIST Quantum Information Science](https://www.nist.gov/topics/quantum-information-science)
- [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning)
- [Google Quantum AI](https://quantumai.google/)
- 前：[Bellとalgorithm](02_entanglement_bell_algorithms.md)
- 次：[相対論・場](../part04_relativistic_qm/01_from_schrodinger_to_quantum_fields.md)
