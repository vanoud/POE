from pokemon import Pokemon

class PokemonFeu(Pokemon):
    
    _type : str = ""
    
    def __init__(self,nom,atk,hp,types):
        super().__init__(nom,atk,hp)
        self._types = types

    def presentation(self):
        return f"{super().presentation()} {super().nom} de type {self._types}"
    
    def statistic(self):
        return f"{super().statistic()}"