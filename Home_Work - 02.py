#Задача №1

print("Доброго времени суток! \n"
      "Задача №1")

fr_01 = input("Введите первый фрукт:")
fr_02 = input("Введите второй фрукт:")
fr_03 = input("Введите третий фрукт:")
fr_04 = input("Введите четвертый фрукт:")

fruits = [fr_01, fr_02, fr_03, fr_04]
for fr in fruits:
    print('{:>20}'.format(fr))

input("Для перехода к следующей задаче нажмите 'Enter' ")

#Задача №2
print("Задача №2")

num_01 = input("Введите 1-е число:")
num_02 = input("Введите 2-е число:")
numbers = num_01 + num_02
print(set(numbers))

input("Для перехода к следующей задаче нажмите 'Enter' ")

#Задача №3

print("Задача №3")
int_01 = int(input("Первое число:"))
int_02 = int(input("Второе число:"))
int_03 = int(input("Третие число:"))
int_04 = int(input("Четвертое число:"))
b = [int_01, int_02, int_03, int_04]
for i in b:
    if i % 2 == 0:
        i /= 4
        print(i)
            
    elif i % 2 != 0:
        i *= 2
        print(i)
    
print("{:_^40}".format("Спасибо за внимание"))

    
