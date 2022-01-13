#dependance de Garage
from person import Person


class Conducteur(Person):

    def __init__(self, nom, age,garage: Garage):
        super().__init__(nom, age)
        self._garage = garage


    def presenter_garage(self):
        print(f"{self.presenter_garage_complet.()}")    #surcharge de methode pour appeler methode parent
    
    def display_pres(self):
        return f"je suis le conducteur {super().display_pres()}"