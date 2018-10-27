class A:
    pass

class B(A):
    pass


a = A()
b = B()


print(type(a))
print(type(b))

print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, A))
print(isinstance(B, B))
