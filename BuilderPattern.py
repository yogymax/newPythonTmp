from abc import ABC
import copy


class Emp(ABC):

    def __init__(self,id,name,age):
        self.empId = id
        self.empName = name
        self.empAge = age


class PEmp(Emp):
    def __init__(self,id,nm,age):
        super().__init__(id,nm,age)

    def __str__(self):
        return 'PEmp Id : {}, Name : {}, Age : {}'.format(self.empId,self.empName,self.empAge)

class CEmp(Emp):
    def __init__(self,id,nm,age):
        super().__init__(id,nm,age)

    def __str__(self):
        return 'CEmp Id : {}, Name : {}, Age : {}'.format(self.empId,self.empName,self.empAge)


class EmpFactory :

    @classmethod
    def getEmpInstance(cls,obj):
            return copy.deepcopy(obj)


p1 = PEmp(10,"A",28)
p2 = EmpFactory.getEmpInstance(p1)

print(p1)
print(p2)

p3 = CEmp(11,"B",29)
p4 = EmpFactory.getEmpInstance(p1)

print(p3)
print(p4)



p1.empAge = 100
p3.empAge = 300
p4.empAge = 400

print(p1) # 100
print(p2)
print(p3)
print(p4) #300



