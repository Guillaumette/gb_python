from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    """Функция считывает данные из базы"""
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    """Функция отображает содержимое базы данных"""
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("База пуста!\n")


def add_new():
    """Функция добавляет новую запись"""
    global last_if

    lst = ['surname', 'name', 'patronym', 'phone number']
    answers = []
    for i in lst:
        answers.append(data_collection(i))
    
    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding='utf-8') as f:
            f.write(f'{" ".join(answers)}\n')
        print('Ваши данные были добавлены в телефонную книгу!\n')
    else:
        print('Данные уже существуют!')


def delete():
    """Функция для удаления записи"""
    global all_data
    symbol = '\n'
    show_all()
    del_rec = input("Введите id-номер записи: ")

    if exist_contact(del_rec, ""):
        all_data = [k for k in all_data if k[0] != del_rec]

        with open(file_base, 'w', encoding='utf-8') as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!\n")
    else:
        print("Данные некорректны!")


def change(data_tuple):
    """Функция для изменения существующей записи"""
    global all_data
    symbol = '\n'

    record_id, num_data, data = data_tuple

    for i, j in enumerate(all_data):
        if j[0] == record_id:
            j = j.split()
            j[int(num_data)] = data
            if exist_contact(0, " ".join(j[1:])):
                print("Данные уже существуют!")
                return
            all_data[i] = " ".join(j)
            break

    with open(file_base, 'w', encoding='utf-8') as f:
            f.write(f'{symbol.join(all_data)}\n')
    print('В данные внесены изменения!\n')


def search_contact():
    """Функция для поиска контакта в базе"""
    search_data = exist_contact(0, input("Что ищем? "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Ввод некорректен")


def exist_contact(rec_id, data):
    """Функция для проверки записи в базе
    :type data: проверка записи
    :type rec_id: проверка id
    """

    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):
    """Функция для проверки полученных данных"""

    answer = input(f'Введите {num}: ')
    while True:
        if num in "surname name patronym":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Данные некорректны!\n"
                       f"Используйте только буквы алфавита,"
                       f"длину номера - 11 цифр\n"
                       f"Введите {num}: ")
    return answer


def edit_menu():
    """Меню редактирования"""
    dicct = {"1": "surname", "2": "name", "3": "patronym", "4": "phone number"}

    show_all()
    record_id = input("Введите id-номер записи: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nИзменить:")
            change = input("1. surname\n"
                           "2. name\n"
                           "3. patronym\n"
                           "4. phone number\n"
                           "5. exit\n")
            
            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(dicct[change])
                case "5":
                    return 0
                case _:
                    print("Данные не распознаны, повторите ввод.")
    else:
        print("Дынные некорректны!")


def exp_bd(name):
    """Сохранение данных в новый файл"""
    symbol = "\n"

    if not path.exists(name):
        with open(f'{name}.txt', 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')


def imp_bd(name):
    global file_base

    if path.exists(name):
        file_base = name
        read_records()


def exp_imp_menu():
    """Меню экспорта/импорта"""

    while True:
        print("\nМеню экспорта/импорта:")
        move = input("1. Импорт\n"
                     "2. Экспорт\n"
                     "3. Выход\n")
        
        match move:
            case "1":
                imp_bd(input("Введите название файла: "))
            case "2":
                exp_bd(input("Введите название файла: "))
            case "3":
                return 0
            case _:
                print("Данные не распознаны, повторите ввод.")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Телефонная книга:\n"
                       "1. Показать все записи\n"
                       "2. Добавить запись\n"
                       "3. Найти запись\n"
                       "4. Внести изменения\n"
                       "5. Удалить\n"
                       "6. Экспорт/импорт\n"
                       "7. Выйти\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change(work)
            case "5":
                delete()
            case "6":
                exp_imp_menu()
            case "7":
                play = False
            case _:
                print("Попробуйте еще!\n")

main_menu()