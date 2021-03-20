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
        self.param = Screenlabel()


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

        self.selection = [RadioButton(elt) for elt in self.param.list_option]
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
        layout = QGridLayout()
        self.setLayout(layout)
        self.label_col1 = [Label(elt + ' :') for elt in self.param.label_col1]
        self.label_col2 = [Label(elt + ' :') for elt in self.param.label_col2]
        self.infos_col1 = [TextBrowser(elt) for elt in
                           range(0, min(len(self.label_col1), len(self.label_col2)))]
        self.infos_col2 = [TextBrowser(elt) for elt in
                           range(0, min(len(self.label_col1), len(self.label_col2)))]

        for i in range(0, min(len(self.label_col1), len(self.label_col2))):
            layout.addWidget(self.label_col1[i], i, 0)
            layout.addWidget(self.infos_col1[i], i, 1)
            layout.addWidget(self.label_col2[i], i, 2)
            layout.addWidget(self.infos_col2[i], i, 3)

        self.textBrowser_comment = TextBrowser()
        self.label_comment = Label('Commentaire :')
        layout.addWidget(self.label_comment, 9, 0)
        layout.addWidget(self.textBrowser_comment, 10, 0, 10, 4)

    def initialize(self):
        self.textBrowser_comment.clear()
        for i in range(0, min(len(self.label_col1), len(self.label_col2))):
            self.infos_col1[i].clear()
            self.infos_col2[i].clear()

    def setValue(self, parc):
        self.infos_col1[0].setText(parc.nom+' ('+parc.trigramme+')')
        self.infos_col1[1].setText(parc.agence.nom)
        self.infos_col1[2].setText(parc.exploitant.nom)
        self.infos_col1[3].setText(parc.responsable.nom)
        self.infos_col1[4].setText(parc.scada)
        self.infos_col1[5].setText(parc.mainteneur.strat_maint)
        self.infos_col1[6].setText(parc.mainteneur.N12.num_referent)
        self.infos_col1[7].setText(parc.longitude)

        self.infos_col2[0].setText(parc.technologie)
        self.infos_col2[1].setText(parc.agence.astreinte)
        self.infos_col2[2].setText(parc.exploitant.telephone)
        self.infos_col2[3].setText(parc.responsable.telephone)
        self.infos_col2[4].setText(parc.statut)
        self.infos_col2[5].setText(parc.mainteneur.N12.nom)
        self.infos_col2[6].setText(parc.mainteneur.N12.astreinte)
        self.infos_col2[7].setText(parc.latitude)

        self.textBrowser_comment.setText(parc.commentaire)


class Navigation(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)
        h_layout = QHBoxLayout()
        self.selection = [QRadioButton(elt) for elt in self.param.list_app]

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

    selectspace.initialize()
    navespace.initialize()
    infosspace.initialize()
    P = Parc(selectspace.comb_selection_parc.currentText())
    infosspace.setValue(P)

    def ok():
        P = Parc(selectspace.comb_selection_parc.currentText())
        infosspace.setValue(P)

    selectspace.button_selection.clicked.connect(ok)

    screen.showMaximized()
    app.exec_()


if __name__ == "__main__":
    go()
