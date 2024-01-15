import random
from random import shuffle

animals = ['cat','dog','horse']
countries = ['greece','italy', 'sweden']
food = ['pasta', 'rice', 'eggs']

print('Hello Tim! Ready to unscrable the word?\n')
print('You will be given words whose letters are scrambled.\n')
print('Your goal is to unscramble them and find the word.\n')
print('Please provide the number of the category of words you want to play with:\n')
print('1.Animals 2. Countries 3. Food\n')

number = input("Enter your choice here:")

def category_choice(number):
        if number == '1':
            print('You chose "Animals"\n')
            while len(animals) > 0 :
                print('Your scrambled word is:\n')
                unscrambled_word = random.choice(animals)
                x = animals.index(unscrambled_word)
                animals.pop(x)
                l = list(unscrambled_word)
                shuffle(l)
                scrambled_word = ''.join(l)
                print(scrambled_word)
                def players_answer():
                    while True:
                        players_guess = input('Unscramble here:\n')
                        if validation_words(players_guess, unscrambled_word):
                            break
                players_answer()
            else:
                print("Game Over")
               
        if number == '2':
            print('You chose "Countries"\n')
            while len(countries) > 0 :
                print('Your scrambled word is:\n')
                unscrambled_word = random.choice(countries)
                x = countries.index(unscrambled_word)
                countries.pop(x)
                l = list(unscrambled_word)
                shuffle(l)
                scrambled_word = ''.join(l)
                print(scrambled_word)
                def players_answer():
                    while True:
                        players_guess = input('Unscramble here:\n')
                        if validation_words(players_guess, unscrambled_word):
                            break
                players_answer()
            else:
                print("Game Over")
                
        if number == '3':
            print('You chose "Food"\n')
            while len(food) > 0 :
                print('Your scrambled word is:\n')
                unscrambled_word = random.choice(food)
                x = food.index(unscrambled_word)
                food.pop(x)
                l = list(unscrambled_word)
                shuffle(l)
                scrambled_word = ''.join(l)
                print(scrambled_word)
                def players_answer():
                    while True:
                        players_guess = input('Unscramble here:\n')
                        if validation_words(players_guess, unscrambled_word):
                            break
                players_answer()
                break
            else:
                print("Game Over")

def validation_numbers(number):
    """
    Raises error if the input is not 1,2 or 3
    """
    try:
        if number != '1' or '2' or '3':
            print('You have to choose one of the numbers 1,2 or 3.Please try again.\n')
            return False
        return True
    except:
        print('You have to choose one of the numbers 1,2 or 3.Please try again.\n')
        return False
    return True


def validation_words(players_guess, unscrambled_word):

    """
    Raises error if the input is not of the correct type, in the correct order
    or does not have the correct length
    """

    if str(players_guess)== str(unscrambled_word):
        print('Right! Next word:')
        category_choice(number)

    try:
        if str(players_guess)!= str(unscrambled_word):
            raise ValueError(
                'The answer you provided is wrong'
            )
    except ValueError as e:
        print('Please try again.\n')
        return False
    return True

def main():
    """
    Calls all the functions
    """
    category_choice(number)

main()