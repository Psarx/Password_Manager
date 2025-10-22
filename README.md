<h1 align="center">🔒 Secure CLI Password Manager</h1>
<p align="center">
  Python CLI | AES Encryption | PBKDF2 Master Password
</p>

---

## 🚀 Features
- 🔑 **Master Password**: PBKDF2 + salt, secure login
- 🗄️ **Encrypted Storage**: AES-256 encrypted passwords
- 🎲 **Password Generator**: Generate strong random passwords
- 🖥️ **CLI Interface**: Fast, lightweight, local-only
- 🔒 **Security First**: No plaintext passwords, individual encryption

---

## 🛠️ Tech Stack
- 🐍 **Python 3**  
- 🔐 **cryptography** library  
- 💻 **CLI interface** (Linux, Windows, MacOS)  

---

## 📝 Installation

```bash
git clone https://github.com/YOUR_USERNAME/password-manager.git
cd password-manager
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 main.py
```
📁 Project Structure
```bash
password_manager/
├── main.py         # CLI interface
├── storage.py      # File/database operations
├── crypto_utils.py # Encryption & hashing
├── password_gen.py # Random password generator
├── requirements.txt
└── README.md
```
🔐 Security Notes
```bash
Master password hashed with PBKDF2 + salt
Credentials encrypted using AES-256
Local storage only, no cloud syncing
Minimal attack surface, CLI-only interface
```
💻 How It Works
```bash
Set master password → hashed + salted
Login → verify master password
Add credentials → AES-256 encryption
Retrieve credentials → decrypted after login
Password generator → create strong random passwords
```
🧑‍💻 Author
Gautham Prasanth – Cybersecurity & Python Enthusiast
<p align="center"> Made with ❤️ & 🔒 </p> 
