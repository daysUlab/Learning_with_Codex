# 電磁気学の単位・符号・向き――答案の検算帳

> 章内位置：14 / 15「単位・符号の整理」
> 単位系：SI
> 時間規約：
>
> $$
> e^{-i\omega t}
> $$

## 1. 主要量のSI単位

| 量 | 記号 | SI単位 |
|---|---|---|
| 電荷 | q | C |
| 電荷密度 | ρ | C/m³ |
| 電流 | I | A |
| 電流密度 | J | A/m² |
| 電位 | φ | V |
| 電場 | E | V/m = N/C |
| 電束密度 | D | C/m² |
| 磁束密度 | B | T = V·s/m² |
| 磁場 | H | A/m |
| 電気分極 | P | C/m² |
| Poyntingベクトル | S | W/m² |
| エネルギー密度 | u | J/m³ |
| 導電率 | σ | S/m |

同じ単位でも同じ概念とは限りません。電束密度と分極は同じ単位ですが、定義と役割が違います。

## 2. Maxwell方程式の次元検算

Gauss則：

$$
[\nabla\cdot\mathbf{D}]=\frac{\mathrm{C/m^2}}{\mathrm m}=\mathrm{C/m^3}=[\rho_{\mathrm f}]
$$

Faraday則：

$$
[\nabla\times\mathbf{E}]=\mathrm{V/m^2}
$$

$$
\left[
\frac{\partial\mathbf{B}}{\partial t}
\right]=\mathrm{T/s}=\mathrm{V/m^2}
$$

Ampère–Maxwell則：

$$
[\nabla\times\mathbf{H}]=\mathrm{A/m^2}
$$

$$
\left[
\mathbf{J}_{\mathrm f}
+\frac{\partial\mathbf{D}}{\partial t}
\right]=\mathrm{A/m^2}
$$

## 3. 面と周回方向

Stokesの定理では、面法線と境界の周回方向は右手則で結びます。右手の親指を面法線へ向け、指が曲がる向きが正の周回方向です。

この図は、符号を決める順番を示します。

```mermaid
flowchart LR
  A["面法線 n を宣言"] --> B["右手則で周回方向"]
  B --> C["磁束・線積分の正負"]
  C --> D["Faradayの負号"]
  D --> E["物理的向きを検算"]
```

閉曲面の面素は外向きです。媒質境界では

$$
\hat{\mathbf n}:1\to2
$$

を最初に宣言します。

## 4. Faraday則の負号

固定回路に対して

$$
\oint_C\mathbf{E}\cdot d\mathbf{l}=-\frac{d}{dt}\int_S\mathbf{B}\cdot d\mathbf{S}
$$

です。負号だけを暗記せず、

1. 法線を決める。
2. 正の周回方向を決める。
3. 磁束の時間微分の符号を求める。
4. その負を起電力の符号とする。

の順で判定します。レンツの法則はこの向きが変化を妨げることを物理的に確認する検算です。

## 5. 外積と右手則

Lorentz力：

$$
\mathbf{F}=q\mathbf{v}\times\mathbf{B}
$$

負電荷では、右手則で求めた

$$
\mathbf{v}\times\mathbf{B}
$$

と反対向きです。

平面波：

$$
\mathbf{S}=\mathbf{E}\times\mathbf{H}
$$

なので、電場から磁場へ右手を回した親指方向がエネルギー流です。

## 6. 境界条件の符号

法線を媒質1から2へ取ると

$$
\hat{\mathbf n}\cdot
(\mathbf{D}_2-\mathbf{D}_1)=\sigma_{\mathrm f}
$$

$$
\hat{\mathbf n}\cdot
(\mathbf{B}_2-\mathbf{B}_1)=0
$$

$$
\hat{\mathbf n}\times
(\mathbf{E}_2-\mathbf{E}_1)=\mathbf 0
$$

$$
\hat{\mathbf n}\times
(\mathbf{H}_2-\mathbf{H}_1)=\mathbf{K}_{\mathrm f}
$$

です。法線を反転すれば、差の順序または右辺の符号も一貫して反転させます。

## 7. 複素表示の符号

時間規約

$$
e^{-i\omega t}
$$

では

$$
\frac{\partial}{\partial t}\longrightarrow-i\omega
$$

です。Faraday則は

$$
\nabla\times\mathbf{E}_0=i\omega\mathbf{B}_0
$$

Ampère–Maxwell則は

$$
\nabla\times\mathbf{H}_0=\mathbf{J}_0-i\omega\mathbf{D}_0
$$

となります。別の規約を混ぜると、複素波数・誘電率・位相の虚部符号が逆転します。

## 8. 最低限の極限検算

- 電荷をゼロにして場の源が消えるか。
- 時間変化をゼロにして静電・静磁場へ戻るか。
- 導電率をゼロにして損失なし媒質へ戻るか。
- 誘電率を真空値へ戻して真空式になるか。
- 距離を無限大にして、近傍場より放射場が支配するか。

## 9. 演習問題

1. Poyntingベクトルの単位を示せ。
2. 表皮深さ

$$
\delta=\sqrt{\frac{2}{\mu\sigma\omega}}
$$

が長さの次元を持つことを示せ。
3. 法線を反転したとき、電束密度の境界条件を書き直せ。
4. 正の電荷が東向きに動き、磁場が北向きのとき磁気力の向きを求めよ。
5. 同じ条件で電子の力の向きを求めよ。
6. 採用時間規約で時間微分の置換を書け。
7. 磁束が正方向へ増えるとき、正の周回方向に測った起電力の符号を答えよ。
8. 電磁エネルギー密度の単位を確認せよ。

## 10. 全解答

1.

$$
[\mathbf{E}\times\mathbf{H}]=\mathrm{\frac{V}{m}\frac{A}{m}}=\mathrm{W/m^2}
$$

です。
2.

$$
[\mu\sigma\omega]=\mathrm{m^{-2}}
$$

なので平方根の逆数は長さです。
3.

$$
(-\hat{\mathbf n})\cdot
(\mathbf{D}_1-\mathbf{D}_2)=\sigma_{\mathrm f}
$$

で、同じ物理内容です。
4. 東を

$$
+\hat{\mathbf x}
$$

北を

$$
+\hat{\mathbf y}
$$

とすれば

$$
\hat{\mathbf x}\times\hat{\mathbf y}=\hat{\mathbf z}
$$

なので上向きです。
5. 負電荷なので下向きです。
6.

$$
\partial_t\to-i\omega
$$

です。
7.

$$
\frac{d\Phi_B}{dt}>0
$$

なら

$$
\mathcal E<0
$$

です。
8.

$$
[\varepsilon E^2]=\mathrm{J/m^3}
$$

で、磁気項も同じです。

## 11. 学習チェックとナビゲーション

- 面法線を先に宣言してから周回方向を決められる。
- 時間規約から微分の符号を再現できる。
- 単位と極限を独立した検算に使える。

- 前：[問題選択](02_problem_selection.md)
- 次：[補習入口](../remedial/README.md)
- 親：[Q&A入口](README.md)
