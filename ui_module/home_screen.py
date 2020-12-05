from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, QFileInfo
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QGuiApplication
from pathlib import Path
from storage_module.dynamo import DynamoModule
from digital_processing_module.digital_processing import OCR
from decoder_module.ceasar_hacker import CeasarHacker
from decoder_module.vigenere_hacker import VigenereHacker
from decoder_module.simpleSubHacker import simple_sub_hacker
import time


class CerebroHome(QMainWindow):
    closed = pyqtSignal()
    item_id = ""
    combo_items = ['Ceaser Cypher', 'Simple Substitution Cypher', 'Vigenere Cypher']

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setObjectName("MainWindow")
        self.resize(1142, 933)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, -1, 300, -1)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setText("")
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username_label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.first_name_label = QtWidgets.QLabel(self.centralwidget)
        self.first_name_label.setText("")
        self.first_name_label.setObjectName("first_name_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.first_name_label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.middle_name_label = QtWidgets.QLabel(self.centralwidget)
        self.middle_name_label.setText("")
        self.middle_name_label.setObjectName("middle_name_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.middle_name_label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.last_name_label = QtWidgets.QLabel(self.centralwidget)
        self.last_name_label.setText("")
        self.last_name_label.setObjectName("last_name_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.last_name_label)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setText("")
        self.email_label.setObjectName("email_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.email_label)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.phone_number_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_number_label.setText("")
        self.phone_number_label.setObjectName("phone_number_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.phone_number_label)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.file_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.file_name_field.setObjectName("file_name_field")
        self.horizontalLayout_2.addWidget(self.file_name_field)
        self.upload_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_button.setObjectName("upload_button")
        self.horizontalLayout_2.addWidget(self.upload_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.uploaded_text_field = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploaded_text_field.sizePolicy().hasHeightForWidth())
        self.uploaded_text_field.setSizePolicy(sizePolicy)
        self.uploaded_text_field.setObjectName("uploaded_text_field")
        self.verticalLayout.addWidget(self.uploaded_text_field)
        self.decode_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decode_button.sizePolicy().hasHeightForWidth())
        self.decode_button.setSizePolicy(sizePolicy)
        self.decode_button.setObjectName("decode_button")
        self.verticalLayout.addWidget(self.decode_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.decoded_text_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.decoded_text_field.setObjectName("decoded_text_field")
        self.gridLayout.addWidget(self.decoded_text_field, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Username:"))
        self.label_4.setText(_translate("MainWindow", "First Name:"))
        self.label_3.setText(_translate("MainWindow", "Middle Name:"))
        self.label_2.setText(_translate("MainWindow", "Last Name:"))
        self.label_5.setText(_translate("MainWindow", "email:"))
        self.label_6.setText(_translate("MainWindow", "phone number:"))
        self.label.setText(_translate("MainWindow", "File name "))
        self.upload_button.setText(_translate("MainWindow", "Upload"))
        self.decode_button.setText(_translate("MainWindow", "Decode"))
        self.decode_button.clicked.connect(self.decode)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.upload_button.clicked.connect(self.convert_to_digital_str)
        QGuiApplication.setQuitOnLastWindowClosed(False)
        self.cyphers_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.cyphers_combo_box.setCurrentText("")
        self.cyphers_combo_box.setObjectName("cyphers_combo_box")
        self.verticalLayout.addWidget(self.cyphers_combo_box)
        self.verticalLayout.addWidget(self.decode_button, 0, QtCore.Qt.AlignHCenter)
        self.cyphers_combo_box.addItems(self.combo_items)
        self.cyphers_combo_box.setCurrentIndex(0)

    def convert_to_digital_str(self):
        file_path = QFileDialog.getOpenFileName()[0]
        if file_path != "":
            username = self.username_label.text()
            file_info = QFileInfo(file_path)
            file_size = file_info.size()
            file_type = Path(file_path).suffix
            self.file_name_field.setText(file_path)
            dynamo = DynamoModule()
            self.item_id = dynamo.create_item(username, str(time.time()), file_type, str(file_size))
            digital_string = OCR.handwritten_to_string(file_path)
            self.uploaded_text_field.setText(digital_string)

    def decode(self):
        picked_cypher = str(self.cyphers_combo_box.currentText())
        if 'Ceaser Cypher' in picked_cypher:
            self.decoded_text_field.setPlainText(CeasarHacker.crack_ceasar(self.uploaded_text_field.toPlainText()))
        elif 'Simple Substitution Cypher' in picked_cypher:
            self.decoded_text_field.setPlainText(simple_sub_hacker(self.uploaded_text_field.toPlainText()))
        elif 'Vigenere Cypher':
            self.decoded_text_field.setPlainText(VigenereHacker.hackVigenere(self.uploaded_text_field.toPlainText()))
        dynamo = DynamoModule()
        dynamo.add_output(self.item_id, self.username_label.text(), self.decoded_text_field.toPlainText())

