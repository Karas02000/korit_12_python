import random

def print_answer(s:list):
    for x in s:
        print(x,end='')
    print()

word_list = ['apple', 'seven', 'angel']
chosen_word = random.choice(word_list)
answer = []
a_len = len(chosen_word)

for i in range(a_len):
    answer.append('_')

game = True
counter1 = 5
counter2 = a_len
win = False
while game:
    print_answer(answer)
    get = input('알파벳을 입력하여 주세요. >>> ').lower()
    if chosen_word.find(get) == -1:
        counter1 -= 1
    else:
        i: int
        for i in range(a_len):
            if chosen_word[i] == get:
                answer[i] = get[0]
                counter2 -= 1
    if counter1 == 0:
        game = False
    elif counter2 == 0:
        win = True
        game = False
if win:
    print(f"축하드립니다. 단어는 {chosen_word}였습니다.")
else:
    print(f"단어는 {chosen_word}였습니다.")