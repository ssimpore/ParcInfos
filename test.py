import sys
from PyQt5.QtWidgets import QFrame, QTextBrowser, QRadioButton, QPushButton, QComboBox, \
    QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QApplication
from PyQt5 import QtCore, QtGui


class Utilisateur:
    anciennete = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


class Client(Utilisateur):
    is_client = True


if __name__ == "__main__":
    sidiki = Utilisateur("Sidiki", 33)
    safi = Client("Safiatou", 30)

    print(safi.is_client)


class Cadre1(QFrame):
    def __init__(self, parent=None, config=None, new=False):
        QFrame.__init__(self, parent)
        if config is not None:
            self.setGeometry(QtCore.QRect(config[0], config[1], config[2], config[3]))
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet("background-color: yellow")


class Cadre2(Cadre1):
    def __init__(self, parent=None, config=None, new=False):
        super().__init__(parent, config, new)
        self.data = [1, 2, 3]



class Fenetre(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1300, 700)
        self.setWindowIcon(QtGui.QIcon('solar-panel.png'))
        self.setWindowTitle('Help')



if __name__ == "__main__":
    new = 0
    app = QApplication(sys.argv)
    screen = Fenetre()
    app1 = Cadre1(screen, (20, 20, 300, 400))
    app2 = Cadre2(screen, (400, 20, 300, 400))
    print(app1.data)

    screen.showMaximized()
    app.exec_()
