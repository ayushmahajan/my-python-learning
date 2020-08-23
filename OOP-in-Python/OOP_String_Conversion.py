class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    First way is to add a custom method to get the description we want and
    call it every time we want to debug
    """
    def introduction(self):
        return "Hi, I'm {} and I'm {} years old".format(self.name, self.age)

    """
    Second way is to have a __str__ method defined in our class since the __str__ method gets called when we 
    print our instance. Also, we can simply add our own description for our person instance.
    """
    # def __str__(self):
    #     return "Hi, I'm {} and I'm {} years old".format(self.name, self.age)

    """
    Third way is to have a __repr__ method which can be used to print the person instance and 
    to inspect the instance while debugging. Provides us with both the __str__ and __repr__
    methods with a single method.
    """
    def __repr__(self):
        # If we don't want to re-write the class name again we can also access the __name__ method of the class
        # return "Person({self.name}, {self.age})".format(self=self)
        return "{self.__class__.__name__}({self.name}, {self.age})".format(self=self)


if __name__ == '__main__':
    person1 = Person("Ayush", 25)
    person2 = Person("Mahajan", 26)
    """
    When we only have a __init__ method inside our Person class.
    """
    # print(person1)  # Prints <__main__.Person object at 0x10e7e4210> which is not very useful in case of debugging

    """
    What if we have multiple instances of class person and we want to get the person instance named Ayush. 
    Since just printing the instance gives us a little to no value we need a brief description everytime
    we print the instance of class Person.
    """
    # First way
    # print(person1.introduction())  # We need to call this method instead of just simply printing the person object
    # print(person2.introduction())

    # Second way: Better and more Pythonic
    """
    We can use the dunder(or double underscore) __str__ method (or the magic method)
    """
    # print(person1)  # Prints Hi, I'm Ayush and I'm 25 years old

    """
    Now, the __str__ method can be used in all of our classes to have a nice description of
    each person instance we print. But this isn't useful as a developer. Since, the only thing
    str provides us with is the description of our person instance and not how the instance was
    actually created in the first place which is useful to know for debugging purposes.
    """

    # Third way: Getting better of both worlds
    """
    We will implement __repr__ method. Since __str__ internally calls the repr method
    we will get the best of both repr and str.
    """
    print(person1)  # calls the __str__ method which internally call the __repr__ method
