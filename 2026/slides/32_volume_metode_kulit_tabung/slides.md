---
theme: default
background: '#0c1018'
title: 'MA1101 Kalkulus I - Volume Benda Putar, Metode Kulit Tabung'
info: |
  ## MA1101 Kalkulus I
  FMIPA Institut Teknologi Bandung
  Subtopik 5.3: Volume Benda Putar, Metode Kulit Tabung
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
---

# MA1101 Kalkulus I
<p class="text-xl text-amber-400 font-semibold mt-2">Bab 5: Penggunaan Integral</p>
<p class="text-sm text-slate-300 mt-1">Subtopik 5.3: Volume Benda Putar, Metode Kulit Tabung</p>

<div class="mt-8 max-w-xl mx-auto text-left">
<SocraticBlock type="question" title="Pertanyaan Kita Hari Ini">

Cakram dan cincin mengiris benda **tegak lurus** sumbu putar. Bagaimana kalau cara itu sulit dipakai? Adakah cara lain mengiris benda yang sama?

</SocraticBlock>
</div>

<!--
Jangan dijawab sekarang. Bacakan, beri jeda 10 detik, lalu katakan: "Di akhir kuliah, kalian sendiri yang akan menjawabnya."
-->

---

<h2 class="slide-title">
  <span>Mulai dari Soal: Cakram Mulai Macet</span>
  <span class="text-xs text-slate-400 font-mono">Pakai yang sudah kita tahu</span>
</h2>

<BeamerBlock type="example" title="Soal">

Daerah di bawah kurva $y = 2x^2 - x^3$, di atas sumbu-$x$, untuk $0 \le x \le 2$, diputar mengelilingi **sumbu-$y$**. Hitung volume benda yang terbentuk.

</BeamerBlock>

<SocraticBlock type="question" mode="Diskusi berpasangan · 1 mnt">

Kalian ingin memakai metode cakram atau cincin. Apa yang harus kalian lakukan lebih dulu pada rumus kurvanya? Apakah mudah?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Yang biasanya muncul">

Iris datar (tegak lurus sumbu-$y$), jadi jari-jari harus ditulis sebagai fungsi $y$: kita perlu menyelesaikan $y = 2x^2 - x^3$ untuk $x$. Itu persamaan pangkat tiga, dan kurvanya naik lalu turun sehingga tiap $y$ punya **dua** nilai $x$.

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Bagaimana kalau kita iris **sejajar** sumbu putar, yaitu irisan tegak seperti $x$ tetap? Irisan setipis itu kalau diputar mengelilingi sumbu-$y$ menjadi apa?

</SocraticBlock>

<!--
Tanya: beri 1 menit berpasangan. Minta dua pasangan menyebut langkah pertama mereka.
Jawaban diharapkan: "tulis x sebagai fungsi y", lalu sadar sulit karena persamaan pangkat tiga.
Jika ada yang menjawab "pakai rumus abc": "Rumus abc untuk pangkat berapa? Persamaan kita pangkat berapa?"
Jika hening: "Coba tulis y = 2x² − x³ lalu pindahkan ke x = ... Bisa?"
Pertanyaan lanjutan: arahkan sampai ada yang menggambarkan tabung tipis atau pipa tipis. Jangan sebut kata kulit dulu.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Irisan Tegak Diputar</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Satu irisan tegak (merah) diputar mengelilingi sumbu-$y$. Bentuk yang terjadi paling mirip:

**A.** cakram datar  
**B.** pipa tipis berongga  
**C.** bola kecil

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Geser $x$. Apa yang ikut berubah pada bentuk di bawah?
2. Kalau pipa itu dipotong lurus lalu dibentangkan, jadi bangun apa?

</SocraticBlock>

::right::

<ShellBoard height="400px" />

