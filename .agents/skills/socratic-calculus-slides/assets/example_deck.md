---
theme: default
background: '#0c1018'
title: MA1101 Kalkulus I - Dari Tali Busur ke Garis Singgung
info: |
  ## MA1101 Kalkulus I
  FMIPA Institut Teknologi Bandung
  Subtopik 2.1: Turunan sebagai Limit Kemiringan Tali Busur
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
---

# MA1101 Kalkulus I
<p class="text-xl text-amber-400 font-semibold mt-2">Bab 2: Turunan</p>
<p class="text-sm text-slate-300 mt-1">Subtopik 2.1: Dari Tali Busur ke Garis Singgung</p>

<div class="mt-8 max-w-xl mx-auto text-left">
<SocraticBlock type="question" title="Pertanyaan Kita Hari Ini">

Speedometer menunjukkan kecepatan **pada satu saat**. Tetapi kecepatan adalah jarak dibagi waktu, dan pada satu saat tidak ada waktu yang berlalu. Jadi, apa sebenarnya yang ditunjukkan speedometer?

</SocraticBlock>
</div>

<!--
Jangan dijawab sekarang. Bacakan pertanyaannya, beri jeda 10 detik, lalu katakan: "Di akhir kuliah, kalian sendiri yang akan menjawabnya."
-->

---

<h2 class="slide-title">
  <span>Mulai dari Soal: Kecepatan pada Satu Saat</span>
  <span class="text-xs text-slate-400 font-mono">Pakai yang sudah kita tahu</span>
</h2>

<SocraticBlock type="question" mode="Diskusi berpasangan · 1 mnt">

Sebuah bola dijatuhkan. Setelah $t$ detik ia telah menempuh $s(t) = 5t^2$ meter. Dengan alat yang sudah kalian punya, kecepatan apa saja yang **bisa** kalian hitung di sekitar $t = 1$?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Yang biasanya muncul dari kelas">

Kecepatan **rata-rata** pada suatu selang, misalnya dari $t = 1$ sampai $t = 2$:

$$\frac{s(2) - s(1)}{2 - 1} = \frac{20 - 5}{1} = 15 \text{ m/dtk}$$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Apakah $15$ m/dtk sudah menjawab "kecepatan **tepat di** $t = 1$"? Selang mana yang akan memberi jawaban lebih baik, dan mengapa?

</SocraticBlock>

<!--
Tanya: beri 1 menit berpasangan, lalu minta 2 pasangan menyebutkan apa yang mereka hitung.
Jawaban diharapkan: kecepatan rata-rata pada selang [1, 2] atau selang lain yang memuat t = 1.
Jika ada yang menjawab "v = s/t = 5 m/dtk": tanyakan "Itu kecepatan rata-rata pada selang yang mana?" (selang [0, 1], bukan di t = 1).
Jika hening: "Kalau saya minta kecepatan rata-rata dari detik ke-1 sampai ke-2, bisa?"
Pertanyaan lanjutan: arahkan sampai seseorang berkata "selangnya diperkecil". Jangan sebut kata limit dulu.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Apa yang Terjadi Bila Selang Mengecil?</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Titik $Q$ digeser mendekati $P$. Kemiringan tali busur $PQ$ akan:

**A.** terus mengecil menuju $0$  
**B.** mendekati satu nilai tertentu  
**C.** tidak menentu

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati">

1. Besaran apa yang **berubah** ketika $Q$ digeser? Apa yang **tetap**?
2. Tali busur $PQ$ makin mirip dengan garis apa?

</SocraticBlock>

::right::

<JSXGraphBoard
  height="330px"
  :boundingbox="[-0.4, 24, 3.2, -3]"
  :init="(board, JXG) => {
    const s = (t) => 5 * t * t;
    const curve = board.create('functiongraph', [s, 0, 3.2], { strokeColor: '#50a5fa', strokeWidth: 3 });
    const P = board.create('point', [1, 5], { name: 'P', fixed: true, color: '#f5be3c', size: 3 });
    const Q = board.create('glider', [2, 20, curve], { name: 'Q', color: '#fb7185', size: 4 });
    board.create('line', [P, Q], { strokeColor: '#fb7185', strokeWidth: 2 });
    board.create('text', [0.1, 22, () => 'kemiringan PQ = ' + ((Q.Y() - 5) / (Q.X() - 1 || 1e-9)).toFixed(3)], { fontSize: 15 });
    const show = board.create('checkbox', [0.1, 19.5, 'tampilkan garis singgung di P'], { fontSize: 13 });
    board.create('line', [[1, 5], [2, 15]], { strokeColor: '#34d399', strokeWidth: 2, dash: 2, visible: () => show.Value() });
  }"
