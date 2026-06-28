# 🔐 Encrypted Chat App Using AES and Python Sockets

A secure client-server chat application developed using **Python Socket Programming** and **AES (Advanced Encryption Standard)** encryption. The application encrypts every message before transmission and decrypts it on the server, ensuring secure communication over a TCP connection.

---

# 📌 Overview

This project demonstrates secure communication using Python sockets integrated with AES encryption. It provides a lightweight terminal-based chat application where messages are encrypted before being transmitted across the network.

The server also maintains a log of all decrypted messages in `chat.log` for auditing and learning purposes.

---

# 🚀 Features

* 🔒 AES-128 Encryption using PyCryptodome
* 💬 Real-time Client-Server Communication
* 🌐 TCP Socket Programming
* 📝 Automatic Chat Logging
* ⚡ Lightweight Terminal Interface
* 🔑 Base64 Encoding for Secure Transmission
* 🧵 Multi-threaded Server

---

# 📂 Images

### Project Setup  <img width="1918" height="878" alt="Screenshot_2026-06-24_13_11_19 (copy 1)" src="https://github.com/user-attachments/assets/a0afd449-acd9-4dc8-b5eb-d6344cba116f" />


Create project directory, virtual environment and install dependencies.

### AES Encryption Module  <img width="1918" height="878" alt="Screenshot_2026-06-24_13_17_43 (copy 1)" src="https://github.com/user-attachments/assets/3969055a-9ff4-4252-989d-cd93453716e0" />



Implementation of AES encryption and decryption using the PyCryptodome library.

### Server Implementation        <img width="1918" height="878" alt="Screenshot_2026-06-24_13_18_02" src="https://github.com/user-attachments/assets/1eb0f910-39d4-40f1-8cb7-ad4b714ed5fe" />


Python socket server responsible for receiving and decrypting encrypted messages.

### Client Implementation     <img width="1918" height="878" alt="Screenshot_2026-06-24_13_19_34" src="https://github.com/user-attachments/assets/59e63499-fd6e-4762-b7fa-993a731f8deb" />


Client encrypts every message before sending it to the server.

### Server Execution         <img width="1918" height="228" alt="Screenshot_2026-06-24_13_23_15" src="https://github.com/user-attachments/assets/2f5e846a-5e3a-4c02-857f-0faeb12481ba" />

Server successfully starts and waits for incoming client connections.

### Client Execution             <img width="1918" height="878" alt="Screenshot_2026-06-24_13_23_34" src="https://github.com/user-attachments/assets/0bd79fdc-630b-49c0-8386-defe8c4aba15" />


Client connects to the server and securely transmits encrypted messages.

### Chat Logging           <img width="1918" height="878" alt="Screenshot_2026-06-24_13_37_07" src="https://github.com/user-attachments/assets/f862a6ed-ff95-4d6f-8cc6-6cc73eaf1a05" />


All received messages are automatically stored in `chat.log`.

---

# 🎯 Project Objective

The objective of this project is to understand how secure communication works using encryption and socket programming.

The project demonstrates:

* Secure message transmission
* AES Encryption
* TCP Client-Server Communication
* Cryptography Concepts
* Multi-threading
* Logging of communication

---

# 🏗️ Project Architecture

```
User
   │
   ▼
Client Application
   │
Encrypt Message (AES)
   │
   ▼
TCP Socket Connection
   │
   ▼
Server
   │
Decrypt Message
   │
   ▼
Display Message
   │
   ▼
Store in chat.log
```

---

# ⚙️ Technologies Used

## Programming Language

* Python 3

## Networking

* Socket Programming
* TCP Protocol

## Cryptography

* PyCryptodome
* AES (Advanced Encryption Standard)
* Base64 Encoding

## Concurrency

* Python Threading

## Version Control

* Git
* GitHub

---

# 📋 Project Workflow

## 1️⃣ Client Connection

* Create TCP socket
* Connect to server

---

## 2️⃣ Message Encryption

Performed using:

* AES Encryption
* Random Initialization Vector (IV)
* Base64 Encoding

---

## 3️⃣ Message Transmission

* Encrypted message sent over TCP socket

---

## 4️⃣ Message Decryption

Server performs:

* Base64 Decoding
* AES Decryption
* Display Plain Text

---

## 5️⃣ Chat Logging

Every decrypted message is stored inside

```
chat.log
```

---

# 🔐 AES Encryption

## Objective

Protect message confidentiality during communication.

### Process

Plain Text

↓

AES Encryption

↓

Base64 Encoding

↓

Network Transmission

↓

Base64 Decoding

↓

AES Decryption

↓

Original Message

---

# 🌐 Socket Communication

The project uses TCP sockets.

Workflow

```
Client
   │
connect()
   │
send()
   │
────────────►
Server
recv()
decrypt()
display()
```

---

# 📁 Project Structure

```
EncryptedChatApp/
│
├── client.py              # Client application
├── server.py              # Server application
├── crypto.py              # AES encryption & decryption
├── chat.log               # Stores chat history
├── requirements.txt       # Project dependencies
├── README.md
│
├── screenshots/
│   ├── setup.png
│   ├── crypto_module.png
│   ├── server_code.png
│   ├── client_code.png
│   ├── server_running.png
│   ├── client_running.png
│   └── chat_log.png
│
└── venv/
```

---

# ▶️ Installation

Clone Repository

```bash
git clone https://github.com/Sriharireddy12/Encrypted-Chat-App-Using-AES-and-Python-Sockets.git
```

Move to Project

```bash
cd Encrypted-Chat-App-Using-AES-and-Python-Sockets
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate Environment

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install pycryptodome
```

---

# ▶️ Run the Project

Start Server

```bash
python3 server.py
```

Start Client

```bash
python3 client.py
```

---

# 🧩 Challenges Faced

* Understanding AES encryption
* Socket communication
* Handling encrypted data
* Multi-threading implementation
* Managing client-server synchronization
* Logging chat messages

---

# 🎯 Key Learnings

* Python Socket Programming
* AES Encryption
* Cryptography Basics
* TCP Networking
* Multi-threading
* Secure Communication
* Git & GitHub Workflow

---

# 🚀 Future Improvements

* GUI using Tkinter
* Multiple Client Support
* User Authentication
* End-to-End Encryption
* Secure Key Exchange
* Group Chat
* File Sharing
* Message Integrity Verification

---

# 👨‍💻 Author

Kanumuri Sri Hari Reddy

Entry-Level Cybersecurity Professional | SOC Analyst | Network Security | Linux |

🌐 Connect With Me

GitHub:
https://github.com/Sriharireddy12

### LinkedIn: https://www.linkedin.com/in/srihari-reddy-kanumuri-1322b0293/

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
