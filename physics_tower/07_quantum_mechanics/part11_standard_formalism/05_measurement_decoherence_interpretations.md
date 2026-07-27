# 量子力学の解釈――計算規則の後に残る問い

## 先に確定している操作的予測

本章の本線では次を区別しました。

- state：density operator
- outcome probability：POVMと一般化Born則
- post-measurement state：quantum instrument
- open-system change：CPTP channel
- closed reversible change：unitary
- decoherence：system–environment entanglementによるreduced stateの干渉抑制

これらの計算規則と、「stateは何を表すか」「なぜ一つの結果を経験するか」という解釈を同じ節で混同しません。

## 解釈の地図

| 立場 | 概略 | 通常の予測 |
|---|---|---|
| Copenhagen系 | 古典的記録と量子state、測定更新を実用的に区別。単一の厳密定義ではない | 標準形式 |
| many-worlds | 全体unitaryを保ち、branchingをdecoherenceと結びつける | 通常は標準形式 |
| Bohm型 | wavefunctionに加えて粒子配置を導入するnonlocal theory | 量子平衡では標準形式 |
| objective collapse | 確率的・物理的collapse dynamicsを追加 | parameter領域により差を予測 |
| relational・information-based | stateをsystem間関係、情報、期待などとして読む諸立場 | 多くは標準形式 |

decoherenceはpreferred basisとapparent classicalityを説明しますが、単独で全解釈に共通するsingle-outcome解決を与えるとは限りません。人間の意識が標準理論の必須要素であるとも限りません。

## 演習と全解答

1. decoherenceとobjective collapseの違いを述べよ。  
   **解答**：decoherenceは全体系unitaryとpartial traceで局所干渉を抑える標準過程、objective collapseはunitary以外の物理dynamicsを追加します。
2. 多くの解釈を通常実験だけで区別しにくい理由を述べよ。  
   **解答**：同じdensity operator、Born則、unitaryなどの操作的予測を共有するからです。
3. instrumentと解釈は同じものか。  
   **解答**：違います。instrumentはoutcomeごとの確率とstate updateを計算する数理対象で、その存在論的な読み方は別問題です。
4. many-worldsでdecoherenceが担う役割を述べよ。  
   **解答**：environmentとの相関によりbranch間干渉を実用上抑え、安定な記録basisを選ぶ役割です。
5. Bohm型理論が単純なlocal hidden-variable theoryでない理由を述べよ。  
   **解答**：多粒子guiding equationはconfiguration全体に依存し、Bell相関を再現するためnonlocalです。
6. 「意識が見るとcollapseする」が標準量子論の必須公理か。  
   **解答**：必須ではありません。測定は物理的apparatus・environmentとの相互作用としてmodel化でき、意識を導入しない形式と解釈が多数あります。

## 参考・ナビゲーション

Schlosshauer, *Decoherence and the Quantum-to-Classical Transition*；Stanford Encyclopedia of Philosophy, “Philosophical Issues in Quantum Theory”.

- 前：[不確定性](04_commutators_uncertainty_fourier.md)
- 計算規則：[POVM・instrument](../part02_modern_formalism/README.md)
- decoherence：[decoherenceとtomography](../part02_modern_formalism/09_decoherence_tomography.md)
- 次：[Schrödinger方程式](../part09_schrodinger_dynamics/README.md)
