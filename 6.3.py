import random
def func():
    n = int(input("Введіть кількість елементів множини: "))
    s = set()    
    for i in range(n):
        s.add(pow(random.randint(1, 1000), 2))
    s = sorted(s)
    print("Сортований список квадратів цілих чисел", s)
    print("Множина квадратів цілих чисел", set(s))#неможливо вивести сортовану множину
func()