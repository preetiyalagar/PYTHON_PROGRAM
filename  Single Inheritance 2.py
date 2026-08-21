#single inheritance
class person:
    def show_person(self):
        print('I am a Person')

class student(person):
    def show_student(self):
        print('I am a student')

s=student()       #object / instance
s.show_person()   #base class method
s.show_student()  #derive class method

