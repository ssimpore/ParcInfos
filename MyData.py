import pandas as pd
import pickle
import os.path


class Data:
    verify_name = 'None'

    def verify(self, nom_parc, variable):
        if nom_parc in list(self.index):
            r = self.loc[nom_parc, variable]
        else:
            r = Data.verify_name
        if (str(r) != 'nan') and (r != Data.verify_name):
            x = r
        else:
            x = Data.verify_name
        return str(x)

    def __init__(self, new=False):
        self.index = None
        update = new or (not os.path.isfile('data'))
        if update:
            self.path = "data.xlsx"
            self.dfparc = pd.read_excel(self.path, sheet_name='Parc', index_col=1)
            self.dfagence = pd.read_excel(self.path, sheet_name='Agence', index_col=0)
            self.dfresponsable = pd.read_excel(self.path, sheet_name='Responsable', index_col=0)
            self.dfexploitant = pd.read_excel(self.path, sheet_name='Exploitant', index_col=0)
            self.dfmainteneur = pd.read_excel(self.path, sheet_name='Mainteneur', index_col=0)
            self.dfsolar = self.dfparc[self.dfparc['TECHNOLOGIE'] == 'SOLAR']
            self.dfwind = self.dfparc[self.dfparc['TECHNOLOGIE'] == 'WIND']
            self.saveDataAsPickle()

        else:
            data = self.useDataFromPickle()
            self.dfparc = data.dfparc
            self.dfagence = data.dfagence
            self.dfresponsable = data.dfresponsable
            self.dfexploitant = data.dfexploitant
            self.dfmainteneur = data.dfmainteneur
            self.dfsolar = data.dfsolar
            self.dfwind = data.dfwind

    def saveDataAsPickle(self):
        with open('data', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        # print('using New data')

    def useDataFromPickle(self):
        with open('data', 'rb') as f:
            data = pickle.load(f)
        # print('using Pickle data')
        return data

    def __repr__(self):
        return f"Taille :{len(self.dfparc)} éléments"


class Exploitant(Data):
    def __init__(self, nom_parc, new=False):
        super().__init__(new)
        self.nom = Data.verify(self.dfparc, nom_parc, 'EXPLOITANT')
        self.telephone = Data.verify(self.dfexploitant, self.nom, 'TELEPHONE')
        self.email = Data.verify(self.dfexploitant, self.nom, 'EMAIL')

    def __repr__(self):
        msg = f"Exploitant:\nNom: {self.nom}\nTel: {self.telephone}\nEmail: {self.email}"
        return msg


class Responsable(Data):
    def __init__(self, nom_parc, new=False):
        super().__init__(new)
        self.agence = Data.verify(self.dfparc, nom_parc, 'AGENCE')
        self.nom = Data.verify(self.dfresponsable, self.agence, 'NOM')
        self.telephone = Data.verify(self.dfresponsable, self.agence, 'TELEPHONE')
        self.email = Data.verify(self.dfresponsable, self.agence, 'EMAIL')

    def __repr__(self):
        msg = f"Responsable:\nNom: {self.nom}\nTel: {self.telephone}\nEmail: {self.email}"
        return msg


class Agence(Data):
    def __init__(self, nom_parc, new=False):
        super().__init__(new)
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
            super().__init__(new)
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
        super().__init__(new)
        self.strat_maint = Data.verify(self.dfparc, nom_parc, 'STRATÉGIE DE MAINTENANCE')
        self.type_full = Data.verify(self.dfparc, nom_parc, 'TYPE FULL SCOPE')
        self.N12 = Mainteneur.Niveau(Data.verify(self.dfparc, nom_parc, 'MAINTENEUR 1&2'))
        self.N34 = Mainteneur.Niveau(Data.verify(self.dfparc, nom_parc, 'MAINTENEUR 3&4'))
        self.FSC = Mainteneur.Niveau(Data.verify(self.dfparc, nom_parc, 'MAINTENEUR FULL SCOPE'))

    def __repr__(self):
        msg = f"STRATÉGIE DE MAINTENANCE :{self.strat_maint}\n\nMainteneur 1&2 :\nNom: {self.N12} \n\nMainteneur 3&4 :\nNom: {self.N34} \n\nMainteneur Full Scope :\nNom: {self.FSC}"
        return msg


class Parc(Data):
    def verify(self, nom, **kwargs):
        if nom in list(self.index):
            r = nom
        else:
            r = Data.verify_name
        return r

    def __init__(self, nom_parc, new=False):
        super().__init__(new)
        self.index = None
        self.nom = Parc.verify(self.dfparc, nom_parc, )
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


if __name__ == "__main__":
    x = Parc('Arsac 1')
    print(x.mainteneur.N12)




