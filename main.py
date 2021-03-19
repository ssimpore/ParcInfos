import sys
from PyQt5.QtWidgets import QApplication
from MyApp import Fenetre, Navigation, CadreApp, SelectionFonction, InfosGenerale

if __name__ == "__main__":
    new = 0
    app = QApplication(sys.argv)
    screen = Fenetre()
    navespace = Navigation(screen, screen.config.nav, new)
    appspace = CadreApp(screen, screen.config.app)
    selectspace = SelectionFonction(appspace, screen.config.select)
    infosspace = InfosGenerale(appspace, screen.config.infos)
    screen.showMaximized()
    app.exec_()
