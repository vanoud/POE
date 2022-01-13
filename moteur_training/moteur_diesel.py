from moteur_thermique import Moteur_thermique

class moteur_diesel(Moteur_thermique):
    
    def __init__(self,puissance):
        super().__init__(puissance)
      

    def decrire(self):

        return f"je suis un moteur dieslel{self._carburant}"

    def augmenter_tours(self):
        return super().augmenter_tours() + "vroum poluant"