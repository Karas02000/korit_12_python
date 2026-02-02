import random

def printList(List):
    for item in List:
        print(item,end=' ')
    print()

word_list = ['apple', 'seven', 'angel']
chosen_word = random.choice(word_list)
print(f'테스트 단어 : {chosen_word}')

display = []
# display.append('김')
# display.append('영')
# print(display)
# # display[1]=1
# print(display)
# display[4]=4
# print(display)

for letter in chosen_word:
    display.append('_')

printList(display)

guess = input()

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = chosen_word[i]
printList(display)