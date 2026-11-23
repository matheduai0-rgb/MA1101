---
theme: default
background: '#0c1018'
title: 'MA1101 Kalkulus I - Fungsi Eksponen Natural'
info: 'Subtopik 6.3 · Pertemuan 27 (bagian 1 dari 2, lanjut ke deck 38)'
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
---

# MA1101 Kalkulus I
<p class="text-xl text-amber-400 font-semibold mt-2">Bab 6: Fungsi Transenden</p>
<p class="text-sm text-slate-300 mt-1">Subtopik 6.3: Fungsi Eksponen Natural · lalu 6.4: Eksponen dan Logaritma Umum</p>

<div class="mt-8 max-w-xl mx-auto text-left">
<SocraticBlock type="question" title="Pertanyaan Pertama Hari Ini">

Adakah fungsi (selain fungsi nol) yang turunannya **sama dengan dirinya sendiri**?

</SocraticBlock>
</div>

<!--
Jangan dijawab sekarang. Bacakan, beri jeda 10 detik, lalu katakan: "Di akhir bagian pertama, kalian sendiri yang akan menjawabnya."
Buka dengan 2 jawaban anonim tiket keluar pertemuan 26 ("ln x selalu naik, jadi punya invers. Fungsi apa itu? Berapa turunannya?"): satu yang menyebut eˣ, satu yang macet di Teorema B.
Jika ada yang menjawab "eˣ" dari SMA: "Bagus. Hari ini kita cari tahu apa sebenarnya e itu, dan mengapa turunannya sama dengan dirinya."
Pertemuan ini dua bagian: 6.3 (deck ini, sekitar 50 menit), lalu 6.4 (deck 38).
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
class: slide-compact
---

<h2 class="slide-title">
  <span>Temukan Bersama: Invers ln dan Turunannya</span>
  <span class="text-xs text-slate-400 font-mono">Pakai Teorema B dari 6.2</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

Invers $\ln$ kita beri nama $\exp$. Pakai $\ln a^r = r\ln a$ dan $\ln e = 1$: berapa $\ln(e^r)$ untuk $r$ rasional? Jadi $\exp r = \;?$

</SocraticBlock>

<LnAreaBoard mode="area" height="325px" />




  


::right::
<SocraticBlock v-click="1" type="answer">

$\ln(e^r) = r\ln e = r$, jadi $\exp r = e^r$. Misal $\exp 3 = e^3=e \times e \times e.$ Untuk **semua** $x$ real kita definisikan $e^x = \exp x$, termasuk $e^{\sqrt 2}$ dan $e^{\pi}$.

</SocraticBlock>
<SocraticBlock v-click="2" type="question" title="Pertanyaan 2" mode="Diskusi berpasangan · 1 mnt">

Tulis $y = f(x)=\ln x$ sehingga $x = f^{-1}(y)=\exp(y)=e^y$. Berapa $\dfrac{dy}{dx}$? Dengan Teorema $(f^{-1})'(y)=\frac{1}{f'(x)}$, berapa $\dfrac{dx}{dy}$?

</SocraticBlock>

<SocraticBlock v-click="3" type="answer" title="Kesimpulan Kita">

$$\frac{dy}{dx} = \frac{1}{x} \quad\Rightarrow\quad \frac{dx}{dy} =  (f^{-1})'(y)=\frac{1}{f'(x)} = \frac{1}{dy/dx} = x = e^y$$

</SocraticBlock>
<!--
<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Pikir 30 dtk">

Jadi fungsi apa yang turunannya sama dengan dirinya sendiri? Apakah $5e^x$ juga? Bagaimana dengan $e^{2x}$?

</SocraticBlock>

<SocraticBlock v-click="5" type="answer">

$e^x$, dan semua $Ce^x$. Tetapi $\bigl(e^{2x}\bigr)' = 2e^{2x}$ (aturan rantai), jadi tidak. Pertanyaan besar hari ini terjawab.

</SocraticBlock>


