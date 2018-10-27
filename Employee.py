

class Employee:

    def __init__(self,id,nm,age,salary,address):
        self.empId = int(id)
        self.empName=nm
        self.empAge=int(age)
        self.empSalary=float(salary)
        self.empAddress=address

    def setEmpId(self,id):
        self.empId = id

    def setEmpName(self,nm):
        self.empName=nm

    def setEmpAge(self,ag):
        self.empAge=ag

    def setSalary(self,sal):
        self.empSalary=sal

    def setAddress(self,ad):
        self.empAddress=ad


    def __str__(self):
        return 'EmpId : {} , EmpName : {}, EmpAge :{}, EmpSalary : {}, EmpAddress : {}'.format(self.empId,self.empName,self.empAge,self.empSalary,self.empAddress)

    def __repr__(self):
        return str(self)

