a = input("Перше слово: ")
b = input("Друге слово: ")

for i in a:
    if b.count(i) == 1:
        print(i, end = " ")#перевірка      
