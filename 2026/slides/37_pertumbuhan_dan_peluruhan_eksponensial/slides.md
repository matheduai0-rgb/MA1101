---
theme: default
background: '#0c1018'
title: 'MA1101 Kalkulus I - Pertumbuhan dan Peluruhan Eksponensial'
info: 'Subtopik 6.5 · Pertemuan 28 (bagian 2 dari 2, setelah deck 38)'
class: text-white slide-compact
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Bagian Kedua: Siapa yang Menang?</span>
  <span class="text-xs text-cyan-400 font-mono">Subtopik 6.5 · Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan Kedua Hari Ini">

Kapan sesuatu bertambah dengan laju yang **sebanding dengan banyaknya sendiri**, dan rumus apa yang selalu muncul?

</SocraticBlock>

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Koloni **A** mulai dari $1000$ dan bertambah $500$ tiap jam. Koloni **B** mulai dari $10$ saja, tetapi **dua kali lipat** tiap jam. Setelah $12$ jam:

**A.** A jauh lebih banyak  
**B.** B jauh lebih banyak  
**C.** kira-kira sama

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Geser $t$. Kira-kira pada jam ke berapa B menyusul A?
2. Centang "tampilkan laju". Laju A selalu $500$. Laju B selalu berapa kali banyaknya?

</SocraticBlock>

::right::

<GrowthBoard mode="race" height="390px" />

<!--
Bagian kedua pertemuan (sekitar 45 menit). Pertanyaan besar tidak dijawab sekarang; dijawab di slide Beri Nama.
Hubungkan dengan jembatan di akhir deck 38: laju 1000·2^t adalah (ln 2) × banyaknya.
Miskonsepsi yang diuji: pertumbuhan eksponensial dikira linear (B mulai kecil, jadi "pasti kalah").
Urutan: (1) semua mengangkat jari SEBELUM applet disentuh. (2) Geser pelan: berhenti di t = 4 (A = 3000, B = 160: B tampak kalah telak), lalu t = 9 (A = 5500, B = 5120), lalu t = 12.
Jawaban diharapkan: B. Setelah 12 jam A = 7000, B = 40.960. B menyusul sekitar jam ke-9,1.
Jika banyak memilih A: "B mulai dari 10. Setelah 10 jam berapa? Bandingkan dengan tabel tadi."
Pengamatan 2: laju B ≈ 0,693 × B, selalu. Angka 0,693 akan muncul lagi di slide berikutnya; jangan dijelaskan dulu.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Laju Sebanding Banyaknya</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

"Laju bertambahnya $y$ sebanding dengan $y$." Tulis kalimat ini sebagai persamaan, dengan turunan $dy/dt$ dan sebuah konstanta $k$.

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$$\frac{dy}{dt} = k\,y$$

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2" mode="Diskusi berpasangan · 1 mnt">

Selesaikan dengan memisahkan peubah, seperti di 3.9. Kalau $y(0) = y_0$, apa rumus $y(t)$?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer">

$$
\begin{aligned}
\frac{dy}{y} &= k\,dt \\
\ln y &= kt + C \\
y &= e^{C}e^{kt} = y_0\,e^{kt}
\end{aligned}
$$

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Pikir 30 dtk">

Untuk koloni yang dua kali lipat tiap jam, $y(1) = 2y_0$. Berapa $k$? Pernahkah kalian melihat angka itu hari ini?

</SocraticBlock>

<SocraticBlock v-click="5" type="answer" title="Kesimpulan Kita">

$e^{k} = 2$, jadi $k = \ln 2 \approx 0{,}693$, sama dengan angka laju B di applet. Dan $y_0e^{t\ln 2} = y_0\,2^{t}$, rumus bakteri di jembatan tadi.

</SocraticBlock>

<!--
Tiap pertanyaan dibuka dengan klik, beri waktu sebelum klik berikutnya.
P1: "sebanding" berarti sama dengan konstanta kali. Jika ada yang menulis dy/dt = k: "Itu laju tetap, seperti koloni A. Yang sebanding dengan apa?"
P2: y > 0 sehingga ln|y| = ln y. Konstanta e^C ditentukan oleh t = 0: y(0) = e^C = y₀.
P3: hubungkan ke 6.4: 2^t = e^{t ln 2}. Ini menjawab "mengapa 0,693?" dari applet.
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Sekarang Kita Beri Nama</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.5</span>
</h2>

::left::

<BeamerBlock type="block" title="Teorema: Pertumbuhan dan Peluruhan Eksponensial">

Jika $\dfrac{dy}{dt} = ky$ dan $y(0) = y_0$, maka

$$y(t) = y_0\,e^{kt}.$$

