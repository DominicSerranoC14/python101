# For this last Zoolandia exercises for the Foundations Milestone, you need to define all of the Habitats in which all of the animals live. You'll use the aggregation pattern to assign animals to each Habitat.
# In this example code, create the parent Habitat class that all others will derive from, and since every habitat in my Zoo will have animals in it, each specific habitat class will inherit that inhabitants property.

class Habitat:
    ''' Parent Habitat Class '''

    def __init__(self, name = None):
        self.name = name;
        self.inhabitants = [];

    ##########################################

class Aquarium(Habitat):
    ''' Creates an Aquarium subclass of Habitat '''

    def __init__(self, salt_or_fresh):
        Habitat.__init__(self);
        self.name = 'Aquarium';
        self.salt_or_fresh = salt_or_fresh;

    def __str__(self):
        tenants = [each.__str__() for each in self.inhabitants];
        return self.salt_or_fresh + ' ' + self.name + ' Inhabitants: \n' + '\n'.join(tenants);

    ##########################################

class Animal:
    ''' Creates a new animal '''

    def __init__(self, name, species):
        self.name = name;
        self.species = species;

    def __str__(self):
        return self.name + ' the ' + self.species;

    ##########################################


# Create new Saltwater Aquarium habitat w/ inhabitants
aqua = Aquarium('Salt-Water');
aqua.inhabitants.append(Animal('Walter', 'Seal'));
aqua.inhabitants.append(Animal('James', 'Dolphin'));
aqua.inhabitants.append(Animal('Dave','Orca'));
print(aqua);
