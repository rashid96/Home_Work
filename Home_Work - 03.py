print("Задача №1")

def my_round (x,y):
    n = round(x, y)
    return n 

x = float(input("Введите десятичное число:"))
y = int(input("Введите количество знаков:"))

res_01 = my_round(x, y)

print(res_01)


print("Задача №2")

def lucky_tecket(r,l):
    n = (r == l)
    return n

s = input("Введите шестизначный номер лотерейного билета:")
r = int (s[0]) + int (s[1])
    
l = int (s[-1]) + int (s[-2])

res = lucky_tecket(r,l)

if res == True:
    print("Ваш билетик счастливый!")
elif res == False:
    print ("К сожалению вы ничего не выиграли.")

input ("Нажмите 'Enter' для выхода")








