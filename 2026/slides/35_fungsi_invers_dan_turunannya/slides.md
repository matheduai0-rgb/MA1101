---
theme: default
background: '#0c1018'
title: 'MA1101 Kalkulus I - Fungsi Invers dan Turunannya'
info: 'Subtopik 6.2 · Pertemuan 26'
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
---

# MA1101 Kalkulus I
<p class="text-xl text-amber-400 font-semibold mt-2">Bab 6: Fungsi Transenden</p>
<p class="text-sm text-slate-300 mt-1">Subtopik 6.2: Fungsi Invers dan Turunannya</p>

<div class="mt-8 max-w-xl mx-auto text-left">
<SocraticBlock type="question" title="Pertanyaan Kita Hari Ini">

Kalau rumus fungsi invers **tidak bisa** kita tuliskan, bisakah kita tetap menghitung turunannya?

</SocraticBlock>
</div>

<!--
Jangan dijawab sekarang. Bacakan, beri jeda 10 detik, lalu katakan: "Di akhir kuliah, kalian sendiri yang akan menjawabnya."
Hubungkan dengan akhir pertemuan lalu: "ln selalu naik, jadi tiap nilai hanya dicapai satu kali. Hari ini kita lihat apa artinya itu."
-->

---

<h2 class="slide-title">
  <span>Mulai dari Soal: Rumus Invers yang Macet</span>
  <span class="text-xs text-slate-400 font-mono">Pakai yang sudah kita tahu</span>
</h2>

<BeamerBlock type="block" title="Yang sudah kita tahu">

Kalau $f(x) = 2x + 6$, kita bisa membalik rumusnya: dari $y = 2x + 6$ didapat $x = \dfrac{y - 6}{2}$. Jadi $f^{-1}(y) = \dfrac{y - 6}{2}$.

</BeamerBlock>

<SocraticBlock type="question" mode="Kerjakan di kertas · 1 mnt">

Sekarang $f(x) = x^5 + 2x + 1$. Coba balik rumusnya: dari $y = x^5 + 2x + 1$, tuliskan $x$ dalam $y$. Di mana kalian macet?

</SocraticBlock>

<SocraticBlock v-click type="answer" title="Yang biasanya muncul">

Tidak ada cara aljabar biasa untuk menyelesaikan $x^5 + 2x + 1 = y$. Rumus $f^{-1}$ tidak bisa kita tuliskan.

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Padahal $f(1) = 4$. Jadi $f^{-1}(4) = 1$ tetap bisa dibaca. Berapa **kemiringan** grafik $f^{-1}$ di titik $y = 4$?

</SocraticBlock>

<!--
Tanya: beri 1 menit di kertas. Biarkan mahasiswa benar-benar mencoba memindahkan x.
Jawaban diharapkan: macet karena ada x⁵ dan x sekaligus.
Jika ada yang mencoba "akar pangkat lima": "Akar pangkat lima dari apa? Suku 2x masih tertinggal."
Pertanyaan lanjutan tidak dijawab sekarang. Inilah soal yang akan kita selesaikan hari ini (Contoh 1).
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Siapa yang Punya Invers?</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Angkat jari: A / B / C">

Fungsi punya invers kalau tiap nilai $y$ berasal dari **tepat satu** $x$. Mana yang punya invers?

**A.** $f(x) = x^2$  
**B.** $f(x) = x^3 - 3x$  
**C.** $f(x) = x^3 + x$

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Geser garis mendatar naik-turun. Berapa kali ia memotong tiap grafik?
2. Apa bedanya bentuk grafik C dengan A dan B?

</SocraticBlock>

::right::

<InverseBoard mode="test" height="380px" />

<!--
Urutan: (1) minta semua mengangkat jari SEBELUM menyentuh applet. (2) Pilih A, geser garis ke y = 1: memotong 2 kali. (3) Pilih B: ada posisi yang memotong 3 kali. (4) Pilih C: selalu 1 kali.
Jawaban diharapkan: C saja. Jika banyak memilih B karena "B fungsi pangkat tiga seperti x³": "Geser garis ke y = 1. Berapa titik potongnya?"
Pengamatan 2: grafik C selalu naik; A turun lalu naik; B naik, turun, naik lagi. Setelah ada yang menyebutnya, centang "tampilkan kesimpulan".
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Temukan Bersama: Kapan Invers Pasti Ada?</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

