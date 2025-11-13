class DisplayContact:
    def __init__(self, contact):
        self.contact = contact

    def display(self):
        for name in self.contact:
            print(name)
            for lst in self.contact[name]:
                print(lst)
            print()