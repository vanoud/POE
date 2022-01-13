
from engin_motorise import Engin_motorise


class Garage(object):
    
    liste_engin : list[Engin_motorise] = []

    def __init__(self):
        pass

    def ajouter_engin(self,engin):
        self._liste_engin.append(engin)

    def retirer_engin(self,engin):
        self._liste_engin.remove(engin)

    def presenter_garage_complet(self):
        for engin in self.liste_engin:
            print(engin)

    def presenter_motos(self):
        pass
    def presenter_voitures(self):
        pass
    def presenter_camions(self):
        pass
