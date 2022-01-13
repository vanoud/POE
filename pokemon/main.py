from pokemon import Pokemon
from feu import PokemonFeu
from eau import PokemonEau
from combat import Combattre


Salameche = PokemonFeu("salameche",7,5,"feu")
print(Salameche.presentation())
Salameche._hp = 2 #ici on set à 2 les hp on peut imaginer faire une fonction retiré des pv en cas d'attaque 
print(Salameche.statistic())

Carapuce = PokemonEau("Carapuce",5,8,"eau")
print(Carapuce.presentation())
print(Carapuce.statistic())


c = Combattre(Salameche,Carapuce)
print(c.attaquer())

# Combat.lancer_combat(Salameche,Carapuce)

