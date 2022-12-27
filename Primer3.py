# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной 
# части элементов.
import sys
import math

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
            a.append(float(input(f"{st} {i+1} - ")))
    except ValueError:
        print("Вы ввели не число")
        sys.exit()
    return a

name = "Введите дробное число №" 
nSpisok=dataInput("Введите количество чисел - ")
spisokFill=dataList(name,nSpisok)

for i in range(len(spisokFill)):
    spisokFill[i]=float((spisokFill[i]- math.floor(spisokFill[i])))

print (f"Разница между максимальным и минимальным значением дробной \
части элементов: {format(max(spisokFill) - min(spisokFill),'.2f')}")