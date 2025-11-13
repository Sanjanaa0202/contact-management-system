class UpdateContact:
    def __init__(self, contact):
        self.contact = contact
        self.old_name = ""
        self.new_name = ""
        self.old_num = ""
        self.new_num = ""

    def get_input(self):
        cont_loop = True
        while cont_loop:
            print("\nWhat do you want to Update❓")
            action = '''
            1. Update the Contact Name
            2. Update the Contact Number
            3. Stop
            '''
            print(action)
            choice = int(input("Enter Your Choice Number : "))
            if choice == 1:
                old_name = input("Enter the OLD Contact Name : ")
                new_name = input("Enter the NEW Contact Name to Update🤖 : ")
                self.old_name = old_name
                self.new_name = new_name
                self.update_name()
            elif choice == 2:
                old_num = input("Enter the OLD Contact Number : ")
                new_num = input("Enter the NEW Contact Number to Update🤖 : ")
                self.old_num = old_num
                self.new_num = new_num
                self.update_number()
            else:
                print("Update Operation is Stopped🛑")
                cont_loop = False
                continue

    def update_name(self):
        if self.new_name not in self.contact:
            if self.old_name in self.contact:
                self.contact[self.new_name] = self.contact.pop(self.old_name)
                print(f"The Contact Name is Updated from '{self.old_name}' --> '{self.new_name}'✅")
            else:
                print(f"{self.old_name} is not found in your Contacts❌")
        else:
            print(f"'{self.new_name}' is already in your Contacts. Try another name!")
        return

    def update_number(self):
        new = True
        old = True
        for name in self.contact:
            for lst in self.contact[name]:
                if self.new_num not in lst.keys():
                    new = True
                    if self.old_num in lst.keys():
                        old = True
                        deleted = lst[self.old_num]
                        lst[self.new_num] = deleted
                        del lst[self.old_num]
                        print(f"The Contact Number is Updated to '{self.old_num}' --> '{self.new_num}'✅")
                        return
                    else:
                        old = False
                        break
                else:
                    new = False
                    break
            if not new:
                print(f"'{self.new_num}' is already in your Contacts saved as '{name}'")
                return
            if not old:
                print(f"'{self.old_num}' is not in your Contacts❌")
                return