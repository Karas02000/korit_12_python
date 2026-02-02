import random

word_list = ['apple', 'seven', 'angel']
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append('_')

print(' '.join(display))


while '_' in display:
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
    print(' '.join(display))

print(f'정답입니다.!! 답은 {' '.join(display)} 입니다.')