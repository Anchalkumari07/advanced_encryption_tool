from cryptography.fernet import Fernet

# Function to generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the saved key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"[+] File '{filename}' encrypted successfully.")

# Function to decrypt a file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"[+] File '{filename}' decrypted successfully.")

# Main menu
if __name__ == "__main__":
    print("==== Advanced Encryption Tool ====")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        generate_key()
        print("[+] Key generated and saved to 'secret.key'")
    elif choice == "2":
        filename = input("Enter the file name to encrypt: ")
        encrypt_file(filename)
    elif choice == "3":
        filename = input("Enter the file name to decrypt: ")
        decrypt_file(filename)
    else:
        print("[-] Invalid choice.")