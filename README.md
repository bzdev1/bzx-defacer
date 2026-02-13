🚀 BzxDefacer - Mass Defacer Auto Proxy 🚀

```python
# Property of bzdev1 | Jangan sok kuasa ya kontol
```

https://img.shields.io/badge/version-4.0--DEWA%2B-red
https://img.shields.io/badge/platform-Linux%20|%20Termux%20|%20VPS-blue
https://img.shields.io/badge/status-Stable--AF-green

```
╔══════════════════════════════════════════════════════════╗
║    ██████╗ ███████╗██╗  ██╗ █████╗  ██████╗███████╗     ║
║    ██╔══██╗╚══███╔╝██║  ██║██╔══██╗██╔════╝██╔════╝     ║
║    ██████╔╝  ███╔╝ ███████║███████║██║     █████╗       ║
║    ██╔══██╗ ███╔╝  ██╔══██║██╔══██║██║     ██╔══╝       ║
║    ██████╔╝███████╗██║  ██║██║  ██║╚██████╗███████╗     ║
║    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝     ║
║                                                          ║
║         MASS DEFACER | AUTO PROXY | CUSTOM HTML         ║
║         Bzx™ Evolution | DEWA SPEK PREMIUM | v4.0       ║
╚══════════════════════════════════════════════════════════╝
```

---

⚡ TENTANG TOOL INI

BzxDefacer adalah tool mass defacer premium dengan fitur auto proxy dan custom HTML.
Tool ini dirancang untuk penetration testing dan educational purpose dengan kecepatan maksimal.

🔥 FITUR UTAMA:

· ✅ AUTO PROXY - Fetch + test proxy otomatis dari 8+ sumber
· ✅ MULTI-THREADING - Sampai 100 thread parallel
· ✅ CUSTOM HTML - Tempel HTML langsung di terminal
· ✅ TEMPLATE DEFACE - 5 template siap pakai
· ✅ AUTO REFRESH PROXY - Otomatis cari proxy baru kalau habis
· ✅ SCAN VULN - Deteksi kerentanan sebelum deface
· ✅ 7 METHODS EXPLOIT - Upload form, API, webshell, SQL, LFI, XSS, path traversal
· ✅ PROXY MANAGER - Lihat status, test, simpan proxy
· ✅ LOG SYSTEM - Semua hasil tersimpan rapi

---

⚠️ DISCLAIMER PENTING - BACA ATAU MATI

```diff
- [!] TOOL INI HANYA UNTUK TUJUAN PENDIDIKAN DAN PENETRATION TESTING!
- [!] HACKING WEBSITE ORANG TANPA IZIN = PIDANA (UU ITE)!
- [!] GUNANYA CUMA DI SERVER SENDIRI / LAB / YANG LO PUNYA AKSES!
- [!] DEVELOPER TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN!
- [!] KALO LO MAEN HACK SEMBARANGAN, SIAP-SIAP TAMU PAKAI SERAGAM ORANYE!
- [!] LO UDAH DIKASIH TAU. JANGAN NANGIS KALAU KENA BATU!
```

Dengan menggunakan tool ini, lu dianggap udah baca, paham, dan siap masuk penjara kau kontol.

---

📦 INSTALASI

✅ Persyaratan Sistem

· Python 3.8+
· Pip
· Koneksi internet stabil
· Otak (wajib)

📥 Install Dependencies

```bash
# Clone repo dulu
git clone https://github.com/bzdev1/deface-bzx.git
cd deface-bzx

# Install dependencies
pip install -r requirements.txt
```

Isi requirements.txt:

```txt
requests>=2.28.0
fake-useragent>=1.4.0
colorama>=0.4.6
pyfiglet>=0.8.post1
```

🐧 Linux / Ubuntu / Debian

```bash
# Langsung jalanin
python3 bzxdefacer.py
```

