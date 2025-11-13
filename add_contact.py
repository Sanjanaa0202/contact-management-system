class AddContact:
    def __init__(self, contact, speed_dial_object, favorite_object):
        self.name = ""
        self.num = ""
        self.fav = False
        self.contact = contact
        self.num_dict = {}
        self.speed_dial_object = speed_dial_object
        self.favorite_object = favorite_object
        self.speed_dial = 0

    def check_name(self):
        if self.name == "":
            print("Name is Required to save in your Contacts📌")
            return False
        if self.name in self.contact:
            print(f"'{self.name}' is already in your Contacts!👀")
            add = input(f"Do you want to add New Number to '{self.name}' (Y/N)❓ ")
            if add == 'y' or add == "yes":
                return True
            else:
                return False
        else:
            return True

    def check_num(self):
        if self.num == "":
            print("Phone Number is Required to save in your Contacts📌")
            return False
        if len(self.num) > 10:
            self.num = self.num[3:]
        if len(self.num) < 10:
            print(f"Enter a valid 10 Digit Number \n {10 - len(self.num)} number(s) (is/are) missing☠️")
            return False
        elif len(self.num) > 10:
            print(f"Enter a valid 10 Digit Number \n {len(self.num) - 10} number(s) (is/are) more☠️")
            return False
        elif int(self.num[0]) not in [6, 7, 8, 9]:
            print(f"Enter a valid 10 Digit Number.\n{self.num} is Invalid!")
            return False
        else:
            for name in self.contact:
                for lst in self.contact[name]:
                    if self.num in lst:
                        print(f"'{self.num}' is already saved in your contacts in the Name '{name}'👀")
                        return False
        return True

    def get_input(self):
        self.name = input("Enter your Contact Name : ").lower()
        if self.check_name():
            self.num = input("Enter your (10 digit) Contact Number : ")
            if self.check_num():
                to_fav = input("Do you want this Contact in Favorites❤️? (Y/N)? ")
                if to_fav.lower() == 'y' or to_fav.lower() == "yes":
                    if self.favorite_object.add_to_favorites(self.num, self.name):
                        self.fav = True
                    else:
                        self.fav = False
                else:
                    self.fav = False
                self.speed_dial = int(input("Enter any number between (1-9) to add to Speed Dial\n "
                                        "If you don't want speed dial enter (0) : "))
                self.speed_dial_object.add_number_to_speed_dial(self.num, self.speed_dial, self.name)
                self.add_contact()

    def add_contact(self):
        self.num_dict[self.num] = {
            "favorites" : self.fav,
            "speed dial" : self.speed_dial
        }
        if self.name in self.contact:
            self.contact[self.name].append(self.num_dict)
            print(f"'{self.num}' is successfully added with your existing Contact Name '{self.name}'✅")
        else:
            self.contact[self.name] = [self.num_dict]
            print(f"'{self.name}' is successfully added to your Contacts✅")
        return