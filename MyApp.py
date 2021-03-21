import sys
from PyQt5.QtWidgets import QFrame, QTextBrowser, QRadioButton, QPushButton, QComboBox, \
    QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QApplication, QDesktopWidget
from PyQt5 import QtCore, QtGui
from MyData import Data, Parc
from MyParametre import ScreenConfig, Screenlabel


class TextBrowser(QTextBrowser):
    def __init__(self, nom=None):
        super().__init__()
        self.nom = nom


class ComboBox(QComboBox):
    def __init__(self, nom=None):
        super().__init__()
        self.nom = nom


class Label(QLabel):
    def __init__(self, nom):
        super().__init__(nom)


class RadioButton(QRadioButton):
    def __init__(self, nom):
        super().__init__(nom)


class PushButton(QPushButton):
    def __init__(self, nom):
        super().__init__(nom)


class Cadre(QFrame):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent)
        x = positionsize
        if x is not None:
            self.setGeometry(QtCore.QRect(x[0], x[1], x[2], x[3]))
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Raised)
        self.data = Data(new)
        self.label = Screenlabel()
        self.used = 2

    def closeScreen(self):
        self.close()

    def openScreen(self):
        self.show()

    def selectionlabel(self, used):
        if self.used == 1:
            self.label1 = self.label.label_col1
            self.label2 = self.label.label_col2
        if self.used == 2:
            self.label1 = self.label.label_col11
            self.label2 = self.label.label_col22


class CadreApp(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)


class SelectionFonction(Cadre):

    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)
        v_layout_list_option = QVBoxLayout()
        v_layout_combo_execute = QVBoxLayout()
        h_layout_selection = QHBoxLayout()
        h_layout_selection.addLayout(v_layout_list_option)
        h_layout_selection.addLayout(v_layout_combo_execute)
        self.comb_selection_parc = QComboBox()
        self.button_selection = PushButton('GO')

        self.selection = [RadioButton(elt) for elt in self.label.list_option]
        for elt in self.selection:
            v_layout_list_option.addWidget(elt)
        v_layout_combo_execute.addWidget(self.comb_selection_parc)
        v_layout_combo_execute.addWidget(self.button_selection)
        self.setLayout(h_layout_selection)

    def initialize(self):
        self.selection[0].setChecked(True)
        self.comb_selection_parc.addItems(list(self.data.dfsolar.index))


