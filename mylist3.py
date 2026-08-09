mylist=['E001', 'Preeti', 45000, 'HR']
bn=mylist[2]*0.1
pf=mylist[2]*(12/100)
net=mylist[2]+bn-pf

for x in mylist:
    print(x)
print(bn,'\n',pf,'\n',net)