import requests
import random

print('Игра виселица')
res = requests.get('https://raw.githubusercontent.com/LussRus/Rus_words/master/UTF8/txt/nouns/summary.txt')
LIST = res.text.split('\n')
englich_word = 'й ц у к е н г ш щ з х ъ ф ы в а п р о л д ж э я ч с м и т ь б ю'
s = englich_word.split(' ')
def more_than_five(list):
    return len(list) >= 5 and len(list) <= 8
    
word_everybody = list(filter(more_than_five, LIST))
WORD = random.choice(word_everybody)
word = WORD.lower()
print(word)
print('Количетсво букв '+ str(len(word)) + ':' + '_' * len(word))
guess_wold = ['_'] * len(word)
#chances = len(word) + 2

def win(guess_wold):
    win = ''.join(guess_wold)
    return win

def gallows():
    chances = len(word) + 2
    try:
        while guess_wold != word and  chances > 0:
            if win(guess_wold) == word:
                print('Вы угадали слово!)')
                break
            else:
                win(guess_wold)
                symbol = input('Введите пропесную букву: ' )
                if len(symbol) > 1:
                    raise Exception('Введите один символ!')
                if not (symbol in s):
                    raise Exception('Это не прописная буква!')
                if symbol in word:
                    for index, latter in enumerate(word):
                        if latter == symbol:
                            guess_wold[index] = symbol
                else:
                    print('Буква не угадана(')
                    chances = chances - 1
                for i in guess_wold:      
                    print(i , end='')
                print('\nОсталось попыток: ' + str(chances))

    except Exception as e:
        print(e)
        gallows()
gallows()