class InfosGenerale(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)

        self.label = self.label.label
        self.display2()

    def display2(self):
        self.sortie('')
        label = list(self.out.keys())[:24]

        layout = QGridLayout()
        self.setLayout(layout)

        # self.label = [Label(elt + ' :') for elt in label]
        self.label1 = [Label(elt + ' :') for elt in label[:16]]

        self.label2 = [ComboBox(elt + ' :') for elt in label[16:]]
        self.label = self.label1 + self.label2

        for i in range(16, len(self.label)):
            self.label[i].addItems(label)
            self.label[i].setCurrentText(label[i])

        self.infos = [TextBrowser(elt) for elt in range(0, len(label))]
        n = 3

        for i in range(0, int(len(self.label))):
            if i < int(len(self.label) / n):
                layout.addWidget(self.label[i], i, 0)
                layout.addWidget(self.infos[i], i, 1)

            if i >= int(len(self.label) / n) and i < 2 * int(len(self.label) / n):
                layout.addWidget(self.label[i], i - int(len(self.label) / n), 2)
                layout.addWidget(self.infos[i], i - int(len(self.label) / n), 3)

            if i >= 2 * int(len(self.label) / n):
                layout.addWidget(self.label[i], i - 2 * int(len(self.label) / n), 4)
                layout.addWidget(self.infos[i], i - 2 * int(len(self.label) / n), 5)

        self.textBrowser_comment = TextBrowser()
        self.label_comment = Label('Commentaire :')
        layout.addWidget(self.label_comment, 9, 0)
        layout.addWidget(self.textBrowser_comment, 10, 0, 10, 6)

    def initialize(self):
        self.textBrowser_comment.clear()
        for i in range(0, min(len(self.label_col1), len(self.label_col2))):
            self.infos_col1[i].clear()
            self.infos_col2[i].clear()

    def sortie(self, nom_parc):
        parc = Parc()
        self.out = {'Nom du parc': parc.nom,
                    'Agence': parc.agence.nom,
                    'Exploitant': parc.exploitant.nom,
                    'Responsable': parc.responsable.nom,
                    'SCADA principal': parc.scada,
                    'Stratégie. maint': parc.mainteneur.strat_maint,
                    'Tél mainteneur': parc.mainteneur.N12.num_referent,
                    'Longitude': parc.longitude,

                    'Technologie': parc.technologie,
                    'Tél astreinte agence': parc.agence.astreinte,
                    'Tél exploitant': parc.exploitant.telephone,
                    'Tél responsable': parc.responsable.telephone,
                    'Statut parc': parc.statut,
                    'Mainteneur principal': parc.mainteneur.N12.nom,
                    'Tél astreinte maint': parc.mainteneur.N12.astreinte,
                    'Latitude': parc.latitude,

                    'Trigramme': parc.trigramme,
                    'Server': parc.server,
                    'Agregation': parc.agregation,
                    'N° cardi': parc.cardi,
                    'Commentaire': parc.commentaire,
                    'Départ': parc.depart,
                    'IP ADSL': parc.ip_adsl,
                    'IP ASA': parc.ip_asa,
                    'IP Satellite': parc.ip_satellite,
                    'IP SDRT': parc.ip_sdrt,

                    'Tél ACR (ENEDIS)': parc.num_acr,
                    'Tél ADSL': parc.num_adsl,
                    'Poste livraison': parc.pdl,
                    'Poste source': parc.psource,
                    'Parc en récette': parc.recette,
                    }

    def setValue(self, parc):
        # self.infos_col1[0].setText(parc.nom + ' (' + parc.trigramme + ')')
        # self.infos_col1[1].setText(parc.agence.nom)
        # self.infos_col1[2].setText(parc.exploitant.nom)
        # self.infos_col1[3].setText(parc.responsable.nom)
        # self.infos_col1[4].setText(parc.scada)
        # self.infos_col1[5].setText(parc.mainteneur.strat_maint)
        # self.infos_col1[6].setText(parc.mainteneur.N12.num_referent)
        # self.infos_col1[7].setText(parc.longitude)
        #
        # self.infos_col2[0].setText(parc.technologie)
        # self.infos_col2[1].setText(parc.agence.astreinte)
        # self.infos_col2[2].setText(parc.exploitant.telephone)
        # self.infos_col2[3].setText(parc.responsable.telephone)
        # self.infos_col2[4].setText(parc.statut)
        # self.infos_col2[5].setText(parc.mainteneur.N12.nom)
        # self.infos_col2[6].setText(parc.mainteneur.N12.astreinte)
        # self.infos_col2[7].setText(parc.latitude)

        self.textBrowser_comment.setText(parc.commentaire)


class Navigation(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)
        h_layout = QHBoxLayout()
        self.selection = [QRadioButton(elt) for elt in self.label.list_app]

        for elt in self.selection:
            h_layout.addWidget(elt)
            self.setLayout(h_layout)

    def initialize(self):
        self.selection[0].setChecked(True)


class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1300, 700)
        self.setWindowIcon(QtGui.QIcon('solar-panel.png'))
        self.setWindowTitle('Help')
        self.config = ScreenConfig()


def go():
    app = QApplication(sys.argv)
    screen = Fenetre()
    new = False

    navespace = Navigation(screen, screen.config.nav, new)

    appspace = CadreApp(screen, screen.config.app)

    selectspace = SelectionFonction(appspace, screen.config.select)

    infosspace = InfosGenerale(appspace, screen.config.infos)

    # selectspace.initialize()
    # navespace.initialize()
    # infosspace.initialize()
    # P = Parc(selectspace.comb_selection_parc.currentText())
    # infosspace.setValue(P)
    #
    # def ok():
    #     P = Parc(selectspace.comb_selection_parc.currentText())
    #     infosspace.setValue(P)
    #
    # selectspace.button_selection.clicked.connect(ok)
    #
    # selectspace.selection[1].clicked.connect(infosspace.closeScreen)
    # selectspace.selection[0].clicked.connect(infosspace.openScreen)

    screen.showMaximized()
    app.exec_()


if __name__ == "__main__":
    go()
