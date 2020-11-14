class SystemObject():
    def __init__(self, object_type):
        self.object_type = object_type

    def call(self, string):
        print(f"------{string}")
        eval(string)
        

    def get_inform(self):
        print(f"{self.object_type}")


class System(SystemObject):
    def __init__(self, object_type, name, admin):
        super().__init__(object_type)
        self.name = name
        self.admin = admin

class User(SystemObject):
    def __init__(self, object_type, privilegie, name, passw):
        super().__init__(object_type)
        self.name = name
        self.passw = passw
        self.privilegie = privilegie

    def data(self):
        print(f"User:{self.name} has a {self.privilegie} privilegie")

kotobaza = User("user_object", "fulladmin", "kotobaza", "jij")


system = System("sys_type", "synthesa", kotobaza)

while True:
    system.call(input())