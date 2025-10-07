def len_file():
    with open ("dict.txt", "r") as f:
        i = len(f.readlines())
        return i

def read_file(count):
    with open('dict.txt', 'r', encoding='utf-8') as f:
        j = 1
        while j <= count:
            line = f.readline()
            j += 1
    riddle = line.split(" : ")
    return riddle

def count_live(count = 4):
    if count > 1:
        count -= 1
        return count
    else:
        count = 0
        return count

def start_game(riddle):
    print('\nДобро пожаловать в игру "Виселица"!')
    print('\nВам загадали загадку:' , riddle.lower())
    print ('Нужно отгадать загаданное слово.')
    print('Угадывать можно букву или слово целиком.')

def print_results(count_life): # функция вывода картинок
    if count_life == 3:
        with open('3_life.txt', 'r', encoding='utf-8') as f:
            i = 1
            for line in f:
                print(f'{i} {line}', end='')
                i += 1
    elif count_life == 2:
        with open('2_life.txt', 'r', encoding='utf-8') as f:
            i = 1
            for line in f:
                print(f'{i} {line}', end='')
                i += 1
    elif count_life == 1:
        with open('1_life.txt', 'r', encoding='utf-8') as f:
            i = 1
            for line in f:
                print(f'{i} {line}', end='')
                i += 1
    else:
        with open('0_life.txt', 'r', encoding='utf-8') as f:
            i = 1
            for line in f:
                print(f'{i} {line}', end='')
                i += 1

def replacement_char(word):# функция зашифровывания слова
    encoded = ''
    i=0
    while i < len(word):
        encoded += '\u25A0'+' '
        i += 1
    return encoded

def check_ch(word, ch, per):
    per = per.replace(' ','')
    word = word.upper()
    new_word = str('')
    k = 0
    for i in word:
        var = per[k]
        if i == ch:
            new_word += i + ' '
            k += 1
        elif i == var:
            new_word += i + ' '
            k += 1
        else:
            new_word += '\u25A0'+' '
            k += 1
    return new_word

def final(start_word, new_word):
    new_word = new_word.replace(' ', '')
    new_word = new_word.upper()
    start_word = start_word.upper()
    if start_word != new_word:
        return True
    else:
        return False

def win(word):
    print()
    print('Вы выйграли!')
    print('Загаданное слово:')
    print(word.upper())

def lose(word):
    print('\nВы проиграли. Было загадано слово: ', word)

def return_in_game():
    count_riddle = 1
    finish = True
    while count_riddle <= len_file() and finish == True:
        line = read_file(count_riddle)  # cчитываем загадку в виде списка загадка + описание
        count_riddle += 1  # cчётчик для загадок

        live = count_live(4)
        start_game(line[1])  # старт
        print_results(live)  # показываем висилицу
        main_game(live, line[0])

        contin = int(input('\nДля продолжения игры нажмите "1",'
                           '\nЕсли хотите закончить, нажмите любую кнопку: '))
        if contin != 1:
            finish = False
    else:
        print("Слова закончились.")

def main_game(live, start_word):
    word_encoded = replacement_char(start_word) #заменили буквы
    word_encoded_per = word_encoded#переменная для сравнения
    per_final = True # проверка на победу
    while per_final == True and live > 0: # играем до тех пор, пока не проиграем или пока не победим
        print("\nЗагаданное слово: ", word_encoded_per)
        char = str(input('\nВведите букву или слово:' ))
        char = char.upper()#переводим в верхний регистр
        if len(char)>1:#проверка, символ или слово
            char = char.upper()
            start_word = start_word.upper()
            if start_word != char:
                per_final = True
            else:
                per_final = False
                word_encoded = char
        else:
            word_encoded = check_ch(start_word, char, word_encoded)

        if word_encoded_per != word_encoded:
            word_encoded_per = word_encoded
            per_final = final(start_word, word_encoded)#проверяем, не выйграли ли мы случайно
            print("Верно!")
        else:
            live = count_live(live)  # Понижаем количество жизней
            print("Неверно!")
            print_results(live)  # основной вывод

    if per_final != True:
        win(start_word)
    else:
        lose(start_word)
