
#!MRO --> Method Resolution Order

class A1:
    num = 10

class B1(A1):
    pass

class C1(A1):
    num = 1

class D1(B1,C1):
    pass

print(D1.mro())
print(D1.num)


class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.__mro__)