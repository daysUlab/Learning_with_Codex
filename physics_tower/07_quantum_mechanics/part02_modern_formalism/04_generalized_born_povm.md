# 一般化Born則とPOVM――測定結果の確率を表す

## 状態から確率分布へ

状態

$$
\rho
$$

に測定を施し、結果

$$
a
$$

を得る確率を

$$
p(a)=\operatorname{Tr}(\rho E_a)
$$

と書きます。各effect

$$
E_a
$$

は

$$
E_a\geq0,\qquad\sum_aE_a=I
$$

を満たし、この組

$$
\{E_a\}_a
$$

をPOVMと呼びます。正値性から確率は非負、完全性から

$$
\sum_ap(a)=\operatorname{Tr}\rho=1
$$

です。また

$$
I-E_a\geq0
$$

なので

$$
0\leq p(a)\leq1
$$

です。

## なぜ一般測定が必要か

binary detectorのclick/no-click、dark countを含むdetector、有限分解能の位置検出、非直交状態の識別は、常に直交射影だけでは表せません。

たとえば読み出しerror

$$
\epsilon
$$

を持つz測定は

$$
E_0=(1-\epsilon)|0\rangle\langle0|
+\epsilon|1\rangle\langle1|,
$$

$$
E_1=I-E_0
$$

です。

$$
0<\epsilon<1/2
$$

ならeffectはprojectorではなく、unsharpなPOVMです。

## affine性からの再構成

同じdensity operatorを異なる確率混合で準備しても、測定統計は同じでなければなりません。この確率混合を保存するaffine mapを有限次元で表現するとeffectとのtrace pairingが現れます。これはPOVMの構造を理解する再構成であり、自然界の測定がこの形式を採ることを少数の前提だけから唯一強制した、という主張ではありません。

## 演習と全解答

1.
   $$
   E_0=\begin{pmatrix}0.8&0\\0&0.2\end{pmatrix},
   \quad E_1=I-E_0
   $$
   がPOVMか確認せよ。
   **解答**：両者の固有値は0.8,0.2で非負、和は
   $$
   I
   $$
   なのでPOVMです。
2.
   $$
   \rho=|0\rangle\langle0|
   $$
   で上の測定をした確率を求めよ。
   **解答**：
   $$
   p(0)=0.8,\quad p(1)=0.2
   $$
3.
   $$
   E_+=|+\rangle\langle+|,\quad E_-=|-\rangle\langle-|
   $$
   の完全性を示せ。
   **解答**：x基底の完全系なので
   $$
   E_++E_-=I
   $$
4. effect
   $$
   E=1.2|0\rangle\langle0|
   $$
   が二値POVMの一要素になれない理由を述べよ。
   **解答**：
   $$
   I-E
   $$
   が負固有値
   $$
   -0.2
   $$
   を持ち、ある状態で確率が1を超えるためです。
5. POVMが定めるものを答えよ。
   **解答**：各状態に対するoutcome probabilityです。一般には測定後状態までは定めません。
6. 確率混合
   $$
   \rho=q\rho_1+(1-q)\rho_2
   $$
   に対するaffine性を示せ。
   **解答**：
   $$
   \operatorname{Tr}(E_a\rho)
   =q\operatorname{Tr}(E_a\rho_1)
   +(1-q)\operatorname{Tr}(E_a\rho_2)
   $$

## 参考・ナビゲーション

- 参考：[ボルンの確率規則はどこから来るのか？（qm大学物理）](https://qmcharge.com/article-povm)（確認日：2026-07-27。凸性・affine性の説明を検討し、唯一の導出とは扱わない）
- 前：[pureとmixed](03_pure_mixed_state_vector.md)
- 次：[PVMと物理量](05_pvm_observables.md)
