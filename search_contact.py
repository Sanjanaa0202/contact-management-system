class SearchContact:
    def __init__(self, contact):
        self.contact = contact
        self.name = ""
        self.num = ""

    def get_input(self):
        cont_loop = True
        while cont_loop:
            print("\nHow do you want to Search❓")
            action = '''
            1. Search by Contact Name
            2. Search by Contact Number
            3. Stop
            '''
            print(action)
            choice = int(input("Enter Your Choice Number : "))
            if choice == 1:
                name = input("Enter the Contact Name to 🔍 : ")
                self.name = name
                self.search_by_name()
            elif choice == 2:
                num = input("Enter the Contact Number to 🔍 : ")
                self.num = num
                self.search_by_number()
            else:
                print("Search Operation is Terminated🛑")
                cont_loop = False
                continue

    def search_by_name(self):
        if self.name in self.contact:
            print(f"{self.name} : ")
            for lst in self.contact[self.name]:
                print(lst)
        else:
            print(f"'{self.name}' is not found in your contacts❌")
        return

    def search_by_number(self):
        for name in self.contact:
            for lst in self.contact[name]:
                if self.num in lst.keys():
                    print(f"{name} : ")
                    print(f"{lst}")
                    return
        print(f"'{self.num}' is not in your Contacts")
        return