#file handling with csv(comma seperate values)
ec=input('Enter emp code:')
en=input('Enter emp name:')
bs=int(input('Enter salary:'))
dp=input('Enter dept name:')
bn=bs+0.1
pf=bs+0.12
net=bs+bn-pf

f1=open('emp.csv','w')
f1.write('Code'+","+'Name'+","+'Salary'+","+'Department'+"\n")

f1.write(ec+","+en+","+str(bs)+","+dp+","+str(bn)+","+str(pf)+","+str(net)+"\n")
f1.close()
print('Data stored into file')