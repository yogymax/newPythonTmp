

'''
DEFAULT -- interpretter -- when there is no other constructor in a class
No-arg -- user has defined a constructor without parameter
paramaterized --user has defined a constructor with parameter

max -- there will one contstructor in class -- last one

'''

class Person :


    def method1(self,**a):
        sum = 0
        if a.__len__()>10 :
            for item in a:
               sum = sum + item
        else :
            for item in a:
               sum = sum * item



p = Person()
d = p.method1(10,40)
print(d)