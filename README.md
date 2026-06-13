# BMTTNC - Bảo Mật Thông Tin Nâng Cao

**MSSV:** 2280602023  
**Sinh viên:** Nguyễn Thành Nam  
**Trường:** HUTECH

---

## 📂 Cấu trúc thư mục

```
bmttnc-hutech-2280602023/
├── lab_01/          # Bài 1: Ôn tập Python cơ bản
│   ├── hello.py
│   ├── ex02_01.py → ex02_10.py
│   ├── ex03/        # List, Tuple, Dictionary
│   └── ex04/        # OOP - Quản lý sinh viên
├── lab_02/          # Bài 2: Mã hóa cổ điển + Flask API
│   ├── cipher/      # Caesar, Vigenere, RailFence, Playfair, Transposition
│   ├── api.py       # Flask REST API
│   └── app.py       # Web UI
├── lab_03/          # Bài 3: RSA, ECC + PyQt5 GUI
│   ├── cipher/      # RSA, ECC cipher
│   ├── api.py       # Flask API
│   └── ui/          # PyQt5 Desktop UI
├── lab_04/          # Bài 4: Socket, Hash, Key Exchange
│   ├── aes_rsa_socket/  # AES + RSA qua Socket
│   ├── dh_key_pair/     # Diffie-Hellman Key Exchange
│   ├── hash/            # MD5, SHA-256, SHA-3, BLAKE2
│   └── websocket/       # WebSocket Client/Server
└── lab_05/          # Bài 5: Ứng dụng bảo mật
    ├── base64/      # Mã hóa/Giải mã Base64
    ├── ssl/         # SSL Client/Server
    ├── blockchain/  # Mô phỏng Blockchain
    └── img-hidden/  # Steganography (giấu tin trong ảnh)
```

---

## ⚙️ Cài đặt

```bash
# Clone repo
git clone https://github.com/ngthnam24/bmttnc-hutech-2280602023.git
cd bmttnc-hutech-2280602023

# Cài đặt thư viện
pip install flask cryptography pyqt5 Pillow websockets pycryptodome
```

---

## 🚀 Cách chạy từng Lab

### Lab 01 - Python cơ bản

```bash
# Hello World
python lab_01/hello.py

# Bài tập biến, vòng lặp, hàm (ex02)
python lab_01/ex02_01.py    # Nhập tên, tuổi
python lab_01/ex02_02.py    # Diện tích hình tròn
python lab_01/ex02_03.py    # Kiểm tra chẵn/lẻ
python lab_01/ex02_04.py    # Số 2000-3200 chia hết 7, không bội 5
python lab_01/ex02_05.py    # Tính lương nhân viên
python lab_01/ex02_06.py    # Mảng 2 chiều
python lab_01/ex02_07.py    # Chuỗi chữ hoa/chữ thường
python lab_01/ex02_08.py    # Nhị phân chia hết cho 5
python lab_01/ex02_09.py    # Kiểm tra số nguyên tố
python lab_01/ex02_10.py    # Đảo ngược chuỗi

# Bài tập List, Tuple, Dictionary (ex03)
python lab_01/ex03/ex03_01.py   # Tổng số chẵn trong List
python lab_01/ex03/ex03_02.py   # Đảo ngược List
python lab_01/ex03/ex03_03.py   # Chuyển List → Tuple
python lab_01/ex03/ex03_04.py   # Phần tử đầu/cuối Tuple
python lab_01/ex03/ex03_05.py   # Đếm số lần xuất hiện
python lab_01/ex03/ex03_06.py   # Xóa phần tử Dictionary

# Bài tập OOP (ex04)
python lab_01/ex04/Main.py      # Quản lý sinh viên CRUD
```

---

### Lab 02 - Mã hóa cổ điển (Flask API)

