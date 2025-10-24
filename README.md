# 🔐 Silent Key – QR Code Encryption Tool with One-Time AES Key

## 📌 Problem Statement
In today’s digital world, secure communication is essential when transmitting sensitive information across public or untrusted channels.  
Traditional tools often require persistent keys, creating security risks.  

**Silent Key** solves this problem using **ephemeral AES keys** and **QR code sharing**, enabling lightweight and secure offline communication.

---

## 🎯 Objectives
- 🔑 Encrypt messages using a **one-time AES key**.  
- 📷 Encode encrypted messages into **QR codes** for easy sharing.  
- 🔓 Decrypt securely using a **passphrase-derived AES key**.  
- ❌ Ensure AES keys are **never exposed in plaintext**.  
- 🗑️ **Temporary keys** that are deleted after use.

---

## ⚙️ System Overview
Silent Key is a **Python + Flask** application with a **web frontend**:

1. User enters a message and passphrase.  
2. Message is encrypted with **AES (via Fernet)**.  
3. Ciphertext is encoded into a **QR code**.  
4. Receiver scans the QR code and enters the passphrase → message is decrypted.  
5. AES keys are **one-time use** and ephemeral.  

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
- 📷 `pyzbar` / `opencv-python` → Scan & decode QR codes  
- ⚡ Flask → Backend server  

**Tools**  
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)

---

## 🚀 How It Works

### 1️⃣ Encryption
- Enter **message**, **passphrase**, and **expiry time (seconds)**.  
- Message is encrypted with a **one-time AES key**.  
- Ciphertext is saved and a **QR code** is generated in `/saved_qr_codes`.

### 2️⃣ Decryption
- Upload the QR code and enter the **same passphrase**.  
- System verifies expiry and decrypts the message.  
- Countdown timer starts from the **original expiry time**.

---

## 📁 Project Structure
