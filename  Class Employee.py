class Emp:


    def __init__(self, name, age): #spl-method
        self.name=name
        self.age=age

    def myfunc(self): #normal-method
        print("Hello my name is", self.name,"and I am", self.age,"year old")

e1=Emp("Ramesh",32)
e2=Emp("Akbar",21)
e1.myfunc()
e2.myfunc()
