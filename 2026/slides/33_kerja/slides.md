---
theme: default
background: '#0c1018'
title: 'MA1101 Kalkulus I - Kerja (Usaha) oleh Gaya yang Berubah'
info: |
  ## MA1101 Kalkulus I
  FMIPA Institut Teknologi Bandung
  Subtopik 5.5: Kerja (bagian tekanan fluida tidak ikut)
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
---

# MA1101 Kalkulus I
<p class="text-xl text-amber-400 font-semibold mt-2">Bab 5: Penggunaan Integral</p>
<p class="text-sm text-slate-300 mt-1">Subtopik 5.5: Kerja (Usaha) oleh Gaya yang Berubah</p>

<div class="mt-8 max-w-xl mx-auto text-left">
<SocraticBlock type="question" title="Pertanyaan Kita Hari Ini">

Rumus usaha $W = F \cdot d$ hanya benar kalau gayanya **tetap** dan perpindahannya seragam. Bagaimana menghitung usaha kalau gaya berubah-ubah sepanjang perpindahan? Atau bagaimana jika perpindahannya tidak seragam?

</SocraticBlock>
</div>

<!--
Jangan dijawab sekarang. Bacakan, beri jeda 10 detik, lalu katakan: "Di akhir kuliah, kalian sendiri yang akan menjawabnya."
Hubungkan dengan akhir pertemuan lalu: "Kemarin kita menjumlahkan volume potongan kecil. Hari ini apa yang dijumlahkan?"
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Mulai dari Soal: Gaya yang Makin Besar</span>
  <span class="text-xs text-slate-400 font-mono">Pakai yang sudah kita tahu</span>
</h2>

::left::

<BeamerBlock type="block" title="Yang sudah kita tahu">

Gaya **tetap** $F$ menggeser benda sejauh $d$: $W = F \cdot d$. Contoh: $10$ N sejauh $3$ m memberi $30$ J.

</BeamerBlock>

<SocraticBlock type="question" mode="Diskusi berpasangan · 1 mnt">

Sebuah pegas ditarik dari panjang alaminya sejauh $0{,}3$ m. Makin panjang tarikannya, makin besar gaya yang diperlukan: $F(x) = 100x$ newton, dengan $x$ meter pertambahan panjang. Mau dipakai $W = F \cdot d$. Gaya **yang mana** kalian masukkan?

</SocraticBlock>

::right::

<WorkFigure kind="spring" height="195px" />

<SocraticBlock v-click="1" type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Bagaimana kalau kita potong tarikan itu menjadi bagian-bagian kecil? Di tiap bagian, gayanya hampir tetap. Apa yang bisa kita lakukan?

</SocraticBlock>

<!--
Tanya: beri 1 menit berpasangan, lalu minta dua pasangan menyebut gaya yang mereka pilih.
Jawaban diharapkan: gaya awal, gaya akhir, atau rata-rata. Semua jawaban dicatat di papan, jangan dinilai dulu.
Jika ada yang menjawab "pakai rata-rata = 15 N, jadi 4,5 J": "Bagus, itu memang benar untuk pegas. Tetapi mengapa boleh rata-rata? Berlaku untuk gaya apa saja?"
Jika hening: "Kalau gayanya selalu 30 N, usahanya berapa? Kalau selalu 0 N?"
Pertanyaan lanjutan: arahkan sampai ada yang mengusulkan memotong jadi bagian kecil dan menjumlahkan. Jangan sebut kata integral dulu.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Memotong Tarikan Pegas</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Tarikan $0 \le x \le 0{,}3$ dipotong menjadi $n$ bagian. Di tiap bagian gaya dianggap tetap (sebesar gaya di ujung kiri), lalu usaha semua bagian dijumlahkan. Kalau $n$ makin besar, jumlahnya:

**A.** terus naik tanpa batas  
**B.** mendekati satu nilai tertentu  
**C.** tetap $0$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Persegi panjang kecil itu menyatakan usaha pada **satu** bagian. Mengapa luasnya sama dengan usaha?
2. Jumlah semua persegi panjang makin mirip bangun apa?

