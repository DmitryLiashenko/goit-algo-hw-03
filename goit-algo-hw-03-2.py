                            #  Функция для генерирования случайных чисел для лотереи
import random
def get_numbers_ticket(min, max, quantity):                       # СОЗДАЕМ ФУНКЦИЮ
    if min >= 1 and max <=1000 and quantity <= max:               # ПРОВЕРЯЕМ ПАРАМЕТРЫ 
        list_with_lotery_digits = []                              # СОЗДАЕМ ПУСТОЙ СПИСОК
        while quantity >= 1:                                      # СОЗДАЕМ ЦИКЛ                                          
            random_digit = random.randint(min, max) 
            for i in list_with_lotery_digits: 
                if random_digit != i:                             #
                    list_with_lotery_digits.append(random_digit)  #
                quantity = quantity - 1            
    else:
        print("Числа выходят из заданного диапазон\nМинимальное значение 1, максимальное 1000\nКолличество желаемых чисел не больше 1000 ")   #
    return sorted(list_with_lotery_digits)                       #
                   
print(get_numbers_ticket(1, 100, 5))

