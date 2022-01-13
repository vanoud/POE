from moteur import Moteur

# dependance


class Engin_motorise(object):

    # ici on met moteur en argument pour lui passer la methode moteur moteur(essence,150chevaux)
    def __init__(self, marque, moteur: Moteur):
        self._marque = marque
        self._moteur = moteur

    @property
    def marque(self):
        return self._marque

    @property
    def moteur(self):
        return self._moteur

    @moteur.setter
    def moteur(self,value):
        self._moteur = value

    def accelerer(self):
        return f"{self.moteur.augmenter_tours()}"

    def freiner(self):
        return f"je freine"

    def decrire(self):
        return f"je suis une {self._marque}"
