from add_contact import AddContact
from search_contact import SearchContact
from update_contact import UpdateContact
from delete_contact import DeleteContact
from display_contact import DisplayContact
from speed_dial import SpeedDial
from favorites import Favorites

contact = {}

speed_dial_object = SpeedDial(contact)
favorites_object = Favorites(contact)
add_contact_object = AddContact(contact, speed_dial_object, favorites_object)
search_contact_object = SearchContact(contact)
update_contact_object = UpdateContact(contact)
delete_contact_object = DeleteContact(contact)
display_contact_object = DisplayContact(contact)

def add_contact():
    add_contact_object.get_input()

def search_contact():
    search_contact_object.get_input()

def speed_dial():
    speed_dial_object.get_input()

def update_contact():
    update_contact_object.get_input()

def delete_contact():
    delete_contact_object.get_input()

def display_contact():
    display_contact_object.display()

def favorites():
    favorites_object.get_input()

def choose(choices):
    match choices:
        case 1:
            add_contact()
        case 2:
            search_contact()
        case 3:
            speed_dial()
        case 4:
            update_contact()
        case 5:
            delete_contact()
        case 6:
            display_contact()
        case 7:
            favorites()


cont_loop = True
while cont_loop:
    print("\nWelcome to Contact Management System")
    action = '''
    1. Add to Contacts
    2. Search Contact
    3. Speed Dial
    4. Update Contact
    5. Delete Contact
    6. Display Contacts
    7. Favorites
    8. Stop
    '''
    print(action)
    my_choice = int(input("Enter your choice number : "))
    if my_choice < 8:
        choose(my_choice)
    elif my_choice == 8:
        print("Actions are Successfully Stopped🛑\n")
        cont_loop = False
        continue
    else:
        print("Enter a Valid Number☠️\n")
        continue