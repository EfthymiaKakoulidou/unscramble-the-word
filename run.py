import random

animals = [['c','a','t'],['d','o','g'],['h','o','r','s','e']]
countries = [['g','r','e','e','c','e'],['i','t','a','l','y'], ['s','w','e','d','e','n']]
food = [['p','a','s','t','a'], ['r','i','c','e'], ['m','e','a','t']]

print('Hello Tim! Ready to unscrable the word?')
print('You will be given words whose letters are scrambled.')
print('Your goal is to unscramble them and find the word')
print('Please provide the number of the category of words you want to play with:')
print('1.Animals 2. Countries 3. Food')

x = input('Write the number of the category here:')
print('You Chose ' + x)
word = random.choice(animals)
print(word)
random.shuffle(word)
print(word)

