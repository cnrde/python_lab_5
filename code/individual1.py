import sys
if __name__ == "__main__":
    m = int(input("Введите номер месяца: "))
    if m == 1:
        print("Первое полугодие, 31 день")
    elif m == 2:
        print("Первое полугодие, 28 дней")
    elif m == 3:
        print("Первое полугодие, 31 день")
    elif m == 4:
        print("Первое полугодие, 30 дней")
    elif m == 5:
        print("Первое полугодие, 31 день")
    elif m == 6:
        print("Второе полугодие, 30 дней")
    elif m == 7:
        print("Второе полугодие, 31 день")
    elif m == 8:
        print("Второе полугодие, 31 день")
    elif m == 9:
        print("Второе полугодие, 30 дней")
    elif m == 10:
        print("Второе полугодие, 31 дней")
    elif m == 11:
        print("Второе полугодие, 30 день")
    elif m == 12:
        print("Второе полугодие, 31 дней")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)