$k \gt 0$: **tumbuh**, dengan waktu dua kali lipat $T = \dfrac{\ln 2}{k}$.

$k \lt 0$: **meluruh**, dengan waktu paruh $T = \dfrac{\ln 2}{|k|}$.

</BeamerBlock>

::right::

<SocraticBlock type="question" title="Mengapa waktunya selalu sama?" mode="Pikir 30 dtk">

Dari $y_0e^{kT} = 2y_0$, berapa $T$? Mengapa jawabannya tidak bergantung pada $y_0$, atau pada kapan kita mulai menghitung?

</SocraticBlock>

<SocraticBlock v-click type="answer">

$e^{kT} = 2$, jadi $T = \dfrac{\ln 2}{k}$. $y_0$ hilang dari persamaan, jadi tiap selang $T$ banyaknya selalu dikali $2$, dari mana pun kita mulai.

</SocraticBlock>

<SocraticBlock v-click type="reflect" title="Kembali ke Pertanyaan Kita">

Sebutkan dua hal lain di sekitar kalian yang lajunya kira-kira sebanding dengan banyaknya. Untuk masing-masing, apakah $k$ positif atau negatif?

</SocraticBlock>

<!--
Teorema ditampilkan SETELAH kelas menemukannya sendiri. Katakan: "Ini hanya nama dan rumus untuk yang tadi kalian temukan."
Pertanyaan: jawaban diharapkan T = ln 2 / k. Untuk peluruhan e^{kT} = 1/2, sehingga T = −ln 2 / k = ln 2 / |k|.
Refleksi: populasi, bunga majemuk kontinu (k > 0); zat radioaktif, kadar obat dalam darah (k < 0). Simpan "suhu kopi" untuk pertanyaan jembatan di akhir.
-->

---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Naik 10% per Tahun</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<SocraticBlock type="pitfall" title="Benarkah Cara Sari?" mode="Angkat jari: A / B / C">

Penduduk sebuah kota naik $10\%$ per tahun. Sari menulis $y = y_0\,e^{0{,}1t}$, karena "$k$ itu persennya". Menurut kalian:

**A.** benar &nbsp;&nbsp; **B.** salah, tetapi hampir benar &nbsp;&nbsp; **C.** salah jauh

</SocraticBlock>

<SocraticBlock v-click type="answer">

Naik $10\%$ per tahun berarti $y(1) = 1{,}1\,y_0$. Jadi $e^{k} = 1{,}1$ dan

$$k = \ln 1{,}1 \approx 0{,}0953, \quad \text{bukan } 0{,}1.$$

Model Sari memberi $e^{0{,}1} \approx 1{,}105$, yaitu naik $10{,}5\%$ per tahun. Hampir benar (B), tetapi tetap salah.

</SocraticBlock>

<!--
Nama tokoh pada slide kesalahan selalu fiktif agar tidak ada mahasiswa yang merasa dituding.
Voting dulu. Banyak yang memilih A; jangan langsung dikoreksi. Tanya: "Kalau model Sari benar, berapa penduduk setelah 1 tahun? Hitung e^{0,1}."
Bila waktu longgar, tanya lisan: "Bakteri naik 100% per jam; cara Sari memberi k = 1. Berapa k yang benar?" Naik 100% berarti dua kali lipat, k = ln 2 ≈ 0,693, bukan 1. Setelah 10 jam: e^{10} ≈ 22.026 kali lawan 2^{10} = 1024 kali. Untuk persen kecil ln(1 + r) ≈ r, makanya kesalahan ini sering tidak ketahuan.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Berapa Umur Fosil Ini?</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.5</span>
</h2>

<PolyaStepper step="1-2" support="full" />

::left::

<BeamerBlock type="example" title="Soal">

Karbon-14 meluruh dengan waktu paruh $5730$ tahun. Sepotong kayu kuno hanya mengandung $70\%$ karbon-14 dari kayu yang masih hidup. Berapa umurnya?

</BeamerBlock>

<SocraticBlock type="question" title="1 · Pahami Soal" mode="Pikir 30 dtk">

Apa yang ditanya? Apa arti "waktu paruh $5730$ tahun" dalam rumus $y(t) = y_0e^{kt}$? Apa arti "$70\%$"?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Ditanya $t$. Waktu paruh: $y(5730) = \tfrac12 y_0$. Sisa $70\%$: $y(t) = 0{,}7\,y_0$. Nilai $y_0$ tidak diketahui, dan tidak perlu.

</SocraticBlock>

::right::

<div v-click="2" class="flex flex-col">

<SocraticBlock type="question" title="2 · Buat Rencana">

Ada dua yang belum diketahui, $k$ dan $t$. Mana yang dicari lebih dulu, dan dari data yang mana?