::left::

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

Kalau $f$ **selalu naik**, bisakah dua nilai $x$ yang berbeda memberi nilai $y$ yang sama?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

Tidak. Kalau $x_1 \lt x_2$ maka $f(x_1) \lt f(x_2)$, jadi nilainya pasti berbeda. Hal yang sama berlaku bila $f$ selalu turun.

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2">

Bagaimana memeriksa bahwa $f(x) = x^5 + 2x + 1$ selalu naik, tanpa menggambar grafiknya?

</SocraticBlock>

::right::

<SocraticBlock v-click="3" type="answer">

Pakai turunan (Bab 3):

$$f'(x) = 5x^4 + 2 \gt 0 \quad \text{untuk semua } x$$

Jadi $f$ selalu naik, dan $f^{-1}$ ada walaupun rumusnya tidak bisa ditulis.

</SocraticBlock>

<SocraticBlock v-click="4" type="question" title="Pertanyaan 3" mode="Pikir 30 dtk">

$f(x) = x^2$ tidak punya invers di seluruh garis bilangan. Bagaimana kalau kita hanya memakai $x \ge 0$?

</SocraticBlock>

<SocraticBlock v-click="5" type="answer" title="Kesimpulan Kita">

Di $x \ge 0$, $x^2$ selalu naik, jadi punya invers: $f^{-1}(y) = \sqrt{y}$. Kalau perlu, **batasi daerah asal** sampai fungsinya selalu naik atau selalu turun.

</SocraticBlock>

<!--
Tiap pertanyaan dibuka dengan klik, beri waktu sebelum klik berikutnya.
P1, jawaban diharapkan: tidak bisa. Jika hening: "Ambil x₁ = 1 dan x₂ = 2 untuk fungsi yang selalu naik. Mana yang nilainya lebih besar?"
P2: jawaban "turunannya positif". Ingatkan hubungan tanda f' dengan naik-turun dari Bab 3.
P3: arahkan ke √y. Kata "monoton murni" boleh diperkenalkan di slide berikutnya.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Coba Geser: Grafik Invers dan Kemiringannya</span>
  <span class="text-xs text-cyan-400 font-mono">Tebak → Amati → Jelaskan</span>
</h2>

::left::

<SocraticBlock type="predict" mode="Tulis angkanya · 30 dtk">

Titik $(a, b)$ ada di grafik $f$, jadi $(b, a)$ ada di grafik $f^{-1}$. Kalau kemiringan $f$ di $(a, b)$ adalah $3$, berapa kemiringan $f^{-1}$ di $(b, a)$?

</SocraticBlock>

<SocraticBlock v-click type="question" title="Sambil Mengamati" mode="Pikir 30 dtk">

1. Centang "tampilkan grafik $f^{-1}$". Bagaimana kedua grafik terletak terhadap garis $y = x$?
2. Geser $a$, lalu centang "tampilkan kemiringan". Apa hubungan kedua angka itu?

</SocraticBlock>

::right::

<InverseBoard mode="reflect" height="380px" />

<!--
Urutan: (1) minta semua menulis angka tebakan SEBELUM applet dipakai. (2) Centang grafik f⁻¹: cerminan terhadap y = x, karena (a, b) ditukar menjadi (b, a). (3) Geser a ke 1: kemiringan 4 dan 0,25.
Jawaban tebakan yang diharapkan: 1/3. Jika ada yang menjawab −3 atau 3: "Garis singgung juga ikut dicerminkan. Naik dan ke kanan bertukar peran. Kemiringan = naik/ke kanan menjadi?"
Pengamatan 2: hasil kalinya selalu 1. Coba a = 0: kemiringan 1 dan 1.
-->

---

<h2 class="slide-title">
  <span>Temukan Bersama: Rumus Turunan Invers</span>
  <span class="text-xs text-slate-400 font-mono">Satu langkah, satu pertanyaan</span>
</h2>

<div class="grid grid-cols-2 gap-4">
<div>

<SocraticBlock type="question" title="Pertanyaan 1" mode="Pikir 30 dtk">

