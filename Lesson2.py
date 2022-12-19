# Наипишите программу, которая принимает на вход число N и выдает последовательность из N членов
# Например:  Для N = 5: 1, -3, 9, 27, 81
#n = int(input())
#print(n, end=': ')
#for i in range(n - 1):
#    print(((-3) ** i), end=', ')
#print((-3) ** (n - 1))
## второй вариант:
#n = int(input())
#out_list = []
#for i in range(n):
 #   out_list.append((-3) ** i)
#print(*out_list, sep=', ')

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#n = int(input())
#print(f'n = {n}', end=': ')
#for i in range(1, n):
#    x = 3 * i + 1
#    print(f'{i}: {x}', end=', ')
#print(f'{n}: {3 * n + 1}')
## второе решение:
#n = int(input())
#out_dict = {}
#for i in range(1, n + 1):
 #   out_dict[i] = 3 * i + 1
#print(out_dict)
# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
mes = 'Привет Всем привет и приват Опять привет'
m = 'привет'
#print(mes.count(m))
## второе решение !!!!
#i = 0
#c = 0
#while i < len(mes):
   # if mes[i:i + len(m)] == m:
    #    c += 1
   #     i += len(m)
  #  else:
 #       i += 1
#print(c)



count = 1
for el in mes:
    if el == ' ':
        count += 1
print(count)
c = 0
j = 0
temp = ''
while j < len(mes):
    if mes[j] != ' ':
        temp = temp + mes[j]
        j += 1
    else:
        if temp == m:
            c += 1
            temp = ''
        else:
            temp = ''
        j += 1
print(c)


## третье решение
#c = 0
#for el in mes:
#    if el == m:
#        c+=1
#print(c)

