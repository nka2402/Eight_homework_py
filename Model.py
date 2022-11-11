import Controller

phone_book = []
path = 'Data/'

def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path
    path += file

def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)

def save_file():
    global phone_book
    global path
    phone_book = get_phone_book_save()
    with open(path, "w", encoding="UTF-8") as data:
        data.write(phone_book)

def get_phone_book_save():
    global phone_book
    new_phone_book = []
    for contact in phone_book:
        new_phone_book.append(';'.join(contact) + '\n')
    return ''.join(new_phone_book)            

def add_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id, choise, value):
    global phone_book
    phone_book [int(id)][int(choise)] = value

