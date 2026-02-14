# 🔥 BZXDEFACER - Mass Defacer Auto Proxy 🔥

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
║         Bzx™ Evolution | DEWA SPEK PREMIUM | v4.1       ║
╚══════════════════════════════════════════════════════════╝

```

## 📋 DAFTAR ISI
- [TENTANG TOOL](#tentang-tool)
- [FITUR UTAMA](#fitur-utama)
- [DISCLAIMER PENTING](#disclaimer-penting)
- [INSTALASI](#instalasi)
  - [Linux/Ubuntu/Debian](#linuxubuntudebian)
  - [Termux (Android)](#termux-android)
  - [VPS/Cloud Server](#vpscloud-server)
  - [Windows (WSL)](#windows-wsl)
- [CARPAKAI (CARA PAKAI)](#carpakai-cara-pakai)
  - [Menu Utama](#menu-utama)
  - [Langkah Cepat](#langkah-cepat)
- [FITUR DETAIL](#fitur-detail)
  - [1. AUTO PROXY MANAGER](#1-auto-proxy-manager)
  - [2. CUSTOM HTML & TEMPLATE](#2-custom-html--template)
  - [3. INPUT TARGET MANUAL](#3-input-target-manual)
  - [4. SETTINGS LENGKAP](#4-settings-lengkap)
  - [5. SCAN KERENTANAN](#5-scan-kerentanan)
  - [6. 7 METHODS EXPLOIT](#6-7-methods-exploit)
- [STRUKTUR FILE](#struktur-file)
- [DEPENDENCIES](#dependencies)
- [TIPS & TRIK](#tips--trik)
- [TROUBLESHOOTING](#troubleshooting)
- [UPDATE](#update)
- [CREATOR](#creator)
- [LICENSE](#license)

---

## ⚡ TENTANG TOOL

**BzxDefacer** adalah tool mass defacer premium dengan fitur **auto proxy** dan **custom HTML**.  
Tool ini dirancang untuk penetration testing dan educational purpose dengan kecepatan maksimal.

Dibuat untuk memudahkan penetration tester dalam menguji keamanan website dengan metode deface simulation. Dilengkapi auto proxy agar IP lu tetap aman dan tidak terdeteksi.

---

## 🔥 FITUR UTAMA

| No | Fitur | Keterangan |
|----|-------|------------|
| 1 | **AUTO PROXY** | Fetch + test proxy otomatis dari 8+ sumber (ProxyScrape, GitHub, dll) |
| 2 | **MULTI-THREADING** | Sampai 100 thread parallel untuk kecepatan maksimal |
| 3 | **CUSTOM HTML** | Tempel HTML langsung di terminal, preview otomatis |
| 4 | **TEMPLATE DEFACE** | 5 template siap pakai (HACKED, ANONYMOUS, MATRIX, PROTEST, SKULL) |
| 5 | **AUTO REFRESH PROXY** | Otomatis cari proxy baru kalau habis |
| 6 | **SCAN VULN** | Deteksi kerentanan sebelum deface, simpan ke file |
| 7 | **7 METHODS EXPLOIT** | Upload form, API, webshell, SQL, LFI, XSS, path traversal |
| 8 | **INPUT TARGET MANUAL** | Langsung ketik target, gak perlu file (Menu 12) |
| 9 | **PROXY MANAGER** | Lihat status, test, simpan proxy, load ke memory |
| 10 | **LOG SYSTEM** | Semua hasil tersimpan rapi di defaced.log |
| 11 | **CUSTOM HEADERS** | Bypass WAF dengan header custom |
| 12 | **CLEAN CACHE** | Hapus file temporary biar rapi |

---

## ⚠️ DISCLAIMER PENTING

```diff
- [!] TOOL INI HANYA UNTUK TUJUAN PENDIDIKAN DAN PENETRATION TESTING!
- [!] HACKING WEBSITE ORANG TANPA IZIN = PIDANA (UU ITE)!
- [!] GUNANYA CUMA DI SERVER SENDIRI / LAB / YANG LO PUNYA AKSES!
- [!] DEVELOPER TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN!
- [!] KALO LO MAEN HACK SEMBARANGAN, SIAP-SIAP TAMU PAKAI SERAGAM ORANYE!
```

Dengan menggunakan tool ini, lu dianggap udah baca, paham, dan siap masuk penjara. 🗿

---

📦 INSTALASI

✅ Persyaratan Sistem

· Python 3.8+
· Pip
· Koneksi internet stabil
· RAM minimal 512MB
· Otak (wajib)

📥 Install Dependencies

```bash
# Clone repo dulu
git clone https://github.com/bzdev1/defacer-bzx.git
cd defacer-bzx

# Install dependencies
pip install -r requirements.txt
```

🐧 Linux/Ubuntu/Debian

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python & Git
sudo apt install python3 python3-pip git -y

# Clone repo
git clone https://github.com/bzdev1/defacer-bzx.git
cd defacer-bzx

# Install dependencies
pip3 install -r requirements.txt

# Jalankan
python3 bzxdefacer.py
```

📱 Termux (Android)

