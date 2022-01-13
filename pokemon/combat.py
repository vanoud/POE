from pokemon import Pokemon

class Combattre():
    #ici on passe en parametre Pokemon pour definir qu'on passe un objet class pokemon
    def __init__(self, attaquant : Pokemon,cible :Pokemon):
        
        self._attaquant = attaquant
        self._cible = cible
        
        
    
    def attaquer(self):
        

        self._cible._hp = self._cible._hp - self._attaquant._atk

        return f"{self._attaquant._nom} attaque {self._cible._nom} il lui reste {self._cible._hp} PV"
        
        #attanquant.attaquer(defenseur)
    
