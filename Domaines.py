class Domaines:
    def __init__(self, domaine="", complement=""):
        self.domaine = domaine
        self.complement = complement

    # region Getter Setter
    def getDomaine(self):
        return self.domaine

    def getComplement(self):
        return self.complement

    def setDomaine(self, domaine):
        self.domaine = domaine

    def setComplement(self, complement):
        self.complement = complement

    # endregion

    def __str__(self):
        return "Domaine : {} \nComplement : {}".format(self.domaine, self.complement)
