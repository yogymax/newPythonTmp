from __future__ import print_function


class Product :

    def __init__(self,id,name,price):
        self.__set_id(id)
        self.__set_name(name)
        self.__set_price(price)


    def __set_id(self,val):
        if val <= 0:
            self.__id = 1000
        else:
            self.__id= val

    def __set_name(self,name):
        self.__name=name.upper()

    def __set_price(self,p):
        if p <= 0:
            self.__price = 100
        elif p > 1000:
            self.__price = 900
        else:
            self.__price = p

    def __get_id(self):
        if self.__id > 1000:
            return 100
        else:
            return self.__id

    def __get_name(self):
        return self.__name.title()

    def __get_price(self):
        return self.__price

    def __str__(self):
        print(self.__get_price())
        print(self.__get_id())
        print(self.__get_name())
        return ''

    id = property(__get_id,__set_id)
    price = property(__get_price, __set_price)
    name = property(__get_name, __set_name)



p1 = Product(10,'moBILE',35023)
print(p1)




'''

class Emp :

    def __init__(self,val):
        self.__set_id(val)

    def __get_id(self):
        return self.__id

    def __set_id(self,value):
        if value <= 0:
            self.__id = 10
        else :
            self.__id = value

    def __str__(self):
        return '{}'.format(self.__id)

    id = property(__get_id,__set_id)


e1 = Emp(-100)
print(e1)
e1.id=-1200
print(e1)
'''
'''

class Emp:
   
    def __init__(self,id,nm,age):
        self.empName = nm
        self.empAge = age
        if id <= 0:
            self.__empId = 10
        else:
            self.__empId = id

    def __str__(self):
        return 'EmpId : {} , Emp' \
               'Name : {} , EmpAge : {}'.format(self.__empId,self.empName,self.empAge)


e1 = Emp(-17,'Amit',30)
print(e1)
e1.empId= -203

print(e1.__dict__)
print(e1.__doc__)

print(e1.empId)


print(Emp.__mro__)
'''

class A:
    pass #m1

class B(A):
    pass

class C(B):
    pass #m1

class D(B):
    pass

class E(C,D):
    pass

#print('E mro ' , E.__mro__)


class F(C,D):
    pass

class G(E,F,D):
    pass

#print(G.__mro__)

'''
num = 100
def outer():
    global num
    num=250
    def inner():
        global num
        num=300
        print('Inner Function',num) #300

    print('Outer Function', num)  # 250
    inner()
    print('Outer Function', num)  # 300



outer()
print('Globle' , num)#100
'''


'''
num = 100
def outer():
    global num
    num=250
    def inner():
        num=300
        print('Inner Function',num) #300
    inner()
    print('Outer Function',num) # 250
    num=350

outer()
print('Globle' , num)#350

'''


'''
num = 100
def outer():
    global num
    num=250
    def inner():
        num=300
        print('Inner Function',num) #300
    inner()
    print('Outer Function',num) # 250

outer()
print('Globle' , num)#250

'''

''''
num = 100
def outer():
    num=250
    def inner():
        num=300
        print('Inner Function',num) #300
    inner()
    print('Outer Function',num) # 250

outer()
print('Globle' , num)#100
'''




#print(num1 == num2)
#print(num3 == num4)



print('\n\n\n\n')

class Emp:

    def __init__(self,id,name):
        self.empId = id
        self.empName = name

    def __eq__(self, other):
        return self.empName == other.empName


e1 = Emp(1,'A1')
e2 = Emp(1,'A2')
e3 = Emp(2,'A2')
e4 = e1
e5 = e4

'''
print(id(e1) == id(e2)) #False
print(id(e2) == id(e3)) #False
print(id(e3) == id(e4)) #False
print(id(e4) == id(e5)) #True
print(id(e4) == id(e1)) #True

print(e1 == e2) #False
print(e2 == e3) #True
print(e3 == e4) #False
print(e4 == e5) #True
print(e4 == e1) #True

'''

'''
print(e1 == e2)
print(id(e1) , ' : E1 Id')
print(id(e2) ,  ': E2 Id')
print(e1.__hash__() , 'E1 hash')
print(e2.__hash__() , 'E2 Hash')
'''
'''
print(id(e1) == id(e2))
print(e1 == e2)
'''
