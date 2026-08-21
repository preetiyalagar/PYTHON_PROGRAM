#single inheritance
class A:
    def showA(self):
        print('inside the Base class - A')

class B(A):
    def showB(self):
        print('inside the Derive class - B')

b=B()      #object / instance
b.showA()  #base class method
b.showB()  #derive class method
