import logging
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from tkinter import filedialog, messagebox
import os
class RSA:
    backend = default_backend()

    @staticmethod
    def generate_key_pair(key_size_values):
        print("""RSA 密钥对的生成""")
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size_values,
            backend=RSA.backend
        )
        private_key_pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key_pem = key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        print(f"公钥为：{public_key_pem}")
        print(f"私钥为：{private_key_pem}")
        return private_key_pem, public_key_pem

    @staticmethod
    def save_key_to_file(key_data, file_name):
        print("""将密钥保存到文件""")
        with open(file_name, 'wb') as f:
            f.write(key_data)

    @staticmethod
    def load_key_from_file(file_name):
        print("""从文件加载密钥""")
        with open(file_name, 'rb') as f:
            return f.read()

    @staticmethod
    def encrypt_msg_with_key(msg, key_data):
        print("""使用公钥加密消息""")
        try:
            key = serialization.load_pem_public_key(key_data, RSA.backend)
            encrypted = key.encrypt(
                msg.encode('utf-8'),
                padding.PKCS1v15()
            )
            print(f"加密后的密文：{encrypted.hex()}")
            return encrypted
        except Exception as e:
            logging.error(f'Encryption failed: {e}')
            messagebox.showerror("Encryption Error", "Encryption failed. Please check your key.")

    @staticmethod
    def decrypt_msg_with_key(encrypted_msg, key_data):
        print("""使用私钥解密消息""")
        try:
            key = serialization.load_pem_private_key(key_data, password=None, backend=RSA.backend)
            decrypted = key.decrypt(
                encrypted_msg,
                padding.PKCS1v15()
            )
            print(f"解密后的明文：{decrypted.hex()}")
            return decrypted
        except Exception as e:
            logging.error(f'Decryption failed: {e}')
            messagebox.showerror("Decryption Error", "Decryption failed. Please check your key.")

    @staticmethod
    def load_private_key():
        """从文件加载私钥的函数"""
        file_name = filedialog.askopenfilename(filetypes=[("PEM Files", "*.pem")])
        if file_name:
            try:
                private_key = RSA.load_key_from_file(file_name)
                return private_key
            except Exception as e:
                logging.error(f'Private key loading failed: {e}')
                messagebox.showerror("Key Loading Error", "Failed to load the private key.")

    @staticmethod
    def load_public_key():
        """从文件加载公钥的函数"""
        file_name = filedialog.askopenfilename(filetypes=[("PEM Files", "*.pem")])
        if file_name:
            try:
                public_key = RSA.load_key_from_file(file_name)
                return public_key
            except Exception as e:
                logging.error(f'Public key loading failed: {e}')
                messagebox.showerror("Key Loading Error", "Failed to load the public key.")




class AESCipher:
    @staticmethod
    def generate_key(key_sizs_values):
        print("""使用 PBKDF2 生成指定长度的 AES 密钥""")
        key_length_bytes = key_sizs_values // 8
        salt = os.urandom(16)  # 128 bits salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=key_length_bytes,
            salt=salt,
            iterations=100000,  # 通过迭代次数增加安全性
            backend=default_backend()
        )
        key = kdf.derive(b"password")  # 为密钥派生生成密钥
        print(f"密钥为：{key.hex()}")
        return key

    @staticmethod
    def save_key_to_file(key_data, file_name):
        print("""将密钥保存到文件""")
        with open(file_name, 'wb') as f:
            f.write(key_data)

    @staticmethod
    def load_key_from_file(file_name):
        print("""从文件加载密钥""")
        with open(file_name, 'rb') as f:
            return f.read()

    @staticmethod
    def encrypt(message, key):
        print("""使用 AES 密钥加密消息""")
        iv = os.urandom(16)  # 128 bits IV
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message) + encryptor.finalize()
        print(f"加密后的密文为：{(iv+ciphertext).hex()}")
        return iv + ciphertext

    @staticmethod
    def decrypt(ciphertext, key):
        print("""使用 AES 密钥解密密文""")
        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        print(f"解密后的明文为{plaintext.decode('utf-8')}")
        return plaintext



