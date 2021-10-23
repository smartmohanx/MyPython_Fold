class parent_clas:
    def __init__(self):
        print('''
        self.title = "SIGITI"
        self.name1 = "mohan"
        self.name2 = "dill"
        self.name3 = "soudha"
        ''')
        self.title = "SIGITI"
        self.name1 = "mohan"
        self.name2 = "dill"
        self.name3 = "soudha"

class Children(parent_clas):
    def mohan(self):
        #parent_clas.__init__(self)
        print("my name is:{0}".format(self.title),self.name1)


ob = Children()
ob.mohan()