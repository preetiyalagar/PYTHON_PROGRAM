#Multilevel Inheritance in PYTHON
class India:
    def first(self):
        print('1.India is the largest democratic country in the world')
class Karnataka(India):
    def sec(self):
        print('2.Karnataka is famous for IT and Coffee Production')
class Bengaluru(Karnataka):
    def third(self):
        print('3.Bengaluru also known as Silicon valley of India')
b=Bengaluru()
b.first()
b.sec()
b.third()
