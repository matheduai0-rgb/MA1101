---
theme: default
background: '#0c1018'
title: 'MA1101 Kalkulus I - Fungsi Eksponen Natural'
info: |
  ## MA1101 Kalkulus I
  FMIPA Institut Teknologi Bandung
  Subtopik 6.3: Fungsi Eksponen Natural
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
---

# MA1101 Kalkulus I
<p class="text-xl text-amber-400 font-semibold mt-2">Bab 6: Fungsi Transenden</p>
<p class="text-sm text-slate-300 mt-1">Subtopik 6.3: Fungsi Eksponen Natural</p>

<div class="mt-8 max-w-xl mx-auto text-left">
<SocraticBlock type="question" title="Pertanyaan Kita Hari Ini">

Adakah fungsi (selain fungsi nol) yang turunannya **sama dengan dirinya sendiri**?

</SocraticBlock>
</div>

<!--
Jangan dijawab sekarang. Bacakan, beri jeda 10 detik, lalu katakan: "Di akhir kuliah, kalian sendiri yang akan menjawabnya."
Jika ada yang menjawab "eˣ" dari SMA: "Bagus. Hari ini kita cari tahu apa sebenarnya e itu, dan mengapa turunannya sama dengan dirinya."
-->

---

<h2 class="slide-title">
  <span>Mulai dari Soal: x Berapa yang Membuat ln x = 1?</span>
  <span class="text-xs text-slate-400 font-mono">Pakai yang sudah kita tahu</span>
</h2>

<BeamerBlock type="block" title="Yang sudah kita tahu (6.1 dan 6.2)">

$\ln x = \displaystyle\int_1^x \frac{1}{t}\,dt$ selalu naik dan kontinu, dengan $\ln 1 = 0$ dan $\ln x \to \infty$ untuk $x \to \infty$. Fungsi yang selalu naik punya invers (Teorema A).

</BeamerBlock>

<SocraticBlock type="question" mode="Kerjakan di kertas · 1 mnt">

Pasti ada tepat satu $x$ dengan $\ln x = 1$. Mengapa **pasti ada**, dan mengapa **hanya satu**? Kira-kira berapa nilainya: lebih kecil atau lebih besar dari $2$? Dari $3$?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Yang biasanya muncul">

Pasti ada karena $\ln$ kontinu dan naik dari $0$ ke nilai yang sangat besar. Hanya satu karena $\ln$ selalu naik. Nilainya sulit ditebak tanpa alat bantu.

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

$\ln x$ adalah luas di bawah $y = \tfrac1t$ dari $1$ sampai $x$. Bagaimana kita bisa mencari $x$ itu dengan gambar luas?

</SocraticBlock>

<!--
Tanya: beri 1 menit di kertas.
"Pasti ada": Teorema Nilai Antara (ln kontinu, ln 1 = 0 < 1 dan ln x besar untuk x besar). "Hanya satu": monoton murni (Teorema A di 6.2).
Untuk perkiraan: luas dari 1 sampai 2 lebih kecil dari 1 (persegi panjang 1 × 1 di atasnya), jadi x > 2.
Pertanyaan lanjutan dijawab di slide berikutnya dengan applet.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Luas Tepat Satu</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Luas di bawah $y = \tfrac1t$ dari $t = 1$ sampai $t = x$ tepat $1$ ketika $x$:

**A.** antara $2$ dan $2{,}5$  
**B.** antara $2{,}5$ dan $3$  
**C.** lebih dari $3$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Geser $x$ sampai luasnya sedekat mungkin dengan $1$. Di antara dua nilai $x$ mana luas itu melewati $1$?
2. Bilangan itu kita beri nama $e$. Berapa $\ln e$?

</SocraticBlock>

::right::

<LnAreaBoard mode="area" height="350px" />

