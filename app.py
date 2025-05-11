class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe
        self.__secret_identity = None  # Encapsulated attribute

    def set_secret_identity(self, identity):
        self.__secret_identity = identity

    def get_secret_identity(self):
        return self.__secret_identity

    def describe(self):
        return f"{self.name} from {self.universe} uses {self.power} to fight evil!"

    def fight(self):
        return f"{self.name} attacks with {self.power}!"
