
class Pokemon():

    _nom : str = ""
    _hp : int = 0
    _atk : int = 0

    def __init__(self,nom,atk,hp):
        self._nom = nom
        self._atk = atk
        self._hp = hp

    @property
    def nom(self):
        return self._nom
    @property
    def atk(self):
        return self._atk
    @atk.setter
    def atk(self,value):
        self._atk = value
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,value):
        self._hp = value


    def IsDead(self):
        status = bool
        pass

    def presentation(self):
        return f"je suis un Pokemon qui s'appel"

    def statistic(self):
        return f" j'ai {self._atk} d'attaque et {self._hp} points de vie"
    