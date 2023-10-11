n = int(input("n: "))
a = [int(input()) for i in range(n)]

print("Додатні елементів масиву =", end = " ")
for i in a:
    if i > 0:
        print(i, end = " ")        
