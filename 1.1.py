a = int(input("Введіть додатнє значення a: "))
if a < 0:
    print("Введене значення a менше нуля")
b = int(input("Введіть додатнє значення b: "))
if b < 0:
    print("Введене значення b менше нуля")

if b > 0 and a > 0:
    if a > b:
        x = 5 * a + b
    elif a < b: 
        x = (a - b) / b
    else: # if a == b
        x = -125 
    print("Результат", x)
else: 
    print("Значення a i b повинно бути більше нуля")