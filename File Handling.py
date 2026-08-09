#File handling
pc=input('Enter code:')
pn=input('Enter Name:')
pr=int(input('Enter Price:'))
qty=int(input('Enter Qty:'))
tot=pr*qty
f1=open('product.txt', 'a')#w=write, a=append, r=read
f1.write('\nCode:'+pc)
f1.write('\nName:'+pn)
f1.write('\nPrice:'+str(pr))
f1.write('\nQty:'+str(qty))
f1.write('\nTotal:'+str(tot))
f1.close()
print('Data added to file sucessfully')
