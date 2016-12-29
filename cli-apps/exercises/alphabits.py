#!/usr/bin/env python

from sys import argv;

# After each successful input, display the number of letters already entered.
# After each unsuccessful input, display a helpful message explaining why the input was unsuccessful (e.g. 'not a letter', 'duplicate letter', etc.)
# Upon completing the task (entering in all 26 letters), the user should receive some gratifying message like "Congratulations"

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

# Use one Class in addition to the program file.
# Your class should include the __init__ constructor function, an add_char method, and a list_length method.
class Alphabits:
    """
    """

    def __init__(self):
        self.input_list = [];
        self.init_game();

    # Keep your user's successfully input letters as a list of characters.
    def add_char(self, letter):
        self.input_list.append(letter);

    # Use the string interpolation to craft your messages to users.
    def list_length_str(self):
        length = len(self.input_list) + 1;
        if length == 1:
            return '1st';
        elif length == 2:
            return '2nd';
        elif length == 3:
            return '3rd';
        else:
            return str(length) + 'th';

    def list_length(self):
        return len(self.input_list);

    def handle_incorrect(self, letter):
        if letter in self.input_list:
            print('Incorrect. That letter has already been entered.');
        else:
            print('Incorrect answer. Please try again.');

    def init_game(self):
        print('Alphabits is about to begin!');
        print('Please enter each letter of the alphabit one at a time.\n');

    def start_game(self):
        """
        """

        print('What is the ' + self.list_length_str() + ' letter of the alphabet?');
        user_choice = input("> ");

        if user_choice.upper() == alphabet[self.list_length()]:
            print('Correct!');
            print('Correct answers: ' + str(self.list_length() + 1));
            self.add_char(user_choice);
        else:
            self.handle_incorrect(user_choice);


        self.start_game();

Alphabits().start_game();





# Create a return_list method on your class that will return the current list of characters that the user has entered in correctly.
# Create a non-letter "Easter egg" character that will display the current list of successfully input letters (but will not add itself to the list!) which calls the the return_list method.
