# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.ДОП
import sys

def fibanachi(fib1,fib2,nSpisok):
    n=[]
    if fib2==1:
        for i in range(nSpisok-2):
            fibsum=fib1+fib2
            n.append(fibsum)
            fib1=fib2
            fib2=fibsum
    elif fib2==-1:
        for i in range(nSpisok-2):
            fibsum=fib1-fib2
            n.append(fibsum)
            fib1=fib2
            fib2=fibsum
    return n 
    
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
cent = [-1,1,0,1,1]

fib1=fib2=1
a=fibanachi(fib1,fib2,nSpisok)

fib1=1
fib2=-1
b=fibanachi(fib1,fib2,nSpisok)
b.reverse()

print(b+cent+a)