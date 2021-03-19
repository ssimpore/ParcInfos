import sys
from PyQt5.QtWidgets import QFrame, QTextBrowser, QRadioButton, QPushButton, QComboBox, \
    QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QApplication, QDesktopWidget
from PyQt5 import QtCore, QtGui
from MyData import Data
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
        X = positionsize
        if X is not None:
            self.setGeometry(QtCore.QRect(X[0], X[1], X[2], X[3]))
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
        self.selection[0].setChecked(True)
        for elt in self.selection:
            v_layout_list_option.addWidget(elt)
        v_layout_combo_execute.addWidget(self.comb_selection_parc)
        v_layout_combo_execute.addWidget(self.button_selection)
        self.setLayout(h_layout_selection)


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

        self.comment = TextBrowser()
        self.label_comment = Label('Commentaire :')
        layout.addWidget(self.label_comment, 9, 0)
        layout.addWidget(self.comment, 10, 0, 10, 4)


class Navigation(Cadre):
    def __init__(self, parent=None, positionsize=None, new=False):
        super().__init__(parent, positionsize, new)
        h_layout = QHBoxLayout()
        self.selection = [QRadioButton(elt) for elt in self.param.list_app]
        self.selection[0].setChecked(True)
        for elt in self.selection:
            h_layout.addWidget(elt)
            self.setLayout(h_layout)


class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1300, 700)
        self.setWindowIcon(QtGui.QIcon('solar-panel.png'))
        self.setWindowTitle('Help')
        self.config = ScreenConfig()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Fenetre()
    new = False
    navespace = Navigation(screen, screen.config.nav, new)
    appspace = CadreApp(screen, screen.config.app)
    selectspace = SelectionFonction(appspace, screen.config.select)
    infosspace = InfosGenerale(appspace, screen.config.infos)
    screen.showMaximized()
    app.exec_()
