import pandas as pd
import pickle
import os.path
from PyQt5.QtWidgets import QDesktopWidget


class NewData:
    def __init__(self, path, new=True):
        self.path = path
        self.parc = pd.read_excel(self.path, sheet_name='Parc', index_col=1)
        self.agence = pd.read_excel(self.path, sheet_name='Agence', index_col=0)
        self.responsable = pd.read_excel(self.path, sheet_name='Responsable', index_col=0)
        self.exploitant = pd.read_excel(self.path, sheet_name='Exploitant', index_col=0)
        self.mainteneur = pd.read_excel(self.path, sheet_name='Mainteneur', index_col=0)
        self.solar = self.parc[self.parc['TECHNOLOGIE'] == 'SOLAR']
        self.wind = self.parc[self.parc['TECHNOLOGIE'] == 'WIND']
        self.saveDataAsPickle()

    def saveDataAsPickle(self):
        with open('data', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def __repr__(self):
        return f"Taille :{len(self.parc)} éléments"


def getData(new=False):
    def useDataFromPickle():
        with open('data', 'rb') as f:
            data = pickle.load(f)
            return data

    update = new or (not os.path.isfile('data'))
    if update:
        data = NewData('data.xlsx')
        # print('using New data')
    else:
        data = useDataFromPickle()
        # print('using Pickle data')
    return data


class Data:
    verify_name = 'None'
    def verify(df, nom_parc, variable):
        if nom_parc in list(df.index):
            r = df.loc[nom_parc, variable]
        else:
            r = Data.verify_name
        if (str(r) != 'nan') and (r != Data.verify_name):
            x = r
        else:
            x = Data.verify_name
        return x

    def __init__(self, new=False):
        df = getData(new)
        self.dfparc = df.parc
        self.dfagence = df.agence
        self.dfresponsable = df.responsable
        self.dfexploitant = df.exploitant
        self.dfmainteneur = df.mainteneur
        self.dfsolar = df.solar
        self.dfwind = df.wind
        self.param = Parametre()



class Exploitant(Data):
    def __init__(self, nom_parc, new=False):
        Data.__init__(self, new)
        self.nom = Data.verify(self.dfparc, nom_parc, 'EXPLOITANT')
        self.telephone = Data.verify(self.dfexploitant, self.nom, 'TELEPHONE')
        self.email = Data.verify(self.dfexploitant, self.nom, 'EMAIL')

    def __repr__(self):
        msg = f"Exploitant:\nNom: {self.nom}\nTel: {self.telephone}\nEmail: {self.email}"
        return msg


class Responsable(Data):
    def __init__(self, nom_parc, new=False):
        Data.__init__(self, new)
        self.agence = Data.verify(self.dfparc, nom_parc, 'AGENCE')
        self.nom = Data.verify(self.dfresponsable, self.agence, 'NOM')
        self.telephone = Data.verify(self.dfresponsable, self.agence, 'TELEPHONE')
        self.email = Data.verify(self.dfresponsable, self.agence, 'EMAIL')

    def __repr__(self):
        msg = f"Responsable:\nNom: {self.nom}\nTel: {self.telephone}\nEmail: {self.email}"
        return msg


class Agence(Data):
    def __init__(self, nom_parc, new=False):
        Data.__init__(self, new)
        self.nom = Data.verify(self.dfparc, nom_parc, 'AGENCE')
        self.responsable = Data.verify(self.dfresponsable, self.nom, 'NOM')
        self.astreinte = Data.verify(self.dfagence, self.nom, 'N° ASTREINTE')
        self.email = Data.verify(self.dfagence, self.nom, 'EMAIL')

    def __repr__(self):
        msg = f"Agence:\nNom: {self.nom}\nAstreinte: {self.astreinte}\nEmail: {self.email}"
        return msg


class Mainteneur(Data):
    class Niveau(Data):
        def __init__(self, nom, new=False):
            Data.__init__(self, new)
            self.nom = nom
            self.telephone = Data.verify(self.dfmainteneur, self.nom, 'TELEPHONE')
            self.email_entreprise = Data.verify(self.dfmainteneur, self.nom, 'EMAIL ENTREPRISE')
            self.email_referent = Data.verify(self.dfmainteneur, self.nom, 'EMAIL REFERENT')
            self.astreinte = Data.verify(self.dfmainteneur, self.nom, 'N° ASTREINTE')
            self.num_referent = Data.verify(self.dfmainteneur, self.nom, 'N° REFERENT')

        def __repr__(self):
            msg = f"Nom: {self.nom}\nAstreinte: {self.astreinte}\nEmail: {self.email_entreprise}"
            return msg

    def __init__(self, nom_parc, new=False):
        Data.__init__(self, new)
        self.strat_maint = Data.verify(self.dfparc, nom_parc, 'STRATÉGIE DE MAINTENANCE')
        self.type_full = Data.verify(self.dfparc, nom_parc, 'TYPE FULL SCOPE')
        self.N12 = Mainteneur.Niveau(Data.verify(self.dfparc, nom_parc, 'MAINTENEUR 1&2'))
        self.N34 = Mainteneur.Niveau(Data.verify(self.dfparc, nom_parc, 'MAINTENEUR 3&4'))
        self.FSC = Mainteneur.Niveau(Data.verify(self.dfparc, nom_parc, 'MAINTENEUR FULL SCOPE'))

    def __repr__(self):
        msg = f"STRATÉGIE DE MAINTENANCE :{self.strat_maint}\n\nMainteneur 1&2 :\nNom: {self.N12} \n\nMainteneur 3&4 :\nNom: {self.N34} \n\nMainteneur Full Scope :\nNom: {self.FSC}"
        return msg


class Parc(Data):
    def verify(df, nom):
        if nom in list(df.index):
            r = nom
        else:
            r = Data.verify_name
        return r

    def __init__(self, nom_parc, new=False):
        Data.__init__(self, new)
        self.nom = Parc.verify(self.dfparc, nom_parc)
        self.trigramme = Data.verify(self.dfparc, self.nom, 'CODE')
        self.technologie = Data.verify(self.dfparc, self.nom, 'TECHNOLOGIE')
        self.statut = Data.verify(self.dfparc, self.nom, 'STATUT')
        self.agregation = Data.verify(self.dfparc, self.nom, 'AGRÉGATION')
        self.recette = Data.verify(self.dfparc, self.nom, 'RÉCETTE À FAIRE')
        self.cardi = Data.verify(self.dfparc, self.nom, 'N°CARD-I')
        self.pdl = Data.verify(self.dfparc, self.nom, 'POSTE DE LIVRAISON')
        self.psource = Data.verify(self.dfparc, self.nom, 'POSTE SOURCE')
        self.depart = Data.verify(self.dfparc, self.nom, 'DÉPART')
        self.num_acr = Data.verify(self.dfparc, self.nom, 'N° ACR')
        self.server = Data.verify(self.dfparc, self.nom, 'SERVEUR PARC')
        self.ip_sdrt = Data.verify(self.dfparc, self.nom, 'IP SDRT/RIO PDL')
        self.ip_asa = Data.verify(self.dfparc, self.nom, 'IP ASA')
        self.ip_adsl = Data.verify(self.dfparc, self.nom, 'IP ADSL')
        self.num_adsl = Data.verify(self.dfparc, self.nom, 'N° ADSL')
        self.ip_satellite = Data.verify(self.dfparc, self.nom, 'IP SATELLITE')
        self.commentaire = Data.verify(self.dfparc, self.nom, 'COMMENTAIRE')
        self.scada = Data.verify(self.dfparc, self.nom, 'SCADA')
        self.latitude = Data.verify(self.dfparc, self.nom, 'LATITUDE')
        self.longitude = Data.verify(self.dfparc, self.nom, 'LONGITUDE')

        self.exploitant = Exploitant(self.nom)
        self.responsable = Responsable(self.nom)
        self.agence = Agence(self.nom)
        self.mainteneur = Mainteneur(self.nom)

    def __repr__(self):
        msg = f"Nom :{self.nom} ({self.trigramme})"
        return msg


class Parametre:
    def __init__(self):
        self.list_app = ['INFOS', 'ALERTE']
        self.list_option = ['Informations générales', 'Informations ACR (ENEDIS)', 'Informations COM (IP)',
                            'Informations autres']
        self.liste_parc = ['Arsac 1', 'Arsac 1', 'Salonnes 1']

        self.label_colone1 = ['Parc', 'Agence', 'Exploitant', 'Responsable', 'SCADA', 'Maintenance',
                              'N° mainteneur', 'Longitude']

        self.label_colone2 = ['Technologie', 'N° astreinte', 'N° exploitant', 'N° responsable', 'Statut parc',
                              'Mainteneur',
                              'N° astreinte maint.', 'Latitude']

        self.liste_label_sortie = ['Parc', 'Agence', 'Exploitant', 'Responsable', 'SCADA', 'Maintenance',
                                   'N° mainteneur', 'Longitude', 'Technologie', 'N° astreinte', 'N° exploitant',
                                   'N° responsable', 'Statut parc',
                                   'Mainteneur',
                                   'N° astreinte maint.', 'Latitude']


class ScreenConfig:
    def __init__(self):
        w_screen = QDesktopWidget().screenGeometry().width()
        h_screen = QDesktopWidget().screenGeometry().height()
        ratio_x = w_screen / (w_screen * w_screen + h_screen * h_screen) * 1000 * 1.6
        ratio_y = h_screen / (w_screen * w_screen + h_screen * h_screen) * 1000 * 3.5

        w_nav = int(0.13 * w_screen)
        h_nav = int(0.06 * h_screen)
        x_nav = int((w_screen - w_nav) // 2)
        y_nav = int(((h_screen - h_nav) // 2) * 0.1)

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
        self.data = ['Arsac 1', 'Arsac 2', 'Arsac 3']


if __name__ == '__main__':
    # datapath = 'data.xlsx'
    P = Parc('Aéroport de Montpellier')
    x = P.mainteneur.N12.telephone
    print(x)
