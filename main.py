from PyQt5.QtWidgets import QApplication
from PlantClasses import Parc
from MyApps import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    P = Parc('')
    x = P.exploitant
    print(x)

    screen = Fenetre()
    navespace = Navigation(screen, screen.config.nav)
    appspace = CadreApp(screen, screen.config.app)
    selectspace = SelectionFonction(appspace, screen.config.select)
    infosspace = InfosGenerale(appspace, screen.config.infos)

    screen.showMaximized()

    print(screen.data.dfparc.head())

    app.exec_()
