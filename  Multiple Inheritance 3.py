#Multiple Inheritance - Inventory example
#Base class - item_det
class Father_det:
    focc=input("Enter occupation:")
    fname=input("Enter Father Name:")

    def show_Father_det(self):
        print("Father occupation:", self.focc)
        print("Father name:", self.fname)
#Base class - Mother_det
class Mother_det:
    mocc=input("Enter occupation:")
    mname=input("Enter Mother Name:")
    
    def show_Mother_det(self):
        print("Mother occupation:", self.mocc)
        print("Mother name:", self.mname)
        
#Child class child_det Begins with inheriting Base classes Father_det and Mother_det
class child_det(Father_det, Mother_det):
    cedu=input("Enter education:")
    cname=input("Enter child name:")
    
    def show_child_det(self):
        print("child education:",self.cedu)
        print("child name:",self.cname)

print("child details")
print("------------------------------")
i=child_det()        
i.show_Father_det()   
i.show_Mother_det()
i.show_child_det()


    
    

