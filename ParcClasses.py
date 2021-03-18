
def verify1(x):
    if str(x) != 'nan':
        x = x
    else:
        x = 'Non attribé'
    return x


def verify2(df, nom_parc, variable):
    if nom_parc != 'Non attribé':
        result = df.loc[nom_parc, variable]
    else:
        result = 'Non attribé'
    return result


class Exploitant:
    def __init__(self, df, nom_parc):
        self.nom = verify1(df.parc.loc[nom_parc, 'EXPLOITANT'])
        self.telephone = verify2(df.exploitant, self.nom, 'TELEPHONE')
        self.email = verify2(df.exploitant, self.nom, 'EMAIL')

    def __repr__(self):
        msg = f"Exploitant : {self.nom} ({self.telephone})"
        return msg


class Responsable:
    def __init__(self, df, nom_parc):
        self.agence = verify1(df.parc.loc[nom_parc, 'AGENCE'])
        self.nom = verify2(df.responsable, self.agence, 'NOM')
        self.telephone = verify2(df.responsable, self.agence, 'TELEPHONE')
        self.email = verify2(df.responsable, self.agence, 'EMAIL')

    def __repr__(self):
        msg = f"Responsable : {self.nom} ({self.agence})"
        return msg


class Agence:
    def __init__(self, df, nom_parc):
        self.nom = verify1(df.parc.loc[nom_parc, 'AGENCE'])
        self.responsable = verify2(df.responsable, self.nom, 'NOM')
        self.astreinte = verify2(df.agence, self.nom, 'N° ASTREINTE')
        self.email = verify2(df.agence, self.nom, 'EMAIL')

    def __repr__(self):
        msg = f"Agence : {self.nom} ({self.responsable})"
        return msg


class Niveau:
    def __init__(self, df, nom):
        self.nom = nom
        self.telephone = verify2(df.mainteneur, self.nom, 'TELEPHONE')
        self.email_entreprise = verify2(df.mainteneur, self.nom, 'EMAIL ENTREPRISE')
        self.email_referent = verify2(df.mainteneur, self.nom, 'EMAIL REFERENT')
        self.astreinte = verify2(df.mainteneur, self.nom, 'N° ASTREINTE')
        self.num_referent = verify2(df.mainteneur, self.nom, 'N° REFERENT')

    def __repr__(self):
        msg = f"{self.nom} "
        return msg


class Mainteneur:
    def __init__(self, df, nom_parc):
        self.N12 = Niveau(df, verify1(df.parc.loc[nom_parc, 'MAINTENEUR 1&2']))
        self.N34 = Niveau(df, verify1(df.parc.loc[nom_parc, 'MAINTENEUR 3&4']))
        self.FSC = Niveau(df, verify1(df.parc.loc[nom_parc, 'MAINTENEUR FULL SCOPE']))
        self.type = verify1(df.parc.loc[nom_parc, 'STRATÉGIE DE MAINTENANCE'])


    def __repr__(self):
        msg = f"N12 : {self.N12} N34 : {self.N34} FSC : {self.FSC}"
        return msg


class Parc:
    def __init__(self, df, nom):
        self.nom = nom
        self.trigramme = verify1(df.parc.loc[self.nom, 'CODE'])
        self.technologie = verify1(df.parc.loc[self.nom, 'TECHNOLOGIE'])
        self.statut = verify1(df.parc.loc[nom, 'STATUT'])
        self.agregation = verify1(df.parc.loc[nom, 'AGRÉGATION'])
        self.recette = verify1(df.parc.loc[nom, 'RÉCETTE À FAIRE'])
        self.cardi = verify1(df.parc.loc[nom, 'N°CARD-I'])
        self.pdl = verify1(df.parc.loc[nom, 'POSTE DE LIVRAISON'])
        self.psource = verify1(df.parc.loc[nom, 'POSTE SOURCE'])
        self.depart = verify1(df.parc.loc[nom, 'DÉPART'])
        self.num_acr = verify1(df.parc.loc[nom, 'N° ACR'])
        self.server = verify1(df.parc.loc[nom, 'SERVEUR PARC'])
        self.ip_sdrt = verify1(df.parc.loc[nom, 'IP SDRT/RIO PDL'])
        self.ip_asa = verify1(df.parc.loc[nom, 'IP ASA'])
        self.ip_adsl = verify1(df.parc.loc[nom, 'IP ADSL'])
        self.num_adsl = verify1(df.parc.loc[nom, 'N° ADSL'])
        self.ip_satellite = verify1(df.parc.loc[nom, 'IP SATELLITE'])
        self.commentaire = verify1(df.parc.loc[nom, 'COMMENTAIRE'])
        self.scada = verify1(df.parc.loc[nom, 'SCADA'])
        self.latitude = verify1(str(df.parc.loc[nom, 'LATITUDE']))
        self.longitude = verify1(str(df.parc.loc[nom, 'LONGITUDE']))

        self.exploitant = Exploitant(df, self.nom)
        self.responsable = Responsable(df, self.nom)
        self.agence = Agence(df, self.nom)
        self.mainteneur = Mainteneur(df, self.nom)

    def __repr__(self):
        return f"Parc : {self.nom} ({self.trigramme})"


if __name__ == "__main__":
    link = 'data.xlsx'
    #data = getData(link)
    #P = Parc(data, 'Arsac 1')
    #print(P.exploitant.nom)