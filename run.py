import random
import os
import time


# ANSI color codes
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'


# Global variable that will be used to update the score/category
global score
global category
global used_hint
global animals
global countries
global food


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_username():
    global used_hint
    used_hint = False
    print('\n🆄 🅽 🆂 🅲 🆁 🅰  🅼 🅱  🅻 🅴\n')
    print('\n🆃 🅷 🅴\n')
    print('\n🆆 🅾  🆁 🅳\n')

    print('Ready to unscramble the word?\n')
    while True:
        username = input('Enter username: \n')

        try:
            if username.isalpha():
                clear()
                print(f'Hello {username}!\n')
                break
            elif len(username) == 0:
                print('Please provide username')
            else:
                print(f'{username} is invalid. Please enter letters only\n')
        except ValueError as err:
            print(f'{err}. Please try again.')

    print('You will be given 5 words whose letters are scrambled.\n')
    print('Your goal is to unscramble as many words as you can.\n')
    print('If you find the word without a hint you get 2 points.')
    print('If you use a hint you get 1.\n')
    print('Please provide the number of the category ')
    print('of words you want to play with:\n')


def reset_game():
    """
    Function that resets the game when the
    player has played all the words and wants
    to play again
    """
    global score
    global used_hint
    global animals
    global countries
    global food
    score = 0
    used_hint = False
    animals = ['CAT', 'DOG', 'HORSE', 'GIRAFFE', 'ELEPHANT']
    countries = ['GREECE', 'ITALY', 'SWEDEN', 'GERMANY', 'FRANCE']
    food = ['PASTA', 'RICE', 'EGGS', 'BREAD', 'PANCAKES']


# Player chooses category
def category_choice():
    """
    Asks for input to choose the category.
    Validates it.
    """
    global category
    global animals
    global countries
    global food
    while True:
        print(
            f'{Colors.BLUE}1. Animals \n'
            f'2. Countries \n'
            f'3. Food \n {Colors.RESET}'
        )
        number = input("\nEnter your choice here:\n")
        clear()
        if number == '1':
            print('\nYou chose "Animals"\n')
            category = animals
            break

        elif number == '2':
            print('\nYou chose "Countries"\n')
            category = countries
            break

        elif number == '3':
            print('\nYou chose "Food"\n')
            category = food
            break
        elif len(number) == 0:
            print('\nPlease make a choice.\n')
        else:
            print(f'\n{number} is invalid. Please try again.\n')

    scramble_word()


# Function that scrambles the word from the category the player chose
def scramble_word():
    """
    Chooses randomly an item from the list chosen.
    Takes it out of the list.
    Shuffles the item/word.
    Calls the player's answer function.
    Calls the play again function when there are no items left on the list.
    """
    global score
    global category
    global used_hint
    used_hint = False
    while len(category) > 0:
        time.sleep(1.5)
        clear()
        print('\nYour scrambled word is:\n')
        unscrambled_word = random.choice(category)
        ndx = category.index(unscrambled_word)
        category.pop(ndx)
        word = list(unscrambled_word)
        random.shuffle(word)
        # make sure the word never shuffles to the same exact spelling
        while word == list(unscrambled_word):
            random.shuffle(word)
        scrambled_word = str(''.join(word))

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
    # Print the word with spaces between the letters
    for char in scrambled_word:
        print("   " + Colors.RED + char, end=" " + Colors.RESET)
    players_guess = input('\nUnscramble here:\n').upper()
    validation_words(players_guess, unscrambled_word, scrambled_word)


# Function that validates player's answer
def validation_words(players_guess, unscrambled_word, scrambled_word):
    """
    Validates the answer and offers a hint.
    Raises error if the input is not correct.
    Gives the option to retry.
    Updates the score.
    """
    global score
    global category
    global used_hint
    # user's guess was right
    if str(players_guess) == str(unscrambled_word):
        if not used_hint:
            score = score + 2
        else:
            score = score + 1
        print(
            '\nCorrect! The answer is: '
            f'{Colors.GREEN}{unscrambled_word}{Colors.RESET} '
            f'\nYour Score is : {score}\n'
        )
        used_hint = False
        # scramble using the same category
        scramble_word()
        # user does not provide an answer
    elif len(players_guess) == 0:
        print(
            '\nPlease provide an answer.'
            f'\nYour Score is : {score}\n'
        )
    else:
        # user's guess was wrong
        print('\nThe answer you provided is wrong.\n')
        print(f'Your score is {score}')
    while True:
        if used_hint:
            retry = input(
                f'\nDo you want to try again? {Colors.BLUE}Y/N{Colors.RESET}'
                f'\nSee the hint again? {Colors.BLUE}H{Colors.RESET}'
                f'\nExit? {Colors.BLUE}E{Colors.RESET}: \n').upper()
        else:
            retry = input(
                f'\nDo you want to try again? {Colors.BLUE}Y/N{Colors.RESET}'
                f'\nDo you want a hint? {Colors.BLUE}H{Colors.RESET}'
                f'\nExit? {Colors.BLUE}E{Colors.RESET}: \n').upper()
        clear()
        if retry == 'N':
            clear()
            if len(category) != 0:
                print('\nLoading next word...\n')
                scramble_word()
            else:
                print('\n🅶 🅰  🅼 🅴   🅾  🆅 🅴 🆁 \n')
                print(f'Your final score is : {score}')
                play_again()
        elif retry == 'Y':
            players_answer(unscrambled_word, scrambled_word)
            break
        elif retry == 'H':
            used_hint = True
            break
        elif retry == 'E':
            exit()
        else:
            print('\nYour input is invalid.\n')
    if retry == 'H':
        print(
            '\nThe first letter is: '
            f'{Colors.GREEN}{unscrambled_word[0]}{Colors.RESET}.\n'
        )
        time.sleep(2)
        clear()
        players_answer(unscrambled_word, scrambled_word)


# Function to restart game or not
def play_again():
    """
    Option to reset the game
    """
    while True:

        answer = input('\nWould you like to play again Y/N?\n').upper()
        clear()
        if answer == 'N':
            print('\n🆃 🅷 🅰  🅽 🅺  🆈 🅾  🆄  🅵 🅾  🆁  🅿  🅻 🅰  🆈 🅸 🅽 🅶\n')
            exit()
        elif answer == 'Y':
            reset_game()
            category_choice()
        elif len(answer) == 0:
            print('Please provide an answer.')
        else:
            print(f'{answer} is invalid. Please try again.\n')


# Calls the functions and starts the game
if __name__ == '__main__':
    clear()
    reset_game()
    get_username()
    category_choice()
