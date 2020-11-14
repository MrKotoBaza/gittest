import random
import string


class User:
    def __init__(self, name, rules="non_type", mode="user", lvl=-1, system=None):
        self.name = name
        self.rules = rules
        self.mode = mode
        self.lvl = lvl
        self.system = system

        self.__generate_id()

    def set_passwd(self, pswd):
        self.passwd = pswd

    def __generate_id(self):
        using = string.digits
        st = "".join([random.choice(using) for i in range(10)])
        while st in self.system.ID_DICT:
            st = "".join([random.choice(using) for i in range(10)])

        self.system.ID_DICT.update({st: self.name})


class System:
    def __init__(self, name, rules="ADMIN"):
        self.name = name
        self.rules = rules
        self.ID_DICT = {}

    def call(self, string):
        eval(str(string))


system = System("Synthesa")

user = User("kotobaza", system=system)


while True:
    eval(input())


