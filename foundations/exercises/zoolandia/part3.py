# Add a new method to your animal that takes a single string as an argument.
# Inside the new method, using self, assign the value of the name property with the argument value.
# Create an instance of your animal like before, but pass in the name of the animal as an argument.

# Method overloading, can set multiple params and specify
# default values if no value is passed in
class Animal:
    '''
    This is a generic Animal class.
    Arguments:
    name --- title, personal name.
    species --- Binomen.
    '''
    def __init__(self, name = None):
        if name == None:
            self.name = 'with no name';
        else:
            self.name = 'named ' + name;

    def set_name(self, name):
        self.name = 'named ' + name;

    def __str__(self):
        return 'I am an Animal %s.' % (self.name);
    ##########################################


myAnimal = Animal();
print(myAnimal);

myAnimal.set_name('George');
print(myAnimal);
