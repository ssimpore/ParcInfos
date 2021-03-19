import sys
from PyQt5.QtWidgets import QDesktopWidget


class Screenlabel:
    def __init__(self):
        self.list_app = ['INFOS', 'ALERTE']
        self.list_option = ['Informations générales', 'Informations ACR (ENEDIS)', 'Informations COM (IP)',
                            'Informations autres']
        self.label_col1 = ['Parc', 'Agence', 'Exploitant', 'Responsable', 'SCADA', 'Maintenance', 'N° mainteneur',
                           'Longitude']
        self.label_col2 = ['Technologie', 'N° astreinte', 'N° exploitant', 'N° responsable', 'Statut parc',
                           'Mainteneur', 'N° astreinte maint.', 'Latitude']

    def __repr__(self):
        msg = f"Label d'affichage"
        return msg


class ScreenConfig:
    def __init__(self):
        w_screen = QDesktopWidget().screenGeometry().width()
        h_screen = QDesktopWidget().screenGeometry().height()
        ratio_x = w_screen / (w_screen * w_screen + h_screen * h_screen) * 1000 * 1.3
        ratio_y = h_screen / (w_screen * w_screen + h_screen * h_screen) * 1000 * 2.7

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
    config = ScreenConfig()
    print(config)
