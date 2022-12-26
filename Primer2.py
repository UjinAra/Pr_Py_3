# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний 
# и т.д.
import sys
import math

def dataInput(st):
    try:
      n = int(input(st)) # Число N
      if n==0 or n==1:
        print("Вы ввели 0 или 1")
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

nM=[]
j=0
for i in range(math.ceil(nSpisok/2)):
    j=j-1
    nM.append(int(spisokFill[i]*spisokFill[j]))
    
print (f"Новый список - {nM}")