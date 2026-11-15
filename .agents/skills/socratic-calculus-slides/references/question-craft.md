# Question Craft for Socratic Calculus Slides

Contents: 1. Six kinds of question · 2. Weak vs. strong · 3. Question chains · 4. Response modes ·
5. The hint ladder · 6. Presenter notes · 7. Misconception bank by topic

## 1. Six kinds of question

Each has a job. A good deck uses several; a deck that only uses the first kind is a quiz.

| Kind | Job | Stem (Indonesian) | Block |
|------|-----|-------------------|-------|
| Activate | Surface what students already know | "Dengan alat yang sudah kalian punya, apa yang bisa dihitung?" | `question` |
| Predict | Make students commit before evidence | "Sebelum saya geser: A, B, atau C?" | `predict` |
| Notice | Direct attention during exploration | "Apa yang berubah? Apa yang tetap?" | `question` |
| Explain | Ask for the reason, not the result | "Mengapa?" "Bagian mana yang menjelaskan itu?" | `question` |
| Test | Probe the edge of an idea | "Apa yang terjadi bila syarat kontinu dibuang?" "Benarkah cara Dani?" | `pitfall` / `question` |
| Look back | Check and generalise | "Bagaimana kalian yakin jawaban ini masuk akal?" "Kapan cara ini gagal?" | `reflect` / `question` |

## 2. Weak vs. strong

| Weak | Why it fails | Stronger |
|------|--------------|----------|
| "Apa definisi turunan?" | Recall of something not yet taught | "Selang mana yang memberi kecepatan lebih dekat ke 'tepat di $t=1$'? Mengapa?" |
| "Apakah limitnya ada?" | Yes/no, 50% by guessing | "Dari kiri nilainya mendekati berapa? Dari kanan? Apa artinya bagi limitnya?" |
| "Jadi luasnya adalah…?" | Fill in the lecturer's sentence | "Hampiran dengan 4 persegi panjang terlalu besar atau terlalu kecil? Bagaimana kalian tahu tanpa menghitung?" |
| "Ada pertanyaan?" | Invites silence | "Tulis satu langkah yang paling mungkin kalian salah. Bandingkan dengan teman." |
| "Mengapa kita pakai aturan rantai?" | Guess what the lecturer is thinking | "Fungsi ini 'fungsi di dalam fungsi'. Mana yang luar, mana yang dalam?" |

A quick test for any question: could a student who is following along say something sensible
within the wait time? If only a student who already knows the topic could, make it smaller. If
every student would say the same one word, make it ask for a reason.

## 3. Question chains (guided discovery)

A discovery slide is three or four questions where each answer is the input to the next and the
last answer is the result you wanted to teach.

- Each step is one move: write an expression, simplify it, read off a pattern, state it.
- The lecturer's summary block is titled as the class's conclusion ("Kesimpulan Kelas"), because
  by then it is theirs.
- If a step needs more than about a minute of work, give it a "Kerjakan di kertas" mode.
- Do not ask a question whose answer is already visible higher on the slide.

Pattern: concrete numbers → general expression → simplify → interpret.

## 4. Response modes

Put one in the `mode` chip so the whole room responds, not only the front row.

- `Pikir 30 dtk`: silent individual thinking; then cold-call or volunteers.
- `Diskusi berpasangan · 1 mnt`: think-pair-share. Best for explain and test questions.
- `Angkat jari: A / B / C`: instant poll for predictions (1, 2, 3 fingers). Count aloud.
- `Kerjakan di kertas · 2 mnt`: for anything needing algebra.
- `Tunjuk di papan`: matching parts of a formula to a picture.

Rough time cost: a poll is 1 minute, a pair discussion 2 to 3, paper work 3 to 5. Add these up when
planning; a 50-minute lecture holds about 10 to 14 such moments.

## 5. The hint ladder

Three rungs, each revealed only if the room is stuck, with at least a minute between them.

1. **Reorient** to the problem: what is asked, what is given, which definition or theorem is in
   play. "Besaran apa yang diminta, dan definisi mana yang menghitungnya?"
2. **Strategy**: name the tool, not its execution. "Teknik aljabar apa yang menghilangkan akar di
   pembilang?"
3. **First move**: give the opening step and stop. "Kalikan dengan sekawannya, lalu sederhanakan."

Rungs 1 and 2 should themselves be questions. No rung states the answer. After the ladder, show
the final answer with a look-back question, so students who finished can check and students who
did not still have work to do.

## 6. Presenter notes

The note is the lecturer's script for the part the slide cannot do. Keep it short and specific to
this question:

- **Tanya**: how to pose it and how long to wait.
- **Jawaban diharapkan**: what a good answer sounds like in a student's words.
- **Jika ada yang menjawab "…"**: the most likely wrong answer, and a counter-question that lets
  the student find the flaw (a test value, a picture, a unit check). Not "itu salah".
- **Jika hening**: a smaller question that opens the way.
- When to click, when to touch the applet, and what not to say yet.

## 7. Misconception bank by MA1101 topic

Use these for `predict` distractors and `pitfall` slides. Attribute the error to a fictional
student (Dani, Sari, Budi) so no one in the room owns it.

**Limits and continuity**
- "The limit is the value at the point", so an undefined point has no limit.
- "$\frac{0}{0}$ equals 0 (or 1)."
- A limit is "never reached".
- Continuity means "can be drawn" with no reference to the three conditions.

**Derivative concept and rules**
- The tangent line "touches at exactly one point" (fails for $y = x^3$ at 0, or a line).
- $(1+h)^2 = 1 + h^2$; $\sqrt{a+b} = \sqrt a + \sqrt b$.
- $(fg)' = f'g'$; $\left(\frac{f}{g}\right)' = \frac{f'}{g'}$.
- Chain rule: forgetting the inner derivative; $\frac{d}{dx}\sin(x^2) = \cos(x^2)$.
- Differentiable implies "smooth graph" but the converse of "differentiable ⇒ continuous" assumed.

**Implicit differentiation and related rates**
- Treating $y$ as a constant; forgetting $\frac{dy}{dx}$ on $y^2$.
- Substituting the instant's values before differentiating.

**Extrema, monotonicity, concavity, curve sketching**
- "$f'(c) = 0$ means an extremum" ($x^3$ at 0).
- "$f''(c) = 0$ means an inflection point" ($x^4$ at 0).
- The maximum on a closed interval is always at a critical point (forgetting endpoints).
- Increasing means $f > 0$.

**Mean Value Theorem**
- Applying it without checking continuity/differentiability ($|x|$ on $[-1,1]$).
- Reading $c$ as the midpoint.

**Antiderivatives and differential equations**
- Dropping $+C$; one antiderivative is "the" antiderivative.
- $\int f g = \int f \cdot \int g$.

**Definite integral, Riemann sums, FTC**
- The integral "is the area" (ignoring sign).
- More rectangles always overestimate / always underestimate.
- FTC 1: $\frac{d}{dx}\int_a^{x^2} f(t)\,dt = f(x^2)$ (missing chain rule).
- FTC 2 applied across a discontinuity: $\int_{-1}^{1}\frac{1}{x^2}dx = -2$.
- Substitution without changing the limits.

**Area and volume**
- Area between curves as $\int (f - g)$ without checking which is on top.
- Washer: $\pi\int (R - r)^2$ instead of $\pi\int (R^2 - r^2)$.
- Wrong radius when the axis is not a coordinate axis ($x = -1$, $y = 3$).
- Disk vs. shell: slicing parallel to the axis and still using $\pi r^2$.
