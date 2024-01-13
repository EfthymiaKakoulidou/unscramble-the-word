import random

animals = [['c','a','t'],['d','o','g'],['h','o','r','s','e']]
countries = [['g','r','e','e','c','e'],['i','t','a','l','y'], ['s','w','e','d','e','n']]
food = [['p','a','s','t','a'], ['r','i','c','e'], ['m','e','a','t']]

print('Hello Tim! Ready to unscrable the word?\n')
print('You will be given words whose letters are scrambled.\n')
print('Your goal is to unscramble them and find the word\n')
print('Please provide the number of the category of words you want to play with:\n')
print('1.Animals 2. Countries 3. Food\n')

number = int(input("Please enter a number:"))
if number == 1:
    print('You chose "Animals"')
    print('Your word is:')
    word = random.choice(animals)
    random.shuffle(word)
    print(word)
if number == 2:
    print('You chose "Countries"')
    print('Your word is:')
    word = random.choice(countries)
    random.shuffle(word)
    print(word)
if number == 3:
    print('You chose "Food"')
    print('Your word is:')
    word = random.choice(food)
    random.shuffle(word)
    print(word)



