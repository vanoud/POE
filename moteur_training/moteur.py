from engin_motorise import Engin_motorise
#dependance de engin motorise
class Moteur():

    def __init__(self) -> None:
        self._puisance = puissance

        @property
        def puissance(self):
            return self._puissance
        
        @puissance.setter
        def puissance(self,value):
            self._puisance = value

    def augmenter_tours(self):
        return f"le moteur fait plus de bruit"