<!--
Urutan: (1) minta semua mengangkat jari A/B/C SEBELUM menyentuh applet, hitung dengan lantang. (2) Geser x perlahan dari 0,3 ke 1,9. (3) Klik untuk pertanyaan pengamatan.
Jawaban diharapkan: B.
Jika banyak memilih A: "Cakram itu penuh. Apakah irisan kita kena bagian tengah, di dekat sumbu putar?"
Pengamatan 1: tinggi dan keliling berubah; tebal (Δx) tetap kalau tidak digeser.
Pengamatan 2: persegi panjang. Setelah ada yang menyebutnya, centang "tampilkan ukuran" untuk memeriksa panjang dan tinggi.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Ukuran Satu Kulit</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

Irisan berada di posisi $x$. Berapa jari-jari pipa yang terbentuk? Dan berapa tingginya?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

Jari-jari $= x$ (jarak irisan ke sumbu putar). Tinggi $= f(x) = 2x^2 - x^3$.

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2">

Pipa dipotong lurus lalu dibentangkan. Berapa **panjang** persegi panjangnya?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer">

Panjangnya sama dengan keliling lingkaran berjari-jari $x$:

$$2\pi x$$

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Kerjakan di kertas · 1 mnt">

Kulit setebal $\Delta x$ itu hampir seperti balok tipis. Tulis volumenya.

</SocraticBlock>

<SocraticBlock v-click="5" type="answer" title="Kesimpulan Kita">

$$\Delta V \approx \underbrace{2\pi x}_{\text{panjang}} \cdot \underbrace{f(x)}_{\text{tinggi}} \cdot \underbrace{\Delta x}_{\text{tebal}}$$

</SocraticBlock>

<!--
Tiap pertanyaan dibuka dengan klik, beri waktu sebelum klik berikutnya.
P1 jawaban diharapkan: jari-jari x, tinggi f(x). Jika ada yang menjawab "jari-jarinya f(x)": "Jari-jari itu jarak ke sumbu putar. Sumbunya yang mana?"
P2: bayangkan menggulung kertas. Keliling = 2π × jari-jari.
P3: beri 1 menit di kertas. Kesalahan umum: lupa mengalikan tebal Δx. Tanyakan: "Satuan jawabanmu apa? Volume harusnya satuan apa?"
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Dari Banyak Kulit ke Integral</span>
  <span class="text-xs text-slate-400 font-mono">Jumlahkan, lalu limit</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 4" mode="Diskusi berpasangan · 1 mnt">

Benda utuh tersusun dari kulit-kulit seperti ini, dari $x = 0$ sampai $x = 2$. Bagaimana kita mendapat volume totalnya? Apa yang terjadi bila kulitnya dibuat makin tipis?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Kesimpulan Kita">

Jumlahkan semua kulit, lalu biarkan $\Delta x \to 0$:

$$V = \lim_{n \to \infty} \sum_{i=1}^{n} 2\pi x_i f(x_i)\,\Delta x = \int_0^2 2\pi x\,(2x^2 - x^3)\,dx$$

</SocraticBlock>

::right::

<SocraticBlock v-click="2" type="question" title="Pertanyaan 5" mode="Kerjakan di kertas · 2 mnt">

Hitung integralnya.

</SocraticBlock>

<SocraticBlock v-click="3" type="answer">

$$
\begin{aligned}
V &= 2\pi \int_0^2 (2x^3 - x^4)\,dx \\
&= 2\pi \left[ \tfrac{x^4}{2} - \tfrac{x^5}{5} \right]_0^2 \\
&= 2\pi \left( 8 - \tfrac{32}{5} \right) = \tfrac{16\pi}{5}
\end{aligned}
$$

</SocraticBlock>

<!--
P4: biarkan kelas menyebut "jumlahkan". Jika ada yang menjawab "kalikan semuanya": "Kalau ada 3 kulit bervolume 2, 3, dan 5, volume totalnya berapa?"
Untuk membuktikan, kembali ke applet: centang "jumlahkan semua kulit", geser n dari 1 sampai 40, dan tunjukkan jumlahnya mendekati 16π/5 ≈ 10,053.
P5: jawaban 16π/5 ≈ 10,05. Beri 2 menit. Kesalahan umum: lupa mengalikan x pada f(x), jadi pangkatnya salah.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Sekarang Kita Beri Nama</span>
  <span class="text-xs text-slate-400 font-mono">Metode Kulit Tabung</span>
