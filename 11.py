import csv

try:
    file_r = open("Lab.csv", "r")
    reader = csv.DictReader(file_r, delimiter = ",")
    print("Country Name: 2019 [YR2019]")
    for row in reader:

        print(row['Country Name'], ': ', row["2019 [YR2019]"])

    file_r.close

except FileNotFoundError:
    print("Файл Lab.csv не вдалося відкрити")

except:
    print("Виникла якась помилка")


try:
    file_r = open("Lab.csv", "r")
    reader = csv.DictReader(file_r, delimiter = ",")
    m = {int(i["2019 [YR2019]"]):i['Country Name'] for i in reader}
    max_m = max(m)
    min_m = min(m)
    print("Найвище значення показника -", m[max_m], max_m)
    print("Найнижче значення показника -", m[min_m], min_m)
    file_r.close
    with open("New_Lab.csv","w") as new_file:
        write_row = csv.writer(new_file, delimiter = ",", lineterminator="\n")
        write_row.writerow(("The highest value", m[max_m], max_m))
        write_row.writerow(("The lowest value", m[min_m], min_m))
        print("Дані успішно додані до файла")

except FileNotFoundError:
    print("Файл Lab.csv не вдалося відкрити")

except:
    print("Виникла якась помилка")