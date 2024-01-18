import random
import os
import time
import threading

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'

# Global variable that will be used to update the score

score = 0

print('\n🅄 🄽 🅂 🄲 🅁 🄰 🄼 🄱 🄻 🄴\n')
print('\n🅃 🄷 🄴\n')
print('\n🅆 🄾 🅁 🄳\n')

print('Ready to unscrable the word?\n')
username = input('Enter username: \n')
print(f'Hello {username}!\n')
print('You will be given words whose letters are scrambled.\n')
print('Your goal is to unscramble as many words as you can in 30s.\n')
print('Please provide the number of the category of words you want to play with:\n')

    
def game(score):
    
    # Function for countdown

    def countdown(t):
        while len(animals) < 5:
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1
    t=30
    def reset_score():
        """
        Function that resets the score when the
        player has played all the words and wants
        to play again
        """
        global score
        score = 0
    reset_score()
    # Categories

    animals = ['CAT','DOG','HORSE','GIRAFFE','ELEPHANT']
    countries = ['GREECE','ITALY', 'SWEDEN', 'GERMANY', 'FRANCE']
    food = ['PASTA', 'RICE', 'EGGS', 'BREAD', 'PANCAKES']

    # Player chooses category

    def category_choice():
        """
        Asks for input to choose the category.
        Validates it.
        """
        while True:
            print(Colors.BLUE + '1. Animals 2. Countries 3. Food \n' + Colors.RESET)
            number = input("Enter your choice here:\n")
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
                print(f'{number} is invalid. Please try again.\n')
                

    # Function that scrambles the word from the category the player chose

    def scramble_word(category):
        """
        Chooses randomly an item from the list chosen.
        Takes it out of the list.
        Shuffles the item/word.
        Calls the player's answer function.
        Calls the play again function when there are no items left on the list.
        """
        while len(category) > 0:
            print('Your scrambled word is:\n')
            unscrambled_word = random.choice(category)
            x = category.index(unscrambled_word)
            category.pop(x)
            l = list(unscrambled_word)
            random.shuffle(l)
            while l == unscrambled_word:
                random.shuffle(l)
            scrambled_word = str(''.join(l))
            
            # Print the word with spaces between the letters
            for char in scrambled_word:
                print(Colors.RED + char, end=" " + Colors.RESET)
            
            players_answer(unscrambled_word, scrambled_word)
            
        else:
            print(f"Game Over. Your score is: {score}")
            play_again()
        
    #def clear():
        #os.system('cls' if os.name == 'nt' else 'clear')

    # Players answer
    
    def players_answer(unscrambled_word, scrambled_word):
        """
        Player's input and validation
        """
        
        players_guess = input('\nUnscramble here:\n')
        validation_words(players_guess, unscrambled_word,scrambled_word)      

    # Function that validates player's answer

    def validation_words(players_guess, unscrambled_word,scrambled_word):
        """
        Raises error if the input is not correct
        Gives the option to retry
        Updates the score
        """
        global score
        
        if str(players_guess) == str(unscrambled_word):
            score = score + 1
            print('Correct! The answer is: ' + Colors.GREEN + unscrambled_word + Colors.RESET + f'\nYour Score is : {score}\n')
            if len(animals)<len(food):
                scramble_word(animals)
            elif len(food)<len(animals):
                scramble_word(food)
            else:
                scramble_word(countries)
        else:
            print('The answer you provided is wrong.')
            print(f'Your score is {score}')
        while True:    
            retry = input('\nDo you want to try again? Y/N For exit press E: \n')
            if retry == 'N':
                print('Next word:')
                if len(animals)<len(food):
                    scramble_word(animals)
                elif len(food)<len(animals):
                    scramble_word(food)
                else:
                    scramble_word(countries)
                    break
            elif retry == 'Y':
                players_answer(unscrambled_word, scrambled_word)
                break
            elif retry == 'E':
                exit()
            else:
                print('Your answer is invalid.\n') 

    # Function to restart game or not

    def play_again():
        """
        Option to reset the game
        """
        while True:
            answer = input('Would you like to play again Y/N?\n')
            # clear()
            if answer == 'N':
                print('Thanks for playing!\n')
                exit()
            elif answer == 'Y':
                game(score)
            else:
                print(f'{answer} is invalid. Please try again.\n')
                
    if t==0 :
        print('Your time is up!\n')
        play_again()

    # Calls the functions and starts the game

    if __name__ == '__main__':
        # clear()
        category_choice()
        if len(animals)<len(food):
            scramble_word(animals)
        elif len(food)<len(animals):
            scramble_word(food)
        else:
            scramble_word(countries)

game(score)
