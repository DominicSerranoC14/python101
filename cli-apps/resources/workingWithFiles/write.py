# Second argument determines the action
# You are able to write multiple times to file when file is open
# e.g. line 8 will not be overwritten by line 11
# After the file is closed, the next time it is written to
# the current contents will be erased
animals = open('animals.txt', 'w');

# Use the write method to write to file
# Write single string to file
animals.write('I wrote to this page. ');

# Write multiple strings to file
page = list(['\nOne', '\nTwo', '\nThree']);
animals.write(' '.join(page));

animals.close();
##########################################

# Open file now to read
animals = open('animals.txt', 'r');
print(animals.read());
animals.close();
