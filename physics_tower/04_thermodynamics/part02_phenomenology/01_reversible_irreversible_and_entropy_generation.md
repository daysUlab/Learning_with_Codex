# 可逆・不可逆とentropy生成

## 問い

微視的な運動方程式が時間反転対称でも、なぜ熱は一方向へ流れ、摩擦は元に戻らないのでしょうか。熱力学は機構を仮定せず、entropy生成で不可逆性を記述します。

entropy balanceを

$$
dS=\frac{\delta Q}{T_b}+dS_{\mathrm{gen}}
$$

と書きます。境界温度は

$$
T_b
$$

で

$$
dS_{\mathrm{gen}}\ge0
$$

です。

有限温度差の熱伝導、粘性、拡散、電気抵抗、free expansionでentropyが生成します。

## 二物体の熱接触

熱容量

$$
C_1,C_2
$$

が一定で、初期温度

$$
T_1>T_2
$$

なら孤立全体の最終温度はenergy balanceから

$$
T_f=\frac{C_1T_1+C_2T_2}{C_1+C_2}
$$

entropy変化は

$$
\Delta S=C_1\ln\frac{T_f}{T_1}+C_2\ln\frac{T_f}{T_2}>0
$$

です。

## 演習と全解答

1. 準静的なら必ず可逆か。
   **解答**：いいえ。摩擦や有限差があれば不可逆です。
2. free expansionのentropy生成はゼロか。
   **解答**：ideal gasでも正です。
3. 電気抵抗のJoule heatは不可逆か。
   **解答**：有限抵抗でentropyを生成します。
4. 等しい熱容量、400 Kと300 Kの最終温度は何か。
   **解答**：
   $$
   T_f=350\ \mathrm{K}
   $$
5. 逆向きmovieが法則上不可能という意味か。
   **解答**：微視方程式では許されても、低entropyの特殊初期条件が必要で巨視的確率が極小です。
6. entropy生成を負にする冷蔵庫は可能か。
   **解答**：装置単独では低温部のentropyを減らせますが、仕事源と高温側を含む全体では非負です。

## 接続

微視的可逆性から巨視的不可逆性が現れる理由は[横断記事](../../cross_connections/04_micro_reversibility_macro_irreversibility.md)と統計力学で再訪します。

- 前：[第2法則](../part01_laws/04_second_law_entropy_and_engines.md)
- 次：[potentialと平衡](02_potentials_equilibrium_phase_chemical.md)
- 親：[part02](README.md)
