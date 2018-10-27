from DatabaseUtil import DatabaseUtil
from Employee import Employee





class EmployeeCRUD:

    connection = DatabaseUtil.getConnetion()

    def insertEmp(self,emp):

        query = 'insert into EmployeeInfo values('
        insertQuery = query + str(emp.empId) + ',\'' + emp.empName + '\',' + str(
            emp.empAge) + ',\'' + emp.empAddress + '\',' + str(emp.empSalary) + ')'

        EmployeeCRUD.connection.cursor().execute(insertQuery)
        EmployeeCRUD.connection.commit()
        EmployeeCRUD.connection.close()
       # EmployeeCRUD.connection.commit()
        print('Record Saved...!')

    def deleteEmp(self,id):
        deleteQuery = 'delete from EmployeeInfo where empid =' + str(id)
        EmployeeCRUD.connection.execute(deleteQuery)
        EmployeeCRUD.connection.commit()
        print('Record Delete...!')

    def update(self,emp):
        query = 'update EmployeeInfo set '
        updateQuery = query + 'empName = \'' + emp.empName + '\', empAge =' + str(
            emp.empAge) + ',empAddress = \'' + emp.empAddress + '\', empSalary =' + str(emp.empSalary)
        whereCondition = ' where empId = ' + str(emp.empId)
        finalUpdateQuery = updateQuery+whereCondition
        EmployeeCRUD.connection.execute(finalUpdateQuery)
        EmployeeCRUD.connection.commit()
        print('Record Updated...!')

    def getEmp(self,id):
        selectQuery = 'select * from employeeinfo where empId = '+str(id)
        cursor = EmployeeCRUD.connection.execute(selectQuery)
        return cursor.fetchone()

    def getAllEmps(self):
        selectQuery = 'select * from employeeinfo'
        cursor = EmployeeCRUD.connection.execute(selectQuery)
        return cursor.fetchall()



connection = DatabaseUtil.getConnetion(True)
#DatabaseUtil.createEmpLoyeeTable()
e1 = Employee(2,'AAA',23,12311,'Pune')
EmployeeCRUD().insertEmp(e1)

