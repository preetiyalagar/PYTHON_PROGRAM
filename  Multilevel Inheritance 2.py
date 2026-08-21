#Multilevel Inheritance in PYTHON
class Grandparent:
    def first(self):
        print('1.I am a Grandparent')
class parent(Grandparent):
    def sec(self):
        print('2.I am a parent')
class child(parent):
    def third(self):
        print('3.I am a child')
c=child()
c.first()
c.sec()
c.third()