Untuk $f(x) = 2x + 6$ dan $f^{-1}(y) = \tfrac{y - 6}{2}$, berapa kemiringan masing-masing?

</SocraticBlock>

<SocraticBlock v-click="1" type="answer">

$2$ dan $\tfrac12$. Cocok dengan applet: saling berkebalikan.

</SocraticBlock>

<SocraticBlock v-click="2" type="question" title="Pertanyaan 2">

Untuk $f$ umum berlaku $f\bigl(f^{-1}(y)\bigr) = y$. Turunkan kedua ruas terhadap $y$ dengan aturan rantai. Apa yang didapat?

</SocraticBlock>

</div>
<div>

<SocraticBlock v-click="3" type="answer">

$$f'\bigl(f^{-1}(y)\bigr)\cdot\bigl(f^{-1}\bigr)'(y) = 1$$

</SocraticBlock>

<SocraticBlock v-click="4" type="answer" title="Kesimpulan Kita">

Tulis $x = f^{-1}(y)$, yaitu $y = f(x)$. Bila $f'(x) \ne 0$:

$$\bigl(f^{-1}\bigr)'(y) = \frac{1}{f'(x)}$$

Kemiringan invers = satu per kemiringan $f$ di titik **pasangannya**.

</SocraticBlock>

</div>
</div>

<!--
P1: hitung langsung dari rumus. Jawaban diharapkan 2 dan 1/2.
P2: kesalahan umum lupa mengalikan turunan bagian dalam. Tanyakan: "Fungsi luarnya f, fungsi dalamnya f⁻¹(y). Aturan rantai bilang apa?"
Kesimpulan: minta mahasiswa yang mengucapkan rumusnya. Tekankan "titik pasangannya": x dengan f(x) = y.
Mengapa perlu f'(x) ≠ 0: kalau garis singgung f mendatar, garis cerminnya tegak, kemiringannya tidak ada.
-->

---
layout: two-cols-header
class: slide-compact
---

<h2 class="slide-title">
  <span>Sekarang Kita Beri Nama</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.2</span>
</h2>

::left::

<BeamerBlock type="block" title="Teorema A: Kapan Invers Ada">

Jika $f$ **monoton murni** (selalu naik atau selalu turun) pada daerah asalnya, maka $f$ punya invers $f^{-1}$, dengan

$$f^{-1}\bigl(f(x)\bigr) = x, \qquad f\bigl(f^{-1}(y)\bigr) = y.$$

Cara cek: $f'(x) \gt 0$ untuk semua $x$, atau $f'(x) \lt 0$ untuk semua $x$.

</BeamerBlock>

<BeamerBlock type="block" title="Teorema B: Turunan Invers">

Jika $f$ terdiferensialkan dan monoton murni pada selang $I$, dan $f'(x) \ne 0$ di suatu $x$ di $I$, maka $f^{-1}$ terdiferensialkan di $y = f(x)$ dan

$$\bigl(f^{-1}\bigr)'(y) = \frac{1}{f'(x)}.$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="question" mode="Tunjuk di papan">

Cocokkan dengan yang kita temukan: bagian mana dari Teorema A yang tadi kita lihat dengan garis mendatar? Bagian mana dari Teorema B yang tadi kita lihat dengan dua garis singgung?

</SocraticBlock>

<div v-click class="flex flex-col">

<SocraticBlock type="answer" title="Cocokkan dengan Applet">

- garis mendatar memotong satu kali = tiap $y$ dari tepat satu $x$ = monoton murni
- grafik $f^{-1}$ = cerminan grafik $f$ terhadap $y = x$
- kemiringan $4$ dan $0{,}25$ = $f'(x)$ dan $\dfrac{1}{f'(x)}$

</SocraticBlock>

<SocraticBlock type="reflect" title="Kembali ke Pertanyaan Kita">

Untuk menghitung $\bigl(f^{-1}\bigr)'(y)$, apakah kita perlu rumus $f^{-1}$? Apa yang cukup kita ketahui?

</SocraticBlock>

</div>

<!--
Teorema ditampilkan SETELAH kelas menemukannya sendiri. Katakan: "Ini hanya nama dan syarat untuk yang tadi kalian temukan."
Jawaban diharapkan untuk pertanyaan terakhir: tidak perlu rumus f⁻¹. Cukup tahu x dengan f(x) = y, lalu hitung f'(x).
Notasi: Purcell menulis (f⁻¹)'(y) = 1/f'(x); Stewart menulis (f⁻¹)'(a) = 1/f'(f⁻¹(a)). Isinya sama.
-->

