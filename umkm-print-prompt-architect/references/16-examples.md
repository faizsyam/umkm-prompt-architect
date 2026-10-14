# 16. Examples (illustrations of method; never reuse wording)

These show *how decisions diverge* and *how the flow feels*. They are not templates. If two requests produce alike sheets, the second is wrong: revise it.

---

## A. Divergence examples (concept sheets only)
| | Kedai kopi menu A3 | Laundry kiloan banner 4×1 m | Toko batik signboard | Gorengan street banner |
|---|---|---|---|---|
| Mood | calm, neighbourly | fast, clean, trustworthy | premium, rooted | cheeky, loud, youthful |
| Design idea | the quiet morning counter | a clean, folded order | cloth unrolling across the sign | crispy abundance mid-toss |
| Register | calm / warm, spacious | friendly / contemporary | dignified, spacious | exuberant / street, abundant |
| Palette | tonal light, earth + green | bright field, clear blue + fresh accent | deep indigo, muted gold, off-white | bold two-tone, chili + sun, cream |
| Connector | counter-top line + faint ripples | folded-band stripes | rolled-cloth band | oversized cropped hero + overlap |
| Heritage | none | none | named batik family as structural band | none; stamp/halftone texture |
| Layout | banded + grid | centered axis | left-anchored two-zone | diagonal split / hero-led bleed |
| Mark | stacked wordmark + small icon | rounded sign panel | signwriter cartouche | chunky outlined lettering + offset shadow |
| Illustration | thin-line flat | simplified flat shapes | fine textile linework | cut-paper / sticker contour |
| Type | high-contrast serif + light sans | geometric sans + rounded display | refined serif + restrained script | condensed gothic + chunky display |
| Icons | thin monoline in rounded squares | filled rounded glyphs, same blue | fine-line glyphs in gold | chunky sticker-contour glyphs |

## B. Interview feel (compact; owner's language)
> **Owner:** buatkan spanduk sama menu untuk kedai kopi saya, namanya Kopi Senja.
>
> **Claude:** Siap! Tiga hal dulu ya:
> 1. Jual apa saja, andalannya apa?
> 2. Pelanggan utamanya siapa dan datang kapan?
> 3. Sekitar kedai ada apa, dan kedai terdekat seperti apa tampilannya?
>
> **Owner:** es kopi susu gula aren, mahasiswa, sore-malam. Dekat kampus, banyak kedai lain.
>
> **Claude:** Pesaingnya ramai. Kenapa mahasiswa tetap pilih Kopi Senja: rasa gula arennya, harga, tempat nugas, atau cerita?
>
> **Owner:** gula aren masak sendiri, buka sampai tengah malam.
>
> **Claude:** Jadi pembedanya **gula aren masak sendiri + teman nugas sampai tengah malam**, betul? Lanjut: mau dibuat apa saja (ukuran), teks persis yang dicetak, dan ada logo?

(Notes: small batches, hypothesis as a question, nothing concluded early, no style questions yet.)

## C. Recap sample (compressed)
```
Ringkasan (mohon dicek):
1. Kopi Senja: kedai kopi, andalan es kopi susu gula aren, mahasiswa, dine-in & takeaway
2. Dekat kampus, banyak pesaing; dilihat dari jalan ±10 m
3. Pembeda: gula aren masak sendiri; buka sampai tengah malam (teman nugas)
4. Aset: logo (dipakai apa adanya)
5. Dibuat: spanduk 3×1 m (pengenalan) · menu A4 (informasi)
6. Teks persis: [..]
7. Ikon: WhatsApp 08xx · Instagram @kopisenja · lokasi: Jl. ...
8. Hindari: kesan mahal/dingin
✔ Pasti: .. ? Asumsi: .. ✚ Saran: tambah jam buka (ikon jam) di menu
Sudah sesuai? Balas "lanjut" atau koreksi.
```

## D. Direction selection samples (one dimension per request)
**D1 Mood**
> Untuk Kopi Senja yang dekat kampus, kesan pertama yang paling pas:
> A. **Hangat & akrab**: seperti sore di teras, ramah dan tenang
> B. **Muda & kekinian**: berani, rapi, enak di-foto dan dibagikan
> C. **Nostalgia kedai lama**: jadul, hangat, terasa legendaris
> Rekomendasi: **B**, karena pelanggan mahasiswa dan pesaing banyak. Pilih satu, campur (mis. A+B), atau "terserah".

**D2 Style** (after D1 = B)
> A. **Poster Kampus**: blok warna tegas, huruf tebal, gambar gelas besar terpotong
> B. **Papan Kedai Modern**: bersih, huruf geometris, banyak ruang kosong, aksen satu warna
> C. **Senja Ilustrasi**: ilustrasi langit senja datar berlapis, mood tenang tapi segar
> Rekomendasi: **A**, paling menonjol di antara kedai sekitar. …

**D3 Palette** (after D2 = A)
> A. **Senja Jingga**: jingga terbakar, ungu tua, krem, aksen kuning (hangat, berani)
> B. **Kopi & Susu**: cokelat espresso, krem susu, hijau sage (kalem, rapi)
> C. **Malam Kampus**: biru malam, kuning lampu, putih (menyala di malam hari)
> Rekomendasi: **A** …

**D4 Elements** (multi-select)
> ☐ Maskot gelas kecil ☐ Gambar gelas besar (ilustrasi) ☐ Motif daerah ☐ Badge harga ☐ Kotak QR kosong ☐ Tanpa ornamen tambahan
> Rekomendasi: gambar gelas besar + kotak QR kosong.

## E. Fragment: attachments and icons in a prompt (structure only)
```
**Attached references:**
- Image 1 is the business's logo. Use it unchanged as the brand mark ...

**Info block:** one aligned strip along the lower edge, three icon-value pairs left to right: a chat-bubble-with-handset glyph + "0812-xxxx-xxxx", a rounded-square-with-lens glyph + "@namausaha", a map-pin glyph + "Jl. ...". Icons share the contour weight and corner language of the illustrations, one consistent size ≈1.2× text cap height, before their values on a shared baseline. No label words.
```
