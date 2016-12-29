# Append will append new lines to the current contents
animals = open('animals.txt', 'a');
animals.write('\nHello there, I was appended to the file.');
animals.close();
##########################################

animals = open('animals.txt', 'r');
print(animals.read());
animals.close();
##########################################
