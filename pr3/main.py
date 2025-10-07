def get_book(name_file):
    """Функция, которая считывает файл и возвращает список списков"""
    with open(name_file, "r", encoding='utf=8') as f:
        f.readline()#пропускаем первую строку с заголовками, в ТЗ не сказано, что он должен возвращаться
        full_list = f.readlines()
        new_list = list(map(lambda line: line.replace('\n',"").split("|"), full_list))
    return new_list

def filtered_books(all_name, name):
    """Функция проверяет, есть ли заданное слово в списке и вовзращает, в случае, если есть
    после дополнительная функция слепливает 2 и 3 элемент списка через ', '"""
    all_name = list(filter(lambda line: name.lower() in line[1].lower(), all_name))

    def with_str(line):
        new_line = [line[0], ', '.join(line[1:3])] + line[3:]
        return new_line

    all_name = list(map(lambda line: with_str(line), all_name))

    return all_name

def save_file(bwp):
    """Функция со *, для сохранения в файл. использовался иморт csv для осваивания нового модуля"""
    import csv
    with open ("book_with_python.csv", "w", newline="", encoding='utf=8') as f:
        save_text = csv.writer(f, delimiter="|")
        save_text.writerows(bwp)

def list_in_tuple_books(books):
    """функция, которая возвращает 1 элемент списка списков и перемножает последние"""
    def new_line_for_tuple(line):
        multiplic = int(line[2])*float(line[3])
        new_line = (line[0], multiplic)
        return new_line

    tuple_books = list(map(lambda line: new_line_for_tuple(line), books))
    print(type(tuple_books[0]))
    return tuple_books


books = get_book("booking.csv")#задание 1

list_book = filtered_books(books, "python")#задание 2

tuple_book = list_in_tuple_books(list_book)#задание 3
print(tuple_book)

save_file(list_book)
