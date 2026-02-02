import random
from hangman_arts import *
from hangman_word_list import word_list

display = []
def play_hangman():
    chosen_word = random.choice(word_list)
    for _ in range(len(chosen_word)):
        display.append('_')
    live = 0
    win = True
    chance = len(stages)
    print(logo)
    while True:
        print(stages[live])
        print(' '.join(display))
        guess = input('알파벳을 입력하세요 >>> ').lower()
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = chosen_word[i]
        else:
            live += 1
            chance -= 1
        if '_' not in display:
            print(stages[live])
            break
        if stages[live] == stages[-1]:
            print(stages[live])
            win = False
            break
        print(f'앞으로 기회가 {chance-1}번 남았습니다.')
    if win:
        print(f'정답입니다.!! 답은 {' '.join(display)} 입니다.')
    else:
        print(f'오답입니다. 답은 {' '.join(chosen_word)} 였습니다.')