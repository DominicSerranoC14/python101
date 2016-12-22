# Class
class Pet(object):

    # function that is called when an instance of a class is first created
    # self = polly, name = 'Polly', species = 'Parrot'
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    # __str__ method defines the behavior when an instance of the Pet class is used with print
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


# Subclasses
class Dog(Pet):

    # the subclass declares unique properties
    def __init__(self, name, chases_cats):
        # Need to call the parent class init function to inherit it's methods
        # Pass in "Dog" to overwrite the parent class species name
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats


class Bird(Pet):

    # the subclass declares unique properties
    def __init__(self, name, chases_cats):
        # Need to call the parent class init function to inherit it's methods
        # Pass in "Bird" to overwrite the parent class species name
        Pet.__init__(self, name, "Bird")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats


# Create a new instance of Pet
# self = polly, name = 'Polly', species = 'Parrot'
polly = Bird('Polly', False);
print(polly);
print(polly.getName());
print(polly.getSpecies());
print('Instance of Pet?', isinstance(polly, Pet))
print('Instance of Bird?',isinstance(polly, Bird))

alfred = Dog('Alfred', True);
print(alfred);
print(alfred.getName());
print(alfred.getSpecies());
print('Instance of Pet?', isinstance(alfred, Pet))
print('Instance of Dog?',isinstance(alfred, Dog))
