# Create a tuple named zoo that contains your favorite animals.
zoo = ('Boa', 'Panda', 'Giraffe');

# Find one of your animals using the .index(value) method on the tuple.
# This returns an index value
zoo.index('Panda');

# Determine if an animal is in your tuple by using for value in tuple.
for value in zoo:
    print(value);

# Create a variable for each of the animals in your tuple with this cool feature of Python.
(boa, panda, giraffe) = zoo;

# Convert your tuple into a list.
zoo_list = list(zoo);

# Use extend() to add three more animals to your zoo.
# Must put the values in a list to use extend
zoo_list.extend(['Lion', 'Bear', 'Fox']);
print(zoo_list);

# Convert the list back into a tuple.
zoo = tuple(zoo_list);
print(zoo);
