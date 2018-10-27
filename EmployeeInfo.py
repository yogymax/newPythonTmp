

class Emp:

    def __init__(self,eid,ename,eage,esal,eaddress='Pune'):
        self.empId = eid
        self.empName = ename
        self.empAge = eage
        self.empSalary = esal
        self.empAddress = eaddress

    def __str__(self):
        return '\n EmpId : {}, EmpName : {}, EmpAge : {}, EmpSalary : {}, EmpAddress : {}'.format(self.empId,self.empName,self.empAge,self.empSalary,self.empAddress)


    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.empId == other.empId

    def __hash__(self):
        return self.empId


