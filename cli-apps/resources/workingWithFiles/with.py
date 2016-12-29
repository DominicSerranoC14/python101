# Must be used in function to scope it?

def read_animals():

    # Use with statement to read file
    with open('animals.txt', 'r') as animals:
        animal_set = {each.title() for each in animals};

        # Loop through the set and log out each value
        for each in animal_set:
            print(each);


# read_animals();
##########################################


def existing_to_output(existing, output):
    '''
    Function that will copy a files contents to a new file
    Arguments:
    existing -- an existing file, with content to be copied
    output -- a new file, where the contet will be copied
    '''

    # Open a new file
    with open(output, 'w') as output_file:
        with open(existing, 'r') as existing_file:
            # Loop through each line in existing and write to output
            for each in existing_file:
                output_file.write(each);

    ##########################################

existing_to_output('animals.txt', 'people.txt');
