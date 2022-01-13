from moteur_thermique import Moteur_thermique

class Moteur_essence(Moteur_thermique):
    
    def __init__(self,puissance) -> None:
        super().__init__(puissance)

    def decrire(self):
        return f"moteur essence"

    def augmenter_tours(self):
        return super().augmenter_tours() 