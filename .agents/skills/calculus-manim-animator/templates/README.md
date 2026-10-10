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
