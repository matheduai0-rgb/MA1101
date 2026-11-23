---
theme: default
background: '#0c1018'
title: 'MA1101 Kalkulus I - Fungsi Eksponen dan Logaritma Umum'
info: 'Subtopik 6.4 · Pertemuan 28 (bagian 1 dari 2, lanjut ke deck 37)'
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
---

# MA1101 Kalkulus I
<p class="text-xl text-amber-400 font-semibold mt-2">Bab 6: Fungsi Transenden</p>
<p class="text-sm text-slate-300 mt-1">Subtopik 6.4: Fungsi Eksponen dan Logaritma Umum · lalu 6.5: Pertumbuhan dan Peluruhan</p>

<div class="mt-8 max-w-xl mx-auto text-left">
<SocraticBlock type="question" title="Pertanyaan Pertama Hari Ini" mode="Pikir 30 dtk">

Apa arti $2^{\sqrt 2}$, dan seberapa curam grafik $y = 2^x$?

</SocraticBlock>
</div>

<!--
Pertemuan ini dua bagian: 6.4 (deck ini, sekitar 47 menit) lalu 6.5 (deck 37, sekitar 45 menit).
Buka dengan dua jawaban anonim tiket keluar pertemuan 27 (f(x) = x + eˣ, hitung (f⁻¹)'(1)): satu yang benar (pasangan x = 0, jawaban 1/2), satu yang memakai x = 1 (kesalahan Bima). Tanya: "Mana yang benar, dan mengapa x = 0?"
Lalu bacakan pertanyaan ini, beri jeda 30 detik. Jangan dijawab: "Di akhir bagian pertama, kalian sendiri yang akan menjawabnya."
-->

---

<h2 class="slide-title">
  <span>Mulai dari Soal: Pangkat yang Tidak Rasional</span>
  <span class="text-xs text-slate-400 font-mono">Pakai yang sudah kita tahu</span>
</h2>

<BeamerBlock type="block" title="Yang sudah kita tahu">

Pangkat rasional bisa dihitung: $2^{1{,}4} = 2^{7/5} = \sqrt[5]{2^7} \approx 2{,}639$. Dari 6.3: $e^x$ terdefinisi untuk **semua** $x$ real, dan $e^{\ln a} = a$.

</BeamerBlock>

<SocraticBlock type="question" mode="Kerjakan di kertas · 1 mnt">

Kalkulator memberi $2^{\sqrt 2} \approx 2{,}665$. Padahal $\sqrt 2$ tidak bisa ditulis sebagai pecahan. Usulkan cara mendefinisikan $2^{\sqrt 2}$. Petunjuk: tulis $2$ sebagai $e^{\text{sesuatu}}$.

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Yang biasanya muncul">

$2 = e^{\ln 2}$, jadi wajar menulis $2^{\sqrt 2} = e^{\sqrt 2\,\ln 2} = e^{0{,}9803\ldots} \approx 2{,}665$, sama dengan kalkulator.

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Sekarang $2^x$ punya arti untuk semua $x$. Seberapa curam grafiknya di $x = 0$? Lebih curam atau lebih landai dari $e^x$?

</SocraticBlock>

<!--
Tanya: 1 menit di kertas. Jawaban yang diharapkan muncul dari jembatan di akhir pertemuan lalu (2 = e^{ln 2}).
Jika ada yang mengusulkan "barisan 2^{1,4}, 2^{1,41}, 2^{1,414}, …": bagus, itu benar secara intuisi. Tanya: "Rumus apa yang langsung memberi nilainya tanpa barisan?"
Hitung di kalkulator: √2 · ln 2 ≈ 0,9803; e^{0,9803} ≈ 2,6651.
Pertanyaan lanjutan dijawab di applet berikutnya.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Seberapa Curam aˣ?</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Kemiringan grafik $y = 2^x$ di $x = 0$ adalah:

**A.** $0$, karena "turunan $2^x$ adalah $x\cdot 2^{x-1}$"  
**B.** sekitar $0{,}7$  
**C.** $1$, sama seperti $e^x$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Dengan $a = 2$, centang "tampilkan angka" dan geser $x$. Apa yang **tetap** walaupun $x$ berubah?
2. Ubah alas $a$. Untuk $a$ berapa kemiringan sama dengan tinggi?

</SocraticBlock>

::right::

<PowerBaseBoard height="380px" />

<!--
Miskonsepsi yang diuji: turunan a^x dikira x a^(x-1) (aturan pangkat dipakai pada pangkat yang berubah).
Urutan: (1) semua mengangkat jari SEBELUM applet disentuh. (2) Di a = 2, x = 0: kemiringan ≈ 0,693. (3) Geser x ke 1: tinggi 2, kemiringan 1,386, rasionya tetap 0,693. (4) Ubah a ke 3 (rasio 1,099), lalu ke 2,7 (≈ 0,993): mendekati 1 saat a mendekati e.
Jawaban diharapkan: B. Jika banyak memilih A: "Grafik 2^x di x = 0 naik atau datar?" Jika memilih C: "Bandingkan dengan garis putus-putus eˣ. Siapa yang lebih curam?"
Pengamatan 1: kemiringan ÷ tinggi tetap = ln a. Angka ini dijelaskan di slide berikutnya; jangan dijelaskan dulu.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Turunan aˣ</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

Seperti $2^{\sqrt 2}$, tulis $a^x$ sebagai $e$ pangkat sesuatu, untuk $a \gt 0$.

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$$a^x = e^{x\ln a}$$

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2" mode="Diskusi berpasangan · 1 mnt">

Turunkan $e^{x\ln a}$ dengan $(e^{u})' = e^{u}u'$. Cocokkah hasilnya dengan rasio di applet?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer" title="Kesimpulan Kita">

$$\frac{d}{dx}a^x = e^{x\ln a}\cdot\ln a = a^x\ln a$$

Kemiringan ÷ tinggi $= \ln a$: untuk $a = 2$ itu $0{,}693$, dan bernilai $1$ tepat saat $a = e$.

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Pikir 30 dtk">

Kalau turunan $a^x$ adalah $a^x\ln a$, berapa $\displaystyle\int a^x\,dx$?

</SocraticBlock>

<SocraticBlock v-click="5" type="answer">

$$\int a^x\,dx = \frac{a^x}{\ln a} + C \qquad (a \ne 1)$$

</SocraticBlock>

<!--
Tiap pertanyaan dibuka dengan klik, beri waktu sebelum klik berikutnya.
P1: langsung dari slide sebelumnya; definisi a^x untuk semua x real (Purcell §6.4).
P2: u = x ln a, u' = ln a (ln a konstanta!). Kesalahan umum menurunkan ln a menjadi 1/a. Tanya: "a itu variabel atau bilangan tetap?"
P3: jawaban diharapkan dengan "membalik" turunan. Periksa dengan menurunkan hasilnya. Mengapa a ≠ 1? (ln 1 = 0, dan 1^x konstan.)
Pertanyaan pertama hari ini sekarang terjawab.
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Sekarang Kita Beri Nama</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.4</span>
</h2>

::left::

<BeamerBlock type="block" title="Definisi: aˣ dan logₐ x">

Untuk $a \gt 0$ dan semua $x$ real: $\;a^x = e^{x\ln a}$.

Untuk $a \gt 0$, $a \ne 1$: $\log_a x$ adalah invers dari $a^x$, yaitu

$$\log_a x = \frac{\ln x}{\ln a}$$

</BeamerBlock>

<BeamerBlock type="example" title="Rumus Turunan dan Integral">

- $(a^x)' = a^x\ln a$ dan $\int a^x\,dx = \dfrac{a^x}{\ln a} + C$
- $(\log_a x)' = \dfrac{1}{x\ln a}$

</BeamerBlock>

::right::

<SocraticBlock type="question" title="Mengapa logₐ x = ln x / ln a?" mode="Pikir 30 dtk">

Misalkan $y = \log_a x$, artinya $a^y = x$. Ambil $\ln$ kedua ruas. Apa yang didapat untuk $y$?

</SocraticBlock>

<SocraticBlock v-click type="answer">

$y\ln a = \ln x$, jadi $y = \dfrac{\ln x}{\ln a}$. Turunannya $\dfrac{1}{\ln a}\cdot\dfrac{1}{x}$, karena $\ln a$ hanya konstanta.

</SocraticBlock>

<SocraticBlock v-click type="reflect" title="Kembali ke Pertanyaan Kita">

Seberapa curam $2^x$ di $x = 0$? Mengapa justru $e$ yang dipakai sebagai alas "alami"?

</SocraticBlock>

<!--
Definisi ditampilkan SETELAH kelas menemukannya sendiri. Katakan: "Ini hanya nama dan rumus untuk yang tadi kalian temukan."
Pertanyaan: jawaban diharapkan lewat ln kedua ruas. Kesalahan umum: log_a x = ln(x/a) atau ln x − ln a. Tanya: "Periksa dengan a = 10, x = 100. log₁₀ 100 = 2. Rumusmu memberi berapa?"
Refleksi: kemiringan ln 2 ≈ 0,693. Alas e satu-satunya yang membuat kemiringan di 0 tepat 1, sehingga rumus turunannya paling sederhana.
-->

---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Turunan xˣ</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<SocraticBlock type="pitfall" title="Siapa yang Benar?" mode="Angkat jari: A / B / C">

Dodi dan Fani menurunkan $f(x) = x^x$ (untuk $x \gt 0$):

**A.** Dodi pakai aturan pangkat: $f'(x) = x\cdot x^{x-1} = x^x$  
**B.** Fani pakai aturan eksponen: $f'(x) = x^x\ln x$  
**C.** keduanya salah

</SocraticBlock>

<SocraticBlock v-click type="answer">

**C.** Di $x^x$, alas **dan** pangkatnya sama-sama berubah, jadi tidak ada aturan yang cocok langsung. Tulis $x^x = e^{x\ln x}$:

$$f'(x) = e^{x\ln x}\,(x\ln x)' = x^x\,(\ln x + 1)$$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Periksa dengan Angka" mode="Pikir 30 dtk">

Di $x = 2$: berapa nilai rumus Dodi, rumus Fani, dan rumus yang benar? Mengapa di $x = 1$ rumus Dodi kebetulan benar?

</SocraticBlock>

<!--
Nama tokoh pada slide kesalahan selalu fiktif agar tidak ada mahasiswa yang merasa dituding.
Miskonsepsi yang diuji: x^x diturunkan dengan aturan pangkat atau aturan eksponen saja.
Voting dulu; banyak yang memilih A atau B. Jangan langsung dikoreksi. Tanya: "Aturan pangkat untuk alas berubah dan pangkat tetap. Di x^x, pangkatnya tetap?"
Periksa: di x = 2, Dodi 4, Fani 4 ln 2 ≈ 2,77, yang benar 4(ln 2 + 1) ≈ 6,77. Di x = 1: benar = 1·(0 + 1) = 1 = rumus Dodi, kebetulan saja.
Cara ini (menulis sebagai e pangkat, atau ambil ln kedua ruas) disebut turunan logaritmik.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Luas di Bawah 2ˣ</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.4</span>
</h2>

<PolyaStepper step="1-2" support="full" />

::left::

<BeamerBlock type="example" title="Soal">

Hitung $\displaystyle\int_0^1 2^x\,dx$, dan jelaskan arti hasilnya.

</BeamerBlock>

<SocraticBlock type="question" title="1 · Pahami Soal" mode="Pikir 30 dtk">

Integral ini luas daerah apa? Tanpa menghitung, hasilnya pasti di antara dua bilangan berapa?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Luas di bawah $y = 2^x$ dari $0$ sampai $1$. Tinggi grafik naik dari $1$ ke $2$ dan lebarnya $1$, jadi luasnya antara $1$ dan $2$.

</SocraticBlock>

::right::

<div v-click="2" class="flex flex-col">

<SocraticBlock type="question" title="2 · Buat Rencana">

Rumus mana dari slide tadi yang dipakai? Ada cara lain bila rumusnya lupa?

</SocraticBlock>

</div>

<div v-click="3" class="flex flex-col">

<SocraticBlock type="answer" title="Rencana">

1. Antiturunan: $\int a^x\,dx = \dfrac{a^x}{\ln a} + C$ dengan $a = 2$ (atau tulis $2^x = e^{x\ln 2}$ lalu substitusi).
2. Teorema Dasar Kalkulus Kedua: hitung di $1$ dikurangi di $0$.

</SocraticBlock>

</div>

<!--
Contoh dikerjakan bersama: dosen mencontohkan keempat langkah, tetapi tiap langkah dibuka dengan pertanyaan.
Pahami: perkiraan "antara 1 dan 2" ini yang nanti dipakai di Periksa Lagi.
Rencana: kesalahan umum menulis antiturunan 2^{x+1}/(x+1) (aturan pangkat lagi). Tanya: "Turunkan 2^{x+1}/(x+1). Hasilnya 2^x?"
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Luas di Bawah 2ˣ (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.4</span>
</h2>

<PolyaStepper step="3-4" support="full" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan">

$$
\begin{aligned}
\int_0^1 2^x\,dx &= \left[\frac{2^x}{\ln 2}\right]_0^1 \\
&= \frac{2 - 1}{\ln 2} = \frac{1}{\ln 2} \approx 1{,}443
\end{aligned}
$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="question" title="4 · Periksa Lagi" mode="Pikir 1 mnt">

Apakah $1{,}443$ ada di antara $1$ dan $2$? Taksiran trapesium memberi $\tfrac{1 + 2}{2} = 1{,}5$. Mengapa hasil sebenarnya sedikit **lebih kecil**?

</SocraticBlock>

<SocraticBlock v-click type="answer">

$1 \lt 1{,}443 \lt 2$ ✓. Grafik $2^x$ cekung ke atas, jadi ruas lurus trapesium ada di atas grafik dan menaksir terlalu besar: $1{,}443 \lt 1{,}5$ ✓

</SocraticBlock>

<!--
Kerjakan: tulis di papan baris demi baris, slide hanya ringkasan.
Angka: ln 2 ≈ 0,6931, jadi 1/ln 2 ≈ 1,4427.
Periksa Lagi menghubungkan ke aturan trapesium (4.6) dan kecekungan (3.2): (2^x)'' = 2^x (ln 2)² > 0.
-->

---

<h2 class="slide-title">
  <span>Latihan di Rumah, lalu Lanjut ke 6.5</span>
  <span class="text-xs text-slate-400 font-mono">PKH · jembatan</span>
</h2>

<BeamerBlock type="example" title="Latihan di rumah (PKH 6.4)">

1. Turunkan $\log_{10}(x^2 + 1)$ dan $3^{x^2}$.
2. Tentukan persamaan garis singgung $y = x^x$ di $x = 2$.
3. Hitung $\displaystyle\int x\,3^{x^2}\,dx$, lalu periksa dengan menurunkan hasilnya.

</BeamerBlock>

<SocraticBlock type="question" title="Jembatan ke Bagian Kedua" mode="Pikir 30 dtk">

Banyaknya bakteri $y = 1000\cdot 2^t$. Dari rumus tadi, lajunya $y' = 1000\cdot 2^t\ln 2 = (\ln 2)\,y$. Apa artinya laju yang **sebanding dengan banyaknya**?

</SocraticBlock>

<!--
Jawaban PKH: (1) 2x/((x² + 1) ln 10) dan 3^{x²}·2x·ln 3. (2) f(2) = 4, f'(2) = 4(ln 2 + 1) ≈ 6,77, jadi y = 4 + 6,77(x − 2). (3) 3^{x²}/(2 ln 3) + C.
Bila waktu tersisa sebelum menit 47: kerjakan soal 1 bersama di papan.
Pertanyaan jembatan tidak dijawab di sini; ia langsung menjadi bagian kedua (deck 37: 6.5).
-->
