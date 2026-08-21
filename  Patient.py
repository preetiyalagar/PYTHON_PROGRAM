#patient information
class doctor:
    def inp_doc(self):
        self.dn=input('Doctor name:')
        self.sp=input('Specialization:')

    def show_doc(self):
        print("\tDoctor Name:", self.dn, "and specialization:", self.sp)

class patient:
    def inp_pat(self):
        self.pn=input('patient name:')
        self.ag=input('age:')
    def show_pat(self):
        print("\tpatient name:", self.pn, "and age:", self.ag)

class diagnose:
    def inp_dig(self):
        self.dis=input('disease:')
        self.dur=input('How long?:')
        self.pm=input('Prescribe medicine:')
    def show_dig(self):
        print("\tDisease:", self.dis, "for last", self.dur, "and Medicine prescribed is:", self.pm)

class report(doctor, patient, diagnose):
    def inp_rp(self):
        self.dt=input('Enter date:')
        self.ch=input('charges:')
    def show_rep(self):
        print("\tDate:", self.dt, "and Charges:", self.ch)

r=report()
r.inp_doc()
r.inp_pat()
r.inp_dig()
r.inp_rp()
print('\t============Report=============')
r.show_doc()
r.show_pat()
r.show_dig()
r.show_rep()
print('\t=============End=============')