```bash
# Cài thư viện
pip install -r lab_02/requirements.txt

# Chạy API server (port 5000)
python lab_02/api.py

# Test API (mở terminal khác)
# Caesar Encrypt
curl -X POST http://127.0.0.1:5000/api/caesar/encrypt -H "Content-Type: application/json" -d "{\"plain_text\":\"HELLO\",\"key\":\"3\"}"

# Caesar Decrypt
curl -X POST http://127.0.0.1:5000/api/caesar/decrypt -H "Content-Type: application/json" -d "{\"cipher_text\":\"KHOOR\",\"key\":\"3\"}"

# Vigenere Encrypt
curl -X POST http://127.0.0.1:5000/api/vigenere/encrypt -H "Content-Type: application/json" -d "{\"plain_text\":\"HELLO\",\"key\":\"KEY\"}"

# Rail Fence Encrypt
curl -X POST http://127.0.0.1:5000/api/railfence/encrypt -H "Content-Type: application/json" -d "{\"plain_text\":\"HELLO WORLD\",\"key\":\"3\"}"

# Playfair Encrypt
curl -X POST http://127.0.0.1:5000/api/playfair/encrypt -H "Content-Type: application/json" -d "{\"plain_text\":\"HELLOWORLD\",\"key\":\"KEYWORD\"}"

# Transposition Encrypt
curl -X POST http://127.0.0.1:5000/api/transposition/encrypt -H "Content-Type: application/json" -d "{\"plain_text\":\"HELLO WORLD\",\"key\":\"3\"}"

# Chạy Web UI
python lab_02/app.py
```

---

### Lab 03 - RSA, ECC (Flask API + PyQt5 GUI)

```bash
# Cài thư viện
pip install -r lab_03/requirements.txt

# Chạy API server
python lab_03/api.py

# Chạy giao diện Desktop (PyQt5)
python lab_03/caesar.py      # Caesar GUI
python lab_03/rsa.py         # RSA GUI
python lab_03/ecc.py         # ECC GUI
```

---

### Lab 04 - Socket, Hash, Key Exchange

```bash
# --- Hash Functions ---
python lab_04/hash/md5_library.py   # MD5
python lab_04/hash/md5_hash.py      # MD5 tự implement
python "lab_04/hash/sha-256.py"     # SHA-256
python "lab_04/hash/sha-3.py"       # SHA-3
python lab_04/hash/blake2.py        # BLAKE2

# --- AES + RSA qua Socket ---
pip install -r lab_04/aes_rsa_socket/requirements.txt
# Terminal 1: Chạy server
python lab_04/aes_rsa_socket/server.py
# Terminal 2: Chạy client
python lab_04/aes_rsa_socket/client.py

# --- Diffie-Hellman Key Exchange ---
pip install -r lab_04/dh_key_pair/requirements.txt
# Terminal 1: Chạy server
python lab_04/dh_key_pair/server.py
# Terminal 2: Chạy client
python lab_04/dh_key_pair/client.py

# --- WebSocket ---
pip install -r lab_04/websocket/requirements.txt
# Terminal 1: Chạy server
python lab_04/websocket/server.py
# Terminal 2: Chạy client
python lab_04/websocket/client.py
```

---

### Lab 05 - Ứng dụng bảo mật

```bash
# --- Base64 ---
python lab_05/base64/encrypt.py     # Mã hóa Base64
python lab_05/base64/decrypt.py     # Giải mã Base64

# --- SSL ---
# Bước 1: Tạo chứng chỉ SSL
cd lab_05/ssl/certificates
make-cert.bat
cd ../../..
# Bước 2: Chạy server (Terminal 1)
python lab_05/ssl/server.py
# Bước 3: Chạy client (Terminal 2)
python lab_05/ssl/client.py

# --- Blockchain ---
python lab_05/blockchain/test_blockchain.py

# --- Steganography (Giấu tin trong ảnh) ---
pip install -r lab_05/img-hidden/requirements.txt
# Bước 1: Đặt ảnh "image.jpg" vào thư mục lab_05/img-hidden/
# Bước 2: Giấu tin vào ảnh
python lab_05/img-hidden/encrypt.py
# Bước 3: Giải mã tin từ ảnh
python lab_05/img-hidden/decrypt.py
```