</SocraticBlock>

::right::

<WorkForceBoard height="340px" />

<!--
Urutan: (1) minta semua mengangkat jari A/B/C SEBELUM menyentuh applet, hitung dengan lantang. (2) Geser n dari 3 ke 30 perlahan. (3) Klik untuk pertanyaan pengamatan.
Jawaban diharapkan: B. Jumlahnya naik lalu mendekati sekitar 4,5.
Jika banyak memilih A: "Tiap persegi panjang makin kecil. Apakah jumlah yang tadinya terbatas bisa jadi tidak terbatas?"
Pengamatan 1: tinggi = gaya di bagian itu, lebar = panjang bagian itu; gaya × jarak adalah usaha.
Pengamatan 2: segitiga di bawah grafik gaya. Setelah ada yang menyebutnya, centang "tampilkan usaha sebenarnya".
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Lihat Gambarnya: Satu Potongan Tipis</span>
  <span class="text-xs text-slate-400 font-mono">Δx kecil, gaya hampir tetap</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan A" mode="Pikir 30 dtk">

Lihat potongan merah setebal $\Delta x$ di posisi $x$. Di potongan sekecil itu, gaya yang bekerja kira-kira berapa?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

Hampir tetap, sebesar $F(x) = 100x$. Itu tinggi grafik gaya di posisi $x$.

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan B" mode="Diskusi berpasangan · 1 mnt">

Pada grafik, persegi panjang tipis di bawahnya tingginya $F(x)$ dan lebarnya $\Delta x$. Apa arti luasnya?

</SocraticBlock>

<SocraticBlock v-click="3" type="answer" title="Kesimpulan Kita">

Luasnya gaya kali jarak, yaitu usaha pada potongan tadi:

$$\Delta W \approx F(x)\,\Delta x$$

</SocraticBlock>

::right::

<WorkFigure kind="spring-force" />

<!--
Gambar ini menghubungkan pegas (atas) dengan grafik gaya (bawah). Garis putus-putus merah menunjukkan potongan yang sama di kedua gambar.
Pertanyaan A, jawaban diharapkan: hampir tetap, nilainya F(x). Jika ada yang menjawab "nol karena potongannya kecil": "Gaya di x = 0,18 m berapa? Yang kecil itu apanya, gaya atau panjang potongan?"
Pertanyaan B, jawaban diharapkan: gaya kali jarak, yaitu usaha. Jika hening: "Satuan tinggi persegi panjang newton, satuan lebarnya meter. Luasnya satuan apa?"
Tekankan: Δx kecil membuat gaya di dalam potongan hampir tetap. Karena itu rumus gaya × jarak boleh dipakai di potongan itu.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Dari Potongan ke Integral</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

Pada potongan kecil dari $x$ sampai $x + \Delta x$, gayanya hampir tetap sebesar $F(x)$. Berapa usaha pada potongan itu?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$$\Delta W \approx F(x)\,\Delta x$$

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2">

Gaya bekerja dari posisi $a$ sampai $b$. Bagaimana kita mendapat usaha totalnya?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer">

Jumlahkan usaha semua potongan:

$$W \approx \sum_{i=1}^{n} F(x_i)\,\Delta x$$

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Pikir 30 dtk">

Bentuk jumlahan seperti ini kita kenal dari Bab 4. Apa yang terjadi bila potongannya dibuat makin tipis?

</SocraticBlock>

<SocraticBlock v-click="5" type="answer" title="Kesimpulan Kita">

Limit jumlahan Riemann adalah integral tentu:

$$W = \lim_{n \to \infty} \sum_{i=1}^{n} F(x_i)\,\Delta x = \int_a^b F(x)\,dx$$

</SocraticBlock>

