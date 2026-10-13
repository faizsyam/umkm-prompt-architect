# Asisten Desain Cetak UMKM

Skill untuk Claude yang membantu pemilik usaha kecil (warung, kedai, toko, jasa, usaha rumahan) membuat **prompt gambar** untuk desain cetak: spanduk, banner, menu, daftar harga, poster, flyer, brosur, stiker, kemasan, kartu nama, dan lain-lain.

Skill ini **tidak langsung membuat prompt**. Claude akan bertanya dulu seperti konsultan, supaya desainnya benar-benar cocok dengan usaha Anda dan tidak mirip punya orang lain.

---

## Cara pakai (3 langkah)

### 1. Pasang skill ke Claude
1. Buka Claude (claude.ai atau aplikasinya).
2. Masuk ke **Pengaturan (Settings)** lalu menu **Kemampuan / Capabilities** atau **Skills**. Nama menu bisa sedikit berbeda.
3. Pilih **Upload skill**, lalu pilih file **`umkm-print-prompt-architect.skill`**.
4. Nyalakan (aktifkan) skill-nya.

Cukup sekali. Setelah itu skill siap dipakai di percakapan mana pun.

### 2. Minta desain, lalu jawab pertanyaan Claude
Ketik permintaan sederhana, misalnya:
- "Buatkan spanduk untuk warung bakso saya"
- "Saya butuh menu dan banner untuk kedai kopi"
- "Bikin desain stiker untuk usaha kue rumahan"

Claude akan bertanya beberapa hal, sedikit demi sedikit:
- Usaha Anda jual apa dan untuk siapa
- **Apa yang membuat usaha Anda beda** dari yang lain
- Mau dibuat apa saja (boleh lebih dari satu) dan ukurannya
- Tulisan apa yang harus tercetak (nama, menu, harga, nomor WA, Instagram, alamat)
- Kesan yang diinginkan (hangat, ramai, mewah, bersih, dll.)
- Punya logo atau contoh desain atau tidak

**Tidak tahu jawabannya? Tidak apa-apa.** Katakan saja "bingung" atau "terserah". Claude akan memberi pilihan dan saran. Sebelum mulai mendesain, Claude akan merangkum jawaban Anda. Cek dulu, lalu balas **"lanjut"** kalau sudah benar.

### 3. Salin prompt ke generator gambar
- Claude memberi **satu prompt untuk setiap jenis cetakan** (misalnya satu untuk spanduk, satu untuk menu).
- Salin prompt, tempel ke generator gambar AI yang Anda pakai.
- Kalau ada tulisan **"Lampirkan: ..."**, unggah file gambar yang disebutkan (misalnya logo) ke generator gambar bersama prompt itu.
- Setiap prompt bisa dipakai sendiri-sendiri.

---

## Siapkan sebelum mulai (supaya cepat)
- Nama usaha, persis seperti ingin dicetak
- Produk atau layanan andalan, dan alasan pelanggan memilih Anda
- Teks yang mau dicetak: menu, harga, nomor WhatsApp, Instagram, alamat, jam buka
- File logo (kalau ada), foto produk, atau desain lama
- Ukuran cetak (kalau belum tahu, Claude akan menyarankan)

---

## Tips supaya hasil bagus
- **Ceritakan hal yang spesifik.** "Gula aren dimasak sendiri" lebih berguna daripada "enak dan murah".
- **Unggah logo dan foto produk.** Claude akan memakainya di prompt dan menyebutkan file mana yang harus dilampirkan.
- **Sebutkan apa yang tidak Anda suka.** Itu membantu menghindari gaya yang salah.
- **Banyak jenis cetakan?** Bilang sekaligus. Desainnya dibuat senada, tapi tata letak disesuaikan untuk tiap jenis.

## Pertanyaan umum
**Nomor WA dan Instagram akan tampil sebagai apa?** Sebagai ikon kecil (WhatsApp, Instagram, pin lokasi, jam) diikuti isinya, bukan tulisan "WA" atau "Alamat".

**Tulisan di hasil gambar ada yang salah huruf.** Itu hal umum pada generator gambar, terutama tulisan kecil. Perbaiki di aplikasi edit (misalnya Canva), atau minta Claude membuat versi dengan tulisan lebih sedikit.

**Kode QR, logo halal, atau nomor PIRT bagaimana?** Generator gambar tidak bisa membuat kode QR yang bisa dipindai. Lampirkan gambar aslinya, atau Claude menyediakan kotak kosong untuk Anda tempel sendiri nanti. Logo atau sertifikat resmi tidak pernah dibuat-buat.

**Hasilnya kurang pas.** Ceritakan apa yang kurang ("terlalu ramai", "warnanya mirip toko sebelah"). Claude akan memperbaiki bagian yang tepat dan memberi prompt baru.

**Untuk ukuran cetak asli, bagaimana?** Generator gambar punya pilihan rasio terbatas. Sampaikan ukuran asli ke percetakan, dan minta mereka menyesuaikan atau memperluas latar bila perlu.

---

## Isi paket (untuk yang ingin tahu)

```
umkm-print-prompt-architect/
├── SKILL.md                      alur kerja utama dan aturan
└── references/                   panduan per tahap (dibaca Claude sesuai urutan)
    ├── 01-interview-protocol.md          wawancara ala konsultan
    ├── 02-industry-playbooks.md          panduan per jenis usaha
    ├── 03-print-types.md                 isi, struktur, ukuran tiap jenis cetakan
    ├── 04-strategy-and-concept.md        strategi dan ide desain
    ├── 05-design-principles.md           prinsip desain
    ├── 06-style-library.md               pustaka gaya dan budaya lokal
    ├── 07-color-system.md                warna
    ├── 08-typography.md                  tipografi
    ├── 09-layout-and-unity.md            tata letak dan keterpaduan
    ├── 10-brand-mark.md                  logo dan penulisan nama usaha
    ├── 11-content-icons-illustration.md  isi, ikon, ilustrasi, dekorasi
    ├── 12-concept-audit.md               pemeriksaan sebelum menulis prompt
    ├── 13-prompt-writing.md              cara menulis prompt
    ├── 14-delivery-and-qa.md             pengecekan akhir dan revisi
    └── 15-examples.md                    contoh
```

### Membuat ulang file .skill (opsional, untuk pengembang)
Butuh Python 3.8 atau lebih baru, tanpa pustaka tambahan:

```
python build_skill.py
```

Hasilnya ada di `dist/umkm-print-prompt-architect.skill`. Skrip memeriksa isi skill dulu (nama, deskripsi, tautan antar file) sebelum membuat paketnya.
