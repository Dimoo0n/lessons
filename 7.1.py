slovnik = {1:[54, -3], 3:[42, -1], 2:[33, -4], 4:[52, 4], 5:[64, 7], 6:[46, 5]}#переше значення списку це к-сть опадів, друге температура


def vivod(slovnik):
    for key, value in slovnik.items():
        print(f"Число місяця - {key}, кількість опадів {value[0]}, температура {value[1]}")


def del_value_from_dict(slovnik): 
    del_data = int(input("Введіть дату яку потрібно видалити: "))
    if del_data not in slovnik.keys():
        print("Такої дати не має в словнику")
    else:
        del slovnik[del_data]
        print(f"Видалено дату {del_data} з словника")
    

def add_value_to_dict(slovnik):
    new_date = int(input("Введіть дату, яку потрібно додати: "))
    new_amount_of_precipitation = int(input("Введіть кількість опадів яка випала у цей день: "))
    new_temp = int(input("Введіть температуру в цей день: "))

    slovnik[new_date] = [new_amount_of_precipitation, new_temp]


def sorted_keys(slovnik):
    keys = sorted(slovnik)
    for i in keys:
        print(f"{i} число, опади = {slovnik[i][0]}, температура: {slovnik[i][1]}")
    

def snow_or_rain(slovnik):
    snow = rain = 0
    print(slovnik)
    for value in slovnik.values():
        if value[1] > 0:
            rain += value[0]
        else:
            snow += value[0]
    print(rain)
    print(snow)


while True:
    print("1. Виведення на екран всіх значень словника")
    print("2. Додавання нового запису до  словника")
    print("3. Видалення запису зі словника")
    print("4. Перегляд вмісту словника за відсортованими ключами")
    print("5. Кількість опадів, яка випала у вигляді снігу і яка у вигляді дощу")
    print("6. Вихід з програми")
    
    n = int(input("Введіть опцію: "))

    if n == 1:
        vivod(slovnik)
    elif n == 2:
        add_value_to_dict(slovnik)
    elif n == 3:
        del_value_from_dict(slovnik)
    elif n == 4:
        sorted_keys(slovnik)
    elif n == 5:
        snow_or_rain(slovnik)
    elif n == 6:
        print("Вихід з програми")
        break
    else:
        print("Невірно вказана операція")

