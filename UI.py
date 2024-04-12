# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1083, 673)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 511, 661))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.pushButton_generate_key_1 = QPushButton(self.widget)
        self.pushButton_generate_key_1.setObjectName(u"pushButton_generate_key_1")
        self.pushButton_generate_key_1.setGeometry(QRect(390, 70, 75, 24))
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 190, 361, 141))
        self.textEdit_m = QTextEdit(self.groupBox)
        self.textEdit_m.setObjectName(u"textEdit_m")
        self.textEdit_m.setGeometry(QRect(10, 20, 331, 111))
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 340, 361, 141))
        self.textEdit_c = QTextEdit(self.groupBox_2)
        self.textEdit_c.setObjectName(u"textEdit_c")
        self.textEdit_c.setGeometry(QRect(10, 20, 331, 101))
        self.pushButton_encrypt_1 = QPushButton(self.widget)
        self.pushButton_encrypt_1.setObjectName(u"pushButton_encrypt_1")
        self.pushButton_encrypt_1.setGeometry(QRect(390, 220, 75, 24))
        self.pushButton_decrypt_1 = QPushButton(self.widget)
        self.pushButton_decrypt_1.setObjectName(u"pushButton_decrypt_1")
        self.pushButton_decrypt_1.setGeometry(QRect(390, 390, 75, 24))
        self.pushButton_trial_division = QPushButton(self.widget)
        self.pushButton_trial_division.setObjectName(u"pushButton_trial_division")
        self.pushButton_trial_division.setGeometry(QRect(390, 540, 75, 24))
        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 10, 361, 171))
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_p = QLineEdit(self.groupBox_4)
        self.lineEdit_p.setObjectName(u"lineEdit_p")
        self.lineEdit_p.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_p, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 0, 2, 1, 1)

        self.lineEdit_q = QLineEdit(self.groupBox_4)
        self.lineEdit_q.setObjectName(u"lineEdit_q")
        self.lineEdit_q.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_q, 0, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEdit_n = QLineEdit(self.groupBox_4)
        self.lineEdit_n.setObjectName(u"lineEdit_n")
        self.lineEdit_n.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_n, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 1, 2, 1, 1)

        self.lineEdit_fn = QLineEdit(self.groupBox_4)
        self.lineEdit_fn.setObjectName(u"lineEdit_fn")
        self.lineEdit_fn.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_fn, 1, 3, 1, 1)

        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 2, 0, 1, 1)

        self.lineEdit_e = QLineEdit(self.groupBox_4)
        self.lineEdit_e.setObjectName(u"lineEdit_e")
        self.lineEdit_e.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_e, 2, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 2, 1, 1)

        self.lineEdit_d = QLineEdit(self.groupBox_4)
        self.lineEdit_d.setObjectName(u"lineEdit_d")
        self.lineEdit_d.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_d, 2, 3, 1, 1)

        self.groupBox_9 = QGroupBox(self.widget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(0, 490, 361, 111))
        self.textEdit_y = QTextEdit(self.groupBox_9)
        self.textEdit_y.setObjectName(u"textEdit_y")
        self.textEdit_y.setGeometry(QRect(10, 20, 331, 81))

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 10, 491, 511))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 54, 16))
        self.textEdit_public_key = QTextEdit(self.tab_3)
        self.textEdit_public_key.setObjectName(u"textEdit_public_key")
        self.textEdit_public_key.setGeometry(QRect(10, 70, 181, 81))
        self.textEdit_public_key.setStyleSheet(u"")
        self.textEdit_public_key.setReadOnly(True)
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 50, 54, 16))
        self.textEdit_private_key = QTextEdit(self.tab_3)
        self.textEdit_private_key.setObjectName(u"textEdit_private_key")
        self.textEdit_private_key.setGeometry(QRect(210, 70, 181, 81))
        self.textEdit_private_key.setReadOnly(True)
        self.layoutWidget = QWidget(self.tab_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 124, 23))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_rsa = QComboBox(self.layoutWidget)
        self.comboBox_rsa.addItem("")
        self.comboBox_rsa.addItem("")
        self.comboBox_rsa.setObjectName(u"comboBox_rsa")

        self.horizontalLayout.addWidget(self.comboBox_rsa)

        self.pushButton_generate_key_2 = QPushButton(self.tab_3)
        self.pushButton_generate_key_2.setObjectName(u"pushButton_generate_key_2")
        self.pushButton_generate_key_2.setGeometry(QRect(400, 90, 81, 24))
        self.groupBox_10 = QGroupBox(self.tab_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(0, 160, 481, 151))
        self.textEdit_LM = QTextEdit(self.groupBox_10)
        self.textEdit_LM.setObjectName(u"textEdit_LM")
        self.textEdit_LM.setGeometry(QRect(10, 20, 381, 111))
        self.pushButton_encrypt_2 = QPushButton(self.groupBox_10)
        self.pushButton_encrypt_2.setObjectName(u"pushButton_encrypt_2")
        self.pushButton_encrypt_2.setGeometry(QRect(400, 60, 81, 24))
        self.groupBox_11 = QGroupBox(self.tab_3)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(0, 320, 481, 151))
        self.textEdit_LC = QTextEdit(self.groupBox_11)
        self.textEdit_LC.setObjectName(u"textEdit_LC")
        self.textEdit_LC.setGeometry(QRect(10, 20, 381, 111))
        self.pushButton_decrypt_2 = QPushButton(self.groupBox_11)
        self.pushButton_decrypt_2.setObjectName(u"pushButton_decrypt_2")
        self.pushButton_decrypt_2.setGeometry(QRect(400, 60, 81, 24))
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 50, 54, 16))
        self.label_6 = QLabel(self.tab_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 50, 54, 16))
        self.textEdit_encrypt_key = QTextEdit(self.tab_4)
        self.textEdit_encrypt_key.setObjectName(u"textEdit_encrypt_key")
        self.textEdit_encrypt_key.setGeometry(QRect(10, 70, 181, 81))
        self.textEdit_encrypt_key.setReadOnly(True)
        self.textEdit_decrypt_key = QTextEdit(self.tab_4)
        self.textEdit_decrypt_key.setObjectName(u"textEdit_decrypt_key")
        self.textEdit_decrypt_key.setGeometry(QRect(210, 70, 181, 81))
        self.textEdit_decrypt_key.setReadOnly(True)
        self.pushButton_generate_key_3 = QPushButton(self.tab_4)
        self.pushButton_generate_key_3.setObjectName(u"pushButton_generate_key_3")
        self.pushButton_generate_key_3.setGeometry(QRect(400, 90, 81, 24))
        self.groupBox_14 = QGroupBox(self.tab_4)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(0, 160, 481, 151))
        self.textEdit_LM_2 = QTextEdit(self.groupBox_14)
        self.textEdit_LM_2.setObjectName(u"textEdit_LM_2")
        self.textEdit_LM_2.setGeometry(QRect(10, 20, 381, 111))
        self.pushButton_encrypt_3 = QPushButton(self.groupBox_14)
        self.pushButton_encrypt_3.setObjectName(u"pushButton_encrypt_3")
        self.pushButton_encrypt_3.setGeometry(QRect(400, 60, 81, 24))
        self.groupBox_15 = QGroupBox(self.tab_4)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(0, 320, 481, 151))
        self.textEdit_LC_2 = QTextEdit(self.groupBox_15)
        self.textEdit_LC_2.setObjectName(u"textEdit_LC_2")
        self.textEdit_LC_2.setGeometry(QRect(10, 20, 381, 111))
        self.pushButton_decrypt_3 = QPushButton(self.groupBox_15)
        self.pushButton_decrypt_3.setObjectName(u"pushButton_decrypt_3")
        self.pushButton_decrypt_3.setGeometry(QRect(400, 60, 81, 24))
        self.layoutWidget1 = QWidget(self.tab_4)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 102, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.comboBox_aes = QComboBox(self.layoutWidget1)
        self.comboBox_aes.addItem("")
        self.comboBox_aes.addItem("")
        self.comboBox_aes.addItem("")
        self.comboBox_aes.setObjectName(u"comboBox_aes")

        self.horizontalLayout_3.addWidget(self.comboBox_aes)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.groupBox_12 = QGroupBox(self.tab_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 520, 421, 111))
        self.textEdit_13 = QTextEdit(self.groupBox_12)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setGeometry(QRect(10, 20, 391, 81))
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(530, 10, 541, 661))
        self.textEdit_4 = QTextEdit(self.groupBox_3)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(10, 20, 521, 631))

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"RSA\u8fc7\u7a0b\u5c55\u793a\u8f6f\u4ef6", None))
        self.pushButton_generate_key_1.setText(QCoreApplication.translate("Form", u"\u5bc6\u94a5\u751f\u6210", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u660e\u6587\u6846", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u5bc6\u6587\u6846", None))
        self.pushButton_encrypt_1.setText(QCoreApplication.translate("Form", u"\u52a0\u5bc6", None))
        self.pushButton_decrypt_1.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.pushButton_trial_division.setText(QCoreApplication.translate("Form", u"\u56e0\u5b50\u5206\u89e3", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u5bc6\u94a5\u751f\u6210", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"p", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"q", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"n", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u03c6(n)", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"e", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"d", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"\u56e0\u5b50\u5206\u89e3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u5c0f\u6570\u6a21\u62df\u5c55\u793a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u516c\u94a5", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u79c1\u94a5", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5bc6\u94a5\u957f\u5ea6", None))
        self.comboBox_rsa.setItemText(0, QCoreApplication.translate("Form", u"2048", None))
        self.comboBox_rsa.setItemText(1, QCoreApplication.translate("Form", u"4096", None))

        self.pushButton_generate_key_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u94a5\u751f\u6210", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"\u660e\u6587\u6846", None))
        self.pushButton_encrypt_2.setText(QCoreApplication.translate("Form", u"\u52a0\u5bc6", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Form", u"\u5bc6\u6587\u6846", None))
        self.pushButton_decrypt_2.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", u"RSA", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u52a0\u5bc6\u5bc6\u94a5", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6\u5bc6\u94a5", None))
        self.pushButton_generate_key_3.setText(QCoreApplication.translate("Form", u"\u5bc6\u94a5\u751f\u6210", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Form", u"\u660e\u6587\u6846", None))
        self.pushButton_encrypt_3.setText(QCoreApplication.translate("Form", u"\u52a0\u5bc6", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("Form", u"\u5bc6\u6587\u6846", None))
        self.pushButton_decrypt_3.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5bc6\u94a5\u957f\u5ea6", None))
        self.comboBox_aes.setItemText(0, QCoreApplication.translate("Form", u"128", None))
        self.comboBox_aes.setItemText(1, QCoreApplication.translate("Form", u"192", None))
        self.comboBox_aes.setItemText(2, QCoreApplication.translate("Form", u"256", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Form", u"AES", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Form", u"\u6027\u80fd\u5206\u6790", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u5927\u6570\u5c55\u793a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u72b6\u6001\u4fe1\u606f", None))
    # retranslateUi

