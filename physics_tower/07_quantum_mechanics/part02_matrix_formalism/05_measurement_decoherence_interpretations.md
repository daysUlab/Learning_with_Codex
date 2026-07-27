# 測定・状態更新・decoherence・解釈

## 四つを分ける

| 問題 | 標準的な計算規則 |
|---|---|
| 閉じた系の時間発展 | $$|\psi(t)\rangle=U(t)|\psi(0)\rangle$$ |
| 結果確率 | $$p_i=\langle\psi|P_i|\psi\rangle$$ |
| 理想測定後state | $$|\psi_i\rangle=P_i|\psi\rangle/\sqrt{p_i}$$ |
| 環境を捨てた部分系 | $$\rho_S=\operatorname{Tr}_E\rho_{SE}$$ |

decoherenceではsystemとenvironmentがentangleし、reduced density matrixの特定basisでoff-diagonal成分が小さくなります。干渉が局所的に見えない理由を説明しますが、「なぜ一つの結果を経験するか」を全解釈に共通する形で解決した、とまでは言いません。

## 解釈の地図

計算上ほぼ共通する予測規則と、何が実在し結果がどう成立するかという解釈を分けます。

- Copenhagen系：古典的記述と量子状態、測定更新を実用的に分ける。単一の厳密定義ではない。
- many-worlds：全体のunitary発展を保ち、branchingをdecoherenceと結びつける。
- Bohm型：粒子配置とpilot waveを導入するnonlocalな理論。
- objective collapse：確率的・物理的collapse dynamicsを追加する。
- 操作主義・情報論的立場：準備・操作・結果の予測構造を中心に置く。

意識がcollapseを起こすことは、標準量子力学から必然的に導かれる確定事項ではありません。

## 演習と全解答

1.
   $$
   |\psi\rangle=(3|0\rangle+4|1\rangle)/5
   $$
   をZ測定する確率を求めよ。
   **解答**：
   $$
   p_0=9/25,\qquad p_1=16/25
   $$
2. 0を得た後、同じ理想測定を直ちに繰り返す結果は何か。
   **解答**：0を確率1で得ます。
3. 測定器とentangleしただけでsystem単独はpure stateか。
   **解答**：全体系はpureでも、測定器をtrace outしたsystemは一般にmixedです。
4. decoherenceがBorn則を自動的に導出するか。
   **解答**：decoherenceはbasis選択と干渉抑制を説明しますが、確率解釈の全てを単独で与えるとの合意はありません。
5. 解釈の違いが現在の通常実験予測を常に変えるか。
   **解答**：同じ形式を共有する解釈間では通常変えません。collapse modelなど修正理論は原理的に差を予測し得ます。
6. 測定とunitary発展を同じ式で扱えない、という問題の名前と内容を述べよ。
   **解答**：測定問題です。全体系のunitary重ね合わせと、単一結果・状態更新の関係をどう理解するかが論点です。

## 参考・ナビゲーション

Schlosshauer, *Decoherence and the Quantum-to-Classical Transition*；Stanford Encyclopedia of Philosophy, “Philosophical Issues in Quantum Theory”.

- 前：[不確定性](04_commutators_uncertainty_fourier.md)
- 次：[Schrödinger方程式](../part09_schrodinger_dynamics/01_schrodinger_hamiltonian_continuity.md)
- 後続：[density matrix](../part05_many_body/03_density_matrices_entanglement.md)
