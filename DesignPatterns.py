from abc import ABC,abstractmethod

class Computer(ABC):

    @abstractmethod
    def getHDD(self):
        pass

    @abstractmethod
    def getRAM(self):
        pass

    @abstractmethod
    def getCPU(self):
        pass

class PC(Computer):

    def __init__(self,h,r,c):
        self.hdd = h
        self.ram = r
        self.cpu = c

    def getHDD(self):
        return self.hdd

    def getRAM(self):
        return self.ram


    def getCPU(self):
        return self.cpu


class Server(Computer):
    def __init__(self,h,r,c):
        self.hdd = h
        self.ram = r
        self.cpu = c


    def getHDD(self):
        return self.hdd


    def getRAM(self):
        return self.ram


    def getCPU(self):
        return self.cpu


class AbstractFactory(ABC):

    @abstractmethod
    def createComputer(self):
        pass


class PCFactory(AbstractFactory):

    def createComputer(self,hd,rm,cp):
        return PC(hd,rm,cp)

class ServerFactory(AbstractFactory):
    def createComputer(self,hd,rm,cp):
        return Server(hd,rm,cp)

class ComputerFacotry:

    @classmethod
    def createComputer(cls,typ,hd,ra,cp):
        if typ == 'PCF':
            return PCFactory().createComputer(hd,ra,cp)
        elif typ == 'ServerF':
            return ServerFactory().createComputer(hd,ra,cp)

p1 = ComputerFacotry.createComputer('PCF',80,2,'quadcore')

print(type(p1))

p2 = ComputerFacotry.createComputer('ServerF',800,8,'quadcore')
print(type(p2))


print('********************8')





class Vehicle:

    @classmethod
    def getInstance(cls,ty,param1,param2):
        if ty == 'X1':
            return Audi(param1,param2)
        elif ty == 'X2':
            return BMW(param1,param2)
        else:
            print('no criteria found')
            return None


class Audi:

    def __init__(self,id,nm):
        self.carName = nm
        self.carId = id

    def __str__(self):
        return 'AudiId : {}, Name : {}'.format(self.carId,self.carName)


class BMW:

    def __init__(self,id,nm):
        self.Name = nm
        self.Id = id

    def __str__(self):
        return 'ID :{} , Name :{}'.format(self.Id,self.Name)


b = Vehicle.getInstance('B',1,'BWMSeris')
a = Vehicle.getInstance('A',1,'BWMSeris')

print(type(b))# bmw
print(type(a))# bmw

#singleton

#factory --


#import base64

#with open("C:\\Users\Yogesh\Desktop\\bird.jpg", "rb") as imageFile:
    #str = base64.b64encode(imageFile.read())
    #base64.decode(str,"C:\\Users\Yogesh\Desktop\\bird11.jpg")
    #print(str)



class Product:


    subProductRef = None
    def __init__(self,id,nm,price):
        if Product.subProductRef ==None:
            Product.subProductRef = Product.__SubProduct(id,nm,price)
        else:
            Product.subProductRef.productId = id
            Product.subProductRef.productName = nm
            Product.subProductRef.productPrice = price

    def setProductId(self,id):
        Product.subProductRef.productId=id

    def setProductName(self,nm):
        Product.subProductRef.productName=nm

    def setProductPrice(self,pri):
        Product.subProductRef.productPrice = pri


    def __str__(self):
        return 'Id :{}, Name : {}, Price : {}'.format(Product.subProductRef.productId,Product.subProductRef.productName,Product.subProductRef.productPrice)

    class __SubProduct:

        def __init__(self,id,nm,price):
            self.productId = id
            self.productName = nm
            self.productPrice = price


p1 = Product(1,"A",500)
p2 = Product(2,"B",600)

p1.setProductPrice(1000)



print(p1)
print(p2)