/>

<!--
Urutan: (1) minta semua angkat jari A/B/C SEBELUM menyentuh applet, hitung suara dengan lantang. (2) Geser Q perlahan dari t = 2 ke t = 1,1. (3) Klik untuk memunculkan pertanyaan pengamatan.
Jawaban diharapkan: B. Kemiringan mendekati 10.
Jika banyak memilih A: "Selangnya memang mengecil menuju 0. Apakah jaraknya juga? Lalu bagaimana hasil baginya?"
Pertanyaan 1: yang berubah adalah Q, lebar selang, kemiringan; yang tetap adalah P dan kurvanya.
Pertanyaan 2: garis singgung di P. Baru setelah ada yang menyebutkannya, centang kotak "tampilkan garis singgung".
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Menuju Sebuah Rumus</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1">

Bila selangnya $[1,\, 1+h]$, tuliskan kecepatan rata-rata bola sebagai rumus dalam $h$.

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$$\frac{s(1+h) - s(1)}{h} = \frac{5(1+h)^2 - 5}{h}$$

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2" mode="Kerjakan di kertas · 1 mnt">

Sederhanakan untuk $h \neq 0$. Apa yang tersisa?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer">

$$\frac{5 + 10h + 5h^2 - 5}{h} = \frac{h(10 + 5h)}{h} = 10 + 5h$$

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3">

Applet tadi menunjukkan nilai mendekati $10$. Bagian mana dari $10 + 5h$ yang menjelaskan hal itu?

</SocraticBlock>

<SocraticBlock v-click="5" type="answer" title="Kesimpulan Kita">

Saat $h \to 0$, suku $5h$ lenyap dan tersisa $10$. Inilah kecepatan bola **tepat di** $t = 1$: $10$ m/dtk.

</SocraticBlock>

<!--
Setiap pertanyaan dibuka dengan klik; beri waktu sebelum klik berikutnya.
P1 jawaban diharapkan: [s(1+h) - s(1)] / h. Jika ada yang menulis s(h)/h: "Selang kita mulai dari t berapa?"
P2: beri 1 menit di kertas. Kesalahan umum: (1+h)^2 = 1 + h^2. Tanyakan "Coba periksa dengan h = 1: apakah 2^2 = 2?"
P3: minta mahasiswa yang menjawab, bukan dosen. Kata "limit" boleh muncul dari mahasiswa di sini.
Jika ada yang bertanya "kenapa tidak langsung h = 0?": simpan, itu slide "Benarkah?" dua slide lagi.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Sekarang Kita Beri Nama</span>
  <span class="text-xs text-slate-400 font-mono">Definisi 2.1</span>
</h2>

::left::

<BeamerBlock type="block" title="Definisi: Turunan di Suatu Titik">

Turunan fungsi $f$ di $x = c$ adalah

$$f'(c) = \lim_{h \to 0} \frac{f(c+h) - f(c)}{h}$$

asalkan limit ini ada.

</BeamerBlock>

<SocraticBlock v-click type="question" mode="Tunjuk di papan">

Cocokkan tiap bagian definisi dengan yang kita kerjakan tadi: mana $f$, mana $c$, mana hasil bagi, dan mana "$h \to 0$"?

</SocraticBlock>

::right::

<div v-click class="flex flex-col">

<SocraticBlock type="answer" title="Cocokkan dengan Soal Bola Tadi">

- $f = s$ dan $c = 1$
- hasil bagi $=$ kemiringan tali busur $=$ kecepatan rata-rata
- $h \to 0$ $=$ menggeser $Q$ ke $P$
- $f'(c) = s'(1) = 10$ $=$ kemiringan garis singgung $=$ kecepatan sesaat

</SocraticBlock>

<SocraticBlock type="reflect" title="Kembali ke Pertanyaan Besar">

Jadi, apa yang ditunjukkan speedometer?

</SocraticBlock>

</div>

<!--
Definisi baru ditampilkan SETELAH kelas merumuskannya sendiri di slide sebelumnya. Katakan: "Ini hanya nama dan notasi untuk apa yang kalian temukan."
Pertanyaan pencocokan: minta satu mahasiswa per bagian.
Pertanyaan besar: jawaban diharapkan "limit kecepatan rata-rata saat selang waktunya menuju nol".
-->

---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Mengapa Tidak Langsung h = 0?</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<SocraticBlock type="pitfall" title="Benarkah Cara Dani?" mode="Diskusi berpasangan · 1 mnt">

