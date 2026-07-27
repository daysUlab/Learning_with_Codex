# 原子スペクトル・Bohr模型・物質波――許される状態は連続か

## 問い

古典電磁気学では加速する荷電粒子は放射し、原子内のelectronは安定な周回軌道を保てません。また運動周波数は連続に選べるため、鋭い線spectraも説明しにくい。何を離散化すべきでしょうか。

## Bohr模型は何を説明し、何を仮定したか

> 歴史的に導入されたmodel
> Bohr模型は1913年当時の半古典的modelです。以下のHamiltonian・遷移確率・photon detectionによる説明をBohr自身の考えとして遡及させません。

水素原子に対して

$$
\frac{m_ev^2}{r}=\frac{e^2}{4\pi\varepsilon_0r^2}
$$

に加え

$$
m_evr=n\hbar
$$

を仮定すると

$$
E_n=-\frac{13.6\ \mathrm{eV}}{n^2}
$$

を得ます。遷移では

$$
h\nu=E_i-E_f
$$

です。水素spectraの主要構造を説明しますが、量子化条件を外から入れ、多電子原子・強度・spinを説明できません。

## de Broglie関係と電子回折

粒子の運動量へ波長

$$
\lambda=\frac{h}{p}
$$

を対応させます。非相対論的electronを電位差

$$
V
$$

で加速すると

$$
eV=\frac{p^2}{2m_e}
$$

より

$$
\lambda=\frac{h}{\sqrt{2m_eeV}}
$$

です。

$$
V=150\ \mathrm V
$$

では

$$
\lambda\simeq0.100\ \mathrm{nm}
$$

となり、結晶格子間隔と同程度なので回折が観測できます。

## モデル交代

Bohrの周回軌道を波打つ円として残すのではなく、後続では

$$
\hat H|\psi\rangle=E|\psi\rangle
$$

の固有状態を求めます。「軌道 orbital」は古典trajectoryではありません。

## 現在の標準的理解

原子spectraはenergy eigenvalueだけで完結しません。少なくとも

$$
H=H_{\rm atom}+H_{\rm field}+H_{\rm int}
$$

と初期stateを指定し、absorption、stimulated emission、spontaneous emissionのtransition amplitude、selection rule、photon detector responseを考えます。一粒子Schrödinger方程式は

$$
H_{\rm atom}
$$

の準位を計算する重要な部分ですが、photon生成を含む全過程にはquantized fieldが要ります。

de Broglie波とelectron回折は、粒子が古典的な物質波へ変身するという意味ではありません。各path amplitudeがphaseを持ち、detectorでは局在eventが記録されます。

## 演習と全解答

1. 水素の
   $$
   n=2
   $$
   のenergyを求めよ。
   **解答**：
   $$
   E_2=-13.6/4=-3.40\ \mathrm{eV}
   $$
2.
   $$
   n=2\to1
   $$
   のphoton energyを求めよ。
   **解答**：
   $$
   10.2\ \mathrm{eV}
   $$
3. 運動量が2倍ならde Broglie波長はどうなるか。
   **解答**：
   $$
   \lambda'=h/(2p)=\lambda/2
   $$
4. 加速電圧を4倍にすると非相対論的electron波長はどうなるか。
   **解答**：
   $$
   \lambda\propto V^{-1/2}
   $$
   なので半分です。
5. Bohr模型が古典論の単なる解でない理由を述べよ。
   **解答**：角運動量量子化と非放射定常軌道を古典力学・電磁気学にない仮定として加えるためです。
6. 電子回折がelectronを通常の連続物質波と確定するか。
   **解答**：いいえ。検出は局在した事象で、理論は確率振幅の伝播と検出統計を同時に記述する必要があります。

## 参考・ナビゲーション

Bohr (1913), de Broglie (1924), Davisson & Germer (1927).

- 前：[光と量子](01_radiation_quanta_and_photons.md)
- 次：[一粒子干渉とspin](03_single_particle_interference_and_spin.md)
- 後続：[水素原子](../part08_quantum_chemistry/01_hydrogen_atom_and_spectra.md)
