from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    print("Your Fernet key:\n", key.decode())

if __name__ == "__main__":
    generate_key()
