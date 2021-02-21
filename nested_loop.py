# for i in range(2):
#     print("i : {}".format(i))
#     for j in range(4):
#         print("j : {}".format(j))
#     print('----')

for baris in range(2):
    for kolom in range(3):
        print("{}.{}".format(baris+1,kolom+1), end=" ")
    print()