---

<h2 class="slide-title">
  <span>Apakah Ini Benar? Turunan Invers di Titik Mana?</span>
  <span class="text-xs text-rose-400 font-mono">Cari kesalahannya</span>
</h2>

<SocraticBlock type="pitfall" title="Benarkah Cara Bima?" mode="Diskusi berpasangan · 1 mnt">

Untuk $f(x) = x^5 + 2x + 1$, Bima menulis

$$\bigl(f^{-1}\bigr)'(4) = \frac{1}{f'(4)} = \frac{1}{5 \cdot 4^4 + 2} = \frac{1}{1282}$$

Apa yang keliru?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Angka $4$ adalah nilai $y$, bukan $x$. Rumusnya $\bigl(f^{-1}\bigr)'(y) = \dfrac{1}{f'(x)}$ dengan $f(x) = y$. Jadi harus dicari dulu $x$ dengan $f(x) = 4$.

</SocraticBlock>

<SocraticBlock v-click type="question" title="Pertanyaan Lanjutan" mode="Pikir 30 dtk">

Bima juga menulis $f^{-1}(y) = \dfrac{1}{f(y)}$. Periksa dengan $f(x) = 2x + 6$ di $y = 8$. Apa yang ia campur aduk?

</SocraticBlock>

<!--
Nama tokoh pada slide kesalahan selalu fiktif agar tidak ada mahasiswa yang merasa dituding.
Jawaban diharapkan: titiknya salah. Jika hening: "f(4) berapa? Apakah titik (4, ...) ada di grafik f⁻¹?"
Pertanyaan lanjutan: f⁻¹(8) = 1, sedangkan 1/f(8) = 1/22. Tanda pangkat −1 pada f⁻¹ BUKAN berarti "satu per".
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Turunan Invers tanpa Rumus Invers</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.2</span>
</h2>

<PolyaStepper step="1-2" support="full" />

::left::

<BeamerBlock type="example" title="Soal">

Diketahui $f(x) = x^5 + 2x + 1$. Hitung $\bigl(f^{-1}\bigr)'(4)$.

</BeamerBlock>

<SocraticBlock type="question" title="1 · Pahami Soal">

Apa yang diketahui, apa yang ditanya? Angka $4$ itu nilai $x$ atau nilai $y$? Apakah $f^{-1}$ memang ada?

</SocraticBlock>

<SocraticBlock v-click type="answer">

Ditanya kemiringan $f^{-1}$ di $y = 4$. $f^{-1}$ ada karena $f'(x) = 5x^4 + 2 \gt 0$.

</SocraticBlock>

::right::

<div v-click="2" class="flex flex-col">

<SocraticBlock type="question" title="2 · Buat Rencana">

Rumus $f^{-1}$ tidak bisa ditulis. Teorema mana yang tetap bisa dipakai, dan apa yang perlu dicari lebih dulu?

</SocraticBlock>

</div>

<div v-click="3" class="flex flex-col">

<SocraticBlock type="answer" title="Rencana">

1. Cari $x$ dengan $f(x) = 4$ (coba bilangan bulat kecil).
2. Hitung $f'(x)$.
3. Pakai Teorema B: $\bigl(f^{-1}\bigr)'(4) = \dfrac{1}{f'(x)}$.

</SocraticBlock>

</div>

<!--
Contoh dikerjakan bersama: dosen mencontohkan keempat langkah, tetapi tiap langkah dibuka dengan pertanyaan.
Pahami: kesalahan umum sama dengan Bima, menganggap 4 sebagai x. Tanyakan: "Di grafik f⁻¹, sumbu datarnya berisi nilai apa?"
Rencana, jawaban diharapkan: Teorema B, cari x pasangannya dulu.
-->

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Contoh 1: Turunan Invers tanpa Rumus Invers (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Purcell §6.2</span>
</h2>

<PolyaStepper step="3-4" support="full" />

::left::

<BeamerBlock type="example" title="3 · Kerjakan">

Coba $x = 1$: $f(1) = 1 + 2 + 1 = 4$ ✓. Jadi pasangannya $x = 1$.

$$f'(1) = 5 \cdot 1^4 + 2 = 7$$

$$\bigl(f^{-1}\bigr)'(4) = \frac{1}{f'(1)} = \frac{1}{7}$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="question" title="4 · Periksa Lagi" mode="Pikir 1 mnt">

