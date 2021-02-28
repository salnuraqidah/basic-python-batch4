def my_function():
    print("Halo Semua")

# my_function()

# function with parameter
def halo(first_name,last_name):
    print("Halo "+first_name + " "+last_name)

# halo("Nana","Karima")
# halo("Raditya","Dika")
# halo("Salamah","Aqidah")

# function with default parameter
def hai(first_name,last_name=""):
    print("Halo "+first_name + " "+last_name)

# hai("Nana")

# function keyword parameter
def my_function2(child3, child2, child1):
    print("The youngest child is " + child3)

# my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# my_function2("Emil", "Tobias", "Linus")

# function return value

def tambah(x,y):
    tambah = x + y
    return tambah

jumlah = tambah(2,9)
# print(jumlah)

def total():
    return 20

totals = total()
# print(totals)

# f(x) = x + 5

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num


# print(absolute_value(2))

# print(absolute_value(-4))



