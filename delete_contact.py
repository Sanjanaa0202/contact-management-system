class DeleteContact:
    def __init__(self, contact):
        self.contact = contact
        self.name = ""
        self.num = ""

    def get_input(self):
        cont_loop = True
        while cont_loop:
            print("\nWhat do you want to Delete❓")
            action = '''
            1. Delete Contact Name
            2. Delete Contact Number
            3. Stop
            '''
            print(action)
            choice = int(input("Enter Your Choice Number : "))
            if choice == 1:
                name = input("Enter the Contact Name to 🗑️ : ")
                self.name = name
                self.delete_name()
            elif choice == 2:
                num = input("Enter the Contact Number to 🗑️ : ")
                self.num = num
                self.delete_number()
            else:
                print("Delete Operation is Stopped🛑")
                cont_loop = False
                continue

    def delete_name(self):
        if self.name in self.contact:
            length = len(self.contact[self.name])
            if length > 1:
                print(f"'{self.name}' has more than 1 Phone Number!⚠️")
                cont_del = input("Do you want to Continue Deletion of your Contact Name (Y/N)❓")
                if cont_del == 'y' or cont_del == 'yes':
                    self.contact.pop(self.name)
                    print(f"Your Contact '{self.name}' has been Successfully Deleted✅")
                    return
                else:
                    return
            else:
                self.contact.pop(self.name)
                print(f"Your Contact '{self.name}' has been Successfully Deleted✅")
                return
        else:
            print(f"'{self.name}' is not in your Contacts❌")
            return

    def delete_number(self):
        found_num = False
        for name in self.contact:
            for lst in self.contact[name]:
                if self.num in lst:
                    found_num = True
                    del lst[self.num]
                    if len(lst) == 0:
                        print(f"Your Contact Number '{self.num}' is Successfully Deleted✅")
                        print(f"Invalid to store Contact Name without Contact Number!⚠️")
                        self.name = name
                        self.delete_name()
                        return
                    else:
                        print(f"Your Contact Number '{self.num}' is Successfully deleted from the Contact Name '{name}'")
        if not found_num:
            print(f"{self.num} is not in your Contacts❌")
        return