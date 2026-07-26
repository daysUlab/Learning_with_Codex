# 横断6：対称性・保存則・平衡・相転移

## 四つを混同しない

- symmetry：変換してもlawまたはstateが不変。
- conservation：時間発展で量が一定または収支を満たす。
- equilibrium：許された変化に対し適切なpotentialが極値。
- phase transition：control parameterにより平衡stateの構造が非解析的に変わる。

Noetherはactionの連続対称性を保存量へ結びます。一方、equilibrium stateはlawのsymmetryを自発的に破ることがあります。

## ferromagnetの例

外部磁場ゼロのHamiltonianはspin反転に対称でも、低温平衡でmagnetization

$$
M\neq0
$$

を選べます。order parameter

$$
M
$$

のfree energyを

$$
F(M)=a(T-T_c)M^2+bM^4
$$

とmodel化すると、

$$
T>T_c
$$

では

$$
M=0
$$

$$
T<T_c
$$

では

$$
M=\pm\sqrt{\frac{a(T_c-T)}{2b}}
$$

がminimumです。

## 演習と解答

1. equilibriumなら全量が時間不変か。
   **解答**：巨視量は不変でもmicrostateは動きます。
2. symmetryがあれば必ず保存量があるか。
   **解答**：Noether対応はactionの連続対称性です。
3. order parameterとは何か。
   **解答**：phaseを識別する巨視量です。
4. 上式で
   $$
   b>0
   $$
   が必要な理由は何か。
   **解答**：大きな
   $$
   |M|
   $$
   でfree energyを下から有界にするためです。
5. finite systemで真の非解析性はあるか。
   **解答**：通常thermodynamic limitで鋭いtransitionになります。
6. semiconductor pn junctionは自発的対称性破れか。
   **解答**：通常はdoping profileで外的に非対称性を与えた構造で、同じ概念ではありません。

- 前：[Legendre](05_legendre_in_mechanics_and_thermodynamics.md)
- 次：[モデル交代](07_model_changes_to_quantum_statistics.md)
- 関連：[応用map](../05_statistical_mechanics/part03_quantum_and_applications/03_modern_applications_map.md)
