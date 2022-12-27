# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
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
nSpisok=dataInput("Введите число - ")
result = ''
 
while nSpisok > 0:
    result = str(nSpisok % 2) + result
    nSpisok = nSpisok // 2
 
print(result)