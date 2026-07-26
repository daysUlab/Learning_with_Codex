# 横断4：微視的可逆性と巨視的不可逆性

## apparent paradox

Hamilton方程式はmomentumを反転すれば軌道を戻せるのに、gasは自然に箱の片側へ戻らず、heatは高温側へ戻りません。

解決の鍵は、巨視的非平衡状態へ対応するmicrostateが極端に少ないことです。平衡macrostateは圧倒的多数のmicrostateを持ちます。

$$
S=k_B\ln\Omega
$$

したがってtypicalな時間発展では

$$
\Omega
$$

の大きいmacrostateへ進みます。逆過程は力学的に禁止でなく、精密に相関した特殊microstateを要求します。

## Liouvilleと粗視化

fine-grained phase-space densityはHamilton flowでvolumeを保存します。一方、stretchingとfoldingを有限分解能で平均するとcoarse-grained entropyが増え得ます。初期条件、粗視化、thermodynamic limitが矢の向きに関与します。

## 演習と解答

1. 逆過程は確率ゼロか。
   **解答**：有限系では通常ゼロではなく極小です。
2. Loschmidt reversalに必要なものは何か。
   **解答**：全particle momentumの極端に精密な反転です。
3. recurrenceは第2法則に反するか。
   **解答**：非常に長いrecurrence timeと確率的法則を考えれば実用上矛盾しません。
4. Liouville theoremはentropy増大を直接示すか。
   **解答**：fine-grained entropyは保存するので、粗視化等の追加が必要です。
5. 小系では逆fluctuationを観測できるか。
   **解答**：できます。fluctuation theoremの対象です。
6. 不可逆性を摩擦力だけで説明し尽くせるか。
   **解答**：摩擦自体が未追跡自由度へのenergy移送を粗視化したmodelです。

- 前：[状態](03_micro_macro_thermodynamic_state.md)
- 次：[Legendre](05_legendre_in_mechanics_and_thermodynamics.md)
- 関連：[entropy生成](../04_thermodynamics/part02_phenomenology/01_reversible_irreversible_and_entropy_generation.md)
