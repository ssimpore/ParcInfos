import sys
import io

from PyQt5.QtWidgets import QFrame, QTextBrowser, QRadioButton, QPushButton, QComboBox, \
    QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QApplication
from PyQt5 import QtCore, QtGui

from ParcClasses import Parc


# from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEnginePage

class Cadre(QFrame):
    def __init__(self, parent=None, xywh=None):
        QFrame.__init__(self, parent)
        self.parent = parent
        self.xywh = xywh
        if self.xywh is not None:
            self.setGeometry(QtCore.QRect(xywh[0], xywh[1], xywh[2], xywh[3]))
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Raised)
        self.param = Parametre()  # Parametres
        self.data = getData('data.xlsx')  # Données


class Navigation(Cadre):
    def __init__(self, parent, xywh):
        Cadre.__init__(self, parent, xywh)
        h_layout = QHBoxLayout()
        self.choix = [QRadioButton(elt) for elt in self.param.list_app]
        self.choix[0].setChecked(True)
        for elt in self.choix: h_layout.addWidget(elt), self.setLayout(h_layout)
        self.setStyleSheet("background-color: #56F6F6")


class ChoixFonctionalite(Cadre):
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
        self.label_comment = QLabel('Commentaire')
        layout.addWidget(self.label_comment, 9, 0)
        layout.addWidget(self.textbrowser_comment, 10, 0, 10, 4)


class Fenetre(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1300, 700)
        self.setWindowIcon(QtGui.QIcon('solar-panel.png'))
        self.setWindowTitle('Help conduite')
        self.nav = Navigation(self, (580, 40, 150, 40))
        self.appParcInfo = Cadre(self, (300, 80, 800, 600))
        self.choix = ChoixFonctionalite(self.appParcInfo, (50, 40, 300, 120))
        self.infos = InfosGenerale(self.appParcInfo, (50, 200, 700, 350))
        # self.carte = Carte(self.appParcInfo, (450, 10, 300, 190))

        self.initialize()
        self.choix.button_excute.clicked.connect(self.setValue)

    def initialize(self):
        list_parc = list(self.appParcInfo.data.parc.index)
        list_solar = list(self.appParcInfo.data.solar.index)
        list_wind = list(self.appParcInfo.data.wind.index)
        self.choix.comb_choix_parc.addItems(list_solar)
        self.df = self.appParcInfo.data
        self.setValue()

    def setValue(self):
        current_parc = Parc(self.df, self.choix.comb_choix_parc.currentText())
        self.clearOldresult()

        self.infos.textbrowser1[0].setText(current_parc.nom)
        self.infos.textbrowser1[1].setText(current_parc.agence.nom)
        self.infos.textbrowser1[2].setText(current_parc.exploitant.nom)
        self.infos.textbrowser1[3].setText(current_parc.responsable.nom)
        self.infos.textbrowser1[4].setText(current_parc.scada)
        self.infos.textbrowser1[5].setText(current_parc.mainteneur.type)
        self.infos.textbrowser1[6].setText(current_parc.mainteneur.N12.telephone)
        self.infos.textbrowser1[7].setText(current_parc.longitude)

        self.infos.textbrowser2[0].setText(current_parc.technologie)
        self.infos.textbrowser2[1].setText(current_parc.agence.astreinte)
        self.infos.textbrowser2[2].setText(current_parc.exploitant.telephone)
        self.infos.textbrowser2[3].setText(current_parc.responsable.telephone)
        self.infos.textbrowser2[4].setText(current_parc.statut)
        self.infos.textbrowser2[5].setText(current_parc.mainteneur.N12.nom)
        self.infos.textbrowser2[6].setText(current_parc.mainteneur.N12.astreinte)
        self.infos.textbrowser2[7].setText(current_parc.latitude)

        self.infos.textbrowser_comment.setText('Le problème de ce parc est déja connu')

    def clearOldresult(self):

        for elt in self.infos.textbrowser1:
            elt.clear()
        for elt in self.infos.textbrowser2:
            elt.clear()
        self.infos.textbrowser_comment.clear()


def aller():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
        screen = Fenetre()
        screen.show()

        app.exec_()


if __name__ == "__main__":
    aller()
