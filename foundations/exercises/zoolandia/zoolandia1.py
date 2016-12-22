# Create the Animal class. Create some simple properties and methods on Animal. You are going to create some derived classes that inherit from Animal, so make sure that the properties/methods you add are general to all Animals (e.g. name, height, weight, etc).

class Animal(object):

    def __init__(self, name, species):
        self.name = name;
        self.species = species;

    def get_name(self):
        return self.name;

    def get_species(self):
        return self.species;

    def __str__(self):
        return "I am a %s named %s." % (self.species, self.name);


# Subclasses
# After you are happy with your Animal class, create a derived class that defines a particular species of Animal. Create some properties that apply only to that species.
# The species for a Red Panda
class AilurusFulgens(Animal):
    # Define simple properties for a Red Panda here
    '''
    Class which inherit's from the Animal class.
    Arguments:
    name --- title, personal name.
    common_name --- common name.
    '''
    def __init__ (self, name):
        Animal.__init__(self, name, "Ailurus-Fulgens");
        self.common_name = "Red Panda";

    def get_common_name (self):
        return self.common_name;

    def __str__(self):
        return "I am a %s (aka %s) named %s." % (self.species, self.common_name, self.name);
    ##########################################


# Create three more classes for species of animals of your choosing. Wikipedia is a great tool to discover species names.

class PanPaniscus(Animal):
    '''
    Class which inherit's from the Animal class.
    Arguments:
    name --- title, personal name.
    common_name --- common name.
    '''
    def __init__ (self, name):
        Animal.__init__(self, name, "Pan-Paniscus");
        self.common_name = "Bonobo";

    def get_common_name (self):
        return self.common_name;

    def __str__(self):
        return "I am a %s (aka %s), call me %s." % (self.species, self.common_name, self.name);
    ##########################################


class PanTroglodytes(Animal):
    '''
    Class which inherit's from the Animal class.
    Arguments:
    name --- title, personal name.
    common_name --- common name.
    '''
    def __init__ (self, name):
        Animal.__init__(self, name, "Pan-Troglodytes");
        self.common_name = "Chimpanzee";

    def get_common_name (self):
        return self.common_name;

    def __str__(self):
        return "I am a %s (aka %s), call me %s." % (self.species, self.common_name, self.name);
    ##########################################


class NasalisLarvatus(Animal):
    '''
    Class which inherit's from the Animal class.
    Arguments:
    name --- title, personal name.
    common_name --- common name.
    '''
    def __init__ (self, name):
        Animal.__init__(self, name, "Nasalis-Larvatus");
        self.common_name = "Proboscis-Monkey";

    def get_common_name (self):
        return self.common_name;

    def __str__(self):
        return "I am a %s (aka %s), call me %s." % (self.species, self.common_name, self.name);
    ##########################################


# Instantiate each subclass and print the __str__
panda = AilurusFulgens('Big-Red');
print(panda);

bono = PanPaniscus('Pygmy-Chimp');
print(bono);

chimp = PanTroglodytes('Cousin');
print(chimp);

spoony = NasalisLarvatus('Spoon Nose');
print(spoony);
