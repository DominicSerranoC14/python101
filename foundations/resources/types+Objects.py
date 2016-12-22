# LISTS
# list() will create an empty list
# junk = list();

#  A list is similar to an array, an unordered collection of values
# junk = ['carrots', 'celery', 'kale', 2, ['peas', 'corn']];

# list.insert(index, value)
# junk.insert(0, 'kidney beans');

# list.extend will append multiple values to a list
# Values must be inside [], even if only one value
# junk.extend([True, 'corn']);

# list.append will append a single value to a list
# junk.append('hurricane');

# Print is similar to console.log
# print(junk);
##########################################


# DICTIONARIES
# dict() will create an empty dict
# junk = dict();

# Define the dict with key value pairs
# junk = { 'name': 'Steve', 'age': 47, 'role': 'Head Coach' };

# Use bracket notation to insert a new key value pair
# junk['kids'] = 2;

# Use bracket notation to edit an existing key
# junk['name'] = 'Diana';

# Print the value of name
# print(junk['name']);
# print(junk);
##########################################


# SETS
# Sets are like lists but they only accept unique values
# If a value is passed to the set that already exists, the operation will not happen
# Create an empty set
# junk = set();

# Add a single value to a set, can only add 1
# junk.add('Four');

# Create a set with multiple values
# stuff = set(['One', 'Two', 'Three']);

# Update junk with the values from stuff
# Only way to add multiple values?
# junk.update(stuff);

# Remove a specific value
# junk.remove('One');

# Will print the first value
# print(junk.pop())

# Erases all values in the set
# junk.clear();
# print(junk);
##########################################


# TUPLES
# Tuples are immutable data structures
# Iterating over tuples is faster than iterating over a list

# Create an empty tuple
junk = tuple();
junk = ('Joe', 'Instructor', 'Awesome');
print(junk);
##########################################
