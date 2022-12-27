# Дана последовательность из N целых чисел и число K. Необходимо 
# сдвинуть всю последовательность (сдвиг - циклический) на |K| 
# элементов вправо, если K – положительное и влево, если отрицательное.
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
k=dataInput("Введите число К - ")
print(spisokFill)

if k<0:
    k = abs(k)
    for i in range(k):
        spisokFill.append(spisokFill.pop(0))
else:
    for i in range(k):
        spisokFill.insert(0, spisokFill.pop())
print(spisokFill)
    
    