
🔐 Advanced Encryption Tool

A powerful, Python-based file encryption and decryption tool that uses the AES-256 algorithm to secure sensitive files. Designed for both personal and enterprise use, this tool ensures data confidentiality using modern cryptographic techniques.

🚀 Features

🔒 AES-256 Encryption in GCM mode (secure and authenticated)
🔑 Password-based Key Derivation using PBKDF2
🧪 Integrity Check via authentication tags
🗃️ Supports all file types
💡 Lightweight and easy to use

🛠️ How It Works

*User provides a password.
*A secure 256-bit key is derived using PBKDF2 + Salt.
*The file is encrypted using AES-256 (GCM mode).
*The encrypted file contains: salt + nonce + tag + ciphertext.
*During decryption, the tool verifies integrity using the tag.

📦 Requirements

Python 3.6+
PyCryptodome
Install dependencies:
pip install pycryptodome
