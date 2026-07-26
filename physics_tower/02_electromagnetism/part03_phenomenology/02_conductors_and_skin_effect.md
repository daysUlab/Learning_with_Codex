# 導体中の電磁場――Ohm則・拡散・表皮効果

> 章内位置：11 / 15「導体と表皮効果」
> 時間規約：すべての複素振幅で
>
> $$
> e^{-i\omega t}
> $$
>
> を採用する

## このページで答える問い

- 導体内部に電場は存在するのか。
- 交流電流はなぜ表面近くへ偏るのか。
- 表皮深さは何を近似した量で、周波数とどう関係するのか。
- 減衰した電磁エネルギーはどこへ行くのか。

## 1. モデル・仮定・記号

局所的・線形・等方・一様な導体を考えます。巨視的Ohm則は

$$
\mathbf{J}_{\mathrm c}=\sigma\mathbf{E}
$$

です。ここで

$$
\sigma
$$

は導電率、

$$
\mathbf{J}_{\mathrm c}
$$

は伝導電流密度です。媒質の誘電率と透磁率を

$$
\varepsilon,\ \mu
$$

とし、自由電荷密度がバルク内部で十分小さい領域を扱います。

この図は、周波数を上げると伝導応答が波を減衰させ、電流分布が表面へ偏る流れを示します。

```mermaid
flowchart LR
  A["交流電場"] --> B["伝導電流 σE"]
  B --> C["磁場の空間変化"]
  C --> D["複素波数"]
  D --> E["指数減衰"]
  E --> F["Joule損失"]
```

## 2. 導体中のMaxwell方程式

物質中の巨視的方程式を

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

$$
\nabla\times\mathbf{H}=\mathbf{J}_{\mathrm c}
+\frac{\partial\mathbf{D}}{\partial t}
$$

と書きます。構成方程式は

$$
\mathbf{B}=\mu\mathbf{H}
$$

$$
\mathbf{D}=\varepsilon\mathbf{E}
$$

$$
\mathbf{J}_{\mathrm c}=\sigma\mathbf{E}
$$

です。最後の3式には、線形・等方・一様かつ局所応答という条件があります。

## 3. 波動方程式と拡散的振る舞い

Faraday則の回転を取り、

$$
\nabla\times(\nabla\times\mathbf{E})=-\mu\frac{\partial}{\partial t}
\left(\nabla\times\mathbf{H}\right)
$$

を使います。バルク内部で

$$
\nabla\cdot\mathbf{E}\simeq0
$$

とすれば、二重回転恒等式から

$$
\boxed{
\nabla^2\mathbf{E}=\mu\sigma\frac{\partial\mathbf{E}}{\partial t}
+\mu\varepsilon\frac{\partial^2\mathbf{E}}{\partial t^2}
}
$$

を得ます。磁場も同型です。

第1項は拡散方程式型、第2項は波動方程式型です。比は

$$
\frac{\text{伝導電流}}{\text{変位電流}}=\frac{\sigma}{\omega\varepsilon}
$$

で評価できます。

良導体近似は

$$
\boxed{\sigma\gg\omega\varepsilon}
$$

です。このとき

$$
\nabla^2\mathbf{E}
\simeq\mu\sigma\frac{\partial\mathbf{E}}{\partial t}
$$

となり、場は導体内部へ拡散しつつ減衰します。

## 4. 複素波数と表皮深さ

半無限導体を

$$
z>0
$$

に置き、平面波を

$$
\mathbf{E}(z,t)=\Re\left[
\mathbf{E}_0e^{ikz}e^{-i\omega t}
\right]
$$

とします。波動方程式へ代入すると

$$
k^2=\mu\varepsilon\omega^2+i\mu\sigma\omega
$$

です。ここで

$$
k=\beta+i\alpha
$$

と書けば

$$
e^{ikz}=e^{i\beta z}e^{-\alpha z}
$$

なので

$$
\alpha>0
$$

が減衰を表します。

良導体近似では

$$
k^2\simeq i\mu\sigma\omega
$$

より

$$
k\simeq(1+i)\sqrt{\frac{\mu\sigma\omega}{2}}
$$

です。したがって

$$
\alpha\simeq\beta\simeq
\sqrt{\frac{\mu\sigma\omega}{2}}
$$

表皮深さを振幅が

$$
e^{-1}
$$

になる距離として定義すると

$$
\boxed{
\delta=\frac{1}{\alpha}
\simeq\sqrt{\frac{2}{\mu\sigma\omega}}
}
$$

です。

場と電流は

$$
E(z)\propto e^{-z/\delta}
$$

$$
J_{\mathrm c}(z)=\sigma E(z)\propto e^{-z/\delta}
$$

と連続的に減衰します。「電流が表面だけを流れる」は、導体寸法が表皮深さより十分大きい高周波極限の略記にすぎません。

## 5. DC極限と高周波極限

表皮深さの良導体近似式だけを

$$
\omega\to0
$$

へ外挿すると無限大になります。これはDCで一様電流へ戻る傾向を示しますが、厳密なDC分布は導体形状・端子・定常境界条件から求めます。

高周波では

$$
\delta\propto\omega^{-1/2}
$$

なので浸透が浅くなり、実効断面積が減って交流抵抗が増えます。ただし、極端な高周波では

