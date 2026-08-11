class Test:

    inv='Inventory details'
    def inp(self):
        self.pc, self.pn=input('Input Code and Name:').split()
        self.pr, self.qt=input('Price and qty:').split()
        self.pr=int(self.pr)
        self.qt=int(self.qt)

    def cal(self):
        self.tot=self.pr*self.qt
        self.tax=self.tot*(10/100)
        self.dis=self.tot*(5/100)
        self.gtot=self.tot+self.tax-self.dis

    def sho(self):
        print("-----------", self.inv, "-----------")
        print("Code:",self.pc, "\nName:", self.pn, "\nPrice:", self.pr, "\nQty:", self.qt)
        print("\nTotal:",self.tot, "\nTax:", self.tax, "\nDiscount:",self.dis)
        print("Bill amount:",self.gtot)

t=Test()
t.inp()
t.cal()
t.sho()
