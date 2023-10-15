def func():
    print("Введіть список: ")
    lst = list(map(int, input("").split()))
    lst.insert(0, int(input("Введіть елемент, який буде додано до початку списку: ")))
    lst.append(int(input("Введіть елемент, який буде додано до кінця списку: ")))
    print(lst)
func()