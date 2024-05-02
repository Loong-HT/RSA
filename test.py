import time
import cProfile
import pstats
from LargeNumberDisplay import RSA, AESCipher  # 请将YourModule替换为你的模块名称

def generate_rsa_key_pair():
    RSA.generate_key_pair(2048)  # 使用2048位密钥

def generate_aes_key():
    AESCipher.generate_key(256)  # 使用256位密钥

def encrypt_decrypt_rsa():
    private_key, public_key = RSA.generate_key_pair(2048)
    message = "Test message"
    encrypted_msg = RSA.encrypt_msg_with_key(message, public_key)
    decrypted_msg = RSA.decrypt_msg_with_key(encrypted_msg, private_key)

def encrypt_decrypt_aes():
    key = AESCipher.generate_key(256)
    message = b"Test message"
    encrypted_msg = AESCipher.encrypt(message, key)
    decrypted_msg = AESCipher.decrypt(encrypted_msg, key)

if __name__ == "__main__":
    # 测试RSA密钥生成时间
    start_time = time.time()
    generate_rsa_key_pair()
    end_time = time.time()
    print(f"RSA密钥生成时间: {end_time - start_time}秒")

    # 测试AES密钥生成时间
    start_time = time.time()
    generate_aes_key()
    end_time = time.time()
    print(f"AES密钥生成时间: {end_time - start_time}秒")

    # 测试RSA加解密时间
    start_time = time.time()
    encrypt_decrypt_rsa()
    end_time = time.time()
    print(f"RSA加解密时间: {end_time - start_time}秒")

    # 测试AES加解密时间
    start_time = time.time()
    encrypt_decrypt_aes()
    end_time = time.time()
    print(f"AES加解密时间: {end_time - start_time}秒")

    # CPU利用率分析
    cProfile.run('generate_rsa_key_pair()', 'rsa_key_pair_stats')
    p = pstats.Stats('rsa_key_pair_stats')
    p.strip_dirs().sort_stats(-1).print_stats()