Tanpa rumus $f^{-1}$, bagaimana mengecek angka $\tfrac17$? Petunjuk: geser $x$ sedikit, dari $1$ ke $1{,}01$.

</SocraticBlock>

<SocraticBlock v-click type="answer">

$f(1{,}01) \approx 4{,}0710$. Jadi $f^{-1}$ naik dari $1$ ke $1{,}01$ saat $y$ naik dari $4$ ke $4{,}0710$:

$$\text{kemiringan} \approx \frac{0{,}01}{0{,}0710} \approx 0{,}141 \approx \frac{1}{7}\ ✓$$

</SocraticBlock>

<!--
Kerjakan: tulis di papan baris demi baris, slide hanya ringkasan.
Periksa Lagi: tekankan bahwa langkah ini bukan hiasan. Hitung 1,01⁵ ≈ 1,0510 dengan kalkulator.
Masuk akal juga: f naik curam (kemiringan 7), jadi cerminannya landai (kemiringan kecil).
Sekarang Pertanyaan Lanjutan di slide 2 sudah terjawab.
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

Diketahui $f(x) = 2x + \cos x$. Hitung $\bigl(f^{-1}\bigr)'(1)$.

</BeamerBlock>

<SocraticBlock type="question" title="1–2 · Pahami Soal & Buat Rencana" mode="Diskusi berpasangan · 1 mnt">

Rencananya sama dengan Contoh 1. Apa dua hal yang harus kalian peroleh lebih dulu, dan bagaimana memastikan $f^{-1}$ ada?

</SocraticBlock>

::right::

<BeamerBlock type="example" title="Yang sudah kita punya">

Rencana: (1) pastikan $f$ monoton murni, (2) cari $x$ dengan $f(x) = 1$, (3) hitung $\dfrac{1}{f'(x)}$.

</BeamerBlock>

<!--
Dukungan dikurangi: rencana sudah diberikan, mahasiswa yang mengisi langkahnya. Beri 1 menit berpasangan untuk Pahami dan Rencana.
Jawaban diharapkan: x pasangan dan f'(x). Untuk "f⁻¹ ada": f'(x) = 2 − sin x.
Jika ada yang bingung mencari x: "Coba x = 0. cos 0 berapa?"
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
f'(x) &= \boxed{\phantom{000}} \;\ge\; \boxed{\phantom{000}} \gt 0 \\
f(\boxed{\phantom{00}}) &= 1 \\
\bigl(f^{-1}\bigr)'(1) &= \frac{1}{f'(\boxed{\phantom{00}})} = \boxed{\phantom{000}}
\end{aligned}
$$

</BeamerBlock>

::right::

<SocraticBlock v-click type="answer" title="Isian dan Pemeriksaan">

