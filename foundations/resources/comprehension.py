# List comprehension
flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip'];
say_flowers = list();

# Use a for loop to loop over each value and concat with 'a large'
for each in flowers:
    say_flowers.append('This is a ' + each);

# Shorthand to loop through a list
# 'This is a' + each ---- concatenated value from flowers and a string
# for each in flowers ---- the for loop
# This method can be used to create a new list from the original
speak_flowers = [ 'This is a ' + each   for each in flowers];

print(speak_flowers);
##########################################


# Dict comprehension
family = { 'mother': 'Margaret', 'father': 'Reginald', 'sister': 'Jenny'};

# For loop for dict, similar to for in loop for JS object
# Must use the items() property on the family dict to iterate
for (key, value) in family.items():
    print(' : ' + value);

# Dict comprehension Shorthand
# This method can be used to create a new dict from the original
my_family = {'My ' + key + ' is ' + value for (key, value) in family.items()};

print(my_family);
##########################################


# Set comprehension
# Create a set with values 0-99, 99 ints
possible_ratings = set(range(100));
print(possible_ratings);

# Loop through each value in possible_ratings and divide it by 2
funky_ratings = {r/2 for r in possible_ratings};
print(funky_ratings);
##########################################
