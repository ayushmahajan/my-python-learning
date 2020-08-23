"""
In this code sample we are going to look at the usage of super() and how it makes inheritance
complete. Prior knowledge of inheritance is required to understand this simple concept.
Please go to the list of items to refresh Inheritance and then come back to add a new feather
to your OOP cap.
"""


class Animal:
    def __init__(self, name, _weight, food):
        self.name = name
        self._weight = _weight
        self.food = food

    def weight(self):
        return "{}'s weight is {} pounds".format(self.name, self._weight)

    def eats(self):
        return "{} eats {}".format(self.name, self.food)


class Herbivore(Animal):  # syntax to inherit
    """
    The methods defined in Animal class can be defined separately for both Herbivore
    and the Carnivore class. But this will lead to code duplication. More importantly,
    if there is some issue in one of the classes there are chances that we'll need to
    rectify it at several places.
    """
    def __init__(self, name, weight, food):
        super().__init__(name, weight, food)  # super() just helps us to call the parent class's methods


class Carnivore(Animal):
    def __init__(self, name, weight, food):
        """
        Similar to Herbivores the Carnivores do the same thing as other animals. So, we have an Animal class.
        We create our own init method but we call the super() method to use our Animal class's init().
        We can add our own methods applicable only for Carnivores. For eg: hunt()
        """
        super().__init__(name, weight, food)

    def hunt(self):
        return "{} is going to hunt it's prey".format(self.name)


class Wolf(Carnivore):
    """
    Observe. Our Wolf class doesn't have an __init__() method. Because it's parent has one.
    Also, we are overriding the hunt() method here. We are using the hunt() method of the parent class
    i.e. Carnivore class and adding the smell attribute just for the wolves.
    """
    def hunt(self):
        hunt = super().hunt()
        return "{} smells and then {}".format(self.name, hunt)


if __name__ == '__main__':
    """
    We can access the attributes of the Animal class via elephant and tiger instances.
    """
    elephant = Herbivore("Elephant", 6000, "sugarcane")  # weight in lbs
    tiger = Carnivore("Tiger", 800, "meat")

    wolf = Wolf("wolf", 300, "meat")
    print(wolf.hunt())
