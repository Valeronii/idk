import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
np.random.shuffle(a)
# массив с перемешанными элементами


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def btntext(self):
        # функция для заполнения кнопок текстом
        self.btn.setText('{}'.format(a[0][0]))

        self.btn2.setText('{}'.format(a[0][1]))

        self.btn3.setText('{}'.format(a[0][2]))

        self.btn4.setText('{}'.format(a[0][3]))

        self.btn5.setText('{}'.format(a[1][0]))

        self.btn6.setText('{}'.format(a[1][1]))

        self.btn7.setText('{}'.format(a[1][2]))

        self.btn8.setText('{}'.format(a[1][3]))

        self.btn9.setText('{}'.format(a[2][0]))

        self.btn10.setText('{}'.format(a[2][1]))

        self.btn11.setText('{}'.format(a[2][2]))

        self.btn12.setText('{}'.format(a[2][3]))

        self.btn13.setText('{}'.format(a[3][0]))

        self.btn14.setText('{}'.format(a[3][1]))

        self.btn15.setText('{}'.format(a[3][2]))

        self.btn16.setText('{}'.format(a[3][3]))




    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Spiel der Funfzehn')
        self.label = QLabel(self)
        self.label.setText("Поехали!")
        self.label.move(260, 70)
        self.label2 = QLabel(self)
        self.label2.setText("                                      ")
        self.label2.move(180, 440)
        # описание поля
        self.btn = QPushButton('1', self)
        self.btn.resize(71, 71)
        self.btn.move(150, 110)
        self.btn2 = QPushButton('', self)
        self.btn2.resize(71, 71)
        self.btn2.move(220, 110)
        self.btn3 = QPushButton('', self)
        self.btn3.resize(71, 71)
        self.btn3.move(290, 110)
        self.btn4 = QPushButton('', self)
        self.btn4.resize(71, 71)
        self.btn4.move(360, 110)
        self.btn5 = QPushButton('', self)
        self.btn5.resize(71, 71)
        self.btn5.move(150, 180)
        self.btn6 = QPushButton('', self)
        self.btn6.resize(71, 71)
        self.btn6.move(220, 180)
        self.btn7 = QPushButton('', self)
        self.btn7.resize(71, 71)
        self.btn7.move(290, 180)
        self.btn8 = QPushButton('', self)
        self.btn8.resize(71, 71)
        self.btn8.move(360, 180)
        self.btn9 = QPushButton('', self)
        self.btn9.resize(71, 71)
        self.btn9.move(150, 250)
        self.btn10 = QPushButton('', self)
        self.btn10.resize(71, 71)
        self.btn10.move(220, 250)
        self.btn11 = QPushButton('', self)
        self.btn11.resize(71, 71)
        self.btn11.move(290, 250)
        self.btn12 = QPushButton('', self)
        self.btn12.resize(71, 71)
        self.btn12.move(360, 250)
        self.btn13 = QPushButton('', self)
        self.btn13.resize(71, 71)
        self.btn13.move(150, 320)
        self.btn14 = QPushButton('', self)
        self.btn14.resize(71, 71)
        self.btn14.move(220, 320)
        self.btn15 = QPushButton('', self)
        self.btn15.resize(71, 71)
        self.btn15.move(290, 320)
        self.btn16 = QPushButton('', self)
        self.btn16.resize(71, 71)
        self.btn16.move(360, 320)
        # описание кнопок
        self.btntext()
        # вызов функции для присвоения кнопкам текста

        self.btn.clicked.connect(self.change)
        self.btn2.clicked.connect(self.change)
        self.btn3.clicked.connect(self.change)
        self.btn4.clicked.connect(self.change)
        self.btn5.clicked.connect(self.change)
        self.btn6.clicked.connect(self.change)
        self.btn7.clicked.connect(self.change)
        self.btn8.clicked.connect(self.change)
        self.btn9.clicked.connect(self.change)
        self.btn10.clicked.connect(self.change)
        self.btn11.clicked.connect(self.change)
        self.btn12.clicked.connect(self.change)
        self.btn13.clicked.connect(self.change)
        self.btn14.clicked.connect(self.change)
        self.btn15.clicked.connect(self.change)
        self.btn16.clicked.connect(self.change)

    def change(self):
        # функция для проверки на возможность перемещения, и самого перемещения текста кнопок
        ok = 0
        b = int(self.sender().text())

        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == b:
                    if ok == 0:
                     if j != 0:
                        if a[i][j-1] == 0:
                            a[i][j-1] = b
                            a[i][j] = 0
                            ok = 1
                    if ok == 0:
                     if j != 3:
                        if a[i][j+1] == 0:
                            a[i][j+1] = b
                            a[i][j] = 0
                            ok = 1
                    if ok == 0:
                     if i != 0:
                        if a[i-1][j] == 0:
                            a[i-1][j] = b
                            a[i][j] = 0
                            ok = 1
                     if ok == 0:
                      if i != 3:
                        if a[i+1][j] == 0:
                            a[i+1][j] = b
                            a[i][j] = 0
                            ok = 1
        if ok == 0:
            self.label2.setText("Нельзя!!!")
        else:
            self.label2.setText("                                      ")
        win = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        if win == a:
            self.label.setText("Победа!!!!!!!")
            # условия победы
        else:
            self.label.setText("Поехали!")

        self.btntext()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())