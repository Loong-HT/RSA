import random

class SmallNumberDisplay:
    @staticmethod
    def gcd(a, b):
        print("计算两个整数的最大公约数")
        print("当前整数对:", a, b)
        if b == 0:
            print("最大公约数:", a)
            return a
        else:
            print("取余数:", a % b)
            return SmallNumberDisplay.gcd(b, a % b)

    @staticmethod
    def exgcd(a, b):
        """计算两个整数的扩展欧几里德算法"""
        print("执行扩展欧几里德算法")
        print("当前整数对:", a, b)
        if b == 0:
            print("扩展欧几里德算法结果:", 1, 0, a)
            return 1, 0, a
        else:
            x, y, d = SmallNumberDisplay.exgcd(b, a % b)
            new_x = y
            new_y = x - (a // b) * y
            print("扩展欧几里德算法结果:", new_x, new_y, d)
            return new_x, new_y, d

    @staticmethod
    def ni(a, mod):
        """计算 a 在模 mod 下的乘法逆元"""
        print("计算乘法逆元")
        print("当前数:", a)
        print("当前模数:", mod)
        x, y, d = SmallNumberDisplay.exgcd(a, mod)
        if d == 1:
            result = x % mod
            print("乘法逆元:", result)
            return result
        else:
            print("无法计算乘法逆元")
            return -1

    @staticmethod
    def pow_mod(a, b, c):
        """计算 a 的 b 次方对 c 取模的结果"""
        print("计算幂取模")
        print("底数:", a)
        print("指数:", b)
        print("模数:", c)
        y = 1
        while b > 0:
            if b % 2 == 1:
                y = (y * a) % c
            b >>= 1
            a = (a * a) % c
        print("幂取模结果:", y)
        return y

    @staticmethod
    def miller_rabin(n, t):
        print("*************Miller-Rabin 素性测试*************")
        s = 0
        r = n - 1
        print(f"n: {n} (待检测的数), t: {t} (迭代次数), s: {s} (计数器), r: {r} (指数)")
        while r & 1 == 0:
            s += 1
            r >>= 1
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
        print("*************生成 RSA 密钥对*************")
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
        print("生成的密钥为：p:{} q:{} n:{} phi_n:{} e:{} d:{}".format(p, q, n, phi_n, e, d))
        return n, e, d, p, q, phi_n, dp, dq,  inv_p

    @staticmethod
    def encrypt(message, e, n):
        """使用 RSA 公钥加密消息"""
        encrypted_message = []
        for char in message:
            char_ord = ord(char)
            print(f"加密字符 '{char}' 的 ASCII 码为 {char_ord}")
            encrypted_char = SmallNumberDisplay.pow_mod(char_ord, e, n)
            print(f"加密字符 '{char}' 的加密结果为 {encrypted_char}")
            encrypted_message.append(encrypted_char)
        return encrypted_message

    @staticmethod
    def decrypt(ciphertext, p, q, dp, dq, inv_p):
        """使用 RSA 私钥解密密文"""
        decrypted_message = ''
        for char in ciphertext:
            m1 = SmallNumberDisplay.pow_mod(char, dp, p)
            m2 = SmallNumberDisplay.pow_mod(char, dq, q)
            inv_q = (1 - p * inv_p) // q
            m = (m1 * q * inv_q + m2 * p * inv_p) % (p * q)
            print(f"解密字符 '{char}' 的解密结果为 {m}")
            decrypted_message += chr(m)
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



