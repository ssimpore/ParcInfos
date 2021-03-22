import sys
from PyQt5.QtWidgets import QFrame, QTextBrowser, QRadioButton, QPushButton, QComboBox, \
    QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QApplication, QCheckBox, QFormLayout, QLineEdit, \
    QToolButton
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
        self.new = new
        if x is not None:
            self.setGeometry(QtCore.QRect(x[0], x[1], x[2], x[3]))
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Raised)
        # self.data = Data(self.new)

        self.label = Screenlabel()

    def makeDisplay(self, text='', n=1):
        if n == 1:
            x = Label(str(text) + ':')
        elif n == 2:
            x = ComboBox(str(text) + ':')
        elif n == 3:
            x = TextBrowser(str(text))
        else:
            x = None
        return x

    def getData(self, new):

        return Data(new)


class CadreApp(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)
        #self.setMaximumSize(1000, 600)


class SelectionFonction1(Cadre):

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


class SelectionFonction(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)
        selection_layout = QVBoxLayout()
        h_layout_parc = QHBoxLayout()
        h_layout_execute = QHBoxLayout()
        login_form_layout = QFormLayout()
        v_login_btn_layout = QVBoxLayout()
        login_layout = QHBoxLayout()
        layout = QVBoxLayout()
        login_layout.addLayout(login_form_layout)
        login_layout.addLayout(v_login_btn_layout)
        selection_layout.addLayout(h_layout_parc)
        selection_layout.addLayout(h_layout_execute)
        layout.addLayout(login_layout)
        layout.addLayout(selection_layout)

        self.setLayout(layout)
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()

        self.username_edit.setFixedWidth(200)
        self.password_edit.setFixedWidth(200)

        login_form_layout.addRow(QLabel("Username"), self.username_edit)
        login_form_layout.addRow(QLabel("Password"), self.password_edit)

        self.login_btn = QPushButton("Log In")
        self.login_btn.setFixedWidth(200)
        v_login_btn_layout.addWidget(self.login_btn)

        self.check_solaire = QCheckBox("Solaire")
        self.check_solaire.setChecked(True)
        self.check_eolien = QCheckBox("Eolien")
        self.check_eolien.setChecked(False)
        self.check_update = QCheckBox("Update")
        self.check_update.setChecked(False)
        self.button_update = QToolButton()
        self.button_update.setFixedWidth(100)
        self.button_update.setText('Valider')
        self.comb_selection_parc = QComboBox()

        self.button_execute = PushButton('GO')
        self.button_execute.setMinimumSize(130, 30)

        h_layout_parc.addWidget(self.check_solaire)
        h_layout_parc.addWidget(self.check_eolien)
        h_layout_parc.addWidget(self.check_update)
        h_layout_parc.addWidget(self.button_update)

        h_layout_parc.addWidget(self.comb_selection_parc)
        h_layout_parc.addWidget(self.button_execute)

        self.button_resume = QTextBrowser()
        h_layout_execute.addWidget(self.comb_selection_parc)
        h_layout_execute.addWidget(self.button_resume)

        self.comb_selection_parc.setMinimumSize(30, 40)
        self.button_resume.setMaximumSize(200, 40)

        # h_layout_execute.addWidget(self.comb_selection_parc)
        # h_layout_execute.addWidget(self.button_execute)