</SocraticBlock>

</div>

<div v-click="3" class="flex flex-col">

<SocraticBlock type="answer" title="Rencana">

1. Cari $k$ dari waktu paruh.
2. Tulis $0{,}7\,y_0 = y_0e^{kt}$, lalu bagi dengan $y_0$.
3. Ambil $\ln$ kedua ruas dan selesaikan $t$.

</SocraticBlock>

</div>

<!--
Contoh dikerjakan bersama: dosen mencontohkan keempat langkah, tetapi tiap langkah dibuka dengan pertanyaan.
Pahami: kesalahan umum mengira y₀ harus diketahui. Tanya: "Kalau kayunya dua kali lebih besar, apakah umurnya berubah?"
Rencana: jawaban diharapkan k dulu, karena hanya waktu paruh yang memberi persamaan dengan satu yang belum diketahui.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Berapa Umur Fosil Ini? (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.5</span>
</h2>

<PolyaStepper step="3-4" support="full" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan">

$$
\begin{aligned}
e^{5730k} &= \tfrac12 \;\Rightarrow\; k = -\frac{\ln 2}{5730} \approx -1{,}210\times 10^{-4} \\
e^{kt} &= 0{,}7 \;\Rightarrow\; t = \frac{\ln 0{,}7}{k} = \frac{5730\,\ln 0{,}7}{-\ln 2} \\
t &\approx 2950 \text{ tahun}
\end{aligned}
$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="question" title="4 · Periksa Lagi" mode="Pikir 1 mnt">

Tanpa kalkulator: sisa $70\%$ lebih banyak dari $50\%$. Jadi umurnya harus lebih atau kurang dari $5730$ tahun? Apakah tanda $k$ dan $t$ masuk akal?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Masih lebih dari separuh, jadi umurnya kurang dari satu waktu paruh: $2950 \lt 5730$ ✓. $k \lt 0$ karena meluruh, dan $\ln 0{,}7 \lt 0$, jadi $t \gt 0$ ✓. Cek: $\left(\tfrac12\right)^{2950/5730} \approx 0{,}70$ ✓

</SocraticBlock>

<!--
Kerjakan: tulis di papan baris demi baris, slide hanya ringkasan.
Angka: ln 0,7 ≈ −0,3567; ln 2 ≈ 0,6931; t ≈ 5730 × 0,5146 ≈ 2948, dibulatkan 2950.
Tekankan: rumus t = T·ln(sisa)/ln(1/2) berlaku untuk semua soal waktu paruh. Lebih baik dipahami daripada dihafal.
Periksa Lagi: langkah ini bukan hiasan. Tanya juga: "Setelah 2 × 5730 tahun, berapa persen yang tersisa?" (25%).
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Penduduk Sebuah Kota</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 6 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal">

Penduduk sebuah kota $1{,}2$ juta pada tahun 2010 dan $1{,}5$ juta pada tahun 2020. Anggap pertumbuhannya eksponensial. (a) Perkirakan penduduk tahun 2030. (b) Kapan penduduknya mencapai $3$ juta?

</BeamerBlock>

<SocraticBlock type="question" title="Sebelum Mulai" mode="Pikir 30 dtk">

Sebelum menghitung, tebak dulu: tahun 2030 lebih atau kurang dari $1{,}8$ juta (kalau naiknya tetap $0{,}3$ juta per $10$ tahun)?

</SocraticBlock>

<!--
Mandiri: tidak ada kerangka langkah. Beri waktu 1 menit sebelum membuka slide petunjuk.
Tebakan: lebih dari 1,8 juta, karena pertumbuhan eksponensial menambah makin banyak. Ini mengulang miskonsepsi "eksponensial dikira linear" dari awal kuliah.
Lanjutkan ke slide berikutnya untuk petunjuk bertingkat.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Penduduk Sebuah Kota (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan berpasangan · 6 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal (ringkas)">

$1{,}2$ juta (2010), $1{,}5$ juta (2020), eksponensial. (a) Tahun 2030? (b) Kapan $3$ juta?

</BeamerBlock>

<div class="grid grid-cols-3 gap-3">

<SocraticBlock v-click type="hint" level="1">

Hitung $t$ dalam tahun sejak 2010. Data mana yang memberi $y_0$, dan data mana yang memberi $k$?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="2">

Pakai $y = 1{,}2\,e^{kt}$. Data tahun 2020 memberi satu persamaan untuk $k$.

</SocraticBlock>

<SocraticBlock v-click type="hint" level="3">

Langkah pertama: $e^{10k} = \dfrac{1{,}5}{1{,}2} = 1{,}25$.

</SocraticBlock>

</div>

<SocraticBlock v-click type="answer" title="Jawaban Akhir & Periksa Lagi">

(a) $1{,}2 \cdot 1{,}25^2 = 1{,}875$ juta. (b) $t = \dfrac{10\ln 2{,}5}{\ln 1{,}25} \approx 41$, jadi sekitar tahun 2051. **Periksa:** mengapa (a) bisa dihitung tanpa logaritma sama sekali?

</SocraticBlock>

<!--
Mandiri: petunjuk dibuka satu per satu HANYA bila kelas macet, beri jeda minimal 1 menit.
Petunjuk 1 mengarahkan ulang, petunjuk 2 menyebut strategi, petunjuk 3 memberi langkah pertama. Tidak ada yang memberi jawaban.
Penyelesaian: k = ln 1,25 / 10 ≈ 0,0223. (a) e^{20k} = 1,25² = 1,5625, jadi 1,875 juta. (b) e^{kt} = 2,5, t = ln 2,5 / k ≈ 0,9163 / 0,0223 ≈ 41,1 tahun.
Periksa: tiap 10 tahun dikali 1,25 (sifat waktu yang sama dari teorema), jadi 2030 = 1,5 × 1,25. Bandingkan dengan tebakan 1,8 juta.
-->

---
class: slide-compact
---

<h2 class="slide-title">
  <span>Latihan di Rumah (PKH 6.5)</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan di rumah</span>
</h2>

<BeamerBlock type="example" title="Latihan di rumah">

1. Kadar obat dalam darah meluruh dengan waktu paruh $4$ jam. Pasien menerima $200$ mg. Kapan obatnya tinggal $25$ mg? Periksa dengan menghitung berapa kali waktu paruh.
2. Bakteri bertambah dari $500$ menjadi $4000$ dalam $6$ jam. Berapa waktu dua kali lipatnya?
3. Uang $10$ juta, bunga $6\%$ per tahun ditambahkan **kontinu**. Berapa setelah $5$ tahun? Bandingkan dengan bunga yang ditambahkan **tahunan**.
4. Zat radioaktif berkurang $20\%$ dalam $3$ hari. Berapa waktu paruhnya?
5. Uang $1$ juta, bunga $100\%$ per tahun ditambahkan $n$ kali setahun menjadi $\left(1 + \tfrac1n\right)^n$ juta. Hitung untuk $n = 12$ dan $n = 365$. Bilangan apa yang didekati?

</BeamerBlock>

<!--
Jawaban: (1) 12 jam (200 → 100 → 50 → 25). (2) 2 jam (8 = 2³). (3) 10e^{0,3} ≈ 13,50 juta; tahunan 10·1,06⁵ ≈ 13,38 juta. (4) k = (ln 0,8)/3 ≈ −0,0744, waktu paruh ≈ 9,3 hari. (5) 2,6130 dan 2,7146, mendekati e.
Soal 1 dan 5 berasal dari draf satu-subbab deck ini (contoh setengah jadi dan applet bunga, GrowthBoard mode="compound"); versi itu ada di riwayat git (commit dc26109).
Slide ini cukup ditunjukkan 30 detik.
-->

---

<h2 class="slide-title">
  <span>Tulis Sebelum Pulang</span>
  <span class="text-xs text-slate-400 font-mono">Tulis di kertas · 3 mnt</span>
</h2>

<SocraticBlock type="reflect" title="Tiket Keluar" mode="Tulis · 3 mnt">

1. Penduduk sebuah kota naik $3\%$ per tahun. Tulis $y(t)$, lalu tentukan kapan penduduknya menjadi dua kali lipat.
2. Dengan kata-katamu sendiri: kapan rumus $y = y_0e^{kt}$ boleh dipakai?

</SocraticBlock>

<SocraticBlock type="question" title="Untuk Pertemuan Berikutnya">

Kopi panas mendingin dengan laju yang sebanding dengan **selisih** suhunya dengan suhu ruang, bukan dengan suhunya sendiri. Apakah ini masih $\dfrac{dy}{dt} = ky$?

</SocraticBlock>

<!--
Kumpulkan kertasnya. Soal 1 memeriksa tujuan hari ini sekaligus miskonsepsi k: jawaban benar y = y₀e^{t ln 1,03}, T = ln 2 / ln 1,03 ≈ 23,4 tahun. Hitung berapa yang memakai k = 0,03 (T ≈ 23,1); catat jumlahnya di retro.md, tanpa nama.
Pilih dua jawaban anonim untuk pembuka pertemuan 29.
Pertanyaan terakhir tidak dijawab; ia menjadi pembuka 6.6 (persamaan diferensial linear orde satu, hukum pendinginan Newton).
-->