---

## ⚡ Test nhanh tất cả Lab (chạy 1 lệnh)

### Windows (PowerShell)

```powershell
$env:PYTHONIOENCODING="utf-8"

Write-Host "===== LAB 01 =====" -ForegroundColor Green
python lab_01/hello.py
echo "5" | python lab_01/ex02_02.py
echo "7" | python lab_01/ex02_03.py
python lab_01/ex02_04.py
echo "50`n100" | python lab_01/ex02_05.py
echo "1,2,3,4,5,6,7,8" | python lab_01/ex03/ex03_01.py
echo "1,2,3,4,5" | python lab_01/ex03/ex03_02.py
python lab_01/ex03/ex03_06.py

Write-Host "===== LAB 04 - HASH =====" -ForegroundColor Green
python lab_04/hash/md5_library.py
python "lab_04/hash/sha-256.py"
python "lab_04/hash/sha-3.py"
python lab_04/hash/blake2.py

Write-Host "===== LAB 05 - BASE64 =====" -ForegroundColor Green
echo "Hello HUTECH" | python lab_05/base64/encrypt.py
echo "SGVsbG8gSFVURUNI" | python lab_05/base64/decrypt.py

Write-Host "===== LAB 05 - BLOCKCHAIN =====" -ForegroundColor Green
python lab_05/blockchain/test_blockchain.py

Write-Host "===== LAB 05 - STEGANOGRAPHY =====" -ForegroundColor Green
echo "Secret Message HUTECH" | python lab_05/img-hidden/encrypt.py
echo "encoded_image.png" | python lab_05/img-hidden/decrypt.py

Write-Host "===== ALL TESTS PASSED =====" -ForegroundColor Cyan
```

### Linux / macOS (Bash)

```bash
export PYTHONIOENCODING=utf-8

echo "===== LAB 01 ====="
python3 lab_01/hello.py
echo "5" | python3 lab_01/ex02_02.py
echo "7" | python3 lab_01/ex02_03.py
python3 lab_01/ex02_04.py
printf "50\n100" | python3 lab_01/ex02_05.py
echo "1,2,3,4,5,6,7,8" | python3 lab_01/ex03/ex03_01.py
echo "1,2,3,4,5" | python3 lab_01/ex03/ex03_02.py
python3 lab_01/ex03/ex03_06.py

echo "===== LAB 04 - HASH ====="
python3 lab_04/hash/md5_library.py
python3 lab_04/hash/sha-256.py
python3 lab_04/hash/sha-3.py
python3 lab_04/hash/blake2.py

echo "===== LAB 05 - BASE64 ====="
echo "Hello HUTECH" | python3 lab_05/base64/encrypt.py
echo "SGVsbG8gSFVURUNI" | python3 lab_05/base64/decrypt.py

echo "===== LAB 05 - BLOCKCHAIN ====="
python3 lab_05/blockchain/test_blockchain.py

echo "===== LAB 05 - STEGANOGRAPHY ====="
echo "Secret Message HUTECH" | python3 lab_05/img-hidden/encrypt.py
echo "encoded_image.png" | python3 lab_05/img-hidden/decrypt.py

echo "===== ALL TESTS PASSED ====="
```

---

## 📝 Ghi chú

- **Lab 02, 03**: Cần chạy Flask API server trước, sau đó test bằng Postman hoặc curl.
- **Lab 04 (Socket/WebSocket)**: Cần mở 2 terminal - một cho server, một cho client.
- **Lab 05 (SSL)**: Cần cài đặt [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) và thêm vào PATH.
- **Lab 05 (Steganography)**: Cần có file `image.jpg` trong thư mục `lab_05/img-hidden/`.
