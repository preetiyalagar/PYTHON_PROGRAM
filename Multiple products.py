#inventory details with multiple products
gtot=0
for x in range(1,4,1):
    pc=input('Enter pcode:')
    pn=input('Enter pname:')
    pr=int(input('Enter price:'))
    qty=int(input('Enter qty:'))
    tot=pr*qty
    gst=tot*0.1
    gtot=tot+gst+gtot
    print('Code:',pc,'Name:','Price:',pr,'Qty:',qty,'Total:',tot)
print('Bill amount with GST for 3 items:', gtot)