mylist=['P001', 'Laptop', 45000, 2]

tot=mylist[2]*mylist[3]
gst=tot*(10/100)
gtot=tot+gst

for x in mylist:
    print(x)

print('Total:', tot, '\nGST:', gst)
print('Grand Total:', gtot)