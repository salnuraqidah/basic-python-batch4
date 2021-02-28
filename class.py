class MyClass:
    x = 5

obj1 = MyClass()
obj2 = MyClass()

# print(obj1.x)
# print(obj2.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print('Hello my name is ' + self.name)


# nama = input('nama: ')
# umur = input('umur: ')

# p1 = Person(nama, umur)
p1 = Person('juju', 23)
# print(p1.name)
# print(p1.age)
p1.greeting()

p2 = Person("Gigi", 20)
# print(p2.name)
# print(p2.age)
p2.greeting()

