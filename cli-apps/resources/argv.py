# Import argv from sys only
from sys import argv;

# Determines if this was the main module
# or the file/module that was executed
# If so, the execute the following code
if __name__ == "__main__":
    greeting = 'Hello';

    if len(argv) == 2:
        greeting = 'Hello ' + argv[1];

    elif len(argv) == 3:
        greeting = 'Hello %s %s' % (argv[1], argv[2]);

    print(greeting);
