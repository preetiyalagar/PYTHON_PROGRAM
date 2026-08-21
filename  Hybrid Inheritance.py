#Hybrid Inheritance using Python
class Emp:
    cname="ABC"
class SystemAdmin(Emp):
    srole="System Admin"
class WebDev(Emp):
    wrole="UI Developer"
class DBA(WebDev, SystemAdmin, Emp):
    drole="Data Base Creating"
obj=DBA()
print("Company Name:"+obj.cname)
print("SysAdmin:"+obj.srole)
print("WebDev:"+obj.wrole)
print("DBA:"+obj.drole)
