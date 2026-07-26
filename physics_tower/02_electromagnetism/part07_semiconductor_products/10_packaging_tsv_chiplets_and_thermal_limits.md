# package・TSV・chiplet・熱

## 用語

- wafer：多数dieを作る基板。
- die：切り出した半導体片。
- package：dieを保護し外部電気・熱接続を提供。
- substrate：package内配線基板。
- interposer：微細なdie間配線を提供。
- TSV：siliconを貫く垂直接続。
- chiplet：機能を分割したdie。
- 2.5D：interposer上で横に接続。
- 3D：dieを垂直積層。

## 性能と熱

配線を短くすれば容量・遅延・energy/bitを減らせます。一方、dieを近接・積層すると電力密度と熱抵抗が問題になります。単純熱モデルは

$$
\Delta T=P R_\theta
$$

です。

## 数値例

300 Wのpackageでjunction-to-coolant熱抵抗が0.08 K/Wなら

$$
\Delta T=24\ \mathrm K
$$

です。局所hot spot、界面熱抵抗、温度依存漏れはこの単一値から外れます。

## 歩留まり

複数dieを一体化すると各dieと接続の良品率が総合歩留まりへ影響します。known-good-die検査、repair、冗長性、assembly順序が重要です。chipletは最適processを分けられますがinterface標準化とpackage設計が必要です。

## 演習と全解答

1. 熱抵抗0.1 K/W、500 Wの温度上昇を求めよ。  
   **解答**：50 Kです。
2. 2.5Dと3Dを区別せよ。  
   **解答**：前者はinterposer上の横並び、後者は垂直積層です。
3. TSVの電気的利点を述べよ。  
   **解答**：長いboard配線より短く広い垂直接続を作れます。
4. chipletの利点と代償を一つずつ述べよ。  
   **解答**：機能別process最適化が利点、die間interface・package複雑化が代償です。
5. Joule発熱だけで温度を決められるか。  
   **解答**：発熱量は求められますが、温度には熱伝導・対流・境界条件が必要です。
6. 積層で上dieが冷えにくい理由を述べよ。  
   **解答**：熱源から冷却面までの材料・界面が増え、熱流経路が制限されるためです。

## ナビゲーション

- 前：[信号品質](09_interconnects_signal_integrity_and_power.md)
- 次：[製造工程](11_semiconductor_manufacturing_overview.md)
- 後で再訪：[熱力学](../../04_thermodynamics/00_overview.md)

## 参考資料

- IEEE Electronics Packaging Society, packaging technology resources。
- JEDEC, high-bandwidth memory family standards（規格本文の公開範囲と版を確認して利用）。
