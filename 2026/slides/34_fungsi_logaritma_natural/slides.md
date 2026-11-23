---
theme: default
background: '#0c1018'
title: 'MA1101 Kalkulus I - Fungsi Logaritma Natural'
info: |
  ## MA1101 Kalkulus I
  FMIPA Institut Teknologi Bandung
  Subtopik 6.1: Fungsi Logaritma Natural
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
---

# MA1101 Kalkulus I
<p class="text-xl text-amber-400 font-semibold mt-2">Bab 6: Fungsi Transenden</p>
<p class="text-sm text-slate-300 mt-1">Subtopik 6.1: Fungsi Logaritma Natural</p>

<div class="mt-8 max-w-xl mx-auto text-left">
<SocraticBlock type="question" title="Pertanyaan Kita Hari Ini">

Kita sudah bisa mencari antiturunan $x^2$, $x^{10}$, bahkan $x^{-5}$. Fungsi apa yang turunannya $\dfrac{1}{x}$?

</SocraticBlock>
</div>

<!--
Jangan dijawab sekarang. Bacakan, beri jeda 10 detik, lalu katakan: "Di akhir kuliah, kalian sendiri yang akan menjawabnya."
Jika ada yang menjawab "ln x" dari SMA: "Bagus. Hari ini kita cari tahu apa sebenarnya ln x itu, dan mengapa turunannya 1/x."
-->

---

<h2 class="slide-title">
  <span>Mulai dari Soal: Aturan Pangkat yang Macet</span>
  <span class="text-xs text-slate-400 font-mono">Pakai yang sudah kita tahu</span>
</h2>

<BeamerBlock type="block" title="Aturan pangkat untuk antiturunan">

$$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$$

</BeamerBlock>

<SocraticBlock type="question" mode="Kerjakan di kertas · 1 mnt">

Pakai rumus itu untuk $n = 2,\ 1,\ 0,\ -2$. Lalu coba $n = -1$, yaitu $\displaystyle\int \frac{1}{x}\,dx$. Di mana rumusnya macet?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Yang biasanya muncul">

$\tfrac{x^3}{3}$, $\tfrac{x^2}{2}$, $x$, $-\tfrac{1}{x}$ semuanya lancar. Untuk $n = -1$ penyebutnya $n + 1 = 0$: rumusnya tidak bisa dipakai.

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Tetapi $\tfrac{1}{x}$ kontinu untuk $x \gt 0$. Teorema Dasar Kalkulus I menjamin antiturunannya ada. Bagaimana kita **menuliskannya**?

</SocraticBlock>

<!--
Tanya: beri 1 menit di kertas untuk empat nilai n, lalu n = −1.
Jawaban diharapkan: pembagian dengan nol.
Jika ada yang menjawab "x⁰/0 = 1/0 tak hingga": "Turunan dari jawaban itu 1/x?"
Pertanyaan lanjutan, jawaban diharapkan: ∫ dari 1 sampai x dari 1/t dt (TDK I). Jika hening: "Ingat TDK I: kalau f kontinu, F(x) = ∫ dari a sampai x f(t) dt adalah antiturunan f. Pilih a berapa?"
Mengapa batas bawah 1 dan bukan 0: 1/t tidak terdefinisi di t = 0.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Luas di Bawah 1/t</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Kita beri nama $L(x) = \displaystyle\int_1^x \frac{1}{t}\,dt$. Untuk $x$ antara $0$ dan $1$, nilai $L(x)$:

**A.** positif  
**B.** negatif  
**C.** nol

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Berapa $L(1)$? Mengapa?
2. Geser $x$ ke kanan. Apakah $L(x)$ terus naik? Cepat atau lambat?

</SocraticBlock>

::right::

<LnAreaBoard mode="area" height="350px" />

