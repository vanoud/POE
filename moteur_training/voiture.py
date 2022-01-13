from engin_motorise import Engin_motorise
from moteur import Moteur
from engin_motorise import Engin_motorise

class voiture(Engin_motorise):

    def __init__(self, marque, moteur: Moteur):
        super().__init__(marque, moteur)

    def reculer(self):
        return f"la voiture de marque {self.marque} recule"