Dani berkata: "Limit itu merepotkan. Masukkan saja $h = 0$ ke $\dfrac{5(1+h)^2 - 5}{h}$ sejak awal." Apa yang terjadi bila saran Dani diikuti? Di langkah mana tepatnya masalah muncul?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Kalau langsung memasukkan $h = 0$, hasilnya $\dfrac{0}{0}$, yang tidak bermakna. Penyederhanaan menjadi $10 + 5h$ hanya sah untuk $h \neq 0$; limit bertanya nilai yang **didekati**, bukan nilai **di** $h = 0$.

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan">

Kalau begitu, mengapa pada akhirnya kita "boleh" mengganti $h$ dengan $0$ di $10 + 5h$?

</SocraticBlock>

<!--
Nama tokoh pada slide miskonsepsi selalu fiktif, agar kesalahan tidak melekat pada mahasiswa di kelas.
Jawaban diharapkan: muncul 0/0.
Pertanyaan lanjutan, jawaban diharapkan: karena 10 + 5h kontinu di h = 0, limitnya sama dengan nilainya. Cukup secara intuitif: "nilainya memang mendekati 10".
Jika hening: "Hitung 10 + 5h untuk h = 0,1; 0,01; 0,001."
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Garis Singgung Parabola</span>
  <span class="text-xs text-slate-400 font-mono">Stewart §2.7</span>
</h2>

<PolyaStepper step="1-2" support="full" />

::left::

<BeamerBlock type="example" title="Soal">

Tentukan persamaan garis singgung kurva $y = x^2 - 3x$ di titik $(2, -2)$.

</BeamerBlock>

<SocraticBlock type="question" title="1 · Pahami Soal">

Apa yang diminta? Informasi apa yang diperlukan untuk menulis persamaan sebuah garis?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Diminta: persamaan garis. Perlu **satu titik** (sudah ada: $(2,-2)$) dan **kemiringan** (belum ada).

</SocraticBlock>

::right::

<div v-click class="flex flex-col">

<SocraticBlock type="question" title="2 · Buat Rencana">

Alat apa yang baru kita punya untuk mencari kemiringan garis singgung?

</SocraticBlock>

</div>

<div v-click class="flex flex-col">

<SocraticBlock type="answer" title="Rencana">

1. Hitung $m = f'(2)$ dengan definisi limit.
2. Susun garis: $y - (-2) = m(x - 2)$.

</SocraticBlock>

</div>