<!--
Urutan: (1) minta semua mengangkat jari SEBELUM menyentuh applet. (2) Geser x ke 2,5 (luas ≈ 0,916), lalu 2,7 (≈ 0,993) dan 2,75 (≈ 1,012).
Jawaban diharapkan: B. Luas melewati 1 antara x = 2,70 dan 2,75. Nilai tepatnya e ≈ 2,71828.
Jika banyak memilih A: "Geser ke 2,5. Luasnya sudah 1?"
Pengamatan 2: ln e = 1, itulah definisi e. Tulis di papan: e ≈ 2,718.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Invers dari ln</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

$\ln$ selalu naik, jadi punya invers. Kita beri nama $\exp$. Kalau $\ln x = y$, berapa $\exp y$? Berapa $\exp(\ln x)$ dan $\ln(\exp y)$?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$\exp y = x$. Jadi $\exp(\ln x) = x$ untuk $x \gt 0$, dan $\ln(\exp y) = y$ untuk semua $y$.

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2">

Pakai sifat $\ln a^r = r\ln a$ dan $\ln e = 1$. Berapa $\ln(e^2)$? $\ln(e^{1/2})$? $\ln(e^r)$ untuk $r$ rasional?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer">

$\ln(e^r) = r \ln e = r$. Jadi $e^r$ adalah bilangan yang $\ln$-nya $r$:

$$\exp r = e^r \quad \text{untuk } r \text{ rasional}$$

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Pikir 30 dtk">

Apa arti $e^{\sqrt 2}$ atau $e^{\pi}$? Pangkat irasional belum pernah kita definisikan. Usulkan cara mendefinisikannya.

</SocraticBlock>

<SocraticBlock v-click="5" type="answer" title="Kesimpulan Kita">

Untuk **semua** $x$ real kita definisikan $e^x = \exp x$. Untuk $x$ rasional artinya sama dengan pangkat biasa, untuk $x$ irasional ini definisi barunya.

</SocraticBlock>

<!--
Tiap pertanyaan dibuka dengan klik, beri waktu sebelum klik berikutnya.
P1: jawaban diharapkan langsung dari arti invers (lihat Teorema A di 6.2).
P2: kesalahan umum: ln(e²) = e. Tanyakan: "ln a^r = r ln a. Di sini a = e, r = 2."
P3: biarkan mahasiswa mengusulkan; arahkan ke "pakai exp, yang sudah terdefinisi untuk semua bilangan real".
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Grafik y = eˣ</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" title="Sketsa Dulu" mode="Kerjakan di kertas · 2 mnt">

Grafik $e^x$ adalah cerminan grafik $\ln x$ terhadap garis $y = x$. Sketsa grafik $e^x$. Apakah ada asimtot? Kalau ada, di mana?

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Geser titik cermin. Mengapa $(1, 0)$ di $\ln$ berpasangan dengan $(0, 1)$ di $e^x$?
2. Asimtot tegak $\ln x$ adalah $x = 0$. Jadi apa asimtot $e^x$? Centang "tampilkan asimtot" untuk memeriksa.
3. Berapa daerah asal dan daerah hasil $e^x$?

</SocraticBlock>

::right::

<ExpBoard mode="reflect" height="380px" />

<!--
Urutan: (1) sketsa di kertas SEBELUM melihat applet. (2) Bandingkan sketsa dengan grafik. (3) Klik untuk pertanyaan pengamatan.
Pengamatan 1: pencerminan menukar x dan y. ln 1 = 0, jadi e⁰ = 1. ln e = 1, jadi e¹ = e.
Pengamatan 2: asimtot tegak x = 0 berubah menjadi asimtot datar y = 0. eˣ → 0 untuk x → −∞, tetapi tidak pernah nol.
Pengamatan 3: daerah asal semua bilangan real (daerah hasil ln), daerah hasil x > 0 (daerah asal ln).
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Temukan Bersama: Turunan eˣ</span>
  <span class="text-xs text-slate-400 font-mono">Pakai Teorema B dari 6.2</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

Tulis $y = e^x$ sebagai $x = \ln y$. Berapa $\dfrac{dx}{dy}$?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$$\frac{dx}{dy} = \frac{1}{y}$$

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2">

