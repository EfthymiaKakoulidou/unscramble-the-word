import random
import os
from colorama import Fore

# Global variable that will be used to update the score

score = 0

def game(score):

    # Categories
    
    animals = ['cat','dog','horse']
    countries = ['greece','italy', 'sweden']
    food = ['pasta', 'rice', 'eggs']

    print('Ready to unscrable the word?\n')
    username = input('Enter username: ')
    print(f'Hello {username}!')
    print('You will be given words whose letters are scrambled.\n')
    print('Your goal is to unscramble them and find the word.\n')
    print('Please provide the number of the category of words you want to play with:\n')
    print('1. Animals 2. Countries 3. Food \n')
    
    # Player chooses category

    def category_choice():
        """
        Asks for input to choose the category.
        Validates it.
        """
        while True:
            number = input("Enter your choice here:")
            if number == '1':
                print('You chose "Animals"\n')
                scramble_word(animals)
                
            elif number == '2':
                print('You chose "Countries"\n')
                scramble_word(countries)
                
            elif number == '3':
                print('You chose "Food"\n')
                scramble_word(food) 

            else:
                print(f'{number} is invalid. Please try again.')
                category_choice()
            return True

    # Function that scrambles the word from the category the player chose

    def scramble_word(category):
        """
        Chooses randomly an item from the list chosen.
        Takes it out of the list.
        Shuffles the item/word.
        Calls the player's answer function.
        Calls the play again function when there are no items left on the list.
        """
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
            print(Fore.RED + scrambled_word  + Fore.RESET)
            players_answer(unscrambled_word, scrambled_word)
        else:
            print("No words left to unscramble. Game Over")
            play_again()
        
    #def clear():
        #os.system('cls' if os.name == 'nt' else 'clear')

    # Players answer

    def players_answer(unscrambled_word, scrambled_word):
        """
        Player's input and validation
        """
        while True:
            players_guess = input('Unscramble here:\n').lower()
            if validation_words(players_guess, unscrambled_word,scrambled_word):
                break

    # Function that validates player's answer

    def validation_words(players_guess, unscrambled_word,scrambled_word):
        """
        Raises error if the input is not correct
        Gives the option to retry
        """
        global score
        if str(players_guess) == str(unscrambled_word):
            score = score + 1
            print(f'Right! Your Score is : {score}')
            return True

        else:
            print(f'The answer you provided is wrong. Your score is {score}')
            retry = input('Do you want to try again? y/n : ')
            if retry == 'n':
                print('Next word:')
                if len(animals)<len(food):
                    scramble_word(animals)
                elif len(food)<len(animals):
                    scramble_word(food)
                else:
                    scramble_word(countries)

            elif retry == 'y':
                players_answer(unscrambled_word, scrambled_word)
                return True
            else:
                print('Your answer is invalid. Do you want to try again? y/n :')
                
            return False

    # Function to restart game or not

    def play_again():
        """
        Option to reset the game
        """
        while True:
            answer = input('Would you like to play again y/n?\n').lower()
           # clear()
            if answer == 'n':
                print('Thanks for playing')
                exit()
            elif answer == 'y':
                game(score)
            else:
                print(f'{answer} is invalid. Please try again.')
                break

    # Calls the functions and starts the game

    if __name__ == '__main__':
       # clear()
        category_choice()
game(score)