📱 Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/bzdev1/deface-bzx.git
cd deface-bzx
pip install -r requirements.txt
python bzxdefacer.py
```

🖥️ VPS / Cloud Server

```bash
# SSH ke VPS
apt update && apt upgrade -y
apt install python3 python3-pip git -y
git clone https://github.com/bzdev1/deface-bzx.git
cd deface-bzx
pip3 install -r requirements.txt
python3 bzxdefacer.py

# Buat running di background
screen -S bzx
python3 bzxdefacer.py
# Ctrl+A+D buat detach
```

---

🚀 CARPAKAI (CARA PAKAI)

1️⃣ Jalankan Tool

```bash
python3 bzxdefacer.py
```

2️⃣ Menu Utama

```
┌─────────────────────────────────────────────────────┐
│                     MENU UTAMA                      │
├─────────────────────────────────────────────────────┤
│  1. Load Target List                                 │
│  2. AUTO PROXY - Fetch & Test                        │
│  3. Manual Load Proxy File                           │
│  4. Custom HTML Deface                               │
│  5. Pilih Template Deface                            │
│  6. Setting (Thread/Delay/Proxy Mode)                │
│  7. Scan Kerentanan Target                           │
│  8. Jalankan Mass Defacer                            │
│  9. Lihat Hasil (Log)                                │
│ 10. Proxy Status & Management                        │
│ 11. Bersihin Cache/Temp                              │
│  0. Exit                                             │
└─────────────────────────────────────────────────────┘
```

3️⃣ Langkah Cepat

```bash
# 1. Siapin file targets.txt
nano targets.txt
# Isi: http://target.com (satu per baris)

# 2. Jalankan tool
python3 bzxdefacer.py

# 3. Pilih menu 2 → 3 (Auto proxy fetch + test)
# 4. Pilih menu 5 → pilih template HTML
# 5. Pilih menu 6 → atur thread (10-50)
# 6. Pilih menu 8 → GASSS!
```

---

🔥 FITUR DETAIL

🧦 AUTO PROXY MANAGER

Tool ini bisa auto cari proxy dari berbagai sumber:

· ✅ ProxyScrape
· ✅ TheSpeedX Proxy List
· ✅ ShiftyTR Proxy List
· ✅ jetkai Proxy List
· ✅ roosterkid OpenProxyList
· ✅ mertguvencli Proxy List
· ✅ sunny9577 Proxy Scraper
· ✅ clarketm Proxy List

Menu Auto Proxy:

```
══════════════════ AUTO PROXY MANAGER ══════════════════
  1. Fetch Proxy dari Internet
  2. Test Semua Proxy
  3. Fetch + Test Sekaligus
  4. Simpan ke File
  5. Load ke Memory (Aktifkan)
  6. Hapus Semua Proxy
  7. Lihat Daftar Proxy
  0. Kembali
