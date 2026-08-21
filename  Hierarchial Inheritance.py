#Hierarchial Inheritanc using Python
class Company: #Base class
    def showcmp(self):
        cmp='ABC Ltd'
        print('Company:',cmp)
class Web(Company): #Derive class - 1
    def showweb(self):
        ec='E001'
        role='web developer'
        print("Ecode:",ec)
        print("Role:",role)
class DBA(Company): #Derive class - 2
    def showdba(self):
        ec='E002'
        role='Database admin'
        print("Ecode:",ec)
        print("Role:",role)
def main2():
    print("Web developer")
    w=Web()
    w.showweb()
    w.showcmp()
    print("\nDBA Object")
    d=DBA()
    d.showdba()
    d.showcmp()
#call main2
main2()
        
