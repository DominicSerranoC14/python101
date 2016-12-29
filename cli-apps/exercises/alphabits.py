#!/usr/bin/env python

alphabet = ['A', 'B', 'C', 'D', 'e', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

# Use one Class in addition to the program file.
# Your class should include the __init__ constructor function, an add_char method, and a list_length method.
class Alphabits:
    """
    Class which creates a new alphabet game.
    """

    def __init__(self):
        '''
        Inits and starts the game.
        '''
        self.input_list = [];
        self.init_game();
        self.game_play();

    # Keep your user's successfully input letters as a list of characters.
    def add_char(self, letter):
        '''
        If the user input is correct, append to the input_list set.
        '''
        self.input_list.append(letter);

    # Use the string interpolation to craft your messages to users.
    def list_length_str(self):
        '''
        Return a string of the current user letter postition.
        e.g: What is the 4th letter?
        '''
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
        ''' Returns an int of the input_list '''
        return len(self.input_list);

    # Create a return_list method on your class that will return the current list of characters that the user has entered in correctly.
    def return_list(self):
        collection = '';
        for letter in self.input_list:
            collection += letter.upper() + ' ';
        print(collection);

    def handle_incorrect(self, letter):
        if letter in self.input_list:
            print('Incorrect. That letter has already been entered.');
        else:
            print('Incorrect answer. Please try again.');

    def init_game(self):
        '''
        Alerts user that game is about to start.
        '''
        print('Alphabits is about to begin!');
        print('Please enter each letter of the alphabit one at a time.');

    def determine_gameover(self):
        # Upon completing the task (entering in all 26 letters), the user should receive some gratifying message like "Congratulations"
        if len(alphabet) == self.list_length():
            print('\nCongratulations!');
            print('You have completed the game, you are an Alphabet Master.');
        else:
            self.game_play();

    def game_play(self):
        """
        All game logic executed here.
        """

        # Alert the user to which letter they are on
        print('\nWhat is the ' + self.list_length_str() + ' letter of the alphabet?');
        user_choice = input("> ");

        # Create a non-letter "Easter egg" character that will display the current list of successfully input letters (but will not add itself to the list!) which calls the the return_list method.
        if user_choice == '?':
            self.return_list();
            self.game_play();
        # If user's anser mathches current letter
        elif user_choice.upper() == alphabet[self.list_length()]:
            print('Correct!');
            # After each successful input, display the number of letters already entered.
            print('Correct answers: ' + str(self.list_length() + 1));
            self.add_char(user_choice);
            self.determine_gameover();
        else:
            # After each unsuccessful input, display a helpful message explaining why the input was unsuccessful (e.g. 'not a letter', 'duplicate letter', etc.)
            self.handle_incorrect(user_choice);
            self.game_play();

    ##########################################


# Begin game
Alphabits();
