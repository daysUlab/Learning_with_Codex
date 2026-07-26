# 系・外界・境界・平衡・第0法則

## 問い

粒子を追わずに熱現象を記述する最初の選択は何でしょうか。答えは系の境界と、平衡状態を識別する少数の変数です。

- isolated system：energyもmatterも交換しない。
- closed system：energyは交換するがmatterは交換しない。
- open system：energyとmatterを交換する。
- adiabatic boundary：熱としてのenergy移送を許さない。

平衡状態では、観測時間scaleで巨視量が変化せず、内部に未解消の温度・圧力・chemical potential差がありません。平衡は静止と同義ではなく、微視的運動は続いています。

## 第0法則

系AとB、BとCがそれぞれ熱平衡なら、AとCも熱平衡です。この推移性により各平衡状態へ温度

$$
T
$$

を割り当てられます。

## 状態量

単純圧縮系は例えば

$$
(T,p,V,N,U,S)
$$

で記述しますが、すべて独立ではありません。状態方程式とfundamental relationが制約します。過程は状態空間のpathであり、平衡でない途中を一本の

$$
T,p
$$

で表せない場合があります。

## 演習と全解答

1. 密閉した魔法瓶を分類せよ。
   **解答**：理想化すればisolated、現実には熱漏れの小さいclosed systemです。
2. piston-cylinderはclosedか。
   **解答**：valveを閉じmatterを交換しなければclosedです。
3. 温度が同じならenergyも同じか。
   **解答**：いいえ。質量、物質、相が違えば内部energyは違います。
4. 平衡で分子は止まるか。
   **解答**：止まりません。巨視的平均が時間不変です。
5.
   $$
   300\ \mathrm{K}
   $$
   と
   $$
   310\ \mathrm{K}
   $$
   を接触させると熱はどちらへ移るか。
   **解答**：自発的には高温側から低温側です。
6. 局所平衡とは何か。
   **解答**：全体は非平衡でも、小領域では状態量と平衡関係を近似的に定義できる仮定です。

## 適用範囲・ナビゲーション

急速な衝撃やballistic輸送では局所平衡も破れます。

- 前：[解析力学](../../03_analytical_mechanics/00_overview.md)
- 次：[第1法則](02_first_law_heat_and_work.md)
- 親：[part01](README.md)

## 参考資料

Callen, *Thermodynamics*, Ch.1.
