import random
import os

animals = ['cat','dog','horse']
countries = ['greece','italy', 'sweden']
food = ['pasta', 'rice', 'eggs']

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def players_answer(unscrambled_word, scrambled_word):
    while True:
        players_guess = input('Unscramble here:\n').lower()
        print(scrambled_word)
        if validation_words(players_guess, unscrambled_word):
            break

def play_again():
    while True:
        answer = input('Would you like to play again Y/N?\n').lower()

        clear()
        if answer == 'n':
            print('Thanks for playing')
            exit()
        elif answer == 'y':
            category_choice()
        else:
            print(f'{answer} is invalid. Please try again.')
            break
            
def scramble_word(category):
    
    while len(category) > 0 :
        print('Your scrambled word is:\n')
        unscrambled_word = random.choice(category)
        x = category.index(unscrambled_word)
        category.pop(x)
        l = list(unscrambled_word)
        random.shuffle(l)
        while l == unscrambled_word:
            random.shuffle(l)
        scrambled_word = ''.join(l)
        print(scrambled_word)
        players_answer(unscrambled_word, scrambled_word)
    else:
        print("Game Over")
        play_again()

def category_choice():
    while True:
        print('1. Animals 2. Countries 3. Food \n')
        number = input("Enter your choice here:")
        clear()

        if number == '1':
            print('You chose "Animals"\n')
            scramble_word(animals)
            break
            
        elif number == '2':
            print('You chose "Countries"\n')
            scramble_word(countries)
            break
            
        elif number == '3':
            print('You chose "Food"\n')
            scramble_word(food)
            break
        else:
            print(f'{number} is invalid. Please try again.')
    

def validation_words(players_guess, unscrambled_word):

    """
    Raises error if the input is not of the correct type, in the correct order
    or does not have the correct length
    """

    if str(players_guess) == str(unscrambled_word):
        print('Right!')
        return True

    else:
        print('The answer you provided is wrong')
        return False

if __name__ == '__main__':
    clear()
    print('Ready to unscrable the word?\n')
    username = input('Enter username: ')
    print(f'Hello {username}!')
    print('You will be given words whose letters are scrambled.\n')
    print('Your goal is to unscramble them and find the word.\n')
    print('Please provide the number of the category of words you want to play with:\n')
    
    category_choice()
  