<!--
Tiap pertanyaan dibuka dengan klik, beri waktu sebelum klik berikutnya.
P1 jawaban diharapkan: gaya × panjang potongan. Jika ada yang menjawab "F(x) saja": "Satuannya apa? Usaha harus satuan joule, yaitu newton kali meter."
P2: jawaban "jumlahkan semuanya". Jika ada yang menjawab "kalikan": "Kalau ada tiga potongan bernilai 2, 3, dan 5 joule, usaha totalnya berapa?"
P3: minta mahasiswa yang menjawab, bukan dosen. Kata integral boleh muncul dari mahasiswa di sini.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Sekarang Kita Beri Nama</span>
  <span class="text-xs text-slate-400 font-mono">Definisi: Kerja</span>
</h2>

::left::

<BeamerBlock type="block" title="Definisi: Kerja oleh Gaya yang Berubah">

Gaya $F(x)$ menggerakkan benda sepanjang sumbu-$x$ dari $x = a$ sampai $x = b$. Kerja (usaha) yang dilakukan:

$$W = \int_a^b F(x)\,dx$$

Satuan: joule (J) $=$ newton $\cdot$ meter.

</BeamerBlock>

<SocraticBlock v-click type="question" mode="Tunjuk di papan">

Cocokkan dengan yang kita temukan: apa arti $F(x)\,dx$? Dan apa arti luas di bawah grafik $F$?

</SocraticBlock>

::right::

<div v-click class="flex flex-col">

<SocraticBlock type="answer" title="Cocokkan dengan Soal Pegas">

- $F(x)\,dx$ = usaha pada potongan tipis di posisi $x$
- luas di bawah grafik $F$ = usaha total
- untuk pegas: $F(x) = kx$ (Hukum Hooke), jadi

$$W = \int_0^{0{,}3} 100x\,dx = 50x^2\Big|_0^{0{,}3} = 4{,}5\ \text{J}$$

</SocraticBlock>

<SocraticBlock type="reflect" title="Kembali ke Pertanyaan Kita">

Gaya berubah-ubah: apa yang kita jumlahkan, dan apa yang terjadi ketika potongannya dibuat makin tipis?

</SocraticBlock>

</div>

<!--
Definisi ditampilkan SETELAH kelas menemukannya sendiri. Katakan: "Ini hanya nama dan rumus untuk yang tadi kalian temukan."
Jawaban diharapkan untuk pertanyaan terakhir: jumlahkan "gaya × potongan kecil jarak", lalu limitnya integral.
Cek: 4,5 J ada di antara 0 dan 9 J, sesuai tebakan awal kelas.
-->

---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Selang yang Sama Panjang</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<SocraticBlock type="pitfall" title="Benarkah Cara Sari?" mode="Diskusi berpasangan · 1 mnt">

Pegas tadi, $F(x) = 100x$. Sari berkata: "Usaha menarik dari $x = 0{,}3$ sampai $x = 0{,}6$ sama dengan usaha dari $x = 0$ sampai $x = 0{,}3$, karena sama-sama menarik sejauh $0{,}3$ m." Benarkah? Bagaimana kalian memeriksanya?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Tidak. Gaya di selang kedua lebih besar, jadi usahanya juga lebih besar:

$$\int_{0{,}3}^{0{,}6} 100x\,dx = 50\left(0{,}36 - 0{,}09\right) = 13{,}5\ \text{J} \neq 4{,}5\ \text{J}$$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan">

Pada gambar applet tadi, di mana kesalahan Sari terlihat? Bandingkan luas di bawah grafik pada dua selang itu.

</SocraticBlock>

<!--
Nama tokoh pada slide kesalahan selalu fiktif agar tidak ada mahasiswa yang merasa dituding.
Jawaban diharapkan: gayanya berbeda di dua selang. Jika hening: "Gaya di x = 0,5 berapa? Gaya di x = 0,1 berapa?"
Pertanyaan lanjutan, jawaban diharapkan: luas di bawah grafik pada selang kedua trapesium yang lebih tinggi; luasnya tiga kali lipat segitiga pertama.
Pesan utama: usaha bergantung pada posisi awal dan akhir, bukan hanya pada jarak yang ditempuh.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Meregangkan Pegas</span>
  <span class="text-xs text-slate-400 font-mono">Stewart §6.4</span>
