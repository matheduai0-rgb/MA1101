---
theme: default
background: '#0c1018'
title: MA1101 Kalkulus I - Slidev + JSXGraph
info: |
  ## MA1101 Kalkulus I
  FMIPA Institut Teknologi Bandung
class: text-white
drawings:
  persist: false
transition: slide-left
mdc: true
canvasWidth: 980
lineNumbers: true
---

# MA1101 Kalkulus I
<span class="text-amber-400 font-semibold text-lg">Bab 4: Integral Tentu dan Jumlah Riemann</span>

<div class="mt-8">
<BeamerBlock type="block" title="Informasi Perkuliahan">

**Fakultas Matematika dan Ilmu Pengetahuan Alam (FMIPA)**  
Institut Teknologi Bandung &bull; Format: Slidev + JSXGraph Interactive

</BeamerBlock>
</div>

<div class="abs-bottom-4 text-xs text-slate-500">
  Gunakan tombol panah kanan &rarr; untuk navigasi slide
</div>

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Definisi: Jumlah Riemann</span>
  <span class="text-xs text-slate-400 font-mono">Teori Dasar</span>
</h2>

::left::

<BeamerBlock type="block" title="Definisi Partisi & Titik Sampel">

Misalkan $P: a = x_0 \lt x_1 \lt \dots \lt x_n = b$ adalah partisi dari selang $[a, b]$ dengan panjang subselang:

$$\Delta x_i = x_i - x_{i-1}$$

Pilih titik sampel $x_i^* \in [x_{i-1}, x_i]$. Jumlah Riemann fungsi $f$ didefinisikan sebagai:

$$R_P = \sum_{i=1}^n f(x_i^*) \Delta x_i$$

</BeamerBlock>

<BeamerBlock type="alert" title="Catatan Geometri">

Jika $f(x) \ge 0$, maka $R_P$ merepresentasikan jumlah luas persegi panjang hampiran di bawah kurva $y = f(x)$.

</BeamerBlock>

::right::

<BeamerBlock type="example" title="Limit Menuju Integral Tentu">

Ketika norma partisi $\|P\| = \max \Delta x_i \to 0$ (atau $n \to \infty$ untuk partisi seragam):

$$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*) \Delta x$$

</BeamerBlock>

---

<h2 class="slide-title">
  <span>Eksplorasi Interaktif: Jumlah Riemann</span>
  <span class="text-xs text-cyan-400 font-mono">Live 60 FPS JSXGraph</span>
</h2>

<BeamerBlock type="block" title="Instruksi Interaktif">

Geser slider partisi $n$ di bawah untuk mengamati hampiran luas di bawah kurva $f(x)$ mendekati nilai eksak integral tentu $\int_{0.5}^{4.5} f(x)\,dx$.

</BeamerBlock>

<!-- Interactive JSXGraph Component -->
<CalcRiemannSum :initial-n="6" height="280px" :a="0.5" :b="4.5" />

---
layout: two-cols-header
---

<h2 class="slide-title">
  <span>Garis Singgung & Titik Singgung</span>
  <span class="text-xs text-amber-400 font-mono">Diferensial</span>
</h2>

::left::

<BeamerBlock type="block" title="Kemiringan Garis Singgung">

Turunan fungsi $f$ di titik $x = c$ menyatakan kemiringan garis singgung kurva:

$$m = f'(c) = \lim_{h \to 0} \frac{f(c + h) - f(c)}{h}$$

Persamaan garis singgung di titik $(c, f(c))$:

$$y - f(c) = f'(c)(x - c)$$

</BeamerBlock>

::right::

<JSXGraphBoard 
  height="300px"
  :boundingbox="[-1, 6, 6, -1]"
  :init="(board, JXG) => {
    const f = (x) => 0.25 * x * x + 0.5;
    const curve = board.create('functiongraph', [f, -1, 6], { strokeColor: '#50a5fa', strokeWidth: 3 });
    const pt = board.create('glider', [2, 1.5, curve], { name: 'P', color: '#f5be3c', size: 3 });
    board.create('tangent', [pt], { strokeColor: '#fb7185', strokeWidth: 2, dash: 2 });
  }"
/>
