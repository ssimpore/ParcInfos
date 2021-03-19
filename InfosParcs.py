import sys

from PyQt5.QtWidgets import QApplication, QDesktopWidget

from MyApps import *


def interface():
    app = QApplication(sys.argv)

    screen = Fenetre()

    config = ConfigInterface()


    navespace = Navigation(screen, config.nav)
    appspace = CadreApp(screen, config.app)
    selectspace = SelectionFonction(appspace, config.select)
    infosspace = InfosGenerale(appspace, config.infos)

    screen.showMaximized()
    app.exec_()


if __name__ == "__main__":
    interface()