</h2>

<PolyaStepper step="1-2" support="full" :phases="3" />

::left::

<BeamerBlock type="example" title="Soal">

Gaya $40$ N menahan pegas yang diregangkan dari panjang alaminya $10$ cm menjadi $15$ cm. Berapa kerja untuk meregangkannya dari $15$ cm menjadi $18$ cm?

</BeamerBlock>

<SocraticBlock type="question" title="1 · Pahami Soal">

Apa yang diketahui, apa yang ditanya? Pertambahan panjang $x$ diukur dari mana, dan dalam satuan apa?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Diketahui: $F = 40$ N saat $x = 0{,}05$ m. Ditanya: kerja dari $x = 0{,}05$ m sampai $x = 0{,}08$ m. $x$ diukur dari panjang alami, dalam **meter**.

</SocraticBlock>

::right::

<div v-click="2" class="flex flex-col">

<SocraticBlock type="question" title="2 · Buat Rencana">

Kita belum tahu rumus gayanya. Apa yang harus dicari lebih dulu?

</SocraticBlock>

</div>

<div v-click="3" class="flex flex-col">

<SocraticBlock type="answer" title="Rencana">

1. Hukum Hooke: $F(x) = kx$. Cari $k$ dari $40 = k(0{,}05)$.
2. Hitung $W = \int_{0{,}05}^{0{,}08} kx\,dx$.

</SocraticBlock>

</div>

<WorkFigure kind="spring-ex" height="215px" />

<!--
Contoh dikerjakan bersama: dosen mencontohkan keempat langkah, tetapi tiap langkah dibuka dengan pertanyaan.
Pahami: kesalahan umum adalah memakai 15 cm sebagai x. Tanyakan: "Pegas yang belum ditarik, panjangnya berapa? Jadi pertambahannya berapa?"
Rencana, jawaban diharapkan: cari konstanta pegas k.
-->

---

