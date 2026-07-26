# Newton・Lagrange・Hamiltonは何が違うか

## 問いと到達目標

三形式は異なる自然法則ではなく、同じ古典運動をどの変数で表すかの違いです。本ページでは使う変数、初期条件、保存量、計算の向き不向きを比較します。前提は[Newton力学](../../01_dynamics/00_overview.md)です。

| 形式 | 状態・変数 | 中心式 | 強み |
|---|---|---|---|
| Newton | 位置と速度、力 | force＝mass×acceleration | 力の直観、単純なCartesian問題 |
| Lagrange | 一般化座標と速度 | Euler–Lagrange方程式 | 拘束、曲線座標、対称性 |
| Hamilton | 座標と共役運動量 | Hamiltonの正準方程式 | phase space、統計・量子、構造保存 |

保存力で

$$
L=T-V
$$

とすればEuler–Lagrange式はNewton式へ戻ります。さらに

$$
p_i=\frac{\partial L}{\partial\dot q_i},\qquad H=\sum_i p_i\dot q_i-L
$$

でHamilton形式へ移ります。これは情報を増やす変換ではなく、速度を運動量へ取り替えるLegendre変換です。

## 一次元ばねで同じ軌道を確認

$$
V=\frac12kx^2,\qquad L=\frac12m\dot x^2-\frac12kx^2
$$

Euler–Lagrange式は

$$
m\ddot x+kx=0
$$

でNewton式と同じです。共役運動量とHamiltonianは

$$
p=m\dot x,\qquad H=\frac{p^2}{2m}+\frac12kx^2
$$

Hamilton方程式を合成しても同じ二階方程式になります。

## どれを選ぶか

一定力の一次元運動ならNewton式一本が最短です。振り子をCartesian座標で張力まで求めるならNewton、角度だけ欲しいならLagrangeが短い。長時間の多体系simulationやensembleならHamilton形式が構造を見せます。

## 適用限界・誤解

- Hamiltonianは条件によって全エネルギーと一致しない。
- Lagrangianは一意でなく、全時間微分を加えても運動方程式は同じ。
- 形式を変えても、modelや近似の誤りは消えない。

## 演習と全解答

1. 自由粒子の三形式を書け。
   **解答**：
   $$
   m\ddot x=0,\quad L=\frac12m\dot x^2,\quad H=\frac{p^2}{2m}
   $$
   いずれも等速運動を与えます。
2. ばねで保存される量を答えよ。
   **解答**：
   $$
   E=\frac12m\dot x^2+\frac12kx^2
   $$
3. 一定重力下の鉛直運動に最短の形式は何か。
   **解答**：力が一定で拘束もないためNewton形式が最短です。
4. 二階方程式一つはHamilton形式で何本になるか。
   **解答**：座標と運動量の一階方程式二本です。
5. 座標がLに現れないとき何が保存されるか。
   **解答**：その座標の共役運動量です。
6. 形式変更で空気抵抗を無視してよいか。
   **解答**：いいえ。抵抗を省略する近似の妥当性は形式と独立です。

## 学習チェック・ナビゲーション

同じ軌道を与える条件と、単純問題でNewtonが有利な理由を説明できれば合格です。

- 前：[章overview](../00_overview.md)
- 次：[自由度と座標](02_degrees_of_freedom_and_coordinates.md)
- 親：[part01](README.md)

## 参考資料

Goldstein, *Classical Mechanics*, Ch.1–2.
