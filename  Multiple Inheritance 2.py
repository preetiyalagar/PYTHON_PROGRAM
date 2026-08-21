#multiple Inheritance in Python with Student and Marks Details
#-Base class
class college:
    cname='SB College'
    def show_coll(self):
        print('College name:', self.cname)
class std_per_det:
    regno=input("Enter RegNO:")
    name=input("Enter Name:")
    course=input("Enter Course:")
#-Base class Method
    def show_std(self):
        print('Reg No:',self.regno)
        print('Name:',self.name)
        print('Course:',self.course)
#Derived class
class marks_det(std_per_det,college):
    p=int(input("Enter Physics Marks:"))
    c=int(input("Enter Chemistry Marks:"))
    m=int(input("Enter Maths Marks:"))
    b=int(input("Enter Biology Marks:"))
    tot=p+c+m+b
    avg=tot/4
#Derive class Method
    def show_marks(self):
        print('Physics:',self.p)
        print('Chemistry:',self.c)
        print('Maths:',self.m)
        print('Biology:',self.tot)
        print('Average Marks:',self.avg)
print("\nStudent Marks details")
print("===============================")
m=marks_det()
m.show_coll()
m.show_std()
m.show_marks()