<!--
Contoh terpandu: dosen memodelkan keempat fase, tetapi tiap fase tetap dibuka dengan pertanyaan.
Pahami, jawaban diharapkan: titik dan kemiringan. Jika ada yang menjawab "dua titik": "Bagus, itu juga cukup. Di soal ini, berapa titik yang kita punya?"
Rencanakan, jawaban diharapkan: turunan di x = 2.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Garis Singgung Parabola (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Stewart §2.7</span>
</h2>

<PolyaStepper step="3-4" support="full" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan">

$$
\begin{aligned}
f'(2) &= \lim_{h \to 0} \frac{(2+h)^2 - 3(2+h) - (-2)}{h} \\
&= \lim_{h \to 0} \frac{h^2 + h}{h} = \lim_{h \to 0}\,(h + 1) = 1
\end{aligned}
$$

Garis singgung: $y + 2 = 1\,(x - 2)$, yaitu $\mathbf{y = x - 4}$.

</BeamerBlock>

::right::

<SocraticBlock v-click type="question" title="4 · Periksa Lagi" mode="Pikir 30 dtk">

Tanpa menghitung ulang, bagaimana cara meyakinkan diri bahwa $y = x - 4$ masuk akal?

</SocraticBlock>

<SocraticBlock v-click type="answer">

- Titik $(2,-2)$ memenuhi: $2 - 4 = -2$ ✓
- Parabola berpuncak di $x = 1{,}5$, jadi di $x = 2$ kurva sedang **naik landai**: kemiringan positif kecil ✓

</SocraticBlock>

<!--
Laksanakan: tulis di papan baris demi baris; slide hanya ringkasannya.
Periksa Kembali: tekankan bahwa fase ini bukan hiasan. Jawaban diharapkan: substitusi titik, dan/atau cek tanda kemiringan dari sketsa.
Jika hening: "Kalau saya dapat m = -5, apa yang janggal?"
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 2: Giliran Kalian Mengisi</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 4 mnt</span>
</h2>

<PolyaStepper step="1-4" support="partial" />

::left::

<BeamerBlock type="example" title="Soal">

Tentukan persamaan garis singgung kurva $y = \dfrac{1}{x}$ di titik $\left(2, \tfrac12\right)$.

</BeamerBlock>

<SocraticBlock type="question" title="1–2 · Pahami Soal & Buat Rencana">

Rencananya sama dengan Contoh 1. Apa dua hal yang harus kalian peroleh?

</SocraticBlock>

::right::

<BeamerBlock type="example" title="3 · Kerjakan: lengkapi yang kosong">

$$
\begin{aligned}
f'(2) &= \lim_{h \to 0} \frac{\frac{1}{2+h} - \boxed{\phantom{00}}}{h}
= \lim_{h \to 0} \frac{\boxed{\phantom{00}}}{2h(2+h)} \\
&= \lim_{h \to 0} \frac{-1}{2(2+h)} = \boxed{\phantom{00}}
\end{aligned}
$$

Garis singgung: $y - \tfrac12 = \boxed{\phantom{00}}\,(x - 2)$

</BeamerBlock>

<SocraticBlock v-click type="answer" title="Isian">

$\tfrac12$ &nbsp;·&nbsp; $-h$ &nbsp;·&nbsp; $-\tfrac14$ &nbsp;·&nbsp; $-\tfrac14$. **Periksa:** kurva $\tfrac1x$ turun, jadi kemiringan negatif ✓

</SocraticBlock>

<!--
Dukungan dikurangi: kerangka langkah masih ada, isinya dikerjakan mahasiswa. Beri 4 menit berpasangan, berkeliling.
Pahami & Rencanakan, jawaban diharapkan: kemiringan f'(2) dan persamaan garis melalui (2, 1/2).
Kesalahan umum: lupa menyamakan penyebut; tanda minus hilang. Tanyakan: "Kurva 1/x naik atau turun di x = 2? Cocokkah dengan tanda jawabanmu?"
Klik untuk isian hanya setelah sebagian besar pasangan selesai.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 5 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal">

Sebuah partikel bergerak dengan posisi $s(t) = \sqrt{t}$ meter. Tentukan kecepatan sesaatnya di $t = 4$ detik.

</BeamerBlock>

<div class="grid grid-cols-3 gap-3">

<SocraticBlock v-click type="hint" level="1">

Besaran apa yang diminta, dan definisi mana yang menghitungnya?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="2">

Hasil bagi memuat $\sqrt{4+h} - 2$. Teknik aljabar apa yang menghilangkan akar di pembilang?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="3">

Kalikan dengan $\dfrac{\sqrt{4+h} + 2}{\sqrt{4+h} + 2}$, lalu sederhanakan.

</SocraticBlock>

</div>

<SocraticBlock v-click type="answer" title="Jawaban Akhir & Periksa Kembali">

$s'(4) = \tfrac14$ m/dtk. Masuk akalkah bahwa nilainya positif tetapi kecil? Lihat bentuk grafik $\sqrt{t}$.

</SocraticBlock>

<!--
Mandiri: tidak ada kerangka langkah. Petunjuk dibuka satu per satu HANYA bila kelas macet, dengan jeda minimal 1 menit di antaranya.
Petunjuk 1 mengarahkan ulang ke soal, Petunjuk 2 menyebut strategi, Petunjuk 3 memberi langkah pertama. Tidak ada petunjuk yang memberi jawaban.
Yang ditampilkan hanya jawaban akhir, bukan penyelesaian lengkap; penyelesaian lengkap dibahas di papan bila perlu.
-->

---

<h2 class="slide-title">
  <span>Tulis Sebelum Pulang</span>
  <span class="text-xs text-slate-400 font-mono">Tulis di kertas · 2 mnt</span>
</h2>

<SocraticBlock type="reflect" title="Rangkum dengan Kata-Katamu">

1. Jelaskan kepada teman SMA: apa hubungan antara **tali busur**, **garis singgung**, dan **turunan**?
2. Di langkah mana pada perhitungan hari ini kalian paling mungkin keliru? Mengapa?

</SocraticBlock>

<SocraticBlock type="question" title="Untuk Pertemuan Berikutnya">

Hari ini kita menghitung $f'(c)$ di **satu** titik. Apa yang berubah bila $c$ dibiarkan bebas, sehingga kita mendapat satu rumus untuk **semua** titik sekaligus?

</SocraticBlock>

<!--
Kumpulkan kertasnya. Pertanyaan 2 memberi data miskonsepsi untuk pembuka pertemuan berikutnya.
Pertanyaan terakhir tidak dijawab; ia menjadi pemantik kuliah "turunan sebagai fungsi".
-->
