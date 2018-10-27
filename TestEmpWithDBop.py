from Employee import Employee
from EmployeeCrudOpe import EmployeeCRUD
from DatabaseUtil import DatabaseUtil






if __name__ == '__main__':


    while True:
          print('################################')
          print('''List Of Operation
                1. Insert Employee
                2. Delete Employee
                3. Update Employee
                4. Get Employee
                5. Get All Employees
          ''')
          choiceNo = int(input('Enter you Choice'))







def insertOp():
    print('Enter Employee details')
    while True:
        id = input('Enter EmpId : ')
        name = input('Enter EmpName : ')
        age = input('Enter EmpAge : ')
        salary = input('Enter EmpSalary : ')
        addr = input('Enter EmpAddr : ')
        e1 = Employee(id,name,age,salary,addr)
        EmployeeCRUD().insertEmp(e1)
        print('Emp with {} saved into table'.format(e1.empId))

        flag = int(input('Do you want to Contiue Yes = 1'))
        if flag != 1:
            break


def updateEmpop():
    uid = int(input('Enter ID first'))
    dbemp = EmployeeCRUD().getEmp(uid)
    if dbemp != None:
        name = input('Enter latest EmpName : ')
        age = input('Enter latest  EmpAge : ')
        salary = input('Enter latest  EmpSalary : ')
        addr = input('Enter latest  EmpAddr : ')
        EmployeeCRUD().update(Employee(dbemp[0],name,age,salary,addr))
        print('Emp with {} saved into table'.format(dbemp.empId))
    else:
        print('Empnot not exist..so cannot update')


def deleteOp():
    uid = int(input('Enter Id to delete'))
    dbEmp = EmployeeCRUD().getEmp(uid)
    if dbEmp!=None:
        EmployeeCRUD().deleteEmp(dbEmp[0])
    else:
        print('Not Exist....')


def listOfOperations(choice):
    dict = {
        1 : insertOp(),
        2: deleteOp(),
        3: updateEmpop(),
        4: EmployeeCRUD.getEmp(),
        5: EmployeeCRUD.getAllEmps(),
    }