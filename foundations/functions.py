# Import the Template class
from string import Template

# Python uses _'s instead of camelCasing for funcs and vars
def say_my_name(name):
    '''
    Displays a name with a friendly greeting.
    Arguments:
    name -- string to print
    '''
    # Create a string template
    temp = Template('Hello $who');
    # Returns a new string and substitutes the key word for the name param
    greeting = temp.substitute(who=name);
    # Prints the string template
    print(greeting);


# Displays the doc string
# print(say_my_name.__doc__)

say_my_name('Dom');
say_my_name('Scott');
say_my_name('Callan');
