class SpeedDial:
    def __init__(self, contact):
        self.contact = contact
        self.speed_dial_num = {}
        self.assigned_speed_dial_num = 0
        self.phone_no = ""
        self.name = ""

    def get_input(self):
        cont_loop = True
        while cont_loop:
            print("\nWhat Operation do you want to perform in Speed Dial❓")
            action = '''
            1. Add Number to Speed Dial
            2. Remove Number from Speed Dial
            3. Display Speed Dial Information
            4. Stop
            '''
            print(action)
            choice = int(input("Enter Your Choice Number : "))
            if choice == 1:
                self.assigned_speed_dial_num = input("Enter any number between 1-9 to add to Speed Dial : ")
                self.phone_no = input("Enter the Contact Number to add to Speed Dial : ")
                self.add_number_to_speed_dial(self.phone_no, self.assigned_speed_dial_num, self.name)
            elif choice == 2:
                self.phone_no = input("Enter the Contact Number to remove from Speed Dial : ")
                self.remove_number_from_speed_dial()
            elif choice == 3:
                self.display_speed_dial_number()
            else:
                print("Speed Dial is Terminated🛑")
                cont_loop = False
                continue

    def is_available(self):
        if self.assigned_speed_dial_num > 9 or self.assigned_speed_dial_num < 1:
            print(f"'{self.assigned_speed_dial_num}' is not valid for Speed Dial❌. "
                  f"Speed Dial will not be Assigned to '{self.phone_no}'")
            self.assigned_speed_dial_num = 0
            return False
        elif self.assigned_speed_dial_num == 0:
            print(f"{self.assigned_speed_dial_num} is assigned for Customer Care."
                  f"Speed Dial will not be Assigned to {self.phone_no}")
            return False
        else:
            if self.assigned_speed_dial_num in self.speed_dial_num:
                print(f"{self.assigned_speed_dial_num} is already assigned to {self.speed_dial_num[self.assigned_speed_dial_num]}"
                      f"Speed Dial will not be Assigned to {self.phone_no}")
                self.assigned_speed_dial_num = 0
                return False
        return True

    def add_number_to_speed_dial(self, phone_no, speed_dial, add_name):
        self.phone_no = phone_no
        self.assigned_speed_dial_num = speed_dial
        self.name = add_name
        if self.is_available():
            for name in self.contact:
                for lst in self.contact[name]:
                    if self.phone_no in lst:
                        self.speed_dial_num[self.assigned_speed_dial_num] = {self.phone_no : name}
                        print(f"'{self.assigned_speed_dial_num}' is Successfully assigned to the Contact '{name}' --> '{self.phone_no}'✅")
                        return True

            if len(self.name) == 0:
                print(f"The Contact Number '{self.phone_no}' is not in your Contacts❌")
                return False
            else:
                self.speed_dial_num[self.assigned_speed_dial_num] = {self.phone_no: self.name}
                print(f"'{self.assigned_speed_dial_num}' is Successfully assigned to the Contact '{self.name}' --> '{self.phone_no}'✅")
                return True

        return False

    def remove_speed_dial_num_in_contact(self):
        for name in self.contact:
            for lst in self.contact[name]:
                if self.phone_no in lst:
                    lst[self.phone_no]["speed dial"] = 0
                    return True

    def remove_number_from_speed_dial(self):
        for dial_num in self.speed_dial_num:
            for phone_num in self.speed_dial_num[dial_num]:
                if phone_num == self.phone_no:
                    print(f"The Contact '{self.speed_dial_num[dial_num][self.phone_no]}' --> '{self.phone_no}' is Successfully removed from Speed Dial✅")
                    self.remove_speed_dial_num_in_contact()
                    del self.speed_dial_num[dial_num]
                    return True

        for name in self.contact:
            for lst in self.contact[name]:
                if self.phone_no in lst:
                    print(f"The Contact Number '{self.phone_no}' is not assigned to Speed Dial⚠️")
                    return True

        print(f"The Contact Number '{self.phone_no}' is not in your Contacts❌")
        return True

    def display_speed_dial_number(self):
        if len(self.speed_dial_num) == 0:
            print(f"No Contacts is added to your Speed Dial")
            return True

        for speed_dial in self.speed_dial_num:
            print(f"{speed_dial} --> {self.speed_dial_num[speed_dial]}")
        print(f"The Speed Dial which are assigned to your Contacts are Displayed✅")
        return True