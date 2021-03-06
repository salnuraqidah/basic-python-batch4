r = open("resource/hello.txt","r")

# temp = r.read()
# print(temp)

temp2 = r.readlines()
a = []
for li in temp2:
    a.append(li.strip())

print(a[1])
r.close()