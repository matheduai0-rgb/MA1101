# Calculus I (MA1101) Socratic Animation Templates

These starter templates embody Grant Sanderson's visual philosophy and Socrates' inquiry-based dialogue, structured across the standard ITB curriculum for single-variable calculus (MA1101) in Indonesian.

---

## Template Directory

| File | Topic & Syllabus Subtopic | Manim Concept & Highlight |
| :--- | :--- | :--- |
| **[`template_scene.py`](./template_scene.py)** | Baseline: Garis Sekan ke Garis Singgung | Baseline 4-act template using `ValueTracker` and `always_redraw`. |
| **[`01_limits_and_continuity.py`](./01_limits_and_continuity.py)** | 1.2 Definisi Limit $\varepsilon$-$\delta$ | Tantangan interaktif: pita target horizontal $\varepsilon$ dan interval respon domain $\delta$. |
| **[`02_derivative_local_linearity.py`](./02_derivative_local_linearity.py)** | 2.2 Kelinieran Lokal Turunan | Menggunakan `MovingCameraScene` untuk memperbesar ($15\times$) kurva hingga tampak lurus (garis singgung). |
| **[`03_riemann_sums_and_integral.py`](./03_riemann_sums_and_integral.py)** | 4.2 Jumlah Riemann & Integral Tentu | Penghalusan partisi bertahap ($\Delta x = 0.8 \to 0.4 \to 0.15 \to 0.04$) bertransformasi menjadi luas kontinu $\int_a^b f(x)\,dx$. |
| **[`04_fundamental_theorem_of_calculus.py`](./04_fundamental_theorem_of_calculus.py)** | 4.3 Teorema Dasar Kalkulus I (TDK I) | Mengapa turunan dari luas akumulasi $A(x)$ adalah tinggi kurva itu sendiri: $dA \approx f(x) \cdot dx \implies \frac{dA}{dx} = f(x)$. |
| **[`05_taylor_polynomials.py`](./05_taylor_polynomials.py)** | 6.4 Pendekatan Polinomial Taylor | Polinomial oskulasi bertingkat ($P_0, P_2, P_4, P_6$) mendekati $\cos(x)$ dengan interval kekonvergenan yang makin lebar. |
| **[`06_related_rates_sliding_ladder.py`](./06_related_rates_sliding_ladder.py)** | 2.8 Laju yang Berkaitan (Tangga Meluncur) | Tangga $5\text{ m}$ meluncur di dinding, vektor kecepatan $\vec{v}_x$ dan $\vec{v}_y$, relasi $\frac{dx}{dt} = -\frac{y}{x}\frac{dy}{dt}$. |
| **[`07_mean_value_theorem.py`](./07_mean_value_theorem.py)** | 3.6 Teorema Nilai Rata-rata (TNR) | Menggeser garis sekan sejajar kurva hingga menyinggung di titik $c \in (a, b)$ dengan gradien $f'(c) = \frac{f(b)-f(a)}{b-a}$. |
| **[`08_concavity_and_inflection.py`](./08_concavity_and_inflection.py)** | 3.2 & 3.3 Kecekungan dan Titik Belok | Garis singgung dinamis melacak perubahan arah rotasi (arah jarum jam $f'' < 0$ vs berlawanan $f'' > 0$) dan titik belok $(0, 0)$. |
| **[`09_applied_optimization_box.py`](./09_applied_optimization_box.py)** | 3.1 & 3.4 Masalah Pengoptimuman (Kotak Karton) | Kotak terbuka dari karton $6 \times 6$, pelacakan titik puncak grafik volume $V(x) = x(6 - 2x)^2$, titik kritis $V'(x) = 0 \implies x = 1$. |
| **[`10_implicit_differentiation.py`](./10_implicit_differentiation.py)** | 2.7 Turunan Implisit (Lingkaran & Garis Singgung) | Menurunkan $x^2 + y^2 = 25$ dengan aturan rantai $\frac{d}{dx}[y^2] = 2y \frac{dy}{dx}$, gradien di $(3, 4)$ adalah $m = -3/4$ tegak lurus jari-jari. |
| **[`11_differentials_and_linear_approximation.py`](./11_differentials_and_linear_approximation.py)** | 2.9 Diferensial dan Hampiran ($\Delta y$ vs $dy$) | Memvisualisasikan $f(x)=\sqrt{x}$, perbandingan geometris $\Delta x = dx$, $dy = f'(a)dx$ vs $\Delta y$, penyusutan galat saat $\Delta x \to 0$, dan hampiran $\sqrt{4.08} \approx 2.02$. |
| **[`12_maximum_and_minimum.py`](./12_maximum_and_minimum.py)** | 3.1 Maksimum dan Minimum (Teorema Nilai Ekstrem & Titik Kritis) | Memvisualisasikan $f(x) = 2x^3 - 3x^2 - 12x + 1$ pada $[-2, 3]$, garis singgung dinamis mendatar $f'(c)=0$, 3 habitat titik kritis, Teorema Nilai Ekstrem (EVT), dan metode selang tertutup. |
| **[`13_monotonicity_and_concavity.py`](./13_monotonicity_and_concavity.py)** | 3.2 Kemonotonan dan Kecekungan | Garis singgung dinamis memadukan tanda $f'(x)$ (naik/turun) dan $f''(x)$ (cekung ke atas/bawah), titik belok di $(0, 0)$. |
| **[`14_monotonic_increasing_definition.py`](./14_monotonic_increasing_definition.py)** | 3.2 Definisi Fungsi Monoton Naik | Eksplorasi formal $\forall x_1 < x_2 \implies f(x_1) < f(x_2)$, tali busur sekan $\frac{\Delta y}{\Delta x} > 0$, dan transisi menuju turunan $f'(x) \ge 0$. |
| **[`15_local_extrema_and_open_intervals.py`](./15_local_extrema_and_open_intervals.py)** | 3.3 Ekstrem Lokal & Ekstrem pada Selang Buka | Visualisasi lingkungan buka $(c-\delta, c+\delta)$, Uji Turunan I & II pada $f(x)=x+\frac{4}{x}$, Teorema Titik Kritis Tunggal, dan limit di batas $\lim_{x\to 0^+} f(x)=\infty, \lim_{x\to\infty} f(x)=\infty \implies$ Minimum Mutlak di $(2, 4)$. |
| **[`16_curve_sketching_with_calculus.py`](./16_curve_sketching_with_calculus.py)** | 3.5 Grafik Fungsi dengan Menggunakan Kalkulus | Metode 7-langkah pada $f(x)=\frac{2x^2}{x^2-1}$, kerangka asimtot tegak ($x=\pm 1$) \& datar ($y=2$), titik puncak $(0,0)$, telemetri matriks tanda $f'$ dan $f''$, serta penarikan 3 cabang kurva mulus. |
| **[`17_mathematical_modeling_pipeline.py`](./17_mathematical_modeling_pipeline.py)** | 3.4 Pemodelan Matematika & Optimasi Terapan | Masalah pemasangan pipa lepas pantai $C(x)=5\sqrt{9+x^2}+3(8-x)$, trade-off dinamis biaya air vs darat, titik kritis stasioner $C'(x)=0 \implies x=2.25\text{ km}$ ($C_{\min}=36\text{ juta}$). |
| **[`18_antiderivatives_family_of_curves.py`](./18_antiderivatives_family_of_curves.py)** | 3.8 Antiturunan & Integral Tak Tentu | Rekonstruksi keluarga kurva $F(x)+C$ dari medan kemiringan $f(x)=\frac{3}{4}x^2-\frac{3}{2}$, kesejajaran garis singgung vertikal, pemilihan kurva melalui titik awal $P(2,1)$, dan notasi Leibniz $\int f(x)\,dx = F(x)+C$. |
| **[`19_differential_equations_separable.py`](./19_differential_equations_separable.py)** | 3.9 Pengantar Persamaan Diferensial | Medan arah 2D $\frac{dy}{dx}=\frac{6x-x^3}{2y}$, pemisahan peubah $\int 2y\,dy = \int (6x-x^3)\,dx$, keluarga kurva solusi umum, dan Masalah Nilai Awal $y(0)=3 \implies y=\sqrt{3x^2-\frac{1}{4}x^4+9}$. |
| **[`20_area_polygon_exhaustion.py`](./20_area_polygon_exhaustion.py)** | 4.1 Luas Daerah (Poligon Dalam/Luar & Sigma) | Metode kelelahan Archimedes pada $y=x^2$ di $[0,2]$, penjepitan luas $A(R_n) \le A(R) \le A(S_n)$, penyusutan celah $\frac{8}{n}$, dan limit jumlah kuadrat $\sum i^2 \to \frac{8}{3}$. |
| **[`21_definite_integral_signed_area.py`](./21_definite_integral_signed_area.py)** | 4.2 Integral Tentu (Jumlah Riemann & Luas Bertanda) | Jumlah Riemann pada $f(x)=x^2-1$ di $[0,2]$ dengan kontribusi negatif ($-A_{\text{bawah}}$) dan positif ($+A_{\text{atas}}$), penghalusan $\|P\|\to 0$, serta konvergensi $\int_0^2 (x^2-1)\,dx = \frac{4}{3}-\frac{2}{3} = +\frac{2}{3}$. |
| **[`22_first_fundamental_theorem_of_calculus.py`](./22_first_fundamental_theorem_of_calculus.py)** | 4.3 Teorema Dasar Kalkulus Pertama (Fungsi Akumulasi) | Dua sumbu bertumpuk: luas bertanda di bawah $f(t)=\frac{1}{2}t^2-3t+4$ dan grafik $A(x)=\int_0^x f(t)\,dt$ yang ditelusuri reaktif, pita tipis $A(x+h)-A(x)\approx f(x)\,h$, limit $h\to 0$, garis singgung $A'(x)=f(x)$ (maks. lokal $A(2)=\frac{10}{3}$, min. lokal $A(4)=\frac{8}{3}$), serta TDK I dan varian aturan rantai $f(g(x))\,g'(x)$. |
| **[`23_riemann_difference_telescoping.py`](./23_riemann_difference_telescoping.py)** | 4.1 & 4.2 Selisih Poligon Luar & Dalam (Menara Teleskopik) | Pembuktian geometris $\lim_{n\to\infty}[A(S_n)-A(R_n)]=0$ pada $y=x^2$ di $[0,2]$: blok galat tiap pias digeser horizontal membentuk satu menara persegi panjang tunggal tinggi $f(b)-f(a)$ dan lebar $\Delta x = 2/n \to 0$, mengapit $A(R)=\frac{8}{3}$. |
| **[`24_liquid_flow_net_change_riemann.py`](./24_liquid_flow_net_change_riemann.py)** | 4.2 & 4.4 Laju Alir Fluida & Teorema Perubahan Total | Tata letak sinkron dua panel: tangki fluida fisik (kiri) berpasangan dengan kurva laju alir kontinu $r(t)=\frac{dV}{dt}$ (kanan). Irisan waktu $\Delta t$ membentuk persegi panjang Riemann luas $r(t_i^*)\Delta t$ yang berkorespondensi langsung dengan lapisan air $\Delta V_i$ di tangki. Penghalusan mesh ($n=4 \to 10 \to 25 \to 60$) menghaluskan lapisan air bertingkat menjadi pengisian kontinu tanpa galat, mengkristalkan $\Delta V = V(T) - V(0) = \lim_{n\to\infty} \sum r(t_i^*)\Delta t = \int_0^T r(t)\,dt$. |
| **[`25_second_fundamental_theorem_of_calculus.py`](./25_second_fundamental_theorem_of_calculus.py)** | 4.4 Teorema Dasar Kalkulus Kedua ($A(x) = F(x) + C$) | Dua sumbu bertumpuk pada $f(t)=\frac{1}{2}t^2-2t+3$ di $[1,4]$: penelusuran fungsi akumulasi $A(x)=\int_1^x f(t)\,dt$, perbandingan kemiringan sejajar dengan antiturunan $F(x)=\frac{x^3}{6}-x^2+3x$ ($A'=f=F'$), celah konstan $C=-F(1)$ dari $A(1)=0$, pergeseran $F$ berimpit dengan $A$, kenaikan $F(4)-F(1)=\frac{20}{3}-\frac{13}{6}=\frac{9}{2}$, serta pembatalan konstanta pada $G(x)=F(x)+2$. |
| **[`26_mean_value_theorem_for_integrals.py`](./26_mean_value_theorem_for_integrals.py)** | 4.5 Teorema Nilai Rata-rata untuk Integral ($\bar{f}=f(c)$) | Transisi rata-rata sampel diskrit $\frac{1}{n}\sum f(x_i)$ pada $f(x)=3x-x^2+1$ di $[0,3]$ menuju $\bar{f}=\frac{1}{b-a}\int_a^b f(x)\,dx=2{,}5$, keseimbangan luas "bukit" di atas $y=h$ dan "lembah" di bawah $y=h$, serta penentuan titik potong $c=\frac{3\pm\sqrt{3}}{2}\in(0,3)$ di mana $(b-a)f(c)=\int_a^b f(x)\,dx$. |
| **[`27_symmetry_in_definite_integrals.py`](./27_symmetry_in_definite_integrals.py)** | 4.5 Penggunaan Simetri pada Integral Tentu (Genap & Ganjil) | Dua panel berdampingan pada $[-2,2]$: pelipatan cermin sumbu-$y$ pada fungsi genap $f(-x)=f(x)$ yang menggandakan luas $\int_{-a}^a f=2\int_0^a f$, rotasi $180^\circ$ terhadap titik asal pada fungsi ganjil $g(-x)=-g(x)$ yang saling menghapuskan luas bertanda $\int_{-a}^a g=0$, peringatan selang tak simetris $[-1,2]$, dan bukti substitusi $u=-x$. |
| **[`28_trapezoidal_and_midpoint_rules.py`](./28_trapezoidal_and_midpoint_rules.py)** | 4.6 Integrasi Numerik (Aturan Trapesium & Titik Tengah) | Perbandingan $L_4, R_4, T_4, M_4$ pada $f(x)=\frac{1}{4}x^2+\frac{1}{2}$ di $[0,4]$, rotasi tutup persegi panjang titik tengah menjadi trapesium garis singgung, peran kecekungan $f''>0$ pada tanda galat, serta batas galat $|E_{M_n}|\approx\frac{1}{2}|E_{T_n}|=\mathcal{O}(1/n^2)$. |
| **[`29_simpsons_parabolic_rule.py`](./29_simpsons_parabolic_rule.py)** | 4.6 Integrasi Numerik (Aturan Parabolik Simpson) | Interpolasi busur parabola melalui 3 titik (2 subselang) dengan luas $\frac{h}{3}(y_0+4y_1+y_2)$, penggabungan keping parabola menghasilkan bobot $1-4-2-4-\dots-4-1$ ($n$ wajib genap), serta batas galat orde keempat $|E_{S_n}|\le\frac{M_4(b-a)^5}{180n^4}$ yang eksak untuk polinom derajat $\le 3$. |
| **[`30_area_between_curves_vertical.py`](./30_area_between_curves_vertical.py)** | 5.1 Luas Daerah di Antara Dua Kurva (Pias Tegak $\Delta x$) | Prinsip "Iris, Hampiri, Integralkan" pada $f(x)=3-\frac{1}{2}(x-1)^2$ dan $g(x)=\frac{1}{2}(x-1)^2-1$ di $[-1,3]$, invariansi tinggi pias $y_{\text{atas}}-y_{\text{bawah}}=f(x)-g(x)$ saat $g(x)<0$, penghalusan partisi menuju $A=\frac{32}{3}$, serta pemecahan $\int_a^b |f(x)-g(x)|\,dx$ untuk kurva berpotongan. |
| **[`31_area_horizontal_vs_vertical_slicing.py`](./31_area_horizontal_vs_vertical_slicing.py)** | 5.1 Strategi Pias Mendatar ($\Delta y$) vs Pias Tegak ($\Delta x$) | Perbandingan dua panel pada daerah $x=y^2$ dan $x=y+2$: pias tegak ($\Delta x$) terbelah di $x=1$ menjadi 2 integral bentuk akar, sedangkan pias mendatar ($\Delta y$) menyapu mulus pada $y\in[-1,2]$ dengan 1 integral polinom $\int_{-1}^2 (y+2-y^2)\,dy = \frac{9}{2}$. |
| **[`32_volumes_disk_and_washer_method.py`](./32_volumes_disk_and_washer_method.py)** | 5.2.a Volume Benda Putar (Metode Cakram & Cincin) | Perbandingan dua panel: cakram pejal $\pi[R(x)]^2$ pada $y=\sqrt{x}$ ($V=8\pi$) vs cincin berlubang $\pi([R(x)]^2-[r(x)]^2)$ di antara $y=\sqrt{x}$ dan $y=\frac{1}{2}x$ ($V=\frac{8\pi}{3}$), peringatan $R^2-r^2\neq(R-r)^2$, dan rotasi terhadap garis $y=k$. |
| **[`33_volumes_parallel_cross_sections.py`](./33_volumes_parallel_cross_sections.py)** | 5.2.b Volume Metode Irisan Sejajar (*Known Cross-Sections*) | Daerah alas $y=\sqrt{x}$ pada $[0,4]$ dengan tali busur tegak $s(x)=\sqrt{x}$ yang membangkitkan 3 bentuk penampang sejajar secara sinkron: Persegi ($s^2 \implies V=8$), Setengah Lingkaran ($\frac{\pi}{8}s^2 \implies V=\pi$), dan Segitiga Sama Sisi ($\frac{\sqrt{3}}{4}s^2 \implies V=2\sqrt{3}$). |
| **[`34_volumes_cylindrical_shells_unrolling.py`](./34_volumes_cylindrical_shells_unrolling.py)** | 5.3 Volume Metode Kulit Tabung (*Cylindrical Shells*) | Mengapa Metode Cincin ($\Delta y$) gagal pada $y=2x^2-x^3$ di $[0,2]$ saat diputar mengelilingi sumbu-$y$, sapuan kulit tabung oleh pias tegak ($\Delta x\parallel$ sumbu-$y$), dan pembentangan menjadi balok bervolume $\Delta V\approx 2\pi x f(x)\,\Delta x \implies V=\frac{16\pi}{5}$. |
| **[`35_shells_vs_washers_and_shifted_axis.py`](./35_shells_vs_washers_and_shifted_axis.py)** | 5.3 Kulit Tabung Antara Dua Kurva & Sumbu Putar $x=k$ | Perbandingan rotasi daerah di antara $y=2x-x^2$ dan $y=x^2$ pada $[0,1]$ mengelilingi sumbu-$y$ ($r(x)=x \implies V=\frac{\pi}{3}$) vs garis $x=2$ ($r(x)=2-x \implies V=\pi$), serta aturan emas memilih Cakram/Cincin ($\perp$) vs Kulit Tabung ($\parallel$). |

---


## Batch Render & Lecture Pack Exporter

Gunakan skrip `build_lecture_pack.py` untuk merender seluruh atau sebagian animasi sekaligus:

```bash
# Menampilkan daftar adegan kalkulus yang terdaftar
../scripts/build_lecture_pack.py --list

# Render cepat seluruh tangkapan layar (PNG keyframe) untuk bahan slide
../scripts/build_lecture_pack.py -s

# Render video kualitas tinggi (1080p60) untuk materi Bab 2 dan Bab 3 (persiapan UTS)
../scripts/build_lecture_pack.py -q high --filter "06"
../scripts/build_lecture_pack.py -q high --filter "07"
```

---

## Quick Individual Preview Commands

Untuk meninjau satu adegan secara instan:
```bash
../scripts/preview_scene.sh 06_related_rates_sliding_ladder.py SlidingLadderScene -s
../scripts/preview_scene.sh 07_mean_value_theorem.py MeanValueTheoremScene -s
../scripts/preview_scene.sh 08_concavity_and_inflection.py ConcavityInflectionScene -s
../scripts/preview_scene.sh 09_applied_optimization_box.py BoxOptimizationScene -s
```
