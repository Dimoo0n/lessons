s = input("Введіть речення: ")

for i in s.split():
    if "o" in i:
        print(i, end = ' ')
