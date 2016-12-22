# Define a dictionary that contains information about several members of your family. Use the following example as a template.

# Using a dictionary comprehension, produce output that looks like the following example.
# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

my_family = {'sister': { 'name': 'Krista', 'age': 42 }, 'mother': { 'name': 'Cathie', 'age': 70 }};

family_string = { value['name'] + ' is my ' + key + ' and is ' + str(value['age']) + ' years old.' for (key, value) in my_family.items() };

print(family_string);
