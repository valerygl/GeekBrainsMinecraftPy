file = open("todoList.txt", "w")

while True:
    item = input("ввведите новое дело ")
    if item == "z":
        break
    file.write(item+"\n")

    # C:\Users\Mike\PycharmProjects\pythonProject1\todolist.py


file.close()
