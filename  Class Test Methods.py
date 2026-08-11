class Test:
    def show(self):
        print('normal method')

    def show2(self):
        print('normal method 2')

    def __init__(self): #spl method
        print('spl method - constructor')
t=Test() #creating object / instance
t.show() #normal method
t.show2() #normal method
