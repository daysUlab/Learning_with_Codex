# 黒体放射・光電効果・Compton散乱――光は何を運ぶか

## 三つの実験が否定したもの

古典電磁気学は光の伝播を波として正確に記述します。しかし物質とのenergy・運動量交換まで「連続な波だけ」で記述すると破綻します。

| 実験 | 古典予測 | 観測 | 必要な更新 |
|---|---|---|---|
| 黒体放射 | 高周波ほど発散 | 高周波側で減衰 | oscillatorのenergy交換が量子化 |
| 光電効果 | 強度で電子energy増加 | 最大energyは周波数で決まる | photon energy |
| Compton散乱 | 波長は不変 | 散乱角依存の波長shift | photon momentum |

Planck分布は

$$
u(\nu,T)=\frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/(k_{\mathrm B}T)}-1}
$$

です。完全な導出は[量子統計](../../05_statistical_mechanics/part03_quantum_and_applications/01_classical_limit_fermi_bose.md)へ戻り、ここでは

$$
E=h\nu
$$

という交換単位に注目します。

## 光電効果

金属から出る電子の最大運動energyは

$$
K_{\max}=h\nu-\Phi
$$

です。仕事関数を

$$
\Phi=2.0\ \mathrm{eV}
$$

波長を

$$
\lambda=400\ \mathrm{nm}
$$

とすると

$$
h\nu=\frac{hc}{\lambda}\simeq3.10\ \mathrm{eV}
$$

より

$$
K_{\max}\simeq1.10\ \mathrm{eV}
$$

です。強度は主に単位時間のphoton数を増やし、各電子の最大energyを直接増やしません。

## Compton散乱

photonに

$$
p=\frac{h}{\lambda}
$$

を割り当て、electronとのenergy・運動量保存を解くと

$$
\lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)
$$

を得ます。photonは小球だ、という結論ではありません。伝播の干渉は波、検出では離散的交換が現れ、両方を同じ量子状態で記述します。

## 限界と接続

単一photonの状態、偏光、生成消滅を完全に扱うには量子電磁場が必要です。本章の一粒子Schrödinger波動関数をphotonへそのまま適用しません。

## 演習と全解答

1. 周波数を2倍にしたphoton energyはどうなるか。
   **解答**：
   $$
   E'=h(2\nu)=2E
   $$
2. 光電効果で強度だけを上げたとき主に増えるものは何か。
   **解答**：しきい値より高い周波数なら放出electron数です。最大運動energyは周波数で決まります。
3. 波長620 nmのphoton energyを概算せよ。
   **解答**：
   $$
   E\simeq\frac{1240\ \mathrm{eV\,nm}}{620\ \mathrm{nm}}=2.00\ \mathrm{eV}
   $$
4. Compton shiftが最大になる角度を求めよ。
   **解答**：
   $$
   1-\cos\theta
   $$
   が最大の
   $$
   \theta=\pi
   $$
   です。
5. 黒体放射をenergy量子だけで完全に導出できるか。
   **解答**：mode密度とBose占有、熱平衡も必要です。
6. photonを古典粒子だけと呼べない理由を述べよ。
   **解答**：単一photonでも干渉が生じ、経路ごとの古典確率では説明できないためです。

## 参考・ナビゲーション

Planck (1901), Einstein (1905), Compton (1923)；Griffiths & Schroeter, *Introduction to Quantum Mechanics*.

- 前：[part01](README.md)
- 次：[原子と物質波](02_atomic_spectra_and_matter_waves.md)
- 関連：[電磁波](../../02_electromagnetism/00_overview.md)
