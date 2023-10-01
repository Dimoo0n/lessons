n = int(input("n: "))
a = [[j for i in range(n)] for j in range(n, 0, -1)]

for i in a:
    print(*i)