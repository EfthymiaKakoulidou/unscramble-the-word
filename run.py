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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print('\n🆄 🅽 🆂 🅲 🆁 🅰  🅼 🅱  🅻 🅴\n')
print('\n🆃 🅷 🅴\n')
print('\n🆆 🅾  🆁 🅳\n')

print('Ready to unscrable the word?\n')
username = input('Enter username: \n')
clear()
print(f'Hello {username}!\n')
print('You will be given 5 words whose letters are scrambled.\n')
print('Your goal is to unscramble as many words as you can.\n')
print('If you find the word without a hint you get 2 points.If you use a hint you get 1.\n')
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
            print(Colors.BLUE + '1. Animals \n2. Countries \n3. Food \n' + Colors.RESET)
            number = input("\nEnter your choice here:\n")
            if number == '1':
                print('\nYou chose "Animals"\n')
                clear()
                scramble_word(animals)
                break
                
            elif number == '2':
                print('\nYou chose "Countries"\n')
                clear()
                scramble_word(countries)
                break
                
            elif number == '3':
                print('\nYou chose "Food"\n')
                clear()
                scramble_word(food)
                break

            else:
                print(f'\n{number} is invalid. Please try again.\n')
                

    # Function that scrambles the word from the category the player chose

    def scramble_word(category):
        """
        Chooses randomly an item from the list chosen.
        Takes it out of the list.
        Shuffles the item/word.
        Calls the player's answer function.
        Calls the play again function when there are no items left on the list.
        """
        global score
        while len(category) > 0:
            time.sleep(1)
            clear()
            print('\nYour scrambled word is:\n')
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
            print('\n🅶 🅰  🅼 🅴   🅾  🆅 🅴 🆁 \n')
            print(f'Your final score is : {score}')
            play_again()

    # Players answer
    
    def players_answer(unscrambled_word, scrambled_word):
        """
        Player's input and validation
        """
        players_guess = input('\nUnscramble here:\n'). upper()
        validation_words(players_guess, unscrambled_word,scrambled_word)      

    def players_answer2(unscrambled_word, scrambled_word):
        """
        Player's input and validation
        """
        players_guess = input('\nUnscramble here:\n'). upper()
        validation_words2(players_guess, unscrambled_word,scrambled_word) 

    # Function that validates player's answer

    def validation_words(players_guess, unscrambled_word,scrambled_word):
        """
        Validates the answer the first time and offers a hint.
        Raises error if the input is not correct
        Gives the option to retry
        Updates the score
        """
        global score
        
        if str(players_guess) == str(unscrambled_word):
            score = score + 2
            print('\nCorrect! The answer is: ' + Colors.GREEN + unscrambled_word + Colors.RESET + f'\nYour Score is : {score}\n')
            if len(animals)<len(food):
                scramble_word(animals)
            elif len(food)<len(animals):
                scramble_word(food)
            else:
                scramble_word(countries)
        else:
            print('\nThe answer you provided is wrong.\n')
            print(f'Your score is {score}')
        while True:    
            retry = input('\nDo you want to try again without hint? Y/N\nDo you want a hint? H\nExit? E: \n').upper()
            if retry == 'N':
                clear()
                if len(animals)<len(food) and len(animals) != 0:
                    print('\nNext word:\n')
                    scramble_word(animals)
                elif len(animals) == 0:
                    print('\n🅶 🅰  🅼 🅴   🅾  🆅 🅴 🆁 \n')
                    print(f'Your final score is : {score}')
                    play_again()
                elif len(food)<len(animals) and len(food) != 0:
                    print('\nNext word:\n')
                    scramble_word(food)
                elif len(food) == 0:
                    print('\n🅶 🅰  🅼 🅴   🅾  🆅 🅴 🆁 \n')
                    print(f'Your final score is : {score}')
                    play_again()
                elif len(countries) == 0:
                    print('\n🅶 🅰 🅼 🅴   🅾  🆅 🅴 🆁 \n')
                    print(f'Your final score is : {score}')
                    play_again()
                else:
                    print('\nNext word:\n')
                    scramble_word(countries)
                    break
            elif retry == 'Y':
                players_answer(unscrambled_word, scrambled_word)
                break
            elif retry == 'H':
                break
            elif retry == 'E':
                exit()
            else:
                print('\nYour answer is invalid.\n')
        if retry == 'H':
            print('\nThe first letter is: ' + Colors.GREEN + f'{unscrambled_word[0]}' + Colors.RESET + '.\n')
            players_answer2(unscrambled_word, scrambled_word)

    def validation_words2(players_guess, unscrambled_word,scrambled_word):
        """
        Validates the answers after the first time.
        Raises error if the input is not correct
        Gives the option to retry
        Updates the score
        """
        global score
        
        if str(players_guess) == str(unscrambled_word):
            score = score + 1
            print('\nCorrect! The answer is: ' + Colors.GREEN + unscrambled_word + Colors.RESET + f'\nYour Score is : {score}\n')
            if len(animals)<len(food):
                scramble_word(animals)
            elif len(food)<len(animals):
                scramble_word(food)
            else:
                scramble_word(countries)  
        else:
            print('\nThe answer you provided is wrong.\n')
            if players_guess[0] != unscrambled_word[0]:
                print('Remember your word starts with' + Colors.GREEN + f' {unscrambled_word[0]}'+ Colors.RESET + '!\n')
            print(f'\nYour score is {score}\n')
        while True:    
            retry = input('\nNo more hints.Do you want to try again? Y/N\nExit? E: \n').upper()
            if retry == 'N':
                clear()
                if len(animals)<len(food) and len(animals) != 0:
                    print('\nNext word:\n')
                    scramble_word(animals)
                elif len(animals) == 0:
                    print('\n🅶 🅰  🅼 🅴   🅾  🆅 🅴 🆁 \n')
                    print(f'Your final score is : {score}')
                    play_again()
                elif len(food)<len(animals) and len(food) != 0:
                    print('\nNext word:\n')
                    scramble_word(food)
                elif len(food) == 0:
                    print('\n🅶 🅰  🅼 🅴   🅾  🆅 🅴 🆁 \n')
                    print(f'Your final score is : {score}')
                    play_again()
                elif len(countries) == 0:
                    print('\n🅶 🅰 🅼 🅴   🅾  🆅 🅴 🆁 \n')
                    print(f'Your final score is : {score}')
                    play_again()
                else:
                    print('\nNext word:\n')
                    scramble_word(countries)
                    break
            elif retry == 'Y':
                players_answer2(unscrambled_word, scrambled_word)
                break
            elif retry == 'E':
                exit()
            else:
                print('\nYour answer is invalid.\n')

    # Function to restart game or not

    def play_again():
        """
        Option to reset the game
        """
        while True:
            
            answer = input('\nWould you like to play again Y/N?\n'). upper()
            # clear()
            if answer == 'N':
                print('\nThanks for playing!\n')
                exit()
            elif answer == 'Y':
                game(score)
            else:
                print(f'{answer} is invalid. Please try again.\n')
                
    if t==0 :
        print('\nYour time is up!\n')
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
