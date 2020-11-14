class User():
    name = ""
    e_mail = ""
    age = ""
    passw = ""

    def __init__(self, name, email, passw, age = None):
        self.name = name
        self.e_mail = email
        self.passw = passw
        self.age = age

    def set_age(self, age):
        self.age = age

    def get_data(self):
        print(f"Userdata of user {self.name}")
        print(f"\t{self.e_mail}")
        print(f"\t{self.age}")

class Admin(User):
    privilegies = [] 

    def __init__(self, name, email, passw, age = None):
        super().__init__(name, email, passw, age = None)

    def set_privilegies(self, privilegies):
        self.privilegies = privilegies

    def get_privilegies(self):
        print(f"Admin {self.name} can:")
        for i in self.privilegies:
            print(f"\t{i}")

    

me = Admin("kotobazza", "nicolka.morgashew@gmail.com", "jiterp")

me.set_age(17)
me.set_privilegies(["set objects", "restore_system_configs", "change_privilegies", "reload_system"])

me.get_privilegies()