</h2>

::left::

<BeamerBlock type="block" title="Metode Kulit Tabung (sumbu putar: sumbu-y)">

Daerah di bawah $y = f(x)$, $a \le x \le b$ (dengan $a \ge 0$), diputar mengelilingi sumbu-$y$. Volumenya:

$$V = \int_a^b 2\pi \,\underbrace{x}_{\text{jari-jari}}\;\underbrace{f(x)}_{\text{tinggi}}\,dx$$

</BeamerBlock>

<SocraticBlock v-click type="question" mode="Tunjuk di papan">

Cocokkan tiap bagian rumus dengan yang kita temukan tadi: mana keliling, mana tinggi, mana tebal?

</SocraticBlock>

::right::

<div v-click class="flex flex-col">

<SocraticBlock type="answer" title="Cocokkan dengan Soal Tadi">

- $2\pi x$ = keliling = panjang persegi panjang
- $f(x)$ = tinggi kulit
- $dx$ = tebal kulit
- $a = 0,\ b = 2$ = daerah yang dicakup irisan

</SocraticBlock>

<SocraticBlock type="reflect" title="Kembali ke Pertanyaan Kita">

Cakram mengiris **tegak lurus** sumbu putar. Kulit tabung mengiris dengan cara apa? Kapan cara ini lebih mudah?

</SocraticBlock>

</div>

<!--
Rumus ditampilkan SETELAH kelas menemukannya sendiri. Katakan: "Ini hanya nama dan rumus untuk yang tadi kalian temukan."
Jawaban diharapkan untuk pertanyaan terakhir: kulit mengiris sejajar sumbu putar; lebih mudah saat irisan tegak (fungsi x) sudah ada tetapi rumus x(y) sulit, atau saat sumbu putar tegak.
Peringatan: jari-jari bukan selalu x. Itu masalah di slide berikutnya.
-->

---
class: slide-compact
---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Sumbu Putarnya Digeser</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<div class="grid gap-3" style="grid-template-columns: 1fr 300px">

<SocraticBlock type="pitfall" title="Benarkah Cara Dani?" mode="Diskusi berpasangan · 1 mnt">

Dani memutar daerah yang sama mengelilingi garis **$x = -1$** (di sebelah kiri daerah, bukan sumbu-$y$). Ia tetap menulis

$$V = \int_0^2 2\pi\, x\, f(x)\,dx$$

Apa yang salah? Jari-jari kulit yang benar berapa?

</SocraticBlock>

<ShellAxisFigure :reveal="$clicks >= 1" height="235px" />

</div>

<SocraticBlock v-click type="answer">

Jari-jari adalah **jarak irisan ke sumbu putar**. Irisan di posisi $x$ berjarak $x - (-1) = x + 1$ dari garis $x = -1$, jadi

$$V = \int_0^2 2\pi\,(x + 1)\,f(x)\,dx$$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan">

Hasil Dani dan hasil yang benar, mana yang lebih besar? Cek tanpa menghitung.

</SocraticBlock>

<!--
Nama tokoh pada slide kesalahan selalu fiktif agar tidak ada mahasiswa yang merasa dituding.
Gambar: panah koral = jarak yang dipakai Dani (dari sumbu-y), panah emas = jarak sebenarnya ke sumbu putar. Tanda tanya berubah menjadi x + 1 saat klik pertama.
Jawaban diharapkan: jari-jari tidak lagi x; yang benar x + 1. Jika hening: "Jarak dari x = 1 ke garis x = −1 berapa? Dari x = 1 ke sumbu-y?"
Kesalahan umum: menulis jari-jari 1 − x atau |x| − 1. Tanyakan: "Coba x = 0. Jarak titik itu ke garis x = −1 berapa?"
Pertanyaan lanjutan: jawaban benar lebih besar karena x + 1 lebih besar daripada x (jari-jarinya lebih besar, kulitnya lebih panjang).
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Daerah di Antara Dua Kurva</span>
  <span class="text-xs text-slate-400 font-mono">Stewart §6.3</span>
