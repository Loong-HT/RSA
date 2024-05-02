import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal
from UI import Ui_Form
from SmallNumberDisplay import SmallNumberDisplay
from LargeNumberDisplay import RSA, AESCipher




class Stream(QObject):
    """Redirects console output to text widget."""
    newText = Signal(str)

    def write(self, text):
        # 发出内容
        self.newText.emit(text)

    def flush(self):  # real signature unknown; restored from __doc__
        """ flush(self) """
        pass


class MyWindow(QWidget, Ui_Form, SmallNumberDisplay):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.p = None
        self.q = None
        self.n = None
        self.phi_n = None
        self.e = None
        self.d = None
        self.dp = None
        self.dq = None
        self.inv_p = None
        self.blind()
        self.stream = Stream()
        # 将textEdit_4的setText方法连接到Stream的newText信号上
        sys.stdout = self.stream
        self.stream.newText.connect(self.textEdit_4.append)


    def blind(self):
        self.pushButton_generate_key_1.clicked.connect(self.generate_values)
        self.pushButton_encrypt_1.clicked.connect(self.encrypt_values)
        self.pushButton_decrypt_1.clicked.connect(self.decrypt_values)
        self.pushButton_trial_division.clicked.connect(self.trial_division_values)
        self.pushButton_generate_key_2.clicked.connect(self.generate_key_pair_values)
        self.pushButton_encrypt_2.clicked.connect(self.encrypt_msg)
        self.pushButton_decrypt_2.clicked.connect(self.decrypt_msg)
        self.pushButton_generate_key_3.clicked.connect(self.generate_key_values)
        self.pushButton_encrypt_3.clicked.connect(self.encrypt_m)
        self.pushButton_decrypt_3.clicked.connect(self.decrypt_c)

    def generate_values(self):
        n, e, d, p, q, phi_n, dp, dq, inv_p = SmallNumberDisplay.generate_key()
        # 将生成的值填入 QLineEdit 中
        self.lineEdit_p.setText(str(p))
        self.lineEdit_q.setText(str(q))
        self.lineEdit_n.setText(str(n))
        self.lineEdit_fn.setText(str(phi_n))
        self.lineEdit_e.setText(str(e))
        self.lineEdit_d.setText(str(d))
        self.n = n
        self.e = e
        self.d = d
        self.p = p
        self.q = q
        self.phi_n = phi_n
        self.dp = dp
        self.dq = dq
        self.inv_p = inv_p




    def encrypt_values(self):
        message = self.textEdit_m.toPlainText()
        encrypted_message = SmallNumberDisplay.encrypt(message, self.e, self.n)
        self.textEdit_c.setText(encrypted_message)

    def decrypt_values(self):
        ciphertext = self.textEdit_c.toPlainText()
        decrypted_message = SmallNumberDisplay.decrypt(ciphertext, self.p, self.q, self.dp, self.dq, self.inv_p)
        self.textEdit_c_m.setText(decrypted_message)


    def trial_division_values(self):
        factors = SmallNumberDisplay.trial_division(self.n)
        self.textEdit_y.setText(str(factors))

    def generate_key_pair_values(self):
        key_sizs_values = int(self.comboBox_rsa.currentText())
        private_key, public_key = RSA.generate_key_pair(key_sizs_values)
        RSA.save_key_to_file(private_key, "private_key.pem")
        RSA.save_key_to_file(public_key, "public_key.pem")
        self.textEdit_public_key.setText(str(public_key))
        self.textEdit_private_key.setText(str(private_key))

    def encrypt_msg(self):
        msg = self.textEdit_LM.toPlainText()
        public_key = RSA.load_key_from_file("public_key.pem")
        encrypted_msg = RSA.encrypt_msg_with_key(msg, public_key)
        self.textEdit_LC.setText(str(encrypted_msg.hex()))

    def decrypt_msg(self):
        private_key = RSA.load_key_from_file("private_key.pem")
        hex_encrypted_msg = self.textEdit_LC.toPlainText()
        encrypted_msg = bytes.fromhex(hex_encrypted_msg)
        decrypted_msg = RSA.decrypt_msg_with_key(encrypted_msg, private_key)
        self.textEdit_LC_M.setText(str(decrypted_msg.decode('utf-8')))

    def generate_key_values(self):
        key_sizs_values = int(self.comboBox_aes.currentText())
        key = AESCipher.generate_key(key_sizs_values)
        AESCipher.save_key_to_file(key, "key.txt")
        self.textEdit_encrypt_key.setText(str(key.hex()))
        self.textEdit_decrypt_key.setText(str(key.hex()))

    def encrypt_m(self):
        msg = self.textEdit_LM_2.toPlainText().encode()
        key = AESCipher.load_key_from_file("key.txt")
        ciphertext = AESCipher.encrypt(msg, key)
        self.textEdit_LC_2.setText(str(ciphertext.hex()))

    def decrypt_c(self):
        key = AESCipher.load_key_from_file("key.txt")
        hex_ciphertext = self.textEdit_LC_2.toPlainText()
        ciphertext = bytes.fromhex(hex_ciphertext)
        decrypted_msg = AESCipher.decrypt(ciphertext, key)
        self.textEdit_LC_2_M.setText(str(decrypted_msg.decode('utf-8')))










if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
