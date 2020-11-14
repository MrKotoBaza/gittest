class System:
    def __init__(self, name, rules="ADMIN"):
        self.name = name
        self.rules = rules
        self.ID_DICT = {}

    def call(self, string):
        #if string[:string.find("(")] not in dir(System):
            #eval(str(string))
        #print(dir(System))

        print(string)


    def get_system_info(self):
        print(self.name)
        print(f"Registred {len(self.ID_DICT)} id's")
        print(f"Has {self.rules} rules")

    def change_usergroup(self, usr, grp = None, mode = None):

        if grp:
            usr.rules = grp
        if mode:
            usr.mode = mode

    

        