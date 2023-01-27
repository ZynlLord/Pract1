count = int(input("Введите количество чисел: "))
promnumber = 0

choose = int(input("Выберите действие:\n " +
 "1. Сложение\n" +
 "2. Вычитание \n" +
 "3. Умножение\n" +
 "4. Деление \n" +
 "5. Возведение в степень \n"))

if (choose >= 1 and choose <= 5):
    if (choose == 1): 
        for i in range(count):
            number = int(input("Число: "))
            promnumber += number
            i =+ 1
    elif (choose == 2):
        number = int(input("Число: "))
        promnumber = number
        for i in range(count-1):
            number = int(input("Число: "))
            promnumber -= number
            i =+ 1
    elif (choose == 3):
        promnumber = 1
        for i in range(count):
            number = int(input("Число: "))
            promnumber *= number
            i =+ 1
    elif (choose == 4):
        number = int(input("Число: "))
        promnumber = number
        for i in range(count-1):
            number = int(input("Число: "))
            if (number != 0):
                promnumber /= number
                i =+ 1
            else:
                print("На ноль делить нельзя!")
                continue
    elif (choose == 5 and count == 2):
        number = int(input("Число: "))
        degree = int(input("Введите степень: "))
        promnumber = pow(number, degree)   
else:
    print("Неверное число!")
print(f"Ответ: {promnumber}")



