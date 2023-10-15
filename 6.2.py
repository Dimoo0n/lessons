def func():
    print("Введіть список:")
    lst = list(map(int, input().split()))
    res_lst = []
    for i in lst:
        if i not in res_lst:
            res_lst.append(i)
    return res_lst

print("Список без повторень", func())