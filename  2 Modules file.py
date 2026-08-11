import mod_emp_det as mdet
ecode=input("Enter ecode:")
ename=input("Enter ename:")

import mod_emp_sal as msal
ba=int(input("Enter Basic salary:"))
bn=int(input("Enter Bonus:"))
pf=ba*(12/100)

print(mdet.add_det(ecode,ename))
print("Net salary",msal.show_sal(ba,bn,pf))
