n = int(input("n: "))
a = [int(input()) for i in range(n)]

sum = 0
for i in a:
    if i > 0:
        sum += i
print("Сума додатніх елементів масиву =", sum)