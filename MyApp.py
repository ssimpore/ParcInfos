import sys
from PyQt5.QtWidgets import QFrame, QTextBrowser, QRadioButton, QPushButton, QComboBox, \
    QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QApplication, QDesktopWidget
from PyQt5 import QtCore, QtGui
from MyData import *
from MyParametre import ScreenConfig,Affichage


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
    def __init__(self, parent=None, config=None, new=False):
        QFrame.__init__(self, parent)
        if config is not None:
            self.setGeometry(QtCore.QRect(config[0], config[1], config[2], config[3]))
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameShadow(QFrame.Raised)
        self.data = Data("data.xlsx", new)
        self.param = Affichage()

class CadreApp(Cadre):
    def __init__(self, parent, config, new=False):
        Cadre.__init__(self, parent, config, new)


class SelectionFonction(Cadre):
    def __init__(self, parent, config, new=False):
        Cadre.__init__(self, parent, config, new)
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
    def __init__(self, parent, config, new=False):
        Cadre.__init__(self, parent, config, new)
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
    def __init__(self, parent, config, new=False):
        Cadre.__init__(self, parent, config, new)
        h_layout = QHBoxLayout()
        self.selection = [QRadioButton(elt) for elt in self.param.list_app]
        self.selection[0].setChecked(True)
        for elt in self.selection:
            h_layout.addWidget(elt)
            self.setLayout(h_layout)


# class ScreenConfig:
#     def __init__(self):
#         w_screen = QDesktopWidget().screenGeometry().width()
#         h_screen = QDesktopWidget().screenGeometry().height()
#         ratio_x = w_screen / (w_screen * w_screen + h_screen * h_screen) * 1000 * 1.6
#         ratio_y = h_screen / (w_screen * w_screen + h_screen * h_screen) * 1000 * 3.5
#
#         w_nav = int(0.13 * w_screen)
#         h_nav = int(0.06 * h_screen)
#         x_nav = int((w_screen - w_nav) // 2)
#         y_nav = int(((h_screen - h_nav) // 2) * 0.1)
#
#         w_app = int(ratio_x * w_screen)
#         h_app = int(ratio_y * h_screen)
#         x_app = int((w_screen - w_app) // 2)
#         y_app = h_nav + y_nav
#
#         x_select = int(0.05 * w_app)
#         y_select = int(0.08 * h_app)
#         w_select = int(0.37 * w_app)
#         h_select = int(0.2 * h_app)
#
#         x_infos = int(0.05 * w_app)
#         y_infos = int(0.36 * h_app)
#         w_infos = int(0.9 * w_app)
#         h_infos = int(0.56 * h_app)
#
#         self.nav = (x_nav, y_nav, w_nav, h_nav)
#         self.app = (x_app, y_app, w_app, h_app)
#         self.select = (x_select, y_select, w_select, h_select)
#         self.infos = (x_infos, y_infos, w_infos, h_infos)
#         self.data = ['Arsac 1', 'Arsac 2', 'Arsac 3']


class Fenetre(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
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
