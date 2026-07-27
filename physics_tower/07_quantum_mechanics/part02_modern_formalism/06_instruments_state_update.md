# 測定確率と測定後状態――quantum instrument

## POVMだけでは足りない

POVMは

$$
p(a)=\operatorname{Tr}(\rho E_a)
$$

を定めますが、結果

$$
a
$$

を得た後の状態を一般には一意に定めません。測定の各結果へ、完全正値でtrace非増加なmap

$$
\mathcal I_a
$$

を割り当て、

$$
p(a)=\operatorname{Tr}[\mathcal I_a(\rho)],
\qquad
\rho_a=\frac{\mathcal I_a(\rho)}{p(a)}
$$

とする組をquantum instrumentと呼びます。

## Kraus operator

$$
\mathcal I_a(\rho)
=\sum_\mu M_{a\mu}\rho M_{a\mu}^\dagger,
$$

$$
\sum_\mu M_{a\mu}^\dagger M_{a\mu}=E_a
$$

です。全結果を無視したnon-selective stateは

$$
\rho'=\sum_a\mathcal I_a(\rho)
$$

です。全Kraus operatorが

$$
\sum_{a,\mu}M_{a\mu}^\dagger M_{a\mu}=I
$$

を満たせばtraceを保存します。

## 同じPOVM、違う更新

zのPVMに対するideal Lüders instrumentは

$$
\mathcal I_a(\rho)=P_a\rho P_a
$$

です。一方、結果確率は同じまま、結果

$$
a
$$

の後に必ず別の状態

$$
|\phi_a\rangle
$$

を再準備する破壊的測定も作れます。したがってprojection postulateは重要なidealizationですが、一般測定の定義ではありません。

## 演習と全解答

1.
   $$
   M_0=|0\rangle\langle0|,\quad M_1=|1\rangle\langle1|
   $$
   のcompletenessを確認せよ。
   **解答**：
   $$
   M_0^\dagger M_0+M_1^\dagger M_1=I
   $$
2.
   $$
   |\psi\rangle=(3|0\rangle+4|1\rangle)/5
   $$
   を上のinstrumentで測る確率を求めよ。
   **解答**：
   $$
   p_0=9/25,\quad p_1=16/25
   $$
3. 0を得たselective stateを求めよ。
   **解答**：
   $$
   \rho_0=|0\rangle\langle0|
   $$
4. 結果を捨てたstateを求めよ。
   **解答**：
   $$
   \rho'=\frac9{25}|0\rangle\langle0|
   +\frac{16}{25}|1\rangle\langle1|
   $$
   で、元のcoherenceは消えます。
5. 同じPOVMでも異なる更新が可能な例を述べよ。
   **解答**：z結果をLüders ruleで残す装置と、z結果を記録後に常に
   $$
   |0\rangle
   $$
   を再準備する装置は同じz確率を持ちますがpost-stateが異なります。
6. destructive photon detectorをprojectionだけで表しにくい理由を述べよ。
   **解答**：click確率に加えphoton吸収で入力system自体が失われ、出力空間やpost-stateの指定が必要だからです。

## 参考・ナビゲーション

- 参考：[測定後状態とは何か？（qm大学物理）](https://qmcharge.com/article-post-measurement-state)、[射影仮説と波束の収縮](https://qmcharge.com/article-projection-postulate)（確認日：2026-07-27。条件付きstate、一般測定、Lüders型更新の区別を検討）
- 前：[PVM](05_pvm_observables.md)
- 次：[量子channel](07_channels_unitary.md)
