class Animal:
    '''
    This is a generic Animal class.
    Arguments:
    name --- title, personal name.
    species --- Binomen.
    '''
    def __init__(self, name, diet):
        self.name = name;
        self.diet = diet;

    def my_diet(self, food):
        return ("%s eats %s" % (self.name, food));

    def __str__(self):
        return "I am a %s and I am a %s" % (self.name, self.diet);
    ##########################################


# Choose one of the general methods that you created in the Animal class for overriding.
# Override that method in all of your species classes, giving each a more specialized implementation. For example, the species may only eat certain kinds of food, or have a limit on how much food can be eaten.

class AilurusFulgens(Animal):
    '''
    Class which inherit's from the Animal class.
    Arguments:
    name --- title, personal name.
    '''
    def __init__ (self, diet):
        super().__init__('Ailurus-Fulgens', diet);
        self.diet = diet;

    # Make sure you invoke the parent class' overridden method with the super reference (e.g. super(speciesClass, self).sleep());
    def my_diet (self, food):
        # the super key word call the parents method
        # for possible extension of the method in subclasses
        parent_message = super(AilurusFulgens, self).my_diet(food);
        # message = parent_message + "but doesn't digest it very well.";
        message = ' '.join([parent_message, "but doesn't digest it very well."]);
        return message;

    def __str__(self):
        return "I am a %s and I am a %s." % (self.name, self.diet);
    ##########################################


# Constructors
# Create a class for each of your animals. The class should, at the very least, set the initial name of all animals of that type to a name of your choosing.

# class RedPanda(AilurusFulgens):
#     def __init__(self, name):
#         super().__init__(name);
    ##########################################

# myPanda = RedPanda();
# print(myPanda);
# print(myPanda.name);

# Instantiate new animal
rhino = Animal('White Rhino', 'Vegetarian');
print(rhino);

# Instantiate new AilurusFulgens
red_panda = AilurusFulgens('Vegetarian');
print(red_panda);
print(red_panda.my_diet('pinecones'));