Teorema B: turunan invers adalah satu per turunan fungsinya. Jadi berapa $\dfrac{dy}{dx}$?

</SocraticBlock>

<SocraticBlock v-click="3" type="answer" title="Kesimpulan Kita">

$$\frac{dy}{dx} = \frac{1}{dx/dy} = y = e^x$$

</SocraticBlock>

::right::

<ExpBoard mode="slope" height="300px" />

<SocraticBlock v-click="4" type="question" title="Periksa di Applet" mode="Pikir 30 dtk">

Geser $x$, centang "tampilkan angka". Bandingkan tinggi grafik dengan naiknya garis singgung sejauh $1$ ke kanan.

</SocraticBlock>

<!--
P1: dari 6.1, turunan ln y adalah 1/y.
P2: Teorema B di 6.2. Kesalahan umum: menulis dy/dx = 1/x. Tanyakan: "Variabel bebas di x = ln y itu y. Jadi 1/y, lalu y diganti apa?"
Applet: dua ruas teal sama panjang, yaitu tinggi grafik dan naiknya garis singgung. Di x = 0 keduanya 1; di x = 1 keduanya e ≈ 2,718.
Sekarang Pertanyaan Kita Hari Ini sudah terjawab.
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Sekarang Kita Beri Nama</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.3</span>
</h2>

::left::

<BeamerBlock type="block" title="Definisi: Bilangan e dan Fungsi Eksponen Natural">

$e$ adalah bilangan dengan $\ln e = 1$, yaitu $e \approx 2{,}71828$.

Fungsi $\exp = \ln^{-1}$, dan untuk semua $x$ real ditulis $e^x = \exp x$:

$$e^{\ln x} = x \ (x \gt 0), \qquad \ln(e^y) = y \ (\text{semua } y)$$

</BeamerBlock>

<BeamerBlock type="example" title="Sifat dan Kalkulus">

- $e^a e^b = e^{a + b}$ dan $e^a / e^b = e^{a - b}$
- $(e^x)' = e^x$ dan $(e^{u})' = e^{u}\,u'$
- $\int e^x\,dx = e^x + C$

</BeamerBlock>

::right::

<SocraticBlock type="question" title="Mengapa eᵃeᵇ = eᵃ⁺ᵇ?" mode="Pikir 30 dtk">

Ambil $\ln$ dari ruas kiri: $\ln(e^a e^b) = \;?$ Pakai sifat $\ln$ dari 6.1. Apa kesimpulannya?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Kesimpulan Kita">

$\ln(e^a e^b) = \ln e^a + \ln e^b = a + b = \ln(e^{a + b})$. Karena $\ln$ satu-satu, $e^a e^b = e^{a + b}$.

</SocraticBlock>

<SocraticBlock v-click type="reflect" title="Kembali ke Pertanyaan Kita">

Fungsi apa yang turunannya sama dengan dirinya sendiri? Apakah $5e^x$ juga begitu? Bagaimana dengan $e^{2x}$?

</SocraticBlock>

