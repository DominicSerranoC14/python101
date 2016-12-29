#!/usr/bin/env python

from sys import argv;

# After each successful input, display the number of letters already entered.
# After each unsuccessful input, display a helpful message explaining why the input was unsuccessful (e.g. 'not a letter', 'duplicate letter', etc.)
# Upon completing the task (entering in all 26 letters), the user should receive some gratifying message like "Congratulations"

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

class Alphabits:
  """
  """

  def __init__(self):
      pass;

  def start_game(self):
    """Show teller options

    Arguments: None
    """

    counter = 0;

    print('Alphabits is about to begin!');
    print('Please enter each letter of the alphabit one at a time.');
    choice = input("> ");

    if choice.upper() == alphabet[0]:
        print('Correct!');


    self.start_game();

Alphabits().start_game();

# test = Teller();
# test.show_menu();



# Use one Class in addition to the program file.
# Your class should include the __init__ constructor function, an add_char method, and a list_length method.
# Keep your user's successfully input letters as a list of characters.
# Use the string interpolation to craft your messages to users.

# Create a return_list method on your class that will return the current list of characters that the user has entered in correctly.
# Create a non-letter "Easter egg" character that will display the current list of successfully input letters (but will not add itself to the list!) which calls the the return_list method.