═══════════════════════════════════════════════════════
```

🎨 TEMPLATE DEFACE

5 template keren siap pakai:

1. HACKED BASIC - Hitam merah klasik
2. ANONYMOUS STYLE - Hijau matrix ala Anonymous
3. MATRIX THEME - Glitch effect keren
4. PROTEST PAGE - Buat deface protes
5. SKULL & BONES - Tengkorak ASCII art

⚙️ PENGATURAN LENGKAP

· Thread count - 1-100 thread
· Delay - Anti rate limit
· Timeout - Biar gak nunggu lama
· Mode serangan - normal/aggressive/stealth
· Custom Headers - Bypass WAF
· Auto Refresh Proxy - Otomatis cari proxy baru
· Toggle Proxy ON/OFF

🔍 7 METHODS EXPLOIT

1. Upload Form - Upload via form upload
2. API Upload - Upload via REST API
3. Webshell - Pakai shell existing
4. SQL Injection - INTO OUTFILE technique
5. Path Traversal - Directory traversal
6. LFI Injection - Local File Inclusion
7. XSS Injection - JavaScript injection

---

📂 STRUKTUR FILE

```
deface-bzx/
├── bzxdefacer.py            # Main tool
├── requirements.txt          # Dependencies
├── README.md                 # Dokumentasi (ini)
├── targets.txt               # Daftar target (buat manual)
├── proxies.txt               # Proxy list (auto generated)
├── defaced.log               # Log hasil deface
├── vulnerable.txt            # Hasil scan vuln
└── custom.html               # HTML custom (opsional)
```

---

🧠 TIPS & TRIK

Tips Keterangan
🚀 Thread 20-30 Paling optimal buat serangan
⏱️ Delay 2-5 detik Hindari rate limit
🧦 Proxy WAJIB Biar IP lo gak kena banned
🔄 Auto Refresh ON Biar proxy gak habis
📁 Targets minimal 50 Biar dapet hasil maksimal
🛡️ Mode stealth Buat serangan pelan tapi aman
🧹 Clean cache Bersihin log lama

---

🧪 TESTING DI LOCAL

Buat web vuln buat testing:

```bash
# Pake Docker
docker pull vulnerables/web-dvwa
docker run -d -p 80:80 vulnerables/web-dvwa

# Atau pake XAMPP terus bikin file upload.php
```

Contoh targets.txt buat testing:

```
http://localhost
http://localhost:8080
http://testsite.com
```

---

🐞 KNOWN ISSUES

Issue Solusi
Proxy mati semua Auto refresh akan cari baru
Kena rate limit Naikin delay, turunin thread
Upload gagal terus Coba mode aggressive atau ganti proxy
SSL error Tool udah pake verify=False
Memory full Kurangi thread, bersihin cache

---

📊 HASIL TEST

Tested on:

· ✅ Kali Linux 2024 (100 thread, 500 target)
· ✅ Ubuntu 22.04 VPS (50 thread, 1000 target)
· ✅ Termux Android 13 (20 thread, 200 target)
· ✅ Windows 11 + WSL2 (30 thread, 300 target)

Rata-rata sukses: 15-30% dari total target (tergantung proxy)

---

🔐 BYPASS WAF?

Tool ini support custom headers buat bypass WAF.
Contoh header yang bisa ditambah:

```
X-Forwarded-For: 127.0.0.1
User-Agent: Googlebot
Referer: https://google.com
```

---

🗿 CREATOR

```
Author   : bzdev1 / Bzx
Channel  : [REDACTED]
Telegram : [REDACTED]
GitHub   : https://github.com/bzdev1
```

Dibuat dengan ☕, 🍺, dan amarah.

---

📜 LICENSE

MIT License
Tapi inget disclaimer di atas.
Gunakan untuk kebaikan. Atau setidaknya jangan ketahuan.
Jangan jadi bego.

---

⭐ SUPPORT

Kalau tools ini berguna:

· ⭐ Star repo ini
· 🍴 Fork kalau mau mod
· 💀 Jangan lupa jadi hacker yang bijak
· 🗿 Sembahyang biar gak masuk bui

---

💬 TESTIMONIAL

"Gila, auto proxynya mantap! Gw tinggal tidur, dia nyari proxy sendiri."
— Anonymous User

"Udah 1000 site kena, sampe sekarang VPS gw aman."
— Some Indonesian Kid

"Thanks to Bzx, gw jadi tau betapa rentannya website pemerintah."
— Fed

---

🗿 CLOSING WORDS

"Hacking is not about being evil. It's about knowing how things work,
and sometimes, showing people how broken their shit is."
— Bzx, 2026

Sekarang lu punya senjata. Pake dengan bijak, atau siap-siap tamu pakai seragam batik. 😁🔥💀

---

🔄 UPDATE TERBARU v4.0

· ✅ Nama berubah jadi BzxDefacer
· ✅ Auto proxy makin stabil
· ✅ Bug fixing upload methods
· ✅ Performance improvement
· ✅ Memory management lebih baik