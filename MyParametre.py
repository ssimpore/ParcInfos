import sys
from PyQt5.QtWidgets import QDesktopWidget
from MyData import *


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
        w_screen = QDesktopWidget().screenGeometry().width()
        h_screen = QDesktopWidget().screenGeometry().height()
        ratio_x = w_screen / (w_screen * w_screen + h_screen * h_screen) * 1000 * 1.9
        ratio_y = h_screen / (w_screen * w_screen + h_screen * h_screen) * 1000 * 3.8

        w_nav = int(0.13 * w_screen)
        h_nav = int(0.06 * h_screen)
        x_nav = int((w_screen - w_nav) // 2)
        y_nav = int(((h_screen - h_nav) // 2) * 0.0)

        w_app = int(ratio_x * w_screen)
        h_app = int(ratio_y * h_screen)
        x_app = int((w_screen - w_app) // 2)
        y_app = h_nav + y_nav

        x_select = int(0.05 * w_app)
        y_select = int(0.08 * h_app)
        w_select = int(0.37 * w_app)
        h_select = int(0.2 * h_app)

        x_infos = int(0.05 * w_app)
        y_infos = int(0.36 * h_app)
        w_infos = int(0.9 * w_app)
        h_infos = int(0.56 * h_app)

        self.nav = (x_nav, y_nav, w_nav, h_nav)
        self.app = (x_app, y_app, w_app, h_app)
        self.select = (x_select, y_select, w_select, h_select)
        self.infos = (x_infos, y_infos, w_infos, h_infos)


if __name__ == "__main__":
    s = Screenlabel()
    print(s.x)
