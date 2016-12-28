# Your job is to think about additional classes that can be inherited by groups of your classes. Think about the examples that you were shown in live-coding.

# Animal multiple inheritance
class Animal:
    ''' Creates a new Animal '''
    def __init__(self, name, species):
        self.name = name;
        self.species = species;

    ##########################################

class Fish:
    ''' Creates a new Fish '''
    def __init__(self, fins = 2):
        self.fins = fins;

    ##########################################

class Mammal:
    ''' Creates a new Mammal '''
    def __init__(self, legs = 0):
        if legs > 0:
            self.legs = legs + ' legs.';
        else:
            self.legs = 'no legs.';

    ##########################################

class Shark(Animal, Fish):
    ''' Creates a new Shark '''
    def __init__(self, name):
        Animal.__init__(self, name, 'Shark');
        Fish.__init__(self, 4);

    def __str__(self):
        return 'I am a %s named %s. I have %s fins.' % (self.species, self.name, self.fins);

    ##########################################

class BlueWhale(Animal, Mammal):
    ''' Creates a new BlueWhale '''
    def __init__(self, name):
        Animal.__init__(self, name, 'Blue-Whale');
        Mammal.__init__(self);

    def __str__(self):
        return 'I am a %s named %s. I have %s' % (self.species, self.name, self.legs);

    ##########################################


# Create a new shark, which inherits from Animal and Fish
shark = Shark('George');
print(shark);

# Create a new bluewhale, which inherits from Animal and Mammal
whale = BlueWhale('Sam');
print(whale);
