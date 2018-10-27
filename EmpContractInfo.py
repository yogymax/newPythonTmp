'''
Class
Object
Abstraction --
        Abstraction is nothing showing only and only essentail details to the end user
        whereas hiding implementation part--
        Always fouces on What -- Functionality - rather than Interanals -- How
        ABC -- Abstract classes
        Object cannot be created
        Abstract -- contract -- Implementation

Encapsulation
        -- Wrapping of data and methods/code together into a single unit
            class -- object -- in which we wrap varaibles + methods

Polymorphism
        One thing can be done by multiple ways


Inheritance
'''

from abc import ABC,abstractmethod

class EmpService(ABC):

    @abstractmethod
    def addEmployee(self,emp):
        pass

    @abstractmethod
    def deleteEmployee(self,eid):
        pass

    @abstractmethod
    def getEmployee(self,eid):
        pass

    @abstractmethod
    def getAllEmployees(self):
        pass

    @abstractmethod
    def updateEmployee(self,emp):
        pass


    def empFacilities(self):
        return ['Tranpotation', 'Food Service', 'Vending Machine']