<!--
Urutan: (1) minta semua mengangkat jari A/B/C SEBELUM menyentuh applet. (2) Geser x dari 2 ke 0,3, lalu ke 6. (3) Klik untuk pertanyaan pengamatan.
Jawaban diharapkan: B. Integral dari 1 ke x dengan x < 1 berjalan "mundur", jadi tandanya negatif.
Jika banyak memilih A: "Luas memang positif. Tetapi ∫ dari 1 ke 0,5 sama dengan minus ∫ dari 0,5 ke 1. Apa artinya?"
Pengamatan 1: L(1) = 0 karena batas atas sama dengan batas bawah.
Pengamatan 2: terus naik, tetapi makin lambat. Setelah ada yang menyebutnya, centang "tampilkan grafik L(x)".
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Sifat L dari Definisinya</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

Pakai Teorema Dasar Kalkulus I. Berapa $L'(x)$?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$$L'(x) = \frac{1}{x}, \quad x \gt 0$$

Jadi $L$ adalah antiturunan yang kita cari.

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2">

Dari $L'(x)$, apakah $L$ naik atau turun? Mengapa?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer">

$L'(x) = \tfrac{1}{x} \gt 0$ untuk semua $x \gt 0$, jadi $L$ **selalu naik**.

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Kerjakan di kertas · 1 mnt">

Hitung $L''(x)$. Grafik $L$ cekung ke atas atau ke bawah? Cocokkah dengan yang tadi terlihat di applet?

</SocraticBlock>

<SocraticBlock v-click="5" type="answer" title="Kesimpulan Kita">

$L''(x) = -\tfrac{1}{x^2} \lt 0$, jadi grafiknya **cekung ke bawah**: naik terus, tetapi makin lambat. Ditambah $L(1) = 0$.

</SocraticBlock>

<!--
Tiap pertanyaan dibuka dengan klik; beri waktu sebelum klik berikutnya.
P1 jawaban diharapkan: 1/x. Jika ada yang menjawab "1/t": "Variabel bebas L itu x atau t?"
P2: jika ada yang menjawab "turun karena 1/x makin kecil": "Yang mengecil itu L'(x). Tetapi tandanya positif atau negatif?"
P3: jawaban −1/x². Hubungkan dengan applet: naik makin lambat.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Dua Luas yang Mirip</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Luas di bawah $y = \tfrac{1}{t}$ dari $t = 2$ sampai $t = 4$, dibanding luas dari $t = 1$ sampai $t = 2$:

**A.** sama besar  
**B.** dua kali lebih besar  
**C.** setengahnya

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Diskusi berpasangan · 1 mnt">

Ubah $a$ dan $b$, lalu centang "tampilkan luas". Luas dari $b$ sampai $ab$ selalu sama dengan luas yang mana? Tulis dalam bahasa $L$.

</SocraticBlock>

::right::

<LnAreaBoard mode="scale" height="350px" />

<!--
Urutan: (1) minta semua mengangkat jari A/B/C SEBELUM menyentuh applet; posisi awal a = 2, b = 2 sudah menunjukkan 1→2 dan 2→4. (2) Baru centang "tampilkan luas". (3) Geser a dan b ke nilai lain.
Jawaban diharapkan: A. Daerah 2→4 dua kali lebih lebar tetapi tingginya setengah.
Jika banyak memilih B: "Lebarnya memang dua kali. Bagaimana tingginya dibanding daerah pertama?"
Pengamatan, jawaban diharapkan: luas b→ab = luas 1→a, yaitu L(ab) − L(b) = L(a), atau L(ab) = L(a) + L(b).
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Mengapa L(ab) = L(a) + L(b)?</span>
  <span class="text-xs text-slate-400 font-mono">Bukti dengan aturan rantai</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Kerjakan di kertas · 1 mnt">

Ambil $a \gt 0$ tetap. Turunkan $L(ax)$ terhadap $x$. Hasilnya mirip turunan apa?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$$\frac{d}{dx} L(ax) = \frac{1}{ax}\cdot a = \frac{1}{x} = L'(x)$$

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2">

