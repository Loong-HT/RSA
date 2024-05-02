import random
import base64
class SmallNumberDisplay:
    @staticmethod
    def gcd(a, b):
        """计算两个整数的最大公约数"""
        print(f"Euclid计算gcd(a,b)，当前整数对:{a},{b}")
        if b == 0:
            print("最大公约数:", a)
            return a
        else:
            return SmallNumberDisplay.gcd(b, a % b)

    @staticmethod
    def exgcd(a, b):
        """计算两个整数的扩展欧几里德算法"""
        print(f"扩展Euclid算法当前整数对:{a},{b}")
        if b == 0:
            print(f"扩展Euclid算法结果:, 1, 0, {a}")
            return 1, 0, a
        else:
            x, y, d = SmallNumberDisplay.exgcd(b, a % b)
            new_x = y
            new_y = x - (a // b) * y
            print(f"扩展欧几里德算法结果:{new_x}, {new_y}, {d}")
            return new_x, new_y, d

    @staticmethod
    def ni(a, mod):
        """计算 a 在模 mod 下的乘法逆元"""
        print("计算乘法逆元")
        print(f"当前数:{a}   当前模数:{mod}")
        x, y, d = SmallNumberDisplay.exgcd(a, mod)
        if d == 1:
            result = x % mod
            print(f"乘法逆元:{result}")
            return result
        else:
            print("无法计算乘法逆元")
            return -1

    @staticmethod
    def pow_mod(a, b, c):
        """计算 a 的 b 次方对 c 取模的结果"""
        print("计算幂取模")
        print(f"底数:{a}  指数:{b}  模数:{c}")
        y = 1
        while b > 0:
            if b % 2 == 1:
                y = (y * a) % c
            b >>= 1
            a = (a * a) % c
        print(f"幂取模结果:{y}")
        return y

    @staticmethod
    def miller_rabin(n, t):
        print("Miller-Rabin 素性测试")
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r >>= 1
        print(f"n: {n} (待检测的数), t: {t} (迭代次数), s: {s} (计数器), r: {r} (指数)")
        for i in range(t):
            a = random.randint(2, n - 2)
            if SmallNumberDisplay.gcd(a, n) > 1:
                return False
            b = SmallNumberDisplay.pow_mod(a, r, n)
            if b != 1 and b != n - 1:
                for _ in range(1, s):
                    b = SmallNumberDisplay.pow_mod(b, 2, n)
                    if b == n - 1:
                        break
                else:
                    return False

        return True

    @staticmethod
    def generate_key():
        print("生成 RSA 密钥对")
        p, q = 0, 0
        while True:
            while True:
                p = random.randint(2, 1000)
                if SmallNumberDisplay.miller_rabin(p, 10):
                    break
            while True:
                q = random.randint(2, 1000)
                if SmallNumberDisplay.miller_rabin(q, 10):
                    break
            if p != q:
                print(f"通过miller_rabin素性检验的p:{p},q:{q}")
                break

        n = p * q
        phi_n = (p - 1) * (q - 1)

        # Choose encryption exponent 'e'
        e = 65537
        while SmallNumberDisplay.gcd(e, phi_n) != 1:
            e += 2

        # Compute decryption exponent 'd'
        d = SmallNumberDisplay.ni(e, phi_n)
        dp = d % (p - 1)
        dq = d % (q - 1)
        inv_p = SmallNumberDisplay.ni(p, q) % q
        print(f"生成的密钥为：p:{p} q:{q} n:{n} phi_n:{phi_n} e:{e} d:{d} inv_p:{inv_p}")
        return n, e, d, p, q, phi_n, dp, dq,  inv_p

    @staticmethod
    def encode(msg):
        encoded_message = base64.b64encode(str(msg).encode('utf-8'))
        return encoded_message.decode('utf-8')

    @staticmethod
    def decode(msg):
        s = base64.b64decode(msg.encode('utf-8'))
        ciphertext = eval(s.decode('utf-8'))
        return ciphertext

    @staticmethod
    def encrypt(message, e, n):
        """使用 RSA 公钥加密消息"""
        encrypted_message = []
        for char in message:
            char_ord = ord(char)
            encrypted_char = SmallNumberDisplay.pow_mod(char_ord, e, n)
            encrypted_message.append(encrypted_char)
        print(SmallNumberDisplay.encode(encrypted_message))
        return SmallNumberDisplay.encode(encrypted_message)

    @staticmethod
    def decrypt(ciphertext, p, q, dp, dq, inv_p):
        """使用 RSA 私钥解密密文"""
        decrypted_message = ''
        ciphertext_decode = SmallNumberDisplay.decode(ciphertext)
        for char in ciphertext_decode:
            m1 = SmallNumberDisplay.pow_mod(char, dp, p)
            m2 = SmallNumberDisplay.pow_mod(char, dq, q)
            inv_q = (1 - p * inv_p) // q
            m = (m1 * q * inv_q + m2 * p * inv_p) % (p * q)
            decrypted_message += chr(m)
        print(decrypted_message)
        return decrypted_message

    @staticmethod
    def trial_division(n):
        """对整数 n 进行试除法因式分解"""
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
                print(f"当前除数：{divisor}，余数：{n}")
            divisor += 1
        return factors