<!--
Definisi ditampilkan SETELAH kelas menemukannya sendiri. Katakan: "Ini hanya nama dan rumus untuk yang tadi kalian temukan."
Pembuktian sifat: semua sifat eˣ diturunkan dari sifat ln dengan cara yang sama. Sifat e^a/e^b bisa jadi latihan rumah.
Pertanyaan terakhir: Ce^x juga (semua kelipatan). e^{2x} turunannya 2e^{2x}, jadi tidak. Ini jembatan ke 6.5 (pertumbuhan eksponensial: y' = ky).
-->

---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Turunan e Pangkat Sesuatu</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<SocraticBlock type="pitfall" title="Benarkah Cara Rina?" mode="Diskusi berpasangan · 1 mnt">

Rina menulis

$$\frac{d}{dx}e^{x^2} = x^2\,e^{x^2 - 1}$$

karena "turunkan pangkatnya ke depan, lalu pangkatnya dikurangi satu". Apa yang keliru?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Aturan pangkat $\dfrac{d}{dx}x^n = nx^{n - 1}$ hanya untuk **alas** yang berubah dan pangkat tetap. Di $e^{x^2}$, alasnya tetap ($e$) dan **pangkatnya** yang berubah. Pakai $\dfrac{d}{dx}e^{u} = e^{u}u'$:

$$\frac{d}{dx}e^{x^2} = e^{x^2}\cdot 2x$$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Dani menulis $\dfrac{d}{dx}x^e = x^e$ karena "turunan e pangkat sesuatu sama dengan dirinya". Benarkah? Apa turunan yang benar?

</SocraticBlock>

<!--
Nama tokoh pada slide kesalahan selalu fiktif agar tidak ada mahasiswa yang merasa dituding.
Jawaban diharapkan: salah aturan. Jika hening: "Periksa di x = 1 dengan applet kemiringan. Kemiringan e^{x²} di x = 1 kira-kira berapa? Rumus Rina memberi berapa?" (2e ≈ 5,4 lawan 1).
Pertanyaan lanjutan: x^e adalah pangkat dengan pangkat tetap e, jadi turunannya e·x^{e−1}. Kebalikan dari kesalahan Rina.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Nilai Maksimum x e⁻ˣ</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.3</span>
</h2>

<PolyaStepper step="1-2" support="full" />

::left::

<BeamerBlock type="example" title="Soal">

Tentukan nilai maksimum $f(x) = x\,e^{-x}$ untuk $x \ge 0$.

</BeamerBlock>

<SocraticBlock type="question" title="1 · Pahami Soal">

Apa yang ditanya: titik maksimum atau nilai maksimum? Berapa $f(0)$? Apa yang terjadi pada $f(x)$ untuk $x$ sangat besar?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Ditanya nilai terbesar $f$. $f(0) = 0$, dan untuk $x$ besar $e^{-x}$ mengecil jauh lebih cepat daripada $x$ membesar, jadi $f(x) \to 0$. Maksimumnya ada di tengah.

</SocraticBlock>

::right::

<div v-click="2" class="flex flex-col">

<SocraticBlock type="question" title="2 · Buat Rencana">

Alat apa dari Bab 3 untuk mencari maksimum? Aturan turunan mana yang dipakai untuk $x\,e^{-x}$?

</SocraticBlock>

</div>

<div v-click="3" class="flex flex-col">

<SocraticBlock type="answer" title="Rencana">

1. Turunkan dengan aturan hasil kali dan $\dfrac{d}{dx}e^{u} = e^{u}u'$.
2. Cari titik kritis dari $f'(x) = 0$.
3. Periksa tanda $f'$ di kiri dan kanan titik itu.

</SocraticBlock>

</div>

<!--
Contoh dikerjakan bersama: dosen mencontohkan keempat langkah, tetapi tiap langkah dibuka dengan pertanyaan.
Pahami: kesalahan umum mencampur titik dan nilai. Tanyakan: "Jawabannya berupa x atau f(x)?"
Untuk x besar: hitung f(10) ≈ 0,00045 di kalkulator.
Rencana, jawaban diharapkan: turunan = 0, uji tanda (Bab 3).
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Nilai Maksimum x e⁻ˣ (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.3</span>
</h2>

<PolyaStepper step="3-4" support="full" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan">

$$
\begin{aligned}
f'(x) &= 1\cdot e^{-x} + x\cdot e^{-x}\cdot(-1) \\
&= e^{-x}\,(1 - x)
\end{aligned}
$$

$e^{-x} \gt 0$, jadi $f'(x) = 0$ hanya di $x = 1$. Nilai maksimum:

$$f(1) = 1\cdot e^{-1} = \frac{1}{e} \approx 0{,}368$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="question" title="4 · Periksa Lagi" mode="Pikir 1 mnt">

Benarkah $x = 1$ memberi maksimum, bukan minimum? Periksa tanda $f'$ di $x = 0{,}5$ dan $x = 2$. Cocokkah dengan $f(0) = 0$ dan $f \to 0$?

</SocraticBlock>

<SocraticBlock v-click type="answer">

$f'(0{,}5) = e^{-0{,}5}(0{,}5) \gt 0$ dan $f'(2) = e^{-2}(-1) \lt 0$: naik lalu turun, jadi maksimum ✓. Nilai $0{,}368$ lebih besar dari $f(0) = 0$ dan dari nilai untuk $x$ besar ✓

</SocraticBlock>

<!--
Kerjakan: tulis di papan baris demi baris, slide hanya ringkasan.
Tekankan mengapa e^{-x} boleh "dibuang" saat mencari f' = 0: eˣ tidak pernah nol (lihat daerah hasil).
Periksa Lagi: langkah ini bukan hiasan. Jika ada waktu, hitung f(0,9) ≈ 0,366 dan f(1,1) ≈ 0,366, keduanya sedikit di bawah 0,368.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 2: Lengkapi yang Kosong</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 4 mnt</span>
</h2>

<PolyaStepper step="1-2" support="partial" />

::left::

<BeamerBlock type="example" title="Soal">

Hitung $\displaystyle\int x\,e^{-x^2}\,dx$.

</BeamerBlock>

<SocraticBlock type="question" title="1–2 · Pahami Soal & Buat Rencana" mode="Diskusi berpasangan · 1 mnt">

$\int e^x\,dx$ sudah kita tahu, tetapi pangkatnya di sini $-x^2$. Bagian mana yang turunannya (hampir) muncul di depan? Itulah pilihan $u$ untuk substitusi.

</SocraticBlock>

::right::

<BeamerBlock type="example" title="Yang sudah kita punya">

Rencana: (1) pilih $u$ dan hitung $du$, (2) ubah integral menjadi $\int e^u\,du$, (3) kembalikan ke $x$.

</BeamerBlock>

<!--
Dukungan dikurangi: rencana sudah diberikan, mahasiswa yang mengisi langkahnya. Beri 1 menit berpasangan untuk Pahami dan Rencana.
Jawaban diharapkan untuk u: −x², karena turunannya −2x, dan x ada di depan.
Jika ada yang memilih u = x: "Turunannya 1. Apakah e^{−x²} menjadi lebih sederhana?"
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 2: Lengkapi yang Kosong (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 4 mnt</span>
</h2>

<PolyaStepper step="3-4" support="partial" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan: lengkapi yang kosong">

$$
\begin{aligned}
u &= -x^2, \qquad du = \boxed{\phantom{000}}\,dx \\
x\,dx &= \boxed{\phantom{000}}\,du \\
\int x\,e^{-x^2}\,dx &= \boxed{\phantom{00}}\int e^{u}\,du = \boxed{\phantom{0000}} + C
\end{aligned}
$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="answer" title="Isian dan Pemeriksaan">

$-2x$ &nbsp;·&nbsp; $-\tfrac12$ &nbsp;·&nbsp; $-\tfrac12$ &nbsp;·&nbsp; $-\tfrac12 e^{-x^2}$, jadi $\displaystyle\int x\,e^{-x^2}\,dx = -\tfrac12 e^{-x^2} + C$.

**Periksa:** $\dfrac{d}{dx}\Bigl(-\tfrac12 e^{-x^2}\Bigr) = -\tfrac12\, e^{-x^2}\cdot(-2x) = x\,e^{-x^2}$ ✓

</SocraticBlock>

<!--
Beri 4 menit berpasangan, berkeliling.
Kesalahan umum: lupa tanda minus atau lupa faktor 1/2. Tanyakan: "du = −2x dx. Kita hanya punya x dx. Dibagi berapa?"
Kesalahan kedua: menulis hasil e^{−x²}/(−2x), yaitu membagi dengan turunan pangkat. Minta pasangan itu menurunkan hasilnya sendiri.
Klik untuk isian hanya setelah sebagian besar pasangan selesai.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Integral Tentu dengan eˣ</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 6 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal">

Hitung $\displaystyle\int_0^{\ln 2} \frac{e^x}{1 + e^x}\,dx$.

</BeamerBlock>

<SocraticBlock type="question" title="Sebelum Mulai" mode="Pikir 30 dtk">

Sebelum menghitung, perkirakan dulu: berapa nilai integran di $x = 0$ dan di $x = \ln 2$? Kira-kira berapa hasil integralnya?

</SocraticBlock>

<!--
Mandiri: tidak ada kerangka langkah. Beri waktu 1 menit sebelum membuka slide petunjuk.
Perkiraan: integran 1/2 di x = 0 dan 2/3 di x = ln 2; panjang selang ln 2 ≈ 0,69; hasil kira-kira 0,4.
Soal ini menyambung ke 6.1: ∫ du/u = ln|u| + C, serta e^{ln 2} = 2.
Lanjutkan ke slide berikutnya untuk petunjuk bertingkat.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Integral Tentu dengan eˣ (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 6 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal (ringkas)">

Hitung $\displaystyle\int_0^{\ln 2} \frac{e^x}{1 + e^x}\,dx$.

</BeamerBlock>

<div class="grid grid-cols-3 gap-3">

<SocraticBlock v-click type="hint" level="1">

Bentuk pecahannya: apakah pembilang adalah turunan dari penyebut? Integral apa yang punya bentuk $\dfrac{u'}{u}$?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="2">

Substitusi $u = 1 + e^x$. Jangan lupa mengubah batas integral ke $u$.

</SocraticBlock>

<SocraticBlock v-click type="hint" level="3">

$du = e^x\,dx$. Batas: $x = 0 \Rightarrow u = 2$, dan $x = \ln 2 \Rightarrow u = 1 + e^{\ln 2} = 3$.

</SocraticBlock>

</div>

<SocraticBlock v-click type="answer" title="Jawaban Akhir & Periksa Lagi">

$\ln 3 - \ln 2 = \ln\tfrac32 \approx 0{,}405$. Cocokkah dengan perkiraan kalian di slide sebelumnya?

</SocraticBlock>

<!--
Mandiri: petunjuk dibuka satu per satu HANYA bila kelas macet, beri jeda minimal 1 menit.
Petunjuk 1 mengarahkan ulang, petunjuk 2 menyebut strategi, petunjuk 3 memberi langkah pertama. Tidak ada yang memberi jawaban.
Penyelesaian: ∫ dari 2 sampai 3 du/u = ln 3 − ln 2 = ln(3/2).
Kesalahan umum: lupa mengganti batas, atau menulis e^{ln 2} = ln 2. Tanyakan: "exp dan ln saling invers. e^{ln 2} = ?"
-->

---

<h2 class="slide-title">
  <span>Tulis Sebelum Pulang</span>
  <span class="text-xs text-slate-400 font-mono">Tulis di kertas · 2 mnt</span>
</h2>

<SocraticBlock type="reflect" title="Rangkum dengan Kata-Katamu">

1. Jelaskan kepada teman SMA: apa sebenarnya bilangan $e$, dan mengapa turunan $e^x$ sama dengan $e^x$?
2. Kapan kalian memakai $\dfrac{d}{dx}e^{u} = e^{u}u'$, dan kapan aturan pangkat? Beri satu contoh masing-masing.

</SocraticBlock>

<SocraticBlock type="question" title="Untuk Pertemuan Berikutnya">

Kita sudah punya $e^x$ untuk semua $x$ real. Bagaimana mendefinisikan $2^x$, misalnya $2^{\sqrt 2}$? Petunjuk: $2 = e^{\ln 2}$.

</SocraticBlock>

<!--
Kumpulkan kertasnya. Pertanyaan 2 memberi data miskonsepsi untuk pembukaan pertemuan berikutnya.
Pertanyaan terakhir tidak dijawab; ia menjadi pembuka 6.4 (fungsi eksponen dan logaritma umum: aˣ = e^{x ln a}).
-->
