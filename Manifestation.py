from Domaines import *


class Manifestation:
    def __init__(self,
                 nomManifestation="",
                 codePostal="",
                 siteWeb="",
                 communePrincipal="",
                 date=None,
                 domaines=None):

        if date is None:
            date = []
        if domaines is None:
            domaines = [Domaines()]
        self.nomManifestation = nomManifestation
        self.codePostal = codePostal
        self.siteWeb = siteWeb
        self.date = date
        self.communePrincipal = communePrincipal
        self.domaines = domaines

    # region getter setter

    def setNomManifestation(self, nomManifestation):
        self.nomManifestation = nomManifestation

    def getNomManifestation(self):
        return self.nomManifestation

    def setCodePostal(self, codePostal):
        self.codePostal = codePostal

    def getCodePostal(self):
        return self.codePostal

    def getSiteWeb(self):
        return self.siteWeb

    def setSiteWeb(self, siteWeb):
        self.siteWeb = siteWeb

    def getDate(self):
        return self.date

    def setDate(self, date=None):
        if date is None:
            date = []
        self.date = date

    def getCommunePrincipal(self):
        return self.nomManifestation

    def setCommunePrincipal(self, nomManifestation):
        self.nomManifestation = nomManifestation

    def getDomaines(self):
        return self.domaines

    def setDomaines(self, domaines):
        self.domaines = domaines

    # endregion

    def __str__(self):
        string = "Manifestation : {}\nCode Postal : {}\nSite Web : {}\nDate début : {}\nDate fin : {}\nCommune " \
                 "Principal : {}\n".format(self.nomManifestation,
                                           self.codePostal,
                                           self.siteWeb,
                                           self.date[0],
                                           self.date[1],
                                           self.communePrincipal)
        return string + "\n" + self.domaines.__str__()
