# density matrix・mixed state・entanglement・decoherence

## pureとmixed

pure stateは

$$
\rho=|\psi\rangle\langle\psi|
$$

で、

$$
\rho^2=\rho,\qquad\operatorname{Tr}\rho^2=1
$$

です。classical mixture

$$
\rho=\sum_ip_i|\psi_i\rangle\langle\psi_i|
$$

では一般に

$$
\operatorname{Tr}\rho^2<1
$$

です。期待値は

$$
\langle A\rangle=\operatorname{Tr}(\rho A)
$$

です。

Bell state

$$
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}
$$

は全体ではpureですが、

$$
\rho_A=\operatorname{Tr}_B|\Phi^+\rangle\langle\Phi^+|
=\frac12I
$$

で部分系はmaximally mixedです。entanglementは「相関が強い」だけでなく、全体pure stateが積stateへ因数分解できない構造です。

decoherenceはenvironmentとのentanglementによりreduced stateの干渉項を抑えます。全体系の情報が消滅したとは限らず、環境相関へ拡散します。

## 演習と全解答

1.
   $$
   \rho=|0\rangle\langle0|
   $$
   のpurityを求めよ。
   **解答**：
   $$
   \operatorname{Tr}\rho^2=1
   $$
2.
   $$
   \rho=I/2
   $$
   のpurityを求めよ。
   **解答**：
   $$
   \operatorname{Tr}(I/4)=1/2
   $$
3.
   $$
   |\Phi^+\rangle
   $$
   のZ測定結果を述べよ。
   **解答**：
   $$
   00,\ 11
   $$
   が各1/2で、異なる結果はzeroです。
4. 古典相関
   $$
   (|00\rangle\langle00|+|11\rangle\langle11|)/2
   $$
   とBell stateを区別する測定はあるか。
   **解答**：X basisでBell stateは相関を保ち、古典mixは異なる統計を出します。
5. reduced density matrixから相手側の局所操作を超光速で知れるか。
   **解答**：知れません。局所統計は相手の測定choiceだけでは変わらないno-signallingを満たします。
6. decoherenceとcollapseを同一視しない理由を述べよ。
   **解答**：decoherenceは部分系の干渉抑制をunitary entanglementから説明しますが、単一結果の選択を追加仮定なしに一意化するとは限りません。

## ナビゲーション

- 前：[exchange](02_exchange_slater_mean_field.md)
- 次：[量子情報](../part07_quantum_computing/01_qubits_gates_no_cloning.md)
- 解釈：[測定とdecoherence](../part02_matrix_formalism/05_measurement_decoherence_interpretations.md)