- 導電率の周波数依存
- 表面粗さ
- 異常表皮効果
- 非局所応答

が無視できなくなります。

## 6. Joule損失とエネルギー流

瞬時の単位体積あたり仕事率は

$$
p=\mathbf{J}_{\mathrm c}\cdot\mathbf{E}=\sigma E^2
$$

です。複素振幅を使う時間平均では

$$
\langle p\rangle=\frac{1}{2}\Re\left(
\mathbf{J}_0\cdot\mathbf{E}_0^*
\right)
$$

です。実数の導電率なら

$$
\langle p\rangle=\frac{\sigma}{2}|\mathbf{E}_0|^2
$$

となります。

導体表面へ入るポインティング流束が、内部のJoule損失へ変換されます。したがって「電流分布の減衰」と「電磁エネルギーの散逸」は同じ現象の二つの見方です。

## 7. 数値例：銅の表皮深さ

近似的に

$$
\sigma=5.8\times10^7\ \mathrm{S/m}
$$

$$
\mu\simeq\mu_0
$$

とします。

周波数

$$
f=60\ \mathrm{Hz}
$$

では表皮深さはおよそ

$$
\delta\approx8.5\ \mathrm{mm}
$$

周波数

$$
f=1\ \mathrm{MHz}
$$

では

$$
\delta\approx66\ \mathrm{\mu m}
$$

です。家庭用周波数の細い導線では電流はかなり内部まで流れますが、高周波配線では表面設計が重要になります。

## 8. 回路・送電線・導波路への接続

- 集中定数回路：寸法が波長より十分小さいとき、場の分布を電圧・電流へ圧縮します。
- 送電線：進行波と反射を電圧・電流で記述しつつ、導体損失には表皮効果が入ります。
- 導波路：境界条件が許す横方向モードを解き、導体壁の有限抵抗が減衰を生みます。

回路理論はMaxwell方程式の代替ではなく、長さ・周波数・損失に関する近似の上に作る縮約モデルです。

## 9. 検算・適用範囲・復帰手順

- 次元：

$$
[\mu\sigma\omega]=\mathrm{m^{-2}}
$$

なので表皮深さは長さです。

- 周波数上昇で

$$
\delta
$$

は減少します。

- 導電率上昇で内部電場は小さくなりますが、有限電流には有限電場が必要です。

迷ったら、

1. 時間規約を書く。
2. 伝導電流と変位電流の比を評価する。
3. 一般の複素波数を立てる。
4. 最後に良導体近似を入れる。

の順へ戻ります。

## 10. 演習問題

1. Ohm則の両辺の単位を確認せよ。
2. 導体中の電場の波動方程式を導出せよ。
3. 良導体近似の無次元条件を述べよ。
4. 採用した時間規約で、減衰する波に必要な複素波数の符号を説明せよ。
5. 周波数を100倍にすると表皮深さは何倍になるか。
6. 導電率を4倍にすると表皮深さは何倍になるか。
7. 「表皮効果では表面より内側の電流が厳密にゼロになる」を修正せよ。
8. 平均Joule損失密度を複素振幅で表せ。

## 11. 全解答

1.

$$
[\sigma E]=\mathrm{\frac{A}{V\,m}}\mathrm{\frac{V}{m}}=\mathrm{A/m^2}
$$

で電流密度と一致します。

2. Faraday則へ回転を施し、Ampère–Maxwell則、構成方程式、二重回転恒等式を使うと

$$
\nabla^2\mathbf{E}=\mu\sigma\frac{\partial\mathbf{E}}{\partial t}
+\mu\varepsilon\frac{\partial^2\mathbf{E}}{\partial t^2}
$$

です。

3.

$$
\frac{\sigma}{\omega\varepsilon}\gg1
$$

です。

4.

$$
e^{ikz}e^{-i\omega t}
$$

で

$$
k=\beta+i\alpha,\quad\alpha>0
$$

なら

$$
e^{-\alpha z}
$$

となります。

5.

$$
\delta\propto\omega^{-1/2}
$$

なので10分の1です。

6. 2分の1です。

7. 電場と電流密度は表面から

$$
e^{-z/\delta}
$$

で減衰し、有限の深さで厳密にゼロにはなりません。

8.

$$
\langle p\rangle=\frac{1}{2}\Re\left(
\mathbf{J}_0\cdot\mathbf{E}_0^*
\right)
$$

です。

## 12. 学習チェックとまとめ

- 導体内部の有限電場と伝導電流を説明できる。
- 波動項と拡散項の大小を判定できる。
- 表皮深さの導出、条件、極限を説明できる。
- Joule損失をポインティング定理へ接続できる。

## 回路量への接続

局所Ohm則を一様導体の全長・全断面へ積分すると抵抗値が得られます。[局所Ohm則から抵抗へ](../part04_from_fields_to_circuits/03_resistance_from_local_ohms_law.md)で直流極限を導き、交流では本記事の表皮深さが交流抵抗増加として戻ります。

## ナビゲーション

- 前：[誘電体](01_dielectrics.md)
- 次：[放射](03_radiation_basics.md)
- 親：[現象論README](README.md)
- 補習：[交流の複素表示](../remedial/03_complex_representation_ac.md)
