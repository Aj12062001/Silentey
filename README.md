<!-- Animated Header -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=4000&pause=500&color=F74747&center=true&vCenter=true&width=500&lines=Hi+there!+👋+I'm+Ajin;MCA+Student+%7C+Tech+Explorer;Welcome+to+my+GitHub+Profile!)](https://github.com/Aj12062001)

<p align="center">
  <img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="300" />
</p>

Welcome to my GitHub profile! I'm a passionate developer with a love for **secure systems**, **clean design**, and **efficient code**.  
This repository contains my **20MCA245 Mini Project**: *Silent Key - QR Code Encryption Tool with One-Time AES Key*.  

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=Aj12062001&color=101913&style=flat-square" />
  <img src="https://img.shields.io/github/stars/Aj12062001?label=Stars&color=101913&style=flat-square" />
  <img src="https://img.shields.io/github/followers/Aj12062001?label=Followers&color=101913&style=flat-square" />
</div>

---

# 🔐 Silent Key – QR Code Encryption Tool with One-Time AES Key

## 📌 Problem Statement  
In today’s digital world, secure communication is essential when transmitting sensitive information across public or untrusted channels.  
Traditional tools often require persistent keys, creating risks.  
This project solves it with **ephemeral AES keys** + **QR code sharing** for lightweight and secure offline communication.

---

## 🎯 Objectives
- 🔑 Encrypt messages using a one-time AES key.  
- 📷 Encode encrypted messages into QR codes for sharing.  
- 🔓 Decrypt securely using a passphrase-derived AES key.  
- ❌ Ensure the AES key is never exposed in plaintext.  
- 🗑️ Keys are temporary and deleted after use.  

---

## ⚙️ Proposed System
Silent Key is built using **Python + Flask + Web Frontend**.  
- User enters a message + passphrase.  
- Message is encrypted with AES (via Fernet).  
- Ciphertext is encoded into a QR code.  
- Receiver scans QR + enters passphrase → message is decrypted.  
- Keys are one-time use and ephemeral.  

---

## 🛠️ Tech Stack

**Languages & Frameworks**  
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

**Libraries**  
- 🔐 `cryptography` → AES/Fernet encryption  
- 🧾 `qrcode` → Generate QR codes  
- 📷 `pyzbar` / `opencv-python` → Scan & decode QR  
- ⚡ Flask → Backend server  

**Tools**  
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)

---

## 🚀 How It Works

1. **Encryption**
   - Enter message + passphrase + expiry time (seconds).
   - Message is encrypted with a one-time AES key.
   - Ciphertext is saved and a QR code is generated + stored in `/saved_qr_codes`.

2. **Decryption**
   - Upload the QR code + enter the same passphrase.
   - The system verifies expiry and decrypts message.
   - Countdown timer starts from the *original expiry time* (not remaining time).  

---

## 📂 Project Structure
