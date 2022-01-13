class Moteur(object):
    _puissance: str def __init__(self, puissance) -> None:
        super().__init__()
        self._puissance = puissanceclass Bateau(object):
    _couleur: str    _moteur: Moteur def __init__(self, couleur: str, moteur: Moteur) -> None:
        super().__init__()
        self._couleur = couleur        self._moteur = moteur    @ property def couleur(self) -> str:
        return self._couleur    @ couleur.setter def couleur(self, value: str) -> None:
        self._couleur = value def __str__(self) -> str:
        return f"Le bateau est {self.couleur} et son moteur a une puissance de {self._moteur._puissance}"class AtelierPeinture(object):
    """    une méthode statique est une méthode de la classe et non dépendante d'une instance. Il évite d'avoir à utiliser le self    """    @ staticmethod def repeindre_bateau(bateau: Bateau, nouvelle_couleur: str) -> None:
        bateau.couleur = nouvelle_couleurclass GarageMecanique(object):

    @staticmethod def modifier_puissance_moteur(bateau: Bateau, nouvelle_puissance):
        bateau._moteur._puissance = nouvelle_puissancemoteur = Moteur("120")


moteur2 = moteurbateau = Bateau("bleu", moteur)
bateau2 = Bateau("rouge", moteur2)
GarageMecanique.modifier_puissance_moteur(bateau, "300")
AtelierPeinture.repeindre_bateau(bateau2, "blanc")
print(bateau)
print(bateau2)
print(moteur)
