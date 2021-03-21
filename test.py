
cles, vals = ['a', 'gh', 'er', 'b'], [1, 2, 1, 2]
hist = {a:b for a, b in zip(cles, vals)}
print(hist)

valeur = {'Parc': parc.nom,
          'Agence': parc.agence.nom,
          'Exploitant': parc.exploitant.nom,
          'Responsable': parc.responsable.nom,
          'SCADA': parc.scada,
          'Maintenance': parc.mainteneur.strat_maint,
          'Referent maint': parc.mainteneur.N12.num_referent,
          'Longitude': parc.longitude,
          'Technologie': parc.technologie,
          'Numero Astreinte': parc.agence.astreinte,
          'Numero exploitant': parc.exploitant.telephone,
          'Numero responsable': parc.responsable.telephone,
          'Statut parc': parc.statut,
          'Mainteneur': parc.mainteneur.N12.nom,
          'Astreinte maint': parc.mainteneur.N12.astreinte,
          'latitude': parc.latitude}


def display(self):
    layout = QGridLayout()
    self.setLayout(layout)
    self.label_col1 = [Label(elt + ' :') for elt in self.label1]
    self.label_col2 = [Label(elt + ' :') for elt in self.label2]

    self.infos_col1 = [TextBrowser(elt) for elt in range(0, min(len(self.label_col1), len(self.label_col2)))]
    self.infos_col2 = [TextBrowser(elt) for elt in range(0, min(len(self.label_col1), len(self.label_col2)))]

    for i in range(0, min(len(self.label_col1), len(self.label_col2))):
        layout.addWidget(self.label_col1[i], i, 0)
        layout.addWidget(self.infos_col1[i], i, 1)
        layout.addWidget(self.label_col2[i], i, 2)
        layout.addWidget(self.infos_col2[i], i, 3)

    self.textBrowser_comment = TextBrowser()
    self.label_comment = Label('Commentaire :')
    layout.addWidget(self.label_comment, 9, 0)
    layout.addWidget(self.textBrowser_comment, 10, 0, 10, 4)


def display1(self):
    layout = QGridLayout()
    self.setLayout(layout)
    self.label = [Label(elt + ' :') for elt in self.label]
    self.infos = [TextBrowser(elt) for elt in range(0, len(self.label))]

    for i in range(0, int(len(self.label))):
        if i < int(len(self.label) / 2):
            layout.addWidget(self.label[i], i, 0)
            layout.addWidget(self.infos[i], i, 1)
        else:
            layout.addWidget(self.label[i], i - int(len(self.label) / 2), 2)
            layout.addWidget(self.infos[i], i - int(len(self.label) / 2), 3)

    self.textBrowser_comment = TextBrowser()
    self.label_comment = Label('Commentaire :')
    layout.addWidget(self.label_comment, 9, 0)
    layout.addWidget(self.textBrowser_comment, 10, 0, 10, 4)


