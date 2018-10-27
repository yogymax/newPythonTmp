
# function -- inner function







def make_pretty(func):
    def inner(a,c,d):
        if type(a) == int and type(c) == int and type(d)== int :
            print("Inside ", func.__name__)
            func()
            print('execution completed of ' , func.__name__)
        else:
            print('Business cannot be executed...invalid input...!')

    return inner

@make_pretty
def m4(a,b,z):
    print('Business m4')
    return a + b + z

@make_pretty
def m1():
    print('Business m1')

@make_pretty
def m2():
    print('Business of m2')

@make_pretty
def m3():
    print('Business m3')

if __name__ == '__main__':
    m1()
    m2()
    m3()
    m4()