</h2>

<PolyaStepper step="1-2" support="full" />

::left::

<BeamerBlock type="example" title="Soal">

Daerah di antara $y = x$ dan $y = x^2$ diputar mengelilingi **sumbu-$y$**. Hitung volumenya.

</BeamerBlock>

<SocraticBlock type="question" title="1 · Pahami Soal">

Di mana kedua kurva berpotongan? Kurva mana yang di atas? Bagaimana irisan tegaknya?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Berpotongan di $x = 0$ dan $x = 1$. Pada selang itu $y = x$ di atas $y = x^2$. Irisan tegak setinggi $x - x^2$.

</SocraticBlock>

::right::

<div v-click="2" class="flex flex-col">

<SocraticBlock type="question" title="2 · Buat Rencana">

Dari kulit satu irisan, tulis jari-jari dan tinggi. Lalu apa yang kita lakukan?

</SocraticBlock>

</div>

<div v-click="3" class="flex flex-col">

<SocraticBlock type="answer" title="Rencana">

1. Jari-jari $= x$, tinggi $= x - x^2$.
2. Integralkan $2\pi \cdot x \cdot (x - x^2)$ dari $0$ sampai $1$.

</SocraticBlock>

</div>

<!--
Contoh dikerjakan bersama: dosen mencontohkan keempat langkah, tetapi tiap langkah dibuka dengan pertanyaan.
Pahami: titik potong dengan x = x² memberi x = 0 atau x = 1. Jika ada yang menjawab "x = 1 saja": "Coba masukkan x = 0."
Rencana: tinggi kulit adalah atas dikurangi bawah. Ini beda dengan contoh pertama, di sini ada dua kurva.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Daerah di Antara Dua Kurva (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Stewart §6.3</span>
</h2>

<PolyaStepper step="3-4" support="full" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan">

$$
\begin{aligned}
V &= \int_0^1 2\pi x\,(x - x^2)\,dx \\
&= 2\pi \left[ \tfrac{x^3}{3} - \tfrac{x^4}{4} \right]_0^1 \\
&= 2\pi \cdot \tfrac{1}{12} = \tfrac{\pi}{6}
\end{aligned}
$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="question" title="4 · Periksa Lagi" mode="Pikir 1 mnt">

Soal yang sama bisa dikerjakan dengan cincin. Bagaimana kita memakainya untuk memeriksa $\tfrac{\pi}{6}$?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Pemeriksaan dengan cincin">

Iris datar: jari-jari luar $\sqrt{y}$, jari-jari dalam $y$, untuk $0 \le y \le 1$:

$$V = \pi \int_0^1 (y - y^2)\,dy = \pi\left(\tfrac12 - \tfrac13\right) = \tfrac{\pi}{6}\ \checkmark$$

</SocraticBlock>

<!--
Kerjakan: tulis di papan baris demi baris, slide hanya ringkasan.
Periksa Lagi: tekankan bahwa langkah ini bukan hiasan. Dua metode berbeda yang memberi jawaban sama membuat kita yakin.
Jawaban diharapkan: pakai cincin dengan variabel y. Jika ada yang kesulitan menulis jari-jari: x = √y adalah kurva y = x² dan x = y adalah kurva y = x.
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

Daerah di bawah $y = x^2$, $0 \le x \le 1$, diputar mengelilingi garis **$x = 2$**. Hitung volumenya.

</BeamerBlock>

<SocraticBlock type="question" title="1–2 · Pahami Soal & Buat Rencana">

Rencananya sama seperti Contoh 1. Berapa jarak irisan di $x$ ke garis $x = 2$? Itulah jari-jari kulitnya.

</SocraticBlock>

::right::

<BeamerBlock type="example" title="3 · Kerjakan: lengkapi yang kosong">

$$
\begin{aligned}
V &= \int_0^1 2\pi\,\boxed{\phantom{000}}\cdot\boxed{\phantom{000}}\,dx \\
&= 2\pi \left[ \tfrac{2x^3}{3} - \tfrac{x^4}{4} \right]_0^1 = \boxed{\phantom{000}}
\end{aligned}
$$

</BeamerBlock>

<SocraticBlock v-click type="answer" title="Isian dan Pemeriksaan">

$2 - x$ &nbsp;·&nbsp; $x^2$ &nbsp;·&nbsp; $\tfrac{5\pi}{6}$.  
**Periksa:** kalau sumbunya $x = 0$, hasilnya $\tfrac{\pi}{2}$. Sumbu $x = 2$ lebih jauh, jadi volumenya harus lebih besar: $\tfrac{5\pi}{6} \gt \tfrac{\pi}{2}$ ✓

</SocraticBlock>

<!--
Dukungan dikurangi: kerangka masih ada, isinya dikerjakan mahasiswa. Beri 4 menit berpasangan, berkeliling.
Jawaban diharapkan untuk jari-jari: 2 − x. Kesalahan umum: memakai x. Tanyakan: "Jarak dari x = 1 ke garis x = 2 berapa?"
Klik untuk isian hanya setelah sebagian besar pasangan selesai.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 5 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal">

Daerah yang dibatasi $y = \sqrt{x}$, $y = 0$, dan $x = 4$ diputar mengelilingi **sumbu-$y$**. Hitung volumenya dengan metode kulit tabung.

</BeamerBlock>

<div class="grid grid-cols-3 gap-3">

<SocraticBlock v-click type="hint" level="1">

Tinggi dan jari-jari kulit di posisi $x$: masing-masing berapa?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="2">

Tulis $2\pi \cdot (\text{jari-jari}) \cdot (\text{tinggi})\,dx$. Batas $x$-nya dari mana sampai mana?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="3">

Hasilnya $2\pi \int_0^4 x^{3/2}\,dx$. Naikkan pangkatnya.

</SocraticBlock>

</div>

<SocraticBlock v-click type="answer" title="Jawaban Akhir & Periksa Lagi">

$V = \tfrac{128\pi}{5}$. Bagaimana kita memeriksanya dengan metode cincin (iris datar, $0 \le y \le 2$)?

</SocraticBlock>

<!--
Mandiri: tidak ada kerangka langkah. Petunjuk dibuka satu per satu HANYA bila kelas macet, beri jeda minimal 1 menit.
Petunjuk 1 mengarahkan ulang ke soal, petunjuk 2 menyebut strategi, petunjuk 3 memberi langkah pertama. Tidak ada yang memberi jawaban.
Yang ditampilkan hanya jawaban akhir. Penyelesaian lengkap dikerjakan di papan bila perlu.
Pemeriksaan: cincin dengan jari-jari luar 4 dan dalam y²: π ∫₀² (16 − y⁴) dy = π(32 − 32/5) = 128π/5.
-->

---

<h2 class="slide-title">
  <span>Tulis Sebelum Pulang</span>
  <span class="text-xs text-slate-400 font-mono">Tulis di kertas · 2 mnt</span>
</h2>

<SocraticBlock type="reflect" title="Rangkum dengan Kata-Katamu">

1. Jelaskan kepada teman SMA: dari mana datangnya $2\pi x \cdot f(x) \cdot dx$?
2. Kapan kalian memilih kulit tabung, dan kapan cakram atau cincin? Beri satu alasan.

</SocraticBlock>

<SocraticBlock type="question" title="Untuk Pertemuan Berikutnya">

Sejauh ini kita menjumlahkan **volume** potongan kecil. Kalau gaya yang mendorong sebuah benda berubah-ubah sepanjang jalan, apa yang kita jumlahkan untuk mendapat **usaha**?

</SocraticBlock>

<!--
Kumpulkan kertasnya. Pertanyaan 2 memberi data untuk membuka pertemuan berikutnya.
Pertanyaan terakhir tidak dijawab; ia menjadi pembuka subtopik 5.5 (Kerja).
-->
