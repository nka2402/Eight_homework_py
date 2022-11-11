def show_menu():
    print('0.Показать все контакты')
    print('1.Открыть файл с контактами')
    print('2.Записать файл с контактами')
    print('3.Добавить контакт')
    print('4.Изменить контакт')
    print('5.Удалить контакт')
    print('6.Поиск по контактам')

    choice = int(input('Выберите пункт меню: '))
    return choice
    
def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print('Телефонная книга пуста')
    else:
        for id, item in enumerate(phone_book):
            print(id, *item)

def input_path():
    path = input('Введите имя файла: ')
    return path

def input_contact():
    name_contact = input('Введите имя и фамилию: ')
    number_contact = input('Введите номер телефона: ')
    comment_contact = input('Введите комментарий: ')
    return(name_contact, number_contact, comment_contact)

def get_contact():
    id = int(input('Введите ID контакта: '))
    return id

def input_change():
    id = get_contact()
    print('Что изменить?')
    choise = input('0 - имя, 1 - телефон, 2 - комментарий, 3 -  отмена')
    value = input('Введите изменения: ')
    return(id, choise, value)

def input_delete_contact():
    id = get_contact()
    print(f'Удалить контакт {id}?')
    choise = int(input('0 - нет, 1 - да'))
    if choise == 0:
        show_menu()
    elif choise == 1:
        return(id)
    else:
        print('Вы ввели некорректное значение!')

def search_contact(phone_book):
    search = input('Что мы ищем? ')
    search_book = []
    for contact in phone_book:
        for item in contact:
            if search in item:
                search_book.append(contact)
    if search_book:
        show_phone_book(search_book)
    else:
        print('Ничего не найдено!')

