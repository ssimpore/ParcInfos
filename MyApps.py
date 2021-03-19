import sys
from PyQt5.QtWidgets import QFrame, QTextBrowser, QRadioButton, QPushButton, QComboBox, \
    QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui
from PlantClasses import Parametre, Parc,ScreenConfig


class TextBrowser(QTextBrowser):
    def __init__(self, nom=None):
        QTextBrowser.__init__(self)
        self.nom = nom


class Label(QLabel):
    def __init__(self, nom):
        QLabel.__init__(self, nom)


class RadioButton(QRadioButton):
    def __init__(self, nom):
        QRadioButton.__init__(self, nom)


class PushButton(QPushButton):
    def __init__(self, nom):
        QPushButton.__init__(self, nom)


class Cadre(QFrame):
    def __init__(self, parent=None, config=None):
        QFrame.__init__(self, parent)
        if config is not None:
            self.setGeometry(QtCore.QRect(config[0], config[1], config[2], config[3]))
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Raised)
        self.param = Parametre()


class CadreApp(Cadre):
    def __init__(self, parent, config):
        Cadre.__init__(self, parent, config)


class SelectionFonction(Cadre):
    def __init__(self, parent, config):
        Cadre.__init__(self, parent, config)
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
    def __init__(self, parent, config):
        Cadre.__init__(self, parent, config)
        layout = QGridLayout()
        self.setLayout(layout)
        self.label_col1 = [Label(elt + ' :') for elt in param.label_colone1]
        self.label_col2 = [Label(elt + ' :') for elt in param.label_colone2]
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
    def __init__(self, parent, config):
        Cadre.__init__(self, parent, config)
        h_layout = QHBoxLayout()
        self.selection = [QRadioButton(elt) for elt in param.list_app]
        self.selection[0].setChecked(True)
        for elt in self.selection:
            h_layout.addWidget(elt)
            self.setLayout(h_layout)

class Fenetre(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1300, 700)
        self.setWindowIcon(QtGui.QIcon('solar-panel.png'))
        self.setWindowTitle('Help')
        self.config = ScreenConfig()
        self.data = 4


if __name__ == "__main__":
    app = QApplication(sys.argv)
    P = Parc('Arsac 1')
    x = P.exploitant
    print(x)

    param = Parametre()

    screen = Fenetre()

    navespace = Navigation(screen, screen.config.nav)
    appspace = CadreApp(screen, screen.config.app)
    selectspace = SelectionFonction(appspace, screen.config.select)
    infosspace = InfosGenerale(appspace, screen.config.infos)

    screen.showMaximized()
    app.exec_()
