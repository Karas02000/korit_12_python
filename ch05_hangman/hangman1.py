import random

word_list = ['apple', 'seven', 'angel']
chosen_word = random.choice(word_list)
guess = input('알파벳을 입력하여 주세요.')

for letter in chosen_word:
    if letter == guess:
        print('정답')
    else:
        print('오답')