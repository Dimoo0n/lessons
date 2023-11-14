def Open(file_name, mode):

    try:

        file = open(file_name, mode)

    except:

        print("File", file_name, "wasn't opened!")

        return None

    else:

        print("File", file_name, "was opened!")

        return file



file_name = "TF10_1.txt"
file2_name = "TF10_2.txt"

file1_w = Open(file_name, "w")

if file1_w != None:
    file1_w.write("Airplane-12 was landed at 15 o'clock in Paris")#створення текстового файлу TF10_1 із символьними рядками різної довжини
    file1_w.close()

file1_r = Open(file_name, "r")
file2_w = Open(file2_name, "w")

if file1_r != None or file2_w != None:
    count = 1
    for i in "".join(file1_r.read().split()):#тут я видалив пробіли
        if not i.isdigit(): 
            if count % 10 == 0:
                file2_w.write("\n")#вилучення всіч цифр і запис у файл TF10_2 по 10 символів у рядок
            file2_w.write(i)
            count += 1
    file2_w.close()
    file1_r.close()

file2_r = Open(file2_name, "r")

for i in file2_r.read().split():#читаємо вміст файлу 2 і друкуємо на єкрані
    print(i)
file2_r.close()