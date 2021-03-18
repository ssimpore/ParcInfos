import sys
import io

from PyQt5.QtWidgets import QFrame, QTextBrowser, QRadioButton, QPushButton, QComboBox, \
    QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5 import QtCore, QtGui

from PlantClasses import Parametre


class Cadre(QFrame):
    def __init__(self, parent=None, xywh=None):
        QFrame.__init__(self, parent)
        if xywh is not None:
            self.setGeometry(QtCore.QRect(xywh[0], xywh[1], xywh[2], xywh[3]))
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Raised)
        self.param = Parametre()


class CadreApp(Cadre):
    def __init__(self, parent, xywh):
        Cadre.__init__(self, parent, xywh)


class ChoixFonction(Cadre):
    def __init__(self, parent, xywh):
        Cadre.__init__(self, parent, xywh)
        v_layout_liste_option = QVBoxLayout()
        v_layout_combo_execute = QVBoxLayout()
        h_layout_choix = QHBoxLayout()
        h_layout_choix.addLayout(v_layout_liste_option)
        h_layout_choix.addLayout(v_layout_combo_execute)
        self.comb_choix_parc = QComboBox()
        self.button_excute = QPushButton('GO')

        self.choix = [QRadioButton(elt) for elt in self.param.list_option]
        self.choix[0].setChecked(True)
        for elt in self.choix: v_layout_liste_option.addWidget(elt)
        v_layout_combo_execute.addWidget(self.comb_choix_parc)
        v_layout_combo_execute.addWidget(self.button_excute)
        self.setLayout(h_layout_choix)
        # self.setStyleSheet("background-color:white")


class InfosGenerale(Cadre):
    def __init__(self, parent, xywh):
        Cadre.__init__(self, parent, xywh)
        layout = QGridLayout()
        self.setLayout(layout)
        self.label_colone1 = [QLabel(elt + ' :') for elt in self.param.label_colone1]
        self.label_colone2 = [QLabel(elt + ' :') for elt in self.param.label_colone2]
        self.textbrowser1 = [QTextBrowser() for elt in range(0, min(len(self.label_colone1), len(self.label_colone2)))]
        self.textbrowser2 = [QTextBrowser() for elt in range(0, min(len(self.label_colone1), len(self.label_colone2)))]

        for i in range(0, min(len(self.label_colone1), len(self.label_colone2))):
            layout.addWidget(self.label_colone1[i], i, 0)
            layout.addWidget(self.textbrowser1[i], i, 1)
            layout.addWidget(self.label_colone2[i], i, 2)
            layout.addWidget(self.textbrowser2[i], i, 3)

        self.textbrowser_comment = QTextBrowser()
        self.label_comment = QLabel('Commentaire :')
        layout.addWidget(self.label_comment, 9, 0)
        layout.addWidget(self.textbrowser_comment, 10, 0, 10, 4)

class Fenetre(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1300, 700)
        self.setWindowIcon(QtGui.QIcon('solar-panel.png'))
        self.setWindowTitle('Help')


class Navigation(Cadre):
    def __init__(self, parent, xywh):
        Cadre.__init__(self, parent, xywh)
        h_layout = QHBoxLayout()
        self.choix = [QRadioButton(elt) for elt in self.param.list_app]
        self.choix[0].setChecked(True)
        for elt in self.choix: h_layout.addWidget(elt), self.setLayout(h_layout)
        # self.setStyleSheet("background-color: #56F6F6")
