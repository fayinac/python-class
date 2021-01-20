import random
ls = ['apple','orange','credit','wardrobe']
score = 0

def scramble(w):
    letters = list(w)
    random.shuffle(letters)
    scramble_word = ''
    for i in letters:
        scramble_word = scramble_word + i
    return scramble_word

random.shuffle(ls)
for word in ls:
    new_word = scramble(word)
    print(new_word)
    response = input('unscramble this word:')
    if response == word:
        print('you are correct')
        score += 1 
    else:
        print('the correct word is:', word) 
    asktoquit = input('say y to quit or enter to continue: ')
    if asktoquit == 'y' or 'yes':
        break      

print('you have done all the words!')
print('you got', score, 'correct')
 
