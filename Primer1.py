#Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
import sys

def dataInput(st):
    try:
      n = int(input(st)) # Число N
      if n==0:
        print("Вы ввели 0")
        sys.exit()  
    except ValueError:
        print("Вы ввели не число")
        sys.exit() 
    return n  

def dataList(st,x):
    a = []
    try:
        for i in range(x):
            a.append(int(input(f"{st} {i+1} - ")))
    except ValueError:
        print("Вы ввели не число")
        sys.exit()
    return a

name = "Введите число №" 
nSpisok=dataInput("Введите количество чисел - ")
spisokFill=dataList(name,nSpisok)
sum=0
for i in range(nSpisok):
    if i%2 !=0:
        sum=sum+spisokFill[i]
print (f"Сумма элементов, стоящих на нечетной позиции - {sum}")