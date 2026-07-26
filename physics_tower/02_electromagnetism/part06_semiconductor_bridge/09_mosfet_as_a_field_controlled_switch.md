# MOSFET――ゲート電場でsource–drain電流を制御する

## 構造

MOSFETはsource、drain、gate、bodyの四端子を持ちます。ゲートは酸化膜越しに表面電位を変え、sourceとdrainを結ぶチャネルを作るか消します。

## 巨視的モデル

長チャネルnMOSの単純モデルでは、線形領域で

$$
I_D=\mu_n C_{\mathrm{ox}}'\frac{W}{L}
\left[(V_{GS}-V_T)V_{DS}-\frac{V_{DS}^2}{2}\right]
$$

飽和近似で

$$
I_D=\frac{1}{2}\mu_n C_{\mathrm{ox}}'\frac{W}{L}(V_{GS}-V_T)^2
$$

です。いずれも移動度一定、急峻なthreshold、長channelなどを仮定した近似です。

## スイッチとして読む

gate電圧がしきい値未満ならoff、十分高ければonです。酸化膜が絶縁するため直流gate電流は小さい一方、切替時にはgate容量を充放電します。CMOSではnMOSとpMOSを補完的に使い、静的電力を抑えます。

## 数値例

$$
\mu_n C_{\mathrm{ox}}'\frac{W}{L}=1\ \mathrm{mA/V^2}
$$

$$
V_{GS}-V_T=0.6\ \mathrm V
$$

なら理想飽和電流は

$$
I_D=0.18\ \mathrm{mA}
$$

です。

## 理想像の崩れ

短チャネルではdrain電場も障壁を変え、速度飽和、subthreshold電流、チャネル長変調、gate漏れ、量子閉じ込めが効きます。式は構造理解のための長チャネル近似です。

## 演習と全解答

1. 四端子を列挙せよ。  
   **解答**：source、drain、gate、bodyです。
2. 過駆動電圧を2倍にすると理想飽和電流は何倍か。  
   **解答**：他を固定した二乗則では4倍です。
3. gate直流電流が小さくても電力が必要な理由を述べよ。  
   **解答**：gateと配線の容量を毎回充放電するためです。
4. 上の数値例で係数を2倍にした電流を求めよ。  
   **解答**：0.36 mAです。
5. MOSFETを単なる抵抗と呼べない理由を述べよ。  
   **解答**：gate電圧とdrain電圧で導電チャネルと電流が非線形に変化するためです。
6. 微細化でPoisson方程式が不要になるか。  
   **解答**：不要になりません。量子補正を加えても静電場の自己無撞着計算は中心です。
7. CMOS inverterへの接続を説明せよ。  
   **解答**：入力によりnMOSとpMOSの一方を主にonにし、出力を電源または接地へ接続します。
8. gateを電流源ではなく電場制御と呼ぶ理由を述べよ。  
   **解答**：絶縁膜を越える変位と境界電位がチャネル電荷を変えるためです。

## ナビゲーション

- 前：[MOSコンデンサ](08_mos_capacitor.md)
- 次：[容量・漏れ・破壊](10_device_capacitance_leakage_and_breakdown.md)
- 製品：[CMOSとGPU](../part07_semiconductor_products/02_cmos_logic_and_gpu_switching.md)
