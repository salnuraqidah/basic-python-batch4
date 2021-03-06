my_set = {"apel", "manggis", "pisang", 'pisang'}
print(my_set)
a = set()
print(type(a))
y = []
for x in my_set:
    y.append(x)
print(y[0])
print("apel" in my_set)
print("melon" in my_set)

my_set.add("melon")
print(my_set)

my_set.remove("manggis")
print(my_set)

my_set2 = {1,2,3,4,5,1,4}
print(my_set2)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A & B)
print(A - B)


