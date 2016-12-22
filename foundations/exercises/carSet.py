# Create an empty set named showroom.
showroom = set();

# Add four of your favorite car model names to the set.
showroom.add('Camry');
showroom.add('Avalon');
showroom.add('Rav4');
showroom.add('Corolla');

# Print the length of your set.
print('Show room length: ' + str(len(showroom)));

# Pick one of the items in your show room and add it to the set again.
# Print your showroom. Notice how there's still only one instance of that model in there.
# Won't work, must be unique value
showroom.add('Camry');

# Using update(), add two more car models to your showroom with another set.
showroom.update({'Civic', 'Camaro'});

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard('Corolla');

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = set({'Civic', 'Accord', 'Camaro', 'Diablo'});
print('junkyard: ' + str(junkyard));
print('showroom: ' + str(showroom));

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
diff = showroom.intersection(junkyard);
print('Similar cars in sets: ' + str(diff));

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
combined_set = showroom.union(junkyard);
print('Combined set: ' + str(combined_set));
