def print_class(address):
    list_numbers = address.split('.')
    result = []
    for i in range (0, 4):
        result.append(int(list_numbers[i]))
    if (result[0] >= 0 and result[0] <= 127 and result[0] < 1000 and result[1] < 1000 and result[2] < 1000 and result[3] < 1000):
        print("Класс A : ", address)
    elif (result[0] >= 128 and result[0] <= 191 and result[1] >= 0 and result[1] <= 255 and result[0] < 1000 and result[1] < 1000
          and result[2] < 1000 and result[3] < 1000):
        print("Класс B : ", address)
    elif (result[0] >= 192 and result[0] <= 223 and result[1] >= 0 and result[1] <= 255 and result[2] >= 0 and result[2] <= 255
          and result[0] < 1000 and result[1] < 1000 and result[2] < 1000 and result[3] < 1000):
        print("Класс C : ", address)
    elif (result[0] >= 224 and result[0] <= 239 and result[0] < 1000 and result[1] < 1000 and result[2] < 1000 and result[3] < 1000):
        print("Класс D : ", address)
    elif (result[0] >= 240 and result[0] <= 255 and result[0] < 1000 and result[1] < 1000 and result[2] < 1000 and result[3] < 1000):
        print("Класс E : ", address)
    else :
        print("Вы ввели некорректный ip-адрес!")
# проверим работу функции
# уточню, что под ххх в ip-адрессе может быть число от 0 до 255, но здесь я взял ххх как просто трехзначное число без ограничений
# по количеству бит на символ
print("Введите ip-адрес: ")
address = input()
print_class(address)