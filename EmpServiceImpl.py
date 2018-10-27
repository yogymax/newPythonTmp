from EmpContractInfo import EmpService

class Infosys(EmpService):

    infosysEmployess = set()

    def addEmployee(self,emp):
        Infosys.infosysEmployess.add(emp)
        return emp.empId


    def deleteEmployee(self,uid):
        for emp in Infosys.infosysEmployess:
            if emp.empId == uid:
                Infosys.infosysEmployess.remove(emp)
                return True

        return False


    def getEmployee(self,uid):
        for emp in Infosys.infosysEmployess:
            if emp.empId == uid:
                return emp

        return 'Record not found'.upper()


    def getAllEmployees(self):
        return Infosys.infosysEmployess


    def updateEmployee(self,uemp):
        for emp in Infosys.infosysEmployess :
            if emp.empId == uemp.empId :
                emp.empName = uemp.empName
                emp.empAge = uemp.empAge
                emp.empSalary = uemp.empSalary
                emp.empAddress = uemp.empAddress
                return emp
        return 'Specified Emp doesnt exit so cannot update'.upper()

    def empFacilities(self): #not mandatory to write -- override
        return ['Ac Bus Services', 'Free of Cost Food', 'Safety']



class TCS(EmpService):
    tcsEmployess = set()

    def addEmployee(self, emp):
        TCS.tcsEmployess.add(emp)
        return emp.empId

    def deleteEmployee(self, uid):
        for emp in TCS.tcsEmployess:
            if emp.empId == uid:
                TCS.tcsEmployess.remove(emp)
                return True

        return False

    def getEmployee(self, uid):
        for emp in TCS.tcsEmployess:
            if emp.empId == uid:
                return emp

        return 'Record not found'.upper()

    def getAllEmployees(self):
        return TCS.tcsEmployess

    def updateEmployee(self, uemp):
        for emp in TCS.tcsEmployess:
            if emp.empId == uemp.empId:
                emp.empName = uemp.empName
                emp.empAge = uemp.empAge
                emp.empSalary = uemp.empSalary
                emp.empAddress = uemp.empAddress
                return emp
        return 'Specified Emp doesnt exit so cannot update'.upper()
