from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator
import iss4


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 300)
        MainWindow.setMinimumSize(QtCore.QSize(550, 300))
        MainWindow.setMaximumSize(QtCore.QSize(550, 300))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("CentralWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.label_1st_rect = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_1st_rect.setGeometry(QtCore.QRect(14, 30, 151, 51))
        self.label_1st_rect.setObjectName("label_1st_rect")

        self.label_2nd_rect = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2nd_rect.setGeometry(QtCore.QRect(20, 90, 151, 51))
        self.label_2nd_rect.setObjectName("label_2nd_rect")

        self.centre_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.centre_btn.setGeometry(QtCore.QRect(0, 200, 191, 51))
        self.centre_btn.setObjectName("centre_btn")
        self.centre_btn.clicked.connect(self.func_btn1)

        self.angles_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.angles_btn.setGeometry(QtCore.QRect(340, 200, 211, 51))
        self.angles_btn.setObjectName("angles_btn")
        self.angles_btn.clicked.connect(self.func_btn2)

        self.result_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(90, 160, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")

        self.y11_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.y11_label.setGeometry(QtCore.QRect(270, 27, 13, 49))
        self.y11_label.setObjectName("y11_label")

        self.x11_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.x11_input.setGeometry(QtCore.QRect(200, 40, 63, 22))
        self.x11_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.x11_input.setInputMask("")
        self.x11_input.setMaxLength(3)
        self.x11_input.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.x11_input.setObjectName("x11_input")
        self.x11_input.setValidator(QIntValidator())

        self.x12_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.x12_label.setGeometry(QtCore.QRect(360, 27, 13, 49))
        self.x12_label.setObjectName("x12_label_2")

        self.x11_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.x11_label.setGeometry(QtCore.QRect(180, 27, 13, 49))
        self.x11_label.setObjectName("x11_label_2")

        self.y11_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.y11_input.setGeometry(QtCore.QRect(290, 40, 63, 22))
        self.y11_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.y11_input.setObjectName("y11_input_2")
        self.y11_input.setValidator(QIntValidator())

        self.y12_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.y12_label.setGeometry(QtCore.QRect(450, 27, 13, 49))
        self.y12_label.setObjectName("y12_label_2")

        self.y12_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.y12_input.setGeometry(QtCore.QRect(470, 40, 63, 22))
        self.y12_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.y12_input.setObjectName("y12_input_2")
        self.y12_input.setValidator(QIntValidator())

        self.x12_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.x12_input.setGeometry(QtCore.QRect(380, 40, 63, 22))
        self.x12_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.x12_input.setObjectName("x12_input_2")
        self.x12_input.setValidator(QIntValidator())

        self.y21_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.y21_input.setGeometry(QtCore.QRect(291, 100, 62, 22))
        self.y21_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.y21_input.setObjectName("y21_input")
        self.y21_input.setValidator(QIntValidator())

        self.y21_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.y21_label.setGeometry(QtCore.QRect(271, 87, 13, 49))
        self.y21_label.setObjectName("y21_label")

        self.y22_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.y22_input.setGeometry(QtCore.QRect(469, 100, 62, 22))
        self.y22_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.y22_input.setObjectName("y22_input")
        self.y22_input.setValidator(QIntValidator())

        self.x21_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.x21_input.setGeometry(QtCore.QRect(202, 100, 62, 22))
        self.x21_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.x21_input.setObjectName("x21_input")
        self.x21_input.setValidator(QIntValidator())

        self.y22_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.y22_label.setGeometry(QtCore.QRect(449, 87, 13, 49))
        self.y22_label.setObjectName("y22_label")

        self.x22_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.x22_label.setGeometry(QtCore.QRect(360, 87, 13, 49))
        self.x22_label.setObjectName("x22_label")

        self.x21_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.x21_label.setGeometry(QtCore.QRect(182, 87, 13, 49))
        self.x21_label.setObjectName("x21_label")

        self.x22_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.x22_input.setGeometry(QtCore.QRect(380, 100, 62, 22))
        self.x22_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.x22_input.setObjectName("x22_input")
        self.x22_input.setValidator(QIntValidator())

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор 2-ух прямоугольников"))
        self.label_1st_rect.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Координаты</p><p align=\"center\">первого прямоугольника</p></body></html>"))
        self.label_2nd_rect.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Координаты</p><p align=\"center\">второго прямоугольника</p></body></html>"))
        self.centre_btn.setText(_translate("MainWindow", "Расстояние между центрами"))
        self.angles_btn.setText(_translate("MainWindow", "Сумма расстояний между 2 углами"))
        self.result_label.setText(_translate("MainWindow", "Результат: "))
        self.y11_label.setText(_translate("MainWindow", "y1"))
        self.x12_label.setText(_translate("MainWindow", "x2"))
        self.x11_label.setText(_translate("MainWindow", "x1"))
        self.y12_label.setText(_translate("MainWindow", "y2"))
        self.y21_label.setText(_translate("MainWindow", "y1"))
        self.y22_label.setText(_translate("MainWindow", "y2"))
        self.x22_label.setText(_translate("MainWindow", "x2"))
        self.x21_label.setText(_translate("MainWindow", "x1"))

    def func_btn1(self):
        z = iss4.TwoRect(int(self.x11_input.text()), int(self.y11_input.text()),
                         int(self.x12_input.text()), int(self.y12_input.text()),
                         int(self.x21_input.text()), int(self.y21_input.text()),
                         int(self.x22_input.text()), int(self.y22_input.text()))
        self.result_label.setText(f"Результат {z.distance_center()}")

    def func_btn2(self):
        z = iss4.TwoRect(int(self.x11_input.text()), int(self.y11_input.text()),
                         int(self.x12_input.text()), int(self.y12_input.text()),
                         int(self.x21_input.text()), int(self.y21_input.text()),
                         int(self.x22_input.text()), int(self.y22_input.text()))
        self.result_label.setText(f"Результат {z.distance_angle()}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
