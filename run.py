import random
import os

# Global variable that will be used to update the score

score = 0

def game(score):

    # Categories
    
    animals = ['CAT','DOG','HORSE','GIRAFFE','ELEPHANT']
    countries = ['GREECE','ITALY', 'SWEDEN', 'GERMANY', 'FRANCE']
    food = ['PASTA', 'RICE', 'EGGS', 'BREAD', 'PANCAKES']

    print('Ready to unscrable the word?\n')
    username = input('Enter username: \n')
    print(f'Hello {username}!\n')
    print('You will be given words whose letters are scrambled.\n')
    print('Your goal is to unscramble them and find the word.\n')
    print('Please provide the number of the category of words you want to play with:\n')
    
    
    # Player chooses category

    def category_choice():
        """
        Asks for input to choose the category.
        Validates it.
        """
        while True:
            print('\033[1;32m 1. Animals 2. Countries 3. Food \n')
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
            print("No words left to unscramble. Game Over")
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
        """
        global score
        
        if str(players_guess) == str(unscrambled_word):
            score = score + 1
            print(f'Right! Your Score is : {score}\n')
            if len(animals)<len(food):
                scramble_word(animals)
            elif len(food)<len(animals):
                scramble_word(food)
            else:
                scramble_word(countries)
        else:
            print(f'The answer you provided is wrong. Your score is {score}')
        while True:    
            retry = input('Do you want to try again? Y/N : ')
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
                category_choice()
            else:
                print(f'{answer} is invalid. Please try again.\n')
                

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
