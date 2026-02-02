import random

word_list = ['apple', 'seven', 'angel']
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append('_')

stages = ['''
    +----+
    |    |
         |
         |
         |
=============
''','''
    +----+
    |    |
    0    |
         |
         |
         |
=============
''','''
    +----+
    |    |
    0    |
    |    |
         |
         |
=============
''','''
    +----+
    |    |
    0    |
    |\   |
         |
         |
=============
''','''
    +----+
    |    |
    0    |
   /|\   |
         |
         |
=============
''','''
    +----+
    |    |
    0    |
   /|\   |
   /     |
         |
=============
''','''
    +----+
    |    |
    0    |
   /|\   |
   / \   |
         |
=============
''']

print(stages)