<h2 class="slide-title">
  <span>Contoh 1: Meregangkan Pegas (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Stewart §6.4</span>
</h2>

<PolyaStepper step="3" support="full" :phases="3" />

<div class="max-w-2xl">

<BeamerBlock type="example" title="3 · Kerjakan">

$$k = \frac{40}{0{,}05} = 800\ \text{N/m}$$

$$
\begin{aligned}
W &= \int_{0{,}05}^{0{,}08} 800x\,dx = 400x^2\Big|_{0{,}05}^{0{,}08} \\
&= 400\,(0{,}0064 - 0{,}0025) = 1{,}56\ \text{J}
\end{aligned}
$$

</BeamerBlock>

</div>

<!--
Kerjakan: tulis di papan baris demi baris, slide hanya ringkasan.
Satuan: pastikan semua dalam meter dan newton sehingga hasilnya joule.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 2: Lengkapi yang Kosong</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 4 mnt</span>
</h2>

<PolyaStepper step="1-2" support="partial" :phases="3" />

::left::

<BeamerBlock type="example" title="Soal">

Kabel baja panjang $30$ m bermassa $2$ kg per meter tergantung tegak lurus. Berapa kerja untuk menarik seluruh kabel naik sampai ujung bawahnya setinggi ujung atas? Pakai $g = 10$ m/dtk$^2$.

</BeamerBlock>

<SocraticBlock type="question" title="1–2 · Pahami Soal & Buat Rencana" mode="Diskusi berpasangan · 1 mnt">

Tiap bagian kabel naik dengan jarak yang berbeda. Lihat gambar: potongan setebal $\Delta y$ ada pada kedalaman $y$ dari atas. Berapa berat potongan itu, dan berapa jauh ia naik?

</SocraticBlock>

::right::

<WorkFigure kind="cable" :reveal="false" height="340px" />

<!--
Gambar sengaja tidak memberi berat potongan dan jarak naik; itu yang ditanyakan.
Jawaban diharapkan: jarak naik y (dari kedalaman y sampai ke atas), berat 2 · Δy · 10 = 20Δy N.
Kesalahan umum: jarak naik 30 untuk semua bagian. Tanyakan: "Bagian paling atas naik berapa? Bagian paling bawah?"
Jika hening: "Kabel 2 kg tiap meter. Potongan setebal Δy massanya berapa? Berapa newton beratnya?"
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 2: Lengkapi yang Kosong (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 4 mnt</span>
</h2>

<PolyaStepper step="3" support="partial" :phases="3" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan: lengkapi yang kosong">

$$
\begin{aligned}
\Delta W &\approx \boxed{\phantom{000}}\,\Delta y \cdot \boxed{\phantom{000}} \\
W &= \int_0^{30} 20y\,dy = \boxed{\phantom{000}}\ \text{J}
\end{aligned}
$$

</BeamerBlock>

::right::

<SocraticBlock v-click="1" type="answer" title="Isian">

berat potongan $20\,\Delta y$ N &nbsp;·&nbsp; jarak naik $y$ &nbsp;·&nbsp; $W = 10y^2\big|_0^{30} = 9000$ J.

</SocraticBlock>

<div v-click="1">

<WorkFigure kind="cable" height="230px" />

</div>

<!--
Dukungan dikurangi: kerangka masih ada, isinya dikerjakan mahasiswa. Beri 4 menit berpasangan, berkeliling.
Berat potongan: massa 2Δy kg × g = 10 → 20Δy N. Kesalahan umum: lupa mengalikan g. Tanyakan: "Berat itu satuan apa? Newton atau kilogram?"
Satu klik memunculkan isian beserta gambar kabel berlabel; klik hanya setelah sebagian besar pasangan selesai.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Sendiri: Tangki Kerucut</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 6 mnt</span>
</h2>

<PolyaStepper step="1-3" support="independent" :phases="3" />

::left::

<BeamerBlock type="example" title="Soal">

Tangki berbentuk kerucut terbalik penuh berisi air: tinggi $6$ m, jari-jari bibir $3$ m. Air dipompa keluar lewat bibir tangki. Hitung kerja yang diperlukan. Berat jenis air $\rho g = 10^4$ N/m$^3$.

</BeamerBlock>

<SocraticBlock type="predict" title="Tebak Dulu" mode="Pikir 30 dtk">

Geser lapisan air dari dekat bibir ke dekat dasar. Lapisan mana yang butuh kerja **lebih besar**? Pikirkan luasnya dan jarak naiknya.

</SocraticBlock>

<SocraticBlock v-click type="answer">

Lapisan dekat bibir: naiknya sedikit, tetapi jauh lebih lebar dan lebih berat. Lapisan dekat dasar naik jauh, tetapi hampir tidak ada airnya.

</SocraticBlock>

::right::

<TankBoard height="395px" />

<!--
Mandiri: slide ini hanya memperlihatkan bentuk soal; rumus jari-jari belum diberikan.
Minta mahasiswa memutar gambar 3D dan menggeser kedalaman y. Panah putus-putus kuning adalah jarak angkat, yang sama dengan kedalaman y.
Tebak, jawaban diharapkan: dekat bibir. Jika banyak memilih "dekat dasar karena naiknya jauh": "Bandingkan jari-jari lapisan di y = 1 dan di y = 5. Berapa kali lebih besar luasnya?" (centang "tampilkan ukuran": r = 2,5 dan 0,5, luas 25 kali).
Tekan "Angkat ke bibir" untuk lapisan dekat bibir (y kecil) lalu untuk lapisan dekat dasar (y besar). Minta kelas membandingkan: berapa jauh tiap lapisan naik, dan seberapa lebar lapisannya? Bayangan putus-putus menandai posisi asal.
Lanjutkan ke slide berikutnya untuk petunjuk bertingkat.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Tangki Kerucut (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 6 mnt</span>
</h2>

<PolyaStepper step="1-3" support="independent" :phases="3" />

<BeamerBlock type="example" title="Soal (ringkas)">

Kerucut terbalik tinggi $6$ m, jari-jari bibir $3$ m, penuh air, dipompa lewat bibir; $\rho g = 10^4$ N/m$^3$. Hitung kerjanya.

</BeamerBlock>

<div class="grid grid-cols-3 gap-3">

<SocraticBlock v-click type="hint" level="1">

Iris air menjadi lapisan tipis pada kedalaman $y$ dari bibir tangki. Berapa jauh lapisan itu harus naik?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="2">

Lapisan itu berbentuk cakram tipis. Jari-jarinya berubah menurut $y$. Cari hubungannya dengan kesebangunan segitiga.

</SocraticBlock>

<SocraticBlock v-click type="hint" level="3">

Jari-jari lapisan $= \tfrac{6 - y}{2}$. Volumenya $\pi r^2 \Delta y$, beratnya $10^4$ kali itu. Kalikan dengan $y$, lalu integralkan dari $0$ sampai $6$.

</SocraticBlock>

</div>

<SocraticBlock v-click type="answer" title="Jawaban Akhir">

$W = 270\,000\pi$ J $\approx 8{,}5 \times 10^5$ J.

</SocraticBlock>

<!--
Mandiri: tidak ada kerangka langkah. Petunjuk dibuka satu per satu HANYA bila kelas macet, beri jeda minimal 1 menit.
Petunjuk 1 mengarahkan ulang ke soal, petunjuk 2 menyebut strategi, petunjuk 3 memberi langkah pertama. Tidak ada yang memberi jawaban.
Penyelesaian: W = ∫₀⁶ 10⁴ π ((6−y)/2)² y dy = 2500π ∫₀⁶ y(6−y)² dy = 2500π(648 − 864 + 324) = 270000π.
Yang ditampilkan hanya jawaban akhir; penyelesaian lengkap dikerjakan di papan bila perlu.
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Latihan Gabungan: Kabel Menarik Pegas</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 8 mnt</span>
</h2>

<PolyaStepper step="1-3" support="independent" :phases="3" />

::left::

<BeamerBlock type="example" title="Soal">

Kabel $2$ kg/m tergantung dari katrol setinggi $15$ m, ujungnya menyentuh lantai. Pegas di lantai: panjang alami $5$ m, $k = 10$ N/m. Di ketinggian $5$ m ujung kabel tersangkut di pegas, lalu ikut menariknya sampai $15$ m. $g = 10$ m/s$^2$.

**(a)** Hitung kerja menarik ujung kabel dari lantai ke ketinggian $5$ m.

**(b)** Tentukan rumus gaya tarik $F(y)$ untuk $5 \le y \le 15$.

</BeamerBlock>

<SocraticBlock type="predict" title="Tebak Dulu" mode="Angkat jari: A / B / C">

Setelah kabel tersangkut di pegas ($y \gt 5$), gaya tarik **A** makin besar, **B** makin kecil, atau **C** tetap?

</SocraticBlock>

<SocraticBlock v-click type="answer">

**B: makin kecil.** Tiap naik $1$ m, pegas menambah $10$ N, tetapi berat kabel yang tergantung turun $20$ N.

</SocraticBlock>

::right::

<CableSpringBoard height="400px" />

<!--
Mandiri: soal ini menggabungkan Contoh 1 (pegas) dan Contoh 2 (kabel).
Minta mahasiswa menggeser ujung kabel y dari 0 ke 15. Perhatikan: di bawah 5 m pegas diam; di atas 5 m pegas ikut teregang dan kabel yang tergantung makin pendek.
Tebak dulu, baru centang "tampilkan grafik F". Kebanyakan akan menebak A karena pegas makin teregang. Tanyakan: "Gaya apa saja yang ditahan tangan kita? Mana yang bertambah, mana yang berkurang, dan seberapa cepat?"
Centang "tampilkan angka" untuk mengecek: y = 5 → F = 200 N, y = 15 → F = 100 N. Luas terarsir di grafik adalah kerja sejauh ini.
Lanjutkan ke slide berikutnya untuk petunjuk bertingkat.
-->

---

<h2 class="slide-title">
  <span>Latihan Gabungan (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 8 mnt</span>
</h2>

<PolyaStepper step="1-3" support="independent" :phases="3" />

<div class="grid grid-cols-3 gap-3">

<SocraticBlock v-click type="hint" level="1">

Saat ujung kabel di ketinggian $y$, berapa panjang kabel yang masih tergantung? Berapa beratnya?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="2">

Pada (a), pegas belum ikut ditarik. Gaya tarik hanya berat kabel yang tergantung, dan gaya itu berubah menurut $y$.

</SocraticBlock>

<SocraticBlock v-click type="hint" level="3">

Pada (b), tangan menahan dua gaya sekaligus: gaya pegas $k \cdot (\text{regangan})$ dan berat kabel yang masih tergantung. Jumlahkan.

</SocraticBlock>

</div>

<div v-click class="grid grid-cols-2 gap-3">

<SocraticBlock type="answer" title="Jawaban (a)">

Kabel tergantung $15 - y$ m, beratnya $20(15 - y)$ N.

$$
W = \int_0^5 20(15 - y)\,dy = 20\Big[15y - \tfrac{y^2}{2}\Big]_0^5 = 1250 \text{ J}
$$

</SocraticBlock>

<SocraticBlock type="answer" title="Jawaban (b)">

Regangan pegas $y - 5$, kabel tergantung $15 - y$:

$$
F(y) = 10(y - 5) + 20(15 - y) = 250 - 10y \text{ N}
$$

Cek: $F(5) = 200$ N (hanya kabel), $F(15) = 100$ N (hanya pegas).

</SocraticBlock>

</div>

<!--
Mandiri: petunjuk dibuka satu per satu HANYA bila kelas macet, beri jeda minimal 1 menit.
Petunjuk 1 mengulang ide Contoh 2 (kabel), petunjuk 2 menegaskan batas soal (a), petunjuk 3 menggabungkan Contoh 1 dan Contoh 2.
Kesalahan umum: memakai panjang kabel 15 (bukan 15 − y), lupa mengalikan g, atau menulis regangan pegas y (bukan y − 5).
Cek di applet: y = 7 → F = 180 N.
Tantangan untuk yang cepat selesai: kerja dari 5 m sampai 15 m = ∫₅¹⁵ (250 − 10y) dy = 1500 J (luas trapesium di grafik F).
-->

---

<h2 class="slide-title">
  <span>Tulis Sebelum Pulang</span>
  <span class="text-xs text-slate-400 font-mono">Tulis di kertas · 2 mnt</span>
</h2>

<SocraticBlock type="reflect" title="Rangkum dengan Kata-Katamu">

1. Jelaskan kepada teman SMA: mengapa usaha oleh gaya yang berubah berupa luas di bawah grafik gaya?
2. Pada soal tangki tadi, mengapa tiap lapisan air naik dengan jarak yang berbeda? Di langkah mana kalian paling mungkin keliru?

</SocraticBlock>

<SocraticBlock type="question" title="Untuk Pertemuan Berikutnya">

Volume benda putar dan kerja punya pola yang sama: **potong, hampiri, jumlahkan, limit**. Apa yang membuat kita yakin pola itu selalu bisa dipakai pada masalah baru?

</SocraticBlock>

<!--
Kumpulkan kertasnya. Pertanyaan 2 memberi data miskonsepsi untuk pembukaan pertemuan berikutnya.
Pertanyaan terakhir tidak dijawab; ia menjadi penutup Bab 5 dan jembatan ke Bab 6 (fungsi logaritma natural).
-->
