<!-- Animated Header -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=4000&pause=500&color=F74747&center=true&vCenter=true&width=500&lines=Hi+there!+👋+I'm+Ajin;Silent+Key+%7C+Cryptography+Project;Secure+QR+Code+Encryption+Tool)](https://github.com/Aj12062001)

<p align="center">
  <img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="300" />
</p>

Welcome to **Silent Key** – a secure and lightweight QR code encryption tool using **AES** and **RSA**. This project allows offline sharing of encrypted messages with one-time keys.

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=Aj12062001&color=101913&style=flat-square" />
  <img src="https://img.shields.io/github/stars/Aj12062001/silent_key?label=Stars&color=101913&style=flat-square" />
  <img src="https://img.shields.io/github/followers/Aj12062001?label=Followers&color=101913&style=flat-square" />
</div>

---

## 👨‍💻 About Silent Key

- 🔑 Encrypt messages with **one-time AES keys**  
- 🔐 Secure AES key sharing using **RSA public/private keys**  
- 📷 Encode encrypted messages + AES keys into **QR codes**  
- ⏱️ Supports **expiry timers** for messages  
- ❌ AES keys are **deleted after use**, ensuring maximum security  

---

## 🛠️ Tech Stack

<img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="300px" align="right" />

**Languages & Frameworks**  
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

**Libraries**  
- `cryptography` → AES + RSA encryption  
- `qrcode` → Generate QR codes  
- `pyzbar` / `opencv-python` → Scan QR codes  
- `Flask` → Backend server  

**Tools & Platforms**  
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)

---

## 🚀 How Silent Key Works

### 1️⃣ Encryption
1. Enter **message**, **passphrase**, and **expiry time**.  
2. Generate a **one-time AES key**.  
3. Encrypt the message with the AES key.  
4. Encrypt AES key with **recipient’s RSA public key**.  
5. Encode **encrypted message + encrypted AES key** into a QR code.  
6. Save QR code in `/saved_qr_codes`.

### 2️⃣ Decryption
1. Scan QR code.  
2. Decrypt AES key with **RSA private key**.  
3. Decrypt message with AES key + passphrase.  
4. AES key is deleted immediately after decryption.  



