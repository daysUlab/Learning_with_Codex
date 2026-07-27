# Bell・CHSH実験――局所隠れ変数modelが満たす境界

## 当時の問題

entangled pairの離れた測定結果は強く相関します。量子stateが不完全で、各粒子が測定前から各settingの答えを持つlocal hidden-variable modelで説明できるでしょうか。

## CHSHの前提と不等式

Aliceの二設定

$$
A_0,A_1
$$

とBobの二設定

$$
B_0,B_1
$$

は各回

$$
\pm1
$$

を返すとします。local hidden variable

$$
\lambda
$$

に対し、Aliceの結果はBobのsettingに、Bobの結果はAliceのsettingに依存せず、setting選択が

$$
\lambda
$$

と独立だとすると

$$
S=\langle A_0B_0\rangle+\langle A_0B_1\rangle
+\langle A_1B_0\rangle-\langle A_1B_1\rangle
$$

は

$$
|S|\leq2
$$

を満たします。一回ごとには

$$
A_0(B_0+B_1)+A_1(B_0-B_1)=\pm2
$$

だからです。

## 現代量子論の予測

適切なBell stateと測定軸では

$$
|S|=2\sqrt2
$$

が可能です。実験はloopholeを順に閉じながら量子予測と整合し、上の前提を同時に満たすlocal hidden-variable classを否定しました。

これは「すべての実在論が不可能」「Aliceの操作でBobへmessageを送れる」という意味ではありません。局所marginalは相手のsettingに依存せずno-signallingを満たします。

## 歴史と現代的再解釈

- **歴史的導入**：Bellは1964年、local hidden-variable modelが検証可能な制約を持つことを示した。
- **現在の標準的理解**：entangled density operatorとlocal POVMからjoint probabilityを計算する。
- **測定論**：各wingのsetting・outcome、random choice、detector efficiency、space-like separationを分ける。
- **量子情報**：Bell nonlocalityとalgorithm高速化は別論点である。

## 演習と全解答

1.
   $$
   b_0,b_1=\pm1
   $$
   のとき和と差の一方が0、他方が
   $$
   \pm2
   $$
   であることを示せ。
   **解答**：
   $$
   b_0=b_1
   $$
   なら差が0、異なれば和が0です。
2. deterministic local assignmentで一回のCHSH量の絶対値を求めよ。
   **解答**：非zeroな括弧へ
   $$
   a_i=\pm1
   $$
   が掛かるので必ず2です。
3. 平均して
   $$
   |S|\leq2
   $$
   となる理由を述べよ。
   **解答**：各
   $$
   \lambda
   $$
   で値が
   $$
   \pm2
   $$
   なので、その確率平均は区間
   $$
   [-2,2]
   $$
   内です。
4. 量子最大値はclassical boundの何倍か。
   **解答**：
   $$
   (2\sqrt2)/2=\sqrt2
   $$
5. Bell violationが超光速通信を意味しない理由を述べよ。
   **解答**：各側単独の結果はrandomで、相関は後でclassical communicationにより照合して初めて分かるためです。
6. Bellと量子algorithmを分ける理由を述べよ。
   **解答**：Bellはlocal modelとcorrelationの制約、algorithmは計算problem・circuit・complexityの論点で、前提と結論が異なるためです。

## 参考・ナビゲーション

- Bell, “On the Einstein Podolsky Rosen Paradox” (1964).
- 参考：[Bellの不等式とは？（qm大学物理）](https://qmcharge.com/article-bell-inequality)（確認日：2026-07-27）
- 前：[一粒子干渉・Stern–Gerlach](03_single_particle_interference_and_spin.md)
- 次：[現代量子論の一般構造](../part02_modern_formalism/README.md)
- 発展：[合成系・entanglement](../part02_modern_formalism/08_composite_entanglement.md)