$f'(x) = 2 - \sin x \ge 1 \gt 0$, jadi $f$ selalu naik dan $f^{-1}$ ada. $f(0) = 0 + \cos 0 = 1$, jadi $x = 0$. $\bigl(f^{-1}\bigr)'(1) = \dfrac{1}{f'(0)} = \dfrac{1}{2}$.

**Periksa:** $f'(x)$ selalu antara $1$ dan $3$, jadi kemiringan $f^{-1}$ selalu antara $\tfrac13$ dan $1$. Nilai $\tfrac12$ ada di dalamnya ✓

</SocraticBlock>

<!--
Beri 4 menit berpasangan, berkeliling.
Kesalahan umum: menulis f'(x) = 2 + sin x (tanda turunan cos). Tanyakan: "Turunan cos x itu sin x atau −sin x?"
Kesalahan kedua: memakai x = 1 karena soal menyebut angka 1. Arahkan kembali ke slide Bima.
Klik untuk isian hanya setelah sebagian besar pasangan selesai.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Invers yang Melibatkan ln</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 6 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal">

Diketahui $f(x) = x^3 + \ln x$ untuk $x \gt 0$. Tunjukkan bahwa $f$ punya invers, lalu hitung $\bigl(f^{-1}\bigr)'(1)$.

</BeamerBlock>

<SocraticBlock type="question" title="Sebelum Mulai" mode="Pikir 30 dtk">

Tulis dulu: apa yang harus ditunjukkan, dan apa yang harus dihitung? Kalian mau mulai dari langkah mana?

</SocraticBlock>

<!--
Mandiri: tidak ada kerangka langkah. Beri waktu 1 menit sebelum membuka slide petunjuk.
Soal ini menyambung ke 6.1: turunan ln x adalah 1/x, dan ln 1 = 0.
Lanjutkan ke slide berikutnya untuk petunjuk bertingkat.
-->

---

<h2 class="slide-title">
  <span>Coba Sendiri: Invers yang Melibatkan ln (lanjutan)</span>
  <span class="text-xs text-slate-400 font-mono">Kerjakan sendiri · 6 mnt</span>
</h2>

<PolyaStepper step="1-4" support="independent" />

<BeamerBlock type="example" title="Soal (ringkas)">

$f(x) = x^3 + \ln x$, $x \gt 0$. Tunjukkan $f$ punya invers, lalu hitung $\bigl(f^{-1}\bigr)'(1)$.

</BeamerBlock>

<div class="grid grid-cols-3 gap-3">

<SocraticBlock v-click type="hint" level="1">

Teorema mana yang menjamin invers ada? Apa yang harus kalian periksa tentang $f'(x)$?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="2">

Untuk turunan invers di $y = 1$, kalian perlu $x$ pasangannya. Nilai $x$ berapa yang membuat $\ln x$ hilang?

</SocraticBlock>

<SocraticBlock v-click type="hint" level="3">

$f'(x) = 3x^2 + \tfrac{1}{x}$, positif untuk $x \gt 0$. Coba $x = 1$: $f(1) = 1 + \ln 1$.

</SocraticBlock>

</div>

<SocraticBlock v-click type="answer" title="Jawaban Akhir & Periksa Lagi">

$\bigl(f^{-1}\bigr)'(1) = \dfrac14$. Periksa: $f(1{,}01) \approx 1{,}0403$. Apakah $\dfrac{0{,}01}{0{,}0403}$ dekat dengan $\dfrac14$?

</SocraticBlock>

<!--
Mandiri: petunjuk dibuka satu per satu HANYA bila kelas macet, beri jeda minimal 1 menit.
Petunjuk 1 mengarahkan ulang ke teorema, petunjuk 2 menyebut strategi (cari x pasangan), petunjuk 3 memberi langkah pertama. Tidak ada yang memberi jawaban.
Penyelesaian: f'(x) = 3x² + 1/x > 0 untuk x > 0, jadi monoton murni. f(1) = 1, f'(1) = 4, (f⁻¹)'(1) = 1/4.
Pemeriksaan: 1,01³ ≈ 1,0303 dan ln 1,01 ≈ 0,00995, jumlahnya ≈ 1,0403; 0,01/0,0403 ≈ 0,248 ≈ 1/4.
-->

---

<h2 class="slide-title">
  <span>Tulis Sebelum Pulang</span>
  <span class="text-xs text-slate-400 font-mono">Tulis di kertas · 2 mnt</span>
</h2>

<SocraticBlock type="reflect" title="Rangkum dengan Kata-Katamu">

1. Jelaskan kepada teman SMA: kapan sebuah fungsi punya invers, dan bagaimana grafik inversnya terlihat?
2. Untuk menghitung $\bigl(f^{-1}\bigr)'(y)$, apa yang harus dicari lebih dulu? Di langkah mana kalian paling mungkin keliru?

</SocraticBlock>

<SocraticBlock type="question" title="Untuk Pertemuan Berikutnya">

$\ln x$ selalu naik, jadi punya invers. Fungsi apa itu? Dengan Teorema B, berapa turunannya?

</SocraticBlock>

<!--
Kumpulkan kertasnya. Pertanyaan 2 memberi data miskonsepsi untuk pembukaan pertemuan berikutnya.
Pertanyaan terakhir tidak dijawab; ia menjadi pembuka 6.3 (fungsi eksponen natural, bilangan e).
-->
