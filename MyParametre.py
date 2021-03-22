import sys
from PyQt5.QtWidgets import QDesktopWidget

from MyData import Parc


class Screenlabel:
    def __init__(self):
        self.list_app = ['INFOS', 'ALERTE']
        self.list_option = ['Informations générales', 'Informations ACR (ENEDIS)', 'Informations COM (IP)',
                            'Informations autres']
        self.list_option = ['Informations générales', 'Autres Informations']

        parc = Parc()

        self.x = {'Nom du parc': parc.nom,
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

        self.label = self.x.keys()

    def __repr__(self):
        msg = f"Label d'affichage"
        return msg

class ScreenConfig:
    def __init__(self):
        k_w_app = 0.7
        k_h_app=0.8
        k_nav = 0.0
        k_w_select = 0.35
        k_h_select = 0.22

        w_screen = QDesktopWidget().screenGeometry().width()
        h_screen = QDesktopWidget().screenGeometry().height()

        w_nav = int(0.15 * w_screen)
        h_nav = int(0.07 * h_screen)

        x_nav = int((w_screen - w_nav) // 2)
        y_nav = int(k_nav * h_screen)

        w_app = int(k_w_app * w_screen)
        h_app = int(k_h_app * h_screen)
        x_app = int((w_screen - w_app) // 2)
        y_app = int(h_nav + y_nav)

        x_select = int(0.04 * w_app)
        y_select = int(0.04 * w_app)

        w_select = int(k_w_select * w_app)
        h_select = int(k_h_select * h_app)

        x_infos = int(x_select)
        y_infos = int(h_select + 2 * y_select)

        w_infos = int(w_app - 2 * y_select)
        h_infos = int(h_app - h_select - +3 * x_infos)

        self.nav = (x_nav, y_nav, w_nav, h_nav)
        self.app = (x_app, y_app, w_app, h_app)
        self.select = (x_select, y_select, w_select, h_select)
        self.infos = (x_infos, y_infos, w_infos, h_infos)

#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     config = ScreenConfig()
#     screen = QMainWindow()
#
#     nav = Cadre(screen, config.nav)
#     app1 = Cadre(screen, config.app)
#     select = Cadre(app1, config.select)
#     infos = Cadre(app1, config.infos)
#
#     screen.showMaximized()
#     app.exec_()