```bash
# Update termux
pkg update && pkg upgrade -y

# Install packages
pkg install python git -y

# Clone repo
git clone https://github.com/bzdev1/defacer-bzx.git
cd defacer-bzx

# Install dependencies
pip install -r requirements.txt

# Jalankan
python bzxdefacer.py
```

🖥️ VPS/Cloud Server

```bash
# SSH ke VPS
ssh user@vps-ip

# Update system
apt update && apt upgrade -y

# Install Python & Git
apt install python3 python3-pip git -y

# Clone repo
git clone https://github.com/bzdev1/defacer-bzx.git
cd defacer-bzx

# Install dependencies
pip3 install -r requirements.txt

# Jalankan langsung
python3 bzxdefacer.py

# Atau pake screen biar jalan di background
screen -S bzx
python3 bzxdefacer.py
# Ctrl+A+D untuk detach
# screen -r bzx untuk balik lagi
```

🪟 Windows (WSL)

```bash
# Install WSL dulu (cara: wsl --install di PowerShell)
# Buka WSL Ubuntu

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python & Git
sudo apt install python3 python3-pip git -y

# Clone repo
git clone https://github.com/bzdev1/defacer-bzx.git
cd defacer-bzx

# Install dependencies
pip3 install -r requirements.txt

# Jalankan
python3 bzxdefacer.py
```

---

🚀 CARPAKAI (CARA PAKAI)

Menu Utama

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
│ 12. Input Target Manual (Langsung Ketik)             │
│  0. Exit                                             │
└─────────────────────────────────────────────────────┘
Proxy Status: ON (150 live)
Total Target: 50
```

Langkah Cepat

Cara 1: Pake File targets.txt

```bash
# 1. Siapin file targets.txt
nano targets.txt
# Isi: http://target1.com
#      http://target2.com:8080
#      https://target3.com

# 2. Jalankan tool
python3 bzxdefacer.py

# 3. Pilih menu 2 → 3 (Auto proxy fetch + test)
# 4. Pilih menu 5 → pilih template HTML (1-5)
# 5. Pilih menu 6 → atur thread (10-50)
# 6. Pilih menu 1 → load targets.txt
# 7. Pilih menu 8 → GASSS!
```

Cara 2: Input Target Manual (Tanpa File)

```bash
# 1. Jalankan tool
python3 bzxdefacer.py