Dua fungsi dengan turunan sama. Apa hubungan $L(ax)$ dan $L(x)$?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer">

Selisihnya konstan: $L(ax) = L(x) + C$.

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Pikir 30 dtk">

Masukkan $x = 1$ untuk mencari $C$. Lalu masukkan $x = b$.

</SocraticBlock>

<SocraticBlock v-click="5" type="answer" title="Kesimpulan Kita">

$x = 1$: $L(a) = 0 + C$, jadi $C = L(a)$. Maka $L(ax) = L(x) + L(a)$, dan untuk $x = b$:

$$L(ab) = L(a) + L(b)$$

</SocraticBlock>

<!--
P1: kesalahan umum lupa mengalikan a (aturan rantai). Tanyakan: "Fungsi dalamnya ax. Turunannya berapa?"
P2: jawaban "berbeda konstanta" (akibat Teorema Nilai Rata-rata). Jika hening: "Kalau F' = G', apa yang bisa dikatakan tentang F − G?"
P3: L(1) = 0 adalah kuncinya. Minta mahasiswa yang menyimpulkan, bukan dosen.
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Sekarang Kita Beri Nama</span>
  <span class="text-xs text-slate-400 font-mono">Definisi: logaritma natural</span>
</h2>

::left::

<BeamerBlock type="block" title="Definisi: Fungsi Logaritma Natural">

$$\ln x = \int_1^x \frac{1}{t}\,dt, \qquad x \gt 0$$

Turunannya $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$.

</BeamerBlock>

<BeamerBlock type="example" title="Sifat (untuk a, b > 0, r rasional)">

- $\ln 1 = 0$
- $\ln(ab) = \ln a + \ln b$
- $\ln\left(\tfrac{a}{b}\right) = \ln a - \ln b$
- $\ln a^r = r \ln a$

</BeamerBlock>

::right::

<SocraticBlock type="question" title="Bagaimana kalau x < 0?" mode="Pikir 30 dtk">

$\ln x$ hanya terdefinisi untuk $x \gt 0$, padahal $\tfrac{1}{x}$ juga ada untuk $x \lt 0$. Turunkan $\ln(-x)$ untuk $x \lt 0$. Apa yang kalian dapat?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Kesimpulan Kita">

$\dfrac{d}{dx}\ln(-x) = \dfrac{-1}{-x} = \dfrac{1}{x}$. Jadi untuk $x \neq 0$:

$$\frac{d}{dx}\ln|x| = \frac{1}{x}, \qquad \int \frac{1}{x}\,dx = \ln|x| + C$$

</SocraticBlock>

<!--
Definisi ditampilkan SETELAH kelas menemukannya sendiri. Katakan: "ln hanyalah nama untuk L yang tadi kita selidiki."
Sifat ln(a/b) dan ln aʳ dibuktikan dengan cara yang sama seperti L(ab); bisa dijadikan latihan rumah.
Pertanyaan x < 0: kesalahan umum lupa tanda minus dari aturan rantai. Tanyakan: "Fungsi dalamnya −x. Turunannya berapa?"
Tekankan nilai mutlak pada ∫ dx/x. Tanpa itu, jawaban salah untuk x negatif.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Grafik y = ln x</span>
  <span class="text-xs text-cyan-400 font-mono">Sketsa dulu, lalu periksa</span>
</h2>

::left::

<SocraticBlock type="predict" title="Sketsa Dulu" mode="Kerjakan di kertas · 2 mnt">

Kita tahu $\ln 1 = 0$, $\ln x$ selalu naik, dan grafiknya cekung ke bawah. Buat sketsa $y = \ln x$. Apa yang terjadi saat $x \to \infty$? Saat $x \to 0^+$?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$\ln 2^n = n \ln 2$ dan $\ln 2 \gt 0$, jadi $\ln x \to \infty$ saat $x \to \infty$. Karena $\ln \tfrac{1}{x} = -\ln x$, $\ln x \to -\infty$ saat $x \to 0^+$: garis $x = 0$ asimtot tegak.  
Daerah asal $(0, \infty)$, daerah hasil semua bilangan real.

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Daerah hasilnya semua bilangan real, jadi ada $x$ dengan $\ln x = 1$. Geser titik pada grafik: kira-kira di mana?

