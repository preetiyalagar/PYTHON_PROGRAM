#Multiple Inheritance - Inventory example
#Base class - item_det
class item_det:
    icode=input("Enter item code:")
    iname=input("Enter item Name:")

    def show_item_det(self):
        print("Item code:", self.icode)
        print("Item name:", self.iname)
#Base class - bill_det
class bill_det:
    qty=int(input("Enter Qty:"))
    price=int(input("Enter Price:"))
    tot=qty*price

    def show_bill_det(self):
        print("Item Qty:",self.qty)
        print("Item Price:",self.price)
        print("Total:",self.tot)
#Child class invent_det Begins with inheriting Base classes item_det and bill_det
class invent_det(item_det, bill_det):
    tax=bill_det.tot*18/100
    bill_amt=bill_det.tot+tax
    def show_invent_det(self):
        print("TAX 18%:",self.tax)
        print("Total amount:",self.bill_amt)

print("Inventory details")
print("------------------------------")
i=invent_det()        #Child class instance / obj
i.show_item_det()   
i.show_bill_det()
i.show_invent_det()
