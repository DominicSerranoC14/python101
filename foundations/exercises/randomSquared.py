import random;
# Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.
random_numbers = list();

def create_random_list ():
    '''
    This function creates 20 random numbers from 0-49.
    '''

    for x in range(0,20):
        random_numbers.append(random.randint(0,49));

create_random_list();
print(random_numbers);

# With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].

squared_list = [each * each   for each in random_numbers ];
print(squared_list);