</SocraticBlock>

::right::

<div v-click="1">

<LnAreaBoard mode="graph" height="350px" />

</div>

<!--
Beri 2 menit membuat sketsa di kertas SEBELUM klik. Minta dua mahasiswa menunjukkan sketsanya.
Jawaban diharapkan: naik dari −∞ di dekat sumbu-y, melewati (1, 0), terus naik tanpa batas tetapi makin landai.
Kesalahan umum 1: grafik memotong sumbu-y. Tanyakan: "ln 0 terdefinisi? Apa yang terjadi pada ln(0,1), ln(0,01)?"
Kesalahan umum 2: grafik mendatar ke suatu nilai (ada asimtot datar). Tanyakan: "Berapa ln 4? ln 16? ln 256? Polanya?" (2 ln 2, 4 ln 2, 8 ln 2: naik tanpa batas).
Jika hening: "Hitung ln 2, ln 4, ln 8 dengan sifat ln aʳ. Bertambah berapa tiap kali x dikali 2?"
Klik 1 memunculkan jawaban dan grafik sekaligus. Centang "garis singgung di (1, 0)" untuk menunjukkan kemiringan 1 = ln′(1).
Pertanyaan lanjutan: jawaban sekitar 2,72. Jangan sebut e dulu; itu pembuka 6.3.
-->

---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Turunan ln dari Sebuah Fungsi</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<SocraticBlock type="pitfall" title="Benarkah Cara Dani?" mode="Diskusi berpasangan · 1 mnt">

Dani menulis

$$\frac{d}{dx}\ln(x^2 + 1) = \frac{1}{x^2 + 1}$$

karena "turunan $\ln$ itu satu per isinya". Apa yang terlewat?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Aturan rantai: $\dfrac{d}{dx}\ln u = \dfrac{1}{u}\cdot\dfrac{du}{dx}$. Jadi $\dfrac{d}{dx}\ln(x^2 + 1) = \dfrac{2x}{x^2 + 1}$.

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Sari menulis $\ln(2 + 3) = \ln 2 + \ln 3$. Periksa dengan kalkulator. Sifat mana yang ia salah ingat?

</SocraticBlock>

<!--
Nama tokoh pada slide kesalahan selalu fiktif agar tidak ada mahasiswa yang merasa dituding.
Jawaban diharapkan: lupa mengalikan turunan bagian dalam (2x). Jika hening: "Coba periksa di x = 1 dengan kemiringan grafik ln(x² + 1). Tandanya cocok?"
Pertanyaan lanjutan: ln 5 ≈ 1,609, sedangkan ln 2 + ln 3 = ln 6 ≈ 1,792. Sifatnya ln(ab) = ln a + ln b, untuk perkalian, bukan penjumlahan.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Uraikan Dulu, Baru Turunkan</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.1</span>
</h2>

<PolyaStepper step="1-2" support="full" />

::left::

<BeamerBlock type="example" title="Soal">

Tentukan $\dfrac{dy}{dx}$ untuk $y = \ln \dfrac{(x^2 + 1)^3}{\sqrt{x - 1}}$, dengan $x \gt 1$.

</BeamerBlock>

<SocraticBlock type="question" title="1 · Pahami Soal">

Fungsi di dalam $\ln$ berbentuk apa: perkalian, pembagian, pangkat? Mengapa ada syarat $x \gt 1$?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Pembagian dari dua pangkat. Syarat $x \gt 1$ membuat $\sqrt{x - 1}$ terdefinisi dan isi $\ln$ positif.

</SocraticBlock>

::right::

<div v-click="2" class="flex flex-col">