class InfosGenerale(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)

        self.displayInfos()
        # self.goSetChangeValue('Arsac 1')

    def displayInfos(self):
        N2 = 16

        self.label_used = self.getLabel()

        self.label = [self.makeDisplay(elt, 1) for elt in self.label_used if (self.label_used.index(elt) < N2)] \
                     + [self.makeDisplay(elt, 2) for elt in self.label_used if
                        ((self.label_used.index(elt) >= N2) and (self.label_used.index(elt) < 24))]

        self.textbrowser = [self.makeDisplay(str(elt), 3) for elt in range(0, len(self.label_used))]

        layout = QGridLayout()
        self.setLayout(layout)
        for i in range(N2, len(self.label)):
            self.label[i].addItems(self.label_used)
            self.label[i].setCurrentText(self.label_used[i])
        n = 3
        for i in range(0, int(len(self.label))):

            if i < int(len(self.label) / n):
                layout.addWidget(self.label[i], i, 0)
                layout.addWidget(self.textbrowser[i], i, 1)
            elif i >= int(len(self.label) / n) and (i < 2 * int(len(self.label) / n)):
                layout.addWidget(self.label[i], i - int(len(self.label) / n), 2)
                layout.addWidget(self.textbrowser[i], i - int(len(self.label) / n), 3)
            else:
                layout.setColumnStretch(4, 1)
                layout.addWidget(self.label[i], i - 2 * int(len(self.label) / n), 4)
                layout.addWidget(self.textbrowser[i], i - 2 * int(len(self.label) / n), 5)

        layout.addWidget(self.makeDisplay('Commentaire', 1), 9, 0)
        layout.addWidget(self.makeDisplay('Commentaire', 3), 10, 0, 10, 6)

    def setChangeValue(self, i):
        self.textbrowser[i].setText('R :' + self.out[self.label[i].currentText()])

    def goSetChangeValue(self, curent=None):
        self.out = self.computeOutput(curent)
        for i in range(0, len(self.label)):
            self.textbrowser[i].setText(self.out[self.label_used[i]])

        self.label[16].currentIndexChanged['QString'].connect(lambda: self.setChangeValue(16))
        self.label[17].currentIndexChanged['QString'].connect(lambda: self.setChangeValue(17))
        self.label[18].currentIndexChanged['QString'].connect(lambda: self.setChangeValue(18))
        self.label[19].currentIndexChanged['QString'].connect(lambda: self.setChangeValue(19))
        self.label[20].currentIndexChanged['QString'].connect(lambda: self.setChangeValue(20))
        self.label[21].currentIndexChanged['QString'].connect(lambda: self.setChangeValue(21))
        self.label[22].currentIndexChanged['QString'].connect(lambda: self.setChangeValue(22))
        self.label[23].currentIndexChanged['QString'].connect(lambda: self.setChangeValue(23))

    def initialize(self):
        self.textBrowser_comment.clear()
        for i in range(0, min(len(self.label_col1), len(self.label_col2))):
            self.infos_col1[i].clear()
            self.infos_col2[i].clear()

    def computeOutput(self, nom_parc=None):
        parc = Parc(nom_parc)
        x = {'Nom du parc': parc.nom,
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
             'Commentaire': parc.commentaire,
             }
        return x

    def getLabel(self):
        x = self.computeOutput()
        return list(x.keys())[:24]


class Navigation(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)
        h_layout = QHBoxLayout()
        self.selection = [QRadioButton(elt) for elt in self.label.list_app]
        self.selection[0].setChecked(True)

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
        self.data = Data(False)

        self.nav = Navigation(self, self.config.nav)
        self.app = CadreApp(self, self.config.app)
        self.select = SelectionFonction(self.app, self.config.select)

        self.infos = InfosGenerale(self.app, self.config.infos)

        self.initialize()

        self.select.check_solaire.clicked.connect(self.update)
        self.select.check_eolien.clicked.connect(self.update)
        self.select.check_update.clicked.connect(self.update)

        self.select.button_execute.clicked.connect(self.display)
        self.select.comb_selection_parc.currentIndexChanged['QString'].connect(self.display)

    def update(self):
        solaire = self.select.check_solaire.isChecked()
        eolien = self.select.check_eolien.isChecked()
        update = self.select.check_update.isChecked()
        self.select.comb_selection_parc.clear()
        if update:
            self.data = Data(True)

        liste = self.data.dfsolar.index
        if solaire and not eolien:
            liste = self.data.dfsolar.index
        elif eolien and not solaire:
            liste = self.data.dfwind.index
        elif solaire and eolien:
            liste = self.data.dfparc.index
        elif not solaire and not eolien:
            self.select.check_solaire.setChecked(True)
            liste = self.data.dfsolar.index
        self.liste = liste
        self.select.comb_selection_parc.addItems(self.liste)

    def initialize(self):
        self.select.button_update.hide()
        self.select.button_execute.hide()
        self.update()
        self.display()

    def display(self):
        self.current = self.select.comb_selection_parc.currentText()
        self.infos.goSetChangeValue(self.current)


def go():
    app = QApplication(sys.argv)
    screen = Fenetre()

    screen.showMaximized()
    app.exec_()


if __name__ == "__main__":
    go()
