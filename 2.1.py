import math
m = float(input("Значення повино бути за діапазоном від -3 до 3: "))#ввод значення
   
def z(m):
    
    return math.sqrt((m + 3)/(m - 3))#формула

if -4 < m and m < 4:
    print("Помилка, значення повино бути за діапазоном від -3 до 3: ")#перевіряємо чи введене м за цим діапазоном
else:
    print(z(m))#виклик функції

n = int(input("Введіть n: "))

def y(n):
    s = 1
    for i in range(1, n + 1):
        s = s * 2 * i
    return(s)#обчислення за формулой

print(y(n))#виклик функції