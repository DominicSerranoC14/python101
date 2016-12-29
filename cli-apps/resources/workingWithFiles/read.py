# Use the open() method to open files from the OS, and read(), or readline() methods to start reading the contents. When are you done with a file, always remember to close() it.

animals = open('animals.txt', 'r');

# Print the contents of the file
# print(animals.read());

# Prints one line at a time
# You can pass a byte size to the readline method
# print(animals.readline());
# print(animals.readline());
# print(animals.readline());

# Loop through each line
for each in animals:
    message = 'I am a ' + each;
    print(message);

animals.close();
##########################################

    