Tiap pertanyaan dibuka dengan klik, beri waktu sebelum klik berikutnya.
P1: kesalahan umum ln(e²) = e. Tanya: "ln a^r = r ln a. Di sini a = e, r = 2."
P2: Teorema B dari pertemuan lalu (6.2); biarkan pasangan mengerjakannya sendiri. Kesalahan umum: dy/dx = 1/x. Tanya: "Variabel bebas di x = ln y itu y. Jadi 1/y, lalu y diganti apa?"
P3: e^{2x} menjembatani ke 6.5 (y' = ky). Grafik eˣ (cerminan ln terhadap y = x, asimtot y = 0) cukup digambar cepat di papan; applet ExpBoard ada di draf lengkap (slides.v1-full.md) bila waktu longgar.
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

$e$ adalah bilangan dengan $\ln e = 1$, yaitu $e \approx 2{,}71828$. Fungsi $\exp = \ln^{-1}$, ditulis $e^x = \exp x$ untuk semua $x$ real:

$$e^{\ln x} = x \ (x \gt 0), \qquad \ln(e^y) = y \ (\text{semua } y)$$

</BeamerBlock>

::right::

<BeamerBlock type="example" title="Sifat dan Kalkulus">

- $e^a e^b = e^{a + b}$ dan $e^a / e^b = e^{a - b}$
- $\frac{d}{d x}(e^x) = e^x$ dan $\frac{d}{d x}(e^{u(x)}) = e^{u(x)}\,\frac{d u}{d x}$
- $\displaystyle\int e^x\,dx = e^x + C$

</BeamerBlock>

<SocraticBlock v-click type="reflect" title="Cocokkan dengan yang Kita Temukan" mode="Pikir 30 dtk">

Baris mana di kotak ini yang tadi kita temukan dengan applet luas? Baris mana dengan Teorema B?

</SocraticBlock>

<!--
Definisi ditampilkan SETELAH kelas menemukannya sendiri. Katakan: "Ini hanya nama dan rumus untuk yang tadi kalian temukan."
Jawaban: ln e = 1 dari applet luas; (eˣ)' = eˣ dari Teorema B. Sifat e^a e^b = e^{a+b} dibuktikan dengan mengambil ln kedua ruas; jadikan PKH (lihat slide PKH).
-->

---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Turunan e Pangkat Sesuatu</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<SocraticBlock type="pitfall" title="Benarkah Cara Rina?" mode="Angkat jari: benar / salah">

Rina menulis

$$\frac{d}{dx}e^{x^2} = x^2\,e^{x^2 - 1}$$

karena "turunkan pangkatnya ke depan, lalu pangkatnya dikurangi satu". Apa yang keliru?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Aturan pangkat $\dfrac{d}{dx}x^n = nx^{n - 1}$ hanya untuk **alas** yang berubah dan pangkat tetap. Di $e^{x^2}$, alasnya tetap ($e$) dan **pangkatnya** yang berubah. Pakai $\dfrac{d}{dx}e^{u} = e^{u}u'$:

$$\frac{d}{dx}e^{x^2} = e^{x^2}\cdot 2x$$

</SocraticBlock>

<!--
Nama tokoh pada slide kesalahan selalu fiktif agar tidak ada mahasiswa yang merasa dituding.
Jawaban diharapkan: salah aturan. Jika hening: "Periksa di x = 1 dengan applet kemiringan. Kemiringan e^{x²} di x = 1 kira-kira berapa? Rumus Rina memberi berapa?" (2e ≈ 5,4 lawan 1).
Bila waktu longgar, tanya lisan: "Dani menulis (x^e)' = x^e. Benarkah?" x^e adalah pangkat dengan pangkat tetap e, jadi turunannya e·x^{e−1}. Kebalikan dari kesalahan Rina.
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

Ditanya nilai terbesar $f$. $f(0) = 0$, dan untuk $x$ besar $f'(x) = (1-x)e^{-x} \lt 0$ maka $f$ turun setelah nilai tertentu. Maksimumnya ada di tengah.

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

Benarkah $x = 1$ memberi maksimum, bukan minimum? Periksa tanda $f'$.

</SocraticBlock>

<SocraticBlock v-click type="answer">

$e^{-x}\gt 0$ sehingga tanda dari $f'(x)$ ditentukan oleh $(1-x)$ saja. Untuk $0\leq x \lt 1$, $f'(x)\gt 0$, dan untuk $1 \lt x$, $f'(x)\lt 0$. Jadi $x=1$ menghasilkan maksimum global.

</SocraticBlock>

<!--
Kerjakan: tulis di papan baris demi baris, slide hanya ringkasan.
Tekankan mengapa e^{-x} boleh "dibuang" saat mencari f' = 0: eˣ tidak pernah nol (lihat daerah hasil).
Periksa Lagi: langkah ini bukan hiasan. Jika ada waktu, hitung f(0,9) ≈ 0,366 dan f(1,1) ≈ 0,366, keduanya sedikit di bawah 0,368.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Integral Tentu dengan eˣ</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 6 mnt</span>
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
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 6 mnt</span>
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
  <span>Latihan di Rumah, lalu Lanjut ke Bagian Kedua</span>
  <span class="text-xs text-slate-400 font-mono">PKH 6.3 · jembatan ke 6.4</span>
</h2>

<BeamerBlock type="example" title="Latihan di rumah (PKH 6.3)">

1. Hitung $\displaystyle\int x\,e^{-x^2}\,dx$. Pilih $u$ yang turunannya (hampir) muncul di depan, lalu periksa dengan menurunkan hasilnya.
2. Tunjukkan $e^a e^b = e^{a + b}$ dan $e^a / e^b = e^{a - b}$ dengan mengambil $\ln$ kedua ruas.
3. Turunkan $e^{x^2}$, $x^e$, dan $e^{\sin x}$. Tandai mana yang memakai aturan pangkat dan mana yang memakai $(e^{u})' = e^{u}u'$.

</BeamerBlock>

<SocraticBlock type="question" title="Sekarang, Bagian Kedua" mode="Pikir 30 dtk">

Kita sudah punya $e^x$ untuk semua $x$ real. Bagaimana mendefinisikan $2^x$, misalnya $2^{\sqrt 2}$? Petunjuk: $2 = e^{\ln 2}$.

</SocraticBlock>

<!--
Tunjukkan PKH 30 detik saja; tidak dibahas di kelas. Soal 1: −½e^{−x²} + C. Soal 3 mengulang slide Rina (x^e memakai aturan pangkat).
Bacakan pertanyaan jembatan, beri 30 detik, lalu langsung buka deck 38 (6.4). Jangan dijawab di sini: slide pertama deck 38 mulai dari pertanyaan ini.
Jika telat (lewat menit 50), lewati slide ini dan langsung buka deck 38.
-->
