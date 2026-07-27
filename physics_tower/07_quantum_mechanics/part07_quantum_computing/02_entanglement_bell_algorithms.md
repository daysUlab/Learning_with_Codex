# entanglementを使う量子回路・algorithm

Bell・CHSH不等式は[歴史編のBell実験](../part01_mysteries/04_bell_chsh_experiments.md)を正本とします。local realismの検証とalgorithm高速化を同じ論点として扱いません。

## entangled stateを回路で作る

$$
|00\rangle
\xrightarrow{H\otimes I}
\frac{|00\rangle+|10\rangle}{\sqrt2}
\xrightarrow{\mathrm{CNOT}}
\frac{|00\rangle+|11\rangle}{\sqrt2}
$$

です。このstateは局所stateの積へ分解できません。

このstateはBell testにも使えますが、Bell violationだけで任意のproblemが高速化されるわけではありません。

## algorithmの位置づけ

| algorithm | 速くする対象 | 注意 |
|---|---|---|
| Deutsch–Jozsa | promise problem | 教育的な干渉例 |
| Grover | 非構造探索 | quadratic speedup |
| Shor | 整数因数分解 | fault-tolerant大規模回路が必要 |

Groverではoracleを

$$
O(\sqrt N)
$$

回使い、classicalな

$$
O(N)
$$

queryより少なくします。量子並列性だけで答えが読めるのではなく、正解振幅を増幅する干渉を設計します。

## 演習と全解答

1. Bell stateの二qubit Z測定確率を求めよ。
   **解答**：
   $$
   P(00)=P(11)=1/2
   $$
2. Bell stateを一qubitずつ独立に準備できるか。
   **解答**：できません。積stateへ因数分解できません。
3. Bell testとalgorithmの違いを述べよ。
   **解答**：Bell testはlocal hidden-variable modelのcorrelation boundを検証し、algorithmは入力・出力・queryまたは計算量を比較します。
4.
   $$
   N=10^6
   $$
   のGrover query scaleを概算せよ。
   **解答**：
   $$
   \sqrt N=10^3
   $$
   程度です。
5. Shorが全NP問題を高速化すると言えるか。
   **解答**：言えません。因数分解など特定の代数構造を利用します。
6. reversible computationとquantum computationの違いを述べよ。
   **解答**：unitaryは可逆ですが、量子計算はさらに複素振幅・干渉・entanglement・測定を用います。

## ナビゲーション

- 前：[qubit](01_qubits_gates_no_cloning.md)
- 次：[noiseとhardware](03_noise_error_correction_hardware.md)
- Logic正本：[可逆計算](../../../logic_tower/90_essays/quantum_computing_and_logic/02_reversible_computation.md)
