import json

d = {#ключ - день місяця, переше значення списку це к-сть опадів, друге температура
    1: [2.5, 3],
    2: [0.8, 1],
    3: [5.0, -2],
    4: [0.0, 5],
    5: [1.2, 2],
    6: [3.5, 0],
    7: [0.0, 6],
    8: [1.8, -4],
    9: [4.2, -2],
    10: [0.5, -1],
    11: [2.0, -4],
    12: [0.0, 7],
    13: [3.7, 1],
    14: [0.0, 8],
    15: [1.0, 4],
    16: [2.3, -3],
    17: [0.0, 6],
    18: [1.5, 2],
    19: [4.0, 0],
    20: [0.0, 5],
    21: [2.8, 1],
    22: [0.3, 3],
    23: [3.0, -2],
    24: [0.3, -6],
    25: [1.2, 2],
    26: [2.0, -1],
    27: [0.2, 6],
    28: [1.7, 4],
    29: [3.5, 0],
    30: [0.4, 5],
    31: [2.0, 1],
}

d_add = json.dumps(d)
with open("Lab.json", "wt") as file:
    file.write(d_add)

while True:
    print("1.Вивести вміст файлу")
    print("2.Додавання або заміна значень за датою")
    print("3.Видалення значень за датою")
    print("4.Пошук значень за датою")
    print("5.Визначення кількості опадів які випали у вигляді снігу і дощу")
    print("Для виходу з програми введіть будь-що")
    option = int(input("Введіть число для вибору опції: "))
    if option == 1:
        print("\nВиведення вмісту файлу")
        with open("Lab.json", "rt") as file_r:
            vmist = json.load(file_r)
            print(*(f"{i} : {j}" for i, j in vmist.items()), sep = "\n")
    
    elif option == 2:
        with open("Lab.json", "rt") as file_r:
            date = input("Введіть дату: ")
            change_d = json.load(file_r)
            def add_or_change_date(slovnik):#функція для заміни або ж додавання значень числа в словнику
                opadi = float(input("Введіть кількість опадів: "))
                temp = int(input("Введіть тепературу в цей день: "))
                slovnik[date] = [opadi, temp]
                return json.dumps(slovnik)
            if date in change_d:
                print(f"{date} число вже є в словнику")
            else:
                print(f"Числа {date} немає в словнику")

        with open("Lab.json", "wt") as file_a:
            file_a.write(add_or_change_date(change_d))#використовуєм функцію 
    
    elif option == 3:
        flag = False
        with open("Lab.json", "rt") as file_r:
            date = input("Введіть дату: ")
            change_d = json.load(file_r)
            if date in change_d:
                print(f"{date} число є в словнику")
                change_d.pop(date)
                vixid = json.dumps(change_d)
                flag = True
            else:
                print(f"Числа {date} немає в словнику")

        if flag == True:
            with open("Lab.json", "wt") as file_a:
                file_a.write(vixid)
                print(f"Число {date} було видалено зі словника")

    elif option == 4:
        with open("Lab.json", "rt") as file_r:
            date = input("Введіть дату: ")
            change_d = json.load(file_r)
            if date in change_d:
                print(f"{date} числа випало {change_d[date][0]} опадів і в цей день температура була {change_d[date][1]} градуси")
            else:
                print(f"Числа {date} немає в словнику")

    elif option == 5:
        s1 = s2 = 0
        with open("Lab.json", "rt") as file_r:
            change_d = json.load(file_r)
            for i in change_d.values():
                if i[1] < 1:
                    s1 += i[0]
                else:
                    s2 += i[0]
            print("Кількость опадів які випали у вигляді снігу =", s1)
            print("Кількость опадів які випали у вигляді дощу =", s2)

        with open("New_Lab.json", "wt", encoding="utf-8") as new_file:
            new_file.write("Кількість опадів які випали у вигляді снігу = " + str(s1))
            new_file.write("Кількість опадів які випали у вигляді дощу = " + str(s2))
            print("Дані про кількість опадів які випали у вигляді дощу та снігу успішно додані до новго файлу")

    else:
        print("Вибрана опція виходу")
        quit(0)
       