<SocraticBlock type="question" title="2 · Buat Rencana">

Langsung pakai aturan rantai dan aturan hasil bagi akan panjang. Sifat apa yang bisa membuat bentuknya lebih sederhana dulu?

</SocraticBlock>

</div>

<div v-click="3" class="flex flex-col">

<SocraticBlock type="answer" title="Rencana">

1. Uraikan dengan sifat $\ln$: pembagian jadi pengurangan, pangkat jadi pengali.
2. Turunkan tiap suku dengan $\dfrac{d}{dx}\ln u = \dfrac{u'}{u}$.

</SocraticBlock>

</div>

<!--
Contoh dikerjakan bersama: dosen mencontohkan keempat langkah, tetapi tiap langkah dibuka dengan pertanyaan.
Pahami: jika ada yang menjawab "x > 0 cukup": "Coba x = 0,5. Akar dari −0,5?"
Rencana: jawaban diharapkan "pakai sifat ln dulu". Ini inti pelajaran hari ini: sifat ln memudahkan turunan.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Uraikan Dulu, Baru Turunkan (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.1</span>
</h2>

<PolyaStepper step="3-4" support="full" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan">

$$y = 3\ln(x^2 + 1) - \tfrac{1}{2}\ln(x - 1)$$

$$\frac{dy}{dx} = 3\cdot\frac{2x}{x^2 + 1} - \frac{1}{2}\cdot\frac{1}{x - 1} = \frac{6x}{x^2 + 1} - \frac{1}{2(x - 1)}$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="question" title="4 · Periksa Lagi" mode="Pikir 1 mnt">

Dekat $x = 1$ (sedikit di atas 1), suku mana yang paling besar? Apa artinya bagi grafik $y$ di sana?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Suku $-\tfrac{1}{2(x - 1)}$ menuju $-\infty$, jadi $y' \to -\infty$. Masuk akal: saat $x \to 1^+$ penyebut $\sqrt{x - 1} \to 0$, isi $\ln$ membesar tanpa batas, dan grafik $y$ turun tajam dari $+\infty$ ✓

</SocraticBlock>

<!--
Kerjakan: tulis di papan baris demi baris, slide hanya ringkasan.
Periksa Lagi: tekankan bahwa langkah ini bukan hiasan. Jawaban diharapkan: suku kedua mendominasi dan negatif besar.
Jika hening: "Coba hitung y' di x = 1,01. Kira-kira berapa?" (sekitar −50).
Bandingkan: tanpa menguraikan, kita butuh aturan rantai, hasil bagi, dan pangkat sekaligus.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 2: Lengkapi yang Kosong</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 4 mnt</span>
</h2>

<PolyaStepper step="1-4" support="partial" />

::left::

<BeamerBlock type="example" title="Soal">

Hitung $\displaystyle\int \tan x\,dx$.

</BeamerBlock>

<SocraticBlock type="question" title="1–2 · Pahami Soal & Buat Rencana">

Tulis $\tan x = \dfrac{\sin x}{\cos x}$. Bagian mana yang turunannya muncul di pembilang? Itulah pilihan $u$ untuk substitusi.

</SocraticBlock>

::right::

<BeamerBlock type="example" title="3 · Kerjakan: lengkapi yang kosong">

$$
\begin{aligned}
u &= \boxed{\phantom{000}}, \qquad du = \boxed{\phantom{000}}\,dx \\
\int \frac{\sin x}{\cos x}\,dx &= -\int \frac{du}{u} = \boxed{\phantom{000}} + C
\end{aligned}
$$

</BeamerBlock>

<SocraticBlock v-click type="answer" title="Isian dan Pemeriksaan">

$\cos x$ &nbsp;·&nbsp; $-\sin x$ &nbsp;·&nbsp; $-\ln|u|$, jadi $\displaystyle\int \tan x\,dx = -\ln|\cos x| + C$.  
**Periksa:** $\dfrac{d}{dx}\bigl(-\ln|\cos x|\bigr) = -\dfrac{-\sin x}{\cos x} = \tan x$ ✓

</SocraticBlock>

<!--
Dukungan dikurangi: kerangka masih ada, isinya dikerjakan mahasiswa. Beri 4 menit berpasangan, berkeliling.
Jawaban diharapkan untuk u: cos x, karena turunannya (−sin x) ada di pembilang.
Kesalahan umum: lupa tanda minus dari du; lupa nilai mutlak. Tanyakan: "cos x bisa negatif? Lalu ln cos x terdefinisi?"
Klik untuk isian hanya setelah sebagian besar pasangan selesai.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Turunan Logaritmik</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 6 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal">

Tentukan $\dfrac{dy}{dx}$ untuk $y = \dfrac{(x^2 + 3)^4\,\sqrt{2x + 1}}{(x - 1)^3}$.

</BeamerBlock>

<div class="grid grid-cols-3 gap-3">

<SocraticBlock v-click type="hint" level="1">

Aturan hasil kali dan hasil bagi akan sangat panjang. Alat apa yang mengubah perkalian menjadi penjumlahan?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="2">

Ambil $\ln$ dari kedua ruas (pakai nilai mutlak), lalu uraikan ruas kanan dengan sifat $\ln$.

</SocraticBlock>

<SocraticBlock v-click type="hint" level="3">

$\ln|y| = 4\ln(x^2 + 3) + \tfrac{1}{2}\ln|2x + 1| - 3\ln|x - 1|$. Turunkan kedua ruas terhadap $x$; ruas kiri menjadi $\tfrac{y'}{y}$.

</SocraticBlock>

</div>

<SocraticBlock v-click type="answer" title="Jawaban Akhir & Periksa Lagi">

$y' = y\left(\dfrac{8x}{x^2 + 3} + \dfrac{1}{2x + 1} - \dfrac{3}{x - 1}\right)$. Mengapa kita boleh memakai $\ln|y|$ walaupun $y$ bisa negatif?

</SocraticBlock>

<!--
Mandiri: tidak ada kerangka langkah. Petunjuk dibuka satu per satu HANYA bila kelas macet, beri jeda minimal 1 menit.
Petunjuk 1 mengarahkan ulang, petunjuk 2 menyebut strategi, petunjuk 3 memberi langkah pertama. Tidak ada yang memberi jawaban.
Pemeriksaan: d/dx ln|y| = y'/y berlaku untuk y positif maupun negatif (lihat slide definisi), jadi rumusnya tetap benar di mana y ≠ 0.
Yang ditampilkan hanya jawaban akhir; penyelesaian lengkap dikerjakan di papan bila perlu.
-->

---

<h2 class="slide-title">
  <span>Tulis Sebelum Pulang</span>
  <span class="text-xs text-slate-400 font-mono">Tulis di kertas · 2 mnt</span>
</h2>

<SocraticBlock type="reflect" title="Rangkum dengan Kata-Katamu">

1. Jelaskan kepada teman SMA: apa sebenarnya $\ln x$, dan mengapa turunannya $\tfrac{1}{x}$?
2. Kapan sifat $\ln$ membuat menurunkan jadi lebih mudah? Beri satu contoh.

</SocraticBlock>

<SocraticBlock type="question" title="Untuk Pertemuan Berikutnya">

$\ln x$ selalu naik, jadi tiap nilai $y$ hanya dicapai oleh satu $x$. Artinya $\ln$ punya fungsi invers. Fungsi apa itu, dan berapa nilai $x$ yang membuat $\ln x = 1$?

</SocraticBlock>

<!--
Kumpulkan kertasnya. Pertanyaan 2 memberi data untuk membuka pertemuan berikutnya.
Pertanyaan terakhir tidak dijawab; ia menjadi pembuka 6.2 (fungsi invers) dan 6.3 (fungsi eksponen, bilangan e).
-->
