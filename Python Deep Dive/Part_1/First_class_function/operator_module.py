import operator

my_list = [1,2,3,4]

print(operator.getitem(my_list, 1))

f = operator.itemgetter(2)

print(f(my_list))

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    
    def test(self):
        print('test method running...')
        
obj = MyClass()

print(obj.a)

print(obj.test())

prop_a = operator.attrgetter('a')
print(prop_a(obj))

my_var = 'b'
print(operator.attrgetter(my_var)(obj))

f = lambda x: x.a
x = [1,2,3,4]

print(f(obj))


l = [5-10j,3+3j,2-100j]

print(sorted(l,key=operator.attrgetter('real')))

class MyClass1:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def test(self,c):
        print(self.a,self.b,c)
        print('test method running...')
        
obj = MyClass1()

print(obj.test(100))

print(operator.methodcaller('test',100,200)(obj))

