# for i in range(5):
#     if i == 3:
#         break
#     print(i)

text = input("input text: ")

while True:
    if text == "stop" or text == "end":
        print("program has stopped.")
        break
    print("text : {}".format(text))
    text = input("input text lain : ")

