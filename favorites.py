class Favorites:
    def __init__(self, contact):
        self.contact = contact
        self.fav_list = []
        self.phone_no = ""
        self.name = ""

    def get_input(self):
        cont_loop = True
        while cont_loop:
            print("\nWhat Operation do you want to perform in Favorites❓")
            action = '''
            1. Add Number to Favorites
            2. Remove Number from Favorites
            3. Display Favorites
            4. Stop
            '''
            print(action)
            choice = int(input("Enter Your Choice Number : "))
            if choice == 1:
                self.phone_no = input("Enter the Contact Number to add to Favorites : ")
                self.add_to_favorites(self.phone_no, self.name)
            elif choice == 2:
                self.phone_no = input("Enter the Contact Number to remove from Favorites : ")
                self.remove_from_favorites()
            elif choice == 3:
                self.display_favorites()
            else:
                print("Favorites Functionality is Terminated🛑")
                cont_loop = False
                continue

    def add_to_favorites(self, phone_no, name):
        self.phone_no = phone_no
        self.name = name

        for fav in self.fav_list:
            for key, value in fav.items():
                if value == self.phone_no:
                    print(f"The Contact '{key}' --> '{value}' is already in your Favorites❤️")
                    return False

        for name in self.contact:
            for lst in self.contact[name]:
                if self.phone_no in lst:
                    self.fav_list.append({name : self.phone_no})
                    print(f"The Contact '{name}' --> '{self.phone_no}' is Added to Favorites❤️✅")
                    return True

        if len(self.name) == 0:
            print(f"The Contact Number '{self.phone_no}' is not in your Contacts❌")
            return False
        else:
            self.fav_list.append({self.name : self.phone_no})
            print(f"The Contact '{self.name}' --> '{self.phone_no}' is Added to Favorites❤️✅")
            return True

    def remove_favorites_in_contact(self):
        for name in self.contact:
            for lst in self.contact[name]:
                if self.phone_no in lst:
                    lst[self.phone_no]["favorites"] = False
                    return True

    def remove_from_favorites(self):
        for fav in self.fav_list:
            for key, value in fav.items():
                if value == self.phone_no:
                    print(f"The Contact '{key}' --> '{value}' is removed from your Favorites❤️")
                    self.remove_favorites_in_contact()
                    self.fav_list.remove(fav)
                    return True

        for name in self.contact:
            for lst in self.contact[name]:
                if self.phone_no in lst:
                    print(f"The Contact Number '{self.phone_no}' is your Favorites❤️")
                    return True

        print(f"The Contact Number '{self.phone_no}' is not in your Contacts❌")
        return True

    def display_favorites(self):
        if not self.fav_list:
            print(f"No Contacts is added to your Favorites❤️")
            return True

        for fav in self.fav_list:
            print(fav)
        print(f"The Favorites❤️ which are in your Contacts are Displayed✅")
        return True