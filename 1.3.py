N = int(input("Введіть ціле число від 1 до 9: "))

if 0 < N < 10:
    print("Результат: ")
    c = 1
    for i in range(N, 0, -1):
        for j in range(c, i + c):
            print(j, end = " ")
        c += 1
        print()
else:
    print("Помилка, N повинно бути в діапазоні від 1 до 9")