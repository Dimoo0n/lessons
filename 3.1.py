st = ""
while len(st) < 6:
    st = input("Введіть слово, довжина якого перевищує 6 символів включно: ")

print("Result:", st[-6:-2])#вивід