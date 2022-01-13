from abc import ABC, abstractmethodclass Animal(ABC):
    """    ABC permet de définir une classe abstraite. Cette classe n'a pas vocation à être instanciée et ne sert qu'à définir le comportement commun des classes qui en héritent    Il permet d'utiliser l'annotation abstractmethod    """
    @abstractmethod def marcher_a_quatre_pattes(self):
        return " marche à quatre pattes"


class Chat(Animal):
    def miauler(self):
        print("miaou")

    def marcher_a_quatre_pattes(self):
        return "le chat" + super().marcher_a_quatre_pattes()


class Chien(Animal):
    def aboyer(self):
        print("ouaf")

    def marcher_a_quatre_pattes(self):
        return "le chien" + super().marcher_a_quatre_pattes()


chat = Chat()
chien = Chien()
print(chat.marcher_a_quatre_pattes())
print(chien.marcher_a_quatre_pattes())
