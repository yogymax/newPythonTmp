
class A :

    def m1(self):
        print('inside A\'s m1 ')


class B(A):
    pass

class C(A):

    def m1(self):
        print('inside C\'s m1 ')

class D(A):
    pass
class E(B):
    def m1(self):
        print('inside E\'s m1 ')


class F(C ,D):
    pass

class G(E ,F ,D):
    pass

print(G.__mro__)

g = G()
g.m1()