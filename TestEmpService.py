from EmployeeInfo import Emp
from EmpServiceImpl import Infosys,TCS

'''
self.empId = eid
        self.empName = ename
        self.empAge = eage
        self.empSalary = esal
        self.empAddress = eaddress


'''

if __name__ == '__main__':

    infosysService = TCS()
    #tcsService = TCS()
    e1 = Emp(1, 'Yogesh1', 29, 62312)
    e2 = Emp(1, 'Yogesh2', 41, 52312)
    e3 = Emp(2, 'Yogesh3', 39, 4312)
    e4 = Emp(2, 'Yogesh4', 59, 23312)
    e5 = Emp(3, 'Yogesh5', 29, 44312)
    e6 = Emp(5, 'Yogesh6', 49, 152312)
    e7=e4

    infosysService.addEmployee(e1)
    infosysService.addEmployee(e2)
    infosysService.addEmployee(e3)
    infosysService.addEmployee(e4)
    infosysService.addEmployee(e5)
    infosysService.addEmployee(e6)
    infosysService.addEmployee(e7)


    print(infosysService.getAllEmployees()) # 4 -- e1 e3 e5 e6
    print(infosysService.getEmployee(2)) # Yogesh3
    print(infosysService.deleteEmployee(10)) #False
    print(infosysService.deleteEmployee(2))  # True
    print(infosysService.getEmployee(2))  # RECORD NOT FOUND

    e4.empAddress = 'bglore'
    e4.empSalary=500000
    e4.empId=1
    print(infosysService.updateEmployee(e4)) # not exist
    print(infosysService.getAllEmployees())


'''
    while(True):

        emp = Emp(int(input('Enter EmpId')), input('Enter EmpName'), int(input('Enter EmpAge')),
            float(input('Enter EmpSalary')), input('Enter EmpAddress'))

        for count in range(1,4):
            companyName = input('Your Company Name : Infosys or TCS')
            if companyName.lower() == 'infosys' :
                infosysService.addEmployee(emp)
                break
            elif companyName.lower() == 'tcs' :
                tcsService.addEmployee(emp)
                break
            else
                print('Invalid Attempts (Max-3 Allowed)...re enter Company Name , AttemptNo ',count)

        if 0 == int(input('Do you want to Exit - yes : 0')):
            break


    print('\n\n Here is list of Infosys Emp --' ,Infosys.infosysEmployess)
    print('\n\nHere is list of TCS Emp --', TCS.tcsEmployess)
    
   '''