# 2. Pilih menu 2 → 3 (Auto proxy fetch + test)
# 3. Pilih menu 5 → pilih template HTML
# 4. Pilih menu 12 → input target manual
#    Pilih mode 1: http://a.com, http://b.com, https://c.com
#    Atau mode 2: ketik satu per satu, 'done' selesai
# 5. Pilih menu 8 → GASSS!
```

---

🔥 FITUR DETAIL

1. AUTO PROXY MANAGER

Tool bisa auto cari proxy dari 8+ sumber:

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

Fitur:

· Fetch multi-thread (5 thread parallel)
· Auto extract IP:port pake regex
· Test proxy ke httpbin.org
· Hanya simpan proxy yang hidup
· Auto refresh kalau proxy habis

2. CUSTOM HTML & TEMPLATE

Custom HTML (Menu 4)

· Tempel HTML langsung di terminal
· Ketik 'DONE' di baris baru untuk selesai
· Auto preview 200 karakter pertama
· Bisa simpan ke file custom.html

Template Deface (Menu 5)

5 template siap pakai:

No Nama Tampilan
1 HACKED BASIC Hitam merah klasik
2 ANONYMOUS STYLE Hijau matrix ala Anonymous
3 MATRIX THEME Glitch effect keren
4 PROTEST PAGE Buat deface protes
5 SKULL & BONES Tengkorak ASCII art

3. INPUT TARGET MANUAL (Menu 12)

Mode 1 - Satu Baris:

```
Masukkan target (pisah pake koma):
http://situs1.com, http://situs2.com:8080, https://situs3.com
[✓] 3 target ditambahkan
```

Mode 2 - Satu Per Satu:

```
Target 1: http://site1.com
[✓] Target ditambahkan
Target 2: http://site2.com
[✓] Target ditambahkan
Target 3: done
[✓] Total 2 target ditambahkan
```

4. SETTINGS LENGKAP (Menu 6)

No Setting Range Default
1 Thread count 1-100 10
2 Delay (detik) 0-60 2
3 Timeout (detik) 1-60 10
4 Mode serangan normal/aggressive/stealth aggressive
5 Custom Headers bebas -
6 Auto Refresh Proxy ON/OFF ON
7 Max Proxy Test 50-1000 300
8 Toggle Proxy ON/OFF OFF

5. SCAN KERENTANAN (Menu 7)

· Scan target tanpa deface
· Deteksi path umum yang rentan
· Hasil disimpan di vulnerable.txt
· Multi-thread scanning

Path yang di-scan:

```
/admin/config.php
/wp-admin/admin-ajax.php
/cgi-bin/test.cgi
/shell.php
/upload.php
/.env
/backup.zip
/phpinfo.php
/wp-content/uploads/
/images/
/admin/
```

6. 7 METHODS EXPLOIT

No Method Cara Kerja
1 Upload Form Upload via form upload biasa
2 API Upload Upload via REST API endpoint
3 Webshell Pakai shell existing (c99, r57, dll)
4 SQL Injection INTO OUTFILE technique
5 Path Traversal Directory traversal upload
6 LFI Injection Local File Inclusion
7 XSS Injection JavaScript injection

---

📂 STRUKTUR FILE

```
defacer-bzx/
├── bzxdefacer.py       # Main tool (program utama)
├── requirements.txt    # Dependencies (library yang dibutuhkan)
├── README.md           # Dokumentasi (file ini)
├── LICENSE             # MIT License
├── targets.txt         # Contoh target (opsional, bisa dihapus)
├── proxies.txt         # Auto generated (proxy list)
├── defaced.log         # Auto generated (log hasil deface)
├── vulnerable.txt      # Auto generated (hasil scan vuln)
└── custom.html         # Auto generated (HTML custom, opsional)
```

Keterangan File:

· Wajib manual: targets.txt (bisa ganti pake menu 12)
· Auto generated: proxies.txt, defaced.log, vulnerable.txt, custom.html
· Wajib di repo: bzxdefacer.py, requirements.txt, README.md, LICENSE

---

🔧 DEPENDENCIES

File requirements.txt:

```txt
requests>=2.28.0          # HTTP requests
fake-useragent>=1.4.0     # Rotate User-Agent
colorama>=0.4.6           # Warna di terminal
pyfiglet>=0.8.post1       # Banner ASCII
```

Install:

```bash
pip install -r requirements.txt
```

---

🧠 TIPS & TRIK

Tips Keterangan
🚀 Thread 20-30 Paling optimal buat serangan (coba2 aja)
⏱️ Delay 2-5 detik Hindari rate limit dari server
🧦 Proxy WAJIB Biar IP lo gak kena banned
🔄 Auto Refresh ON Biar proxy gak habis di tengah jalan
📁 Targets minimal 50 Biar dapet hasil maksimal
🛡️ Mode stealth Buat serangan pelan tapi aman (delay gede)
🧹 Clean cache Bersihin log lama sebelum mulai baru
📝 Custom HTML Simpan HTML kesukaan biar gak ngetik ulang
🔍 Scan dulu Scan vuln sebelum deface biar tau sasaran
🎯 Menu 12 Input target manual buat testing dikit

---

❗ TROUBLESHOOTING

Masalah Penyebab Solusi
ModuleNotFoundError Library belum keinstall pip install -r requirements.txt
Proxy mati semua Sumber proxy jelek Coba menu 2 → 3 (fetch ulang)
Kena rate limit Delay terlalu kecil Naikin delay (menu 6 → 2)
Upload gagal terus Target gak vuln Coba mode aggressive (menu 6 → 4)
SSL error Sertifikat expired Tool pake verify=False, aman
Memory full Thread terlalu gede Kurangi thread (menu 6 → 1)
Error File not found File targets.txt gak ada Pake menu 12 atau bikin file
Git push error Token salah Bikin token baru di GitHub

---

🔄 UPDATE

Cara Update Tool ke Versi Terbaru:

```bash
cd ~/defacer-bzx
git pull origin main
pip install -r requirements.txt --upgrade
```

Cek Versi:

```bash
grep "v4." bzxdefacer.py | head -1
```

---

🗿 CREATOR

```
Author  : bzdev1 / Bzx
GitHub  : https://github.com/bzdev1
Repo    : https://github.com/bzdev1/defacer-bzx
Contact : [REDACTED]
```

Dibuat dengan ☕, 🍺, dan amarah.

---

📜 LICENSE

MIT License - Bebas dimodifikasi dan didistribusikan, tapi tetap ingat disclaimer di atas.

---

⭐ SUPPORT

Kalau tools ini berguna:

· ⭐ Star repo ini di GitHub
· 🍴 Fork kalau mau modifikasi
· 🐛 Report issue kalau nemu bug
· 💀 Jangan lupa jadi hacker yang bijak
· 🗿 Sembahyang biar gak masuk bui

---

💬 TESTIMONIAL

"Auto proxynya mantap! Gw tinggal tidur, dia nyari proxy sendiri."
— Anonymous User

"Udah 1000 site kena, sampe sekarang VPS gw aman."
— Some Indonesian Kid

"Menu 12 bikin gampang, gak perlu bikin file targets.txt lagi."
— Bx User

---

🗿 CLOSING WORDS

"Hacking is not about being evil. It's about knowing how things work,
and sometimes, showing people how broken their security is."
— Bzx, 2026

Sekarang lu punya senjata lengkap. Pake dengan bijak, atau siap-siap tamu pakai seragam batik. 😁🔥💀

---

```
╔══════════════════════════════════════════════════════════╗
║  © 2026 bzdev1 - BzxDefacer v4.1 - Dewa Spek Premium    ║
║  "Hanya untuk pendidikan, jangan jadi bego"              ║
╚══════════════════════════════════════════════════════════╝
```

