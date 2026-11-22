Ini agenda untuk pertemuan 28 (6.5 Pertumbuhan dan Peluruhan Eksponensial). Simpan sebagai `agenda.toml` di folder deck baru, lalu buatkan deck-nya.

```toml
meeting = 28
slot_minutes = 100
buffer_minutes = 5
template = "one-subchapter"

[[subchapter]]
code = "6.5"
title = "Pertumbuhan dan Peluruhan Eksponensial"
purcell = "§6.5"
goal = "Menyusun dan menyelesaikan y' = ky dari cerita, lalu menafsirkan k."
big_question = "Kapan sesuatu bertambah dengan laju yang sebanding dengan banyaknya sendiri?"
misconceptions = ["pertumbuhan eksponensial dikira linear"]

[[segment]]
name = "Pertanyaan besar"
stage = 1
minutes = 5
mode = "Pikir 30 dtk"
subchapter = "6.5"

[[segment]]
name = "Tebak: bakteri dua kali lipat tiap jam"
stage = 3
minutes = 12
mode = "Angkat jari: A / B / C"
subchapter = "6.5"
targets = ["pertumbuhan eksponensial dikira linear"]

[[segment]]
name = "Temukan bersama: y' = ky"
stage = 4
minutes = 15
mode = "Diskusi berpasangan · 1 mnt"
subchapter = "6.5"

[[segment]]
name = "Contoh terpandu: waktu paruh karbon-14"
stage = 7
minutes = 14
mode = "Pikir 30 dtk"
subchapter = "6.5"

[[segment]]
name = "Contoh setengah jadi"
stage = 8
minutes = 10
mode = "Kerjakan di kertas · 2 mnt"
subchapter = "6.5"
cut = true

[[segment]]
name = "Latihan berpasangan 1: peluruhan obat"
stage = 9
minutes = 13
mode = "Kerjakan di kertas · 4 mnt"
subchapter = "6.5"

[[segment]]
name = "Latihan berpasangan 2: bunga majemuk kontinu"
stage = 9
minutes = 13
mode = "Kerjakan di kertas · 4 mnt"
subchapter = "6.5"
cut = true

[[segment]]
name = "Tiket keluar"
stage = 10
minutes = 6
mode = "Tulis · 3 mnt"
subchapter = "6.5"

[exit_ticket]
goal = "6.5"
prompt = "Populasi naik 10% per tahun. Tulis y(t) dan kapan populasinya dua kali lipat."
bridge = "Bagaimana kalau ada batas daya tampung?"
```
