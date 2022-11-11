import Model
import View


def start():
    choice = 1
    while choice != 9:
        choice = View.show_menu()  
        match(choice):
            case 0:
                phone_book = Model.get_phone_book()
                View.show_phone_book(phone_book)
            case 1:
                path = View.input_path()
                Model.set_path(path)
                Model.open_file()
            case 2:
                Model.save_file()
            case 3:
                contact = View.input_contact()
                Model.add_contact(contact)
            case 4:
                contact = View.input_change()
                Model.change_contact(*contact)
            case 5:
                pass

            case 6:
                pass