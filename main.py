# Lecture 1

# Арифметические операции
# +, -, *, /, %, //, **
# (), сокращенные операции

a = 1.356465
b = 3
c = a * b
print(c)
c = round(a*b,3)
print(c)

d=3
d+=5
print(d)


# Управляющие конструкции:
# for

for i in 1, 2, 3, 4, 5:  # простой набор значений
    print(i**2)

list = [1, 2, 3, 4, 10, 5]  # список
for i in list:
    print(i)

r = range(5)  # итерируемый объект рэньдж, который
# выдает по умолчанию задается от 0 до n-1, шаг 1 (0,n-1,1)
# если нужны другие аргументы, то прописываем в скобках
for i in r:
    print(i)

# можно и не объявлять переменную
for i in range(5):
    print(i)

# в range можно указать интервал с помощью аргументов
#  и шаг приращения возвращаемого элемента

for i in range(1, 10, 2):
    print(i)

#  использование строки, которая будет возвращаться по
#  знакам c точностью до пробелов

for i in 'qwe - rty':
    print(i)


# Функции

def f(x):              # миксуем типы возвращаемых данных
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 1                 # <class 'str'>
print(f(arg))           # если arg = 2.3 <class 'int'>
print(type(f(arg)))     # если arg = 2 <class 'NoneType'>


# Управляющие конструкции
# if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждал Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)


# работа в цикле со строками

text = 'съешь ещё этих мягких французских булок'

print(len(text))      # 39 количество символов (с пробелами!)
print('ещё' in text)  # True наличие слова "еще" в тексте
print(text.isdigit())  # False наличие цифр в тексте
print(text.islower())  # True наличие символов в нижнем регистре
print(text.replace('ещё', 'ЕЩЁ'))  # замена слов

print(text[0])             # вызов 1 символа в тексте
# print(text[len(text)])   # IndexError  нумерация с 0
print(text[len(text)-1])   # к  последний элемент текста
print(text[-5])            # б отстчет в обратную сторону с конца текста
print(text[:])             # выводит весь текст (сахар)
print(text[:2])            # съ  интервал символов (0 можно не писать)
print(text[len(text)-2:])  # ок
print(text[2:9])           # ешь ещё
print(text[6:-18])         # еще этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6])           # сеикакл
text = text[2:9] + text[-5] + text[:2]


# Списки: введение
# list = list если тип данных range, то его надо трансформировать в list

numbers = [1, 2, 3, 4, 5]  # инициируем переменную с типом список
print(numbers)            # [1, 2, 3, 4, 5]
ran = range(1, 6)         # инициируем переменную с типом range
print(range)              # <class 'range'> выведет в консоль
print(type(ran))          # смотрим тип данных переменной ran
num = list(ran)           # команда, меняющая тип данных с range на list
print(num)
print(type(num))

print(numbers)                # [1, 2, 3, 4, 5]
print(len(numbers))           # 5 размер списка через функцию len
print(f'{len(numbers)} len')  # вывести размер списка через интерполяцию
print(numbers[0])             # обращение к элементу списка по индексу
numbers[0]=10                 # присваиваем новое значение 1 элементу списка
print(numbers)                # [10, 2, 3, 4, 5]

for i in numbers:             # при работе со списком в цикле
    i*=2                      # элементам присваивается новое значение
    print(i)                  # [20, 4, 6, 8, 10]
print(numbers)                # [10, 2, 3, 4, 5] при выходе из цикла возвращаются первоначальные значения элементов

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)                  # red green blue

for e in colors:              # redred greengreen blueblue
    print(e*2)

colors.append('gray')         # добавить в конец
print(colors)                 # red green blue gray
print(colors == ['red', 'green', 'blue', 'gray']) # True

# colors.remove('red')         # удалить элемент 1 вариант кода
del colors[0]          
print(colors)   


# Заполнение списка через рандом

import random

n = int(input('Введите количество элементов множества '))

list_1 = []
for i in range(n):
    list_1.append(random.randint(1, 21))
print(*list_1)


# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 < 4 and 5 > 2
print(a)

b = 1 != 2
print(b)

c = 'qwe'
d = 'qwe'
print(a == b)

e = [1, 2]
f = [1, 2]
print(e == f)

func = 1
T = 4
x = 123
print(func < T > x)

i = 1 > 2 or 4 < 6
print(i)

u = [1, 2, 3, 4]
print(u)
print(not 2 in u)

is_odd = not u[0] % 2
print(is_odd)


# Ввод и вывод данных
# print, input
# работа с текстовым типом данных

#print('Введите а');
#a = input()
#print('Введите b');
#b = input()
#print('{} {}'.format(a,b))
#print(f'{a} {b}')
#print(a, ' + ', b, ' = ', a+b)

# работа с целочисленным и вещественным типом данных

print('Введите а')
a = float(input())
print('Введите b')
b = int(input())
print('{} {}'.format(a,b))
print(f'{a} {b}')
print(a, ' + ', b, ' = ', a+b)


# типы данных и переменная
# int, float, boolean, str, list, None

a = 123
b = 1.23
print(a)       # показать переменную
print(type(a)) # показать тип данных
print(b)
print(type(b))
value = None
print(type(value))
value = 1234
print(type(value))
s = 'hello world'  # \n - переход на новую строку
print(s)
print(type(s))

print(a, b, s)             # варианты вывода строк
print(a, '-',b, '-', s)    
print('{} - {} - {}'.format(a,b,s))
print(f'{a} - {b} - {s}')  # интерполяция
print('{1} - {2} - {0}'.format(a,b,s)) # менять последовательность вывода

f = True
print(f)
e = False
print(e)

list = [1,2,3]
col = ['hello', 1,2,3,4,True]
print(list)
print(col)


# Получить инвертированное (перевернутое) число

original = 123
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

ori = 123
inv = 0
while ori != 0:
    inv = inv * 10 + (ori % 10)
    ori //= 10
    print(ori)
else:
    print('Пожалуй')
    print('хватит ')
print(inv)




# Lecture 2


# 1 способ записи данных

colors = ['red', 'green', 'blue']   # в качестве источника данных выступает список
data = open('file.txt', 'a')        # создаем текстовую переменную data и связываем ее с текстовым файлом
data.writelines(colors)             # будем записывать colors (разделителей не будет)
data.close()                        # закрываем связанный файл запускаем код и создается file.txt в нем добавлена запись 
                                    # redgreenblue повторный запуск скрипта добавить еще раз redgreenblueredgreenblue
                                    # модификатор w перезаписывает запись
data.write('\nLINE 2\n')            # добавит запись с новой строки

# 2 способ записи данных

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n') # запуск привел к перезаписи текста в file.txt


# работа с функциями по умолчанию

# def new_string(symbol, count):
    # return symbol*count

# print(new_string('!', 5))   # получим !!!!!
# print(new_string('!'))        # TypeError:

def new_string(symbol, count=3): # если укажем в аргументе =3
    return symbol*count

print(new_string('!'))       #  то получим !!!
print(new_string('4'))       # 444
print(new_string(4))         # 12


# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу.
# в списках и кортежах мы обращаемся к элементам по индексам, в словарях эту роль
# выполняют ключи.

dictionary = {} # создали пустой словарь \ (обратный слэш на второй строке, нужен для того,
                # чтобы не писать все в одну строку)
d = dict()      # также создает пустой словарь
dictionary = \
    {
        'up': '1',
        'left': '2',
        'down': '3',
        'right': '4'
    }
print(dictionary) # {'up': '1', 'left': '2', 'down': '3', 'right': '4'}
print(dictionary['left']) # 2

for k in dictionary.keys(): # проходимся циклом по коллекции ключей
    print(k)                # up
                            # left
                            # down
                            # right
for k in dictionary.values(): # если хотим посмотреть на конкретные значения
    print(k)                #  1
                            # 2
                            # 3
                            # 4          
for v in dictionary: # если хотим пройтись по циклу и увидеть все значения нашего словаря
    print(v)                # up
                            # left
                            # down
                            # right
    print(dictionary[v])  
# up
# 1
# left
# 2
# down
# 3
# right
# 4        

del dictionary['left'] # удаление элемента                          
print(dictionary)      # {'up': '1', 'down': '3', 'right': '4'}

for item in dictionary:
    print('{}: {}'.format(item,dictionary[item]))
# up: 1
# down: 3
# right: 4

d={}                  # создала словарь
d['q'] = 'qwerty'     # в словаре d под ключом 'q' будет находиться значение 'qwerty'
print(d)              # {'q': 'qwerty'}

d['w'] = 'werty'      # добавила еще один элемент словаря
print(d)              # {'q': 'qwerty', 'w': 'werty'}
print(d['w'])         # werty

d[987] = 485609       # добавали ключ другого типа (int) в словарь {'q': 'qwerty', 'w': 'werty', 987: 485609}
print(d)

print(d.items())      # dict_items([('q', 'qwerty'), ('w', 'werty'), (987, 485609)]) получаем список, 
for (k,v) in d.items():  # где каждый элемент является кортежем из двух значений: ключа и элемента словаря
    print(k,v) 


# Функции

def f(x):              # миксуем типы возвращаемых данных
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 1                 # <class 'str'>
print(f(arg))           # если arg = 2.3 <class 'int'>
print(type(f(arg)))     # если arg = 2 <class 'NoneType'>

# запустим функцию из файла functions.py (главное чтобы этот файл,
# был в той же папке, где идет текущая работа) при этом создается файл picache

import functions

# можно переименовать эту функцию или сократить ее название (если так удобно)

import functions as f

print(f)


# Список - это упорядоченный конечный набор элементов, по сути это тот же самый массив,
# в котором можно хранить элементы любых типов данных.

list_1 = []                # создаем пустой список
print(list_1)              # []
list_2 = list()            # создаем пустой список через функцию
print(list_2)              # []
list_3 = [1, 2, 3, 4, 5]
print(list_3)              # [1, 2, 3, 4, 5]
print(*list_3)             # "открываем" список 1 2 3 4 5

for i in list_3:
    print(i)
# 1
# 2
# 3
# 4
# 5

list_6 = [12, 7, -1, 21, 0]
for i in range(len(list_6)):
    print(list_6[i])               # вывод каждого элемента списка

print(len(list_1))          # 0
print(len(list_3))          # 5

print(list_3[0])            # обращение к элементу списка по индексу
print(list_3[-1])           # [-1] индекс последнего элемента

# заполнение списка во время работы программы последовательно
list_4 = []            # создали пустой список
print(list_4)
for i in range(5):     # цикл выполнится 5 раз
    list_4.append(i)
    print(list_4)

# []
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]

# заполнение списка во время работы программы пользователем произвольно

list_5 = list()         # создание пустого списка
print(list_5)
for i in range(5):      # цикл выполнится 5 раз
    n = int(input())    # пользователь вводит целое число
    list_5.append(n)    # сохранение элемента в конец списка
    print(list_5)

list1 = [1, 2, 3, 4, 5]
list2 = list1       # копируем лист1 в лист2

for e in list1:
    print(e)

print()              # [1, 2, 3, 4, 5]

list1[0] = 123
list2[1] = 231

for e in list2:
    print(e)          # [123, 2, 3, 4, 5]
    # [123, 231, 3, 4, 5] т.е. меняем значение в одном, меняются они и в другом
    # просто так копировать данные не нужно

list3 = [1, 2, 3, 4, 5, 6, 7]
print(len(list3))
print(list3.pop())  # метод pop извлекает последний элемент из списка
print(list3)        # [1, 2, 3, 4, 5, 6]
print(list3.pop())
print(list3)
print(list3.pop(2))  # извлекаем указанный аргумент через индекс
print(list3)        # [1, 2, 4, 5]
print(list3.insert(2, 11))  # вставить элемент в список (2,11)
# 2 - индекс вставляемого элемента начиная с 0
# 11 - значение вставляемого элемента
print(list3)              # [1, 2, 11, 4, 5]
print(list3.append(11))   # добавление элемента в конец списка
print(list3)              # [1, 2, 11, 4, 5, 11]
list3.append(8)
print(list3)              # [1, 2, 11, 4, 5, 11, 8]

# Срезы (отрицательное число в индексе - счет с конца списка)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])                           # 1
print(list_1[1])                           # 2
print(list_1[len(list_1)-1])               # 10
print(list_1[-5])                          # 6
print(list_1[:])                           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])                          # [1, 2]
print(list_1[len(list_1)-2:])              #[9, 10]
print(list_1[2:9])                         # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])                       # []
print(list_1[0:len(list_1):6])             # [1, 7]
print(list_1[::6])                         # [1, 7]


"""
List comprehension — это упрощенный подход к созданию списка, который задействует
цикл for, а также инструкции if-else для определения того, что в итоге окажется
в финальном списке.
Задача. Создать список, состоящий из чисел в диапазоне от 1 до 100.
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)               # [1, 2, 3,..., 100]
"""

# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# print(list_1) 

# Добавляем условие: только четные

list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
print(list_1) 

# Добавляем условие: создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]
print(list_1) 

# Можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)           # [0, 4, 8, 12, 16]


# передача неограниченного количество аргументов: требуется поставить * перед аргументами

def concatenatio(*params):
    res: str = ""      # тип данных строка
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(concatenatio(1, 2, 3, 4))        # TypeError

# если нужно работать с числами, тогда 4 строка должна иметь вид:
# res: int = 0 или res = 0
# print(concatenatio(1, 2, 3, 4))      уже не будет ошибки а выдаст 10


path='file.txt'
data=open('file.txt', 'r')
for line in data:
    print(line)
data.close()


# определение чисел Фибоначчи рекурсивным методом

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # [1, 1, 2, 3, 5, 8, 13, 21, 34]


# Множества - хранилище данных, которое содержит в себе 
# уникальные элементы (может быть как упорядоченным, так и нет)

q = set()           # создаем множество

colors = {'red', 'green', 'blue'}
print(type(colors)) # class 'set'
print(colors)       # {'green', 'blue', 'red'}

colors.add('red')   # добавить элемент ничего не добавит, так как 'red' уже есть
                    # а множество это хранилище уникальных элементов
print(colors)       # {'red', 'blue', 'gray'}


colors.add('gray')  # добавить элемент
print(colors)       # {'red', 'blue', 'gray', 'green'}
colors.remove('red')# удалить элемент
print(colors)       # {'gray', 'green', 'blue'}
#colors.remove('red')# KeyError: 'red'  ошибка, т.к. элемента уже нет
colors.discard('red')# ok функция, которая проверяет наличие элемента в множестве, если
                     # он есть, то удаляет, если нет, то пропускает и дает ошибку
print(colors)        # {'gray', 'blue', 'green'}
colors.clear()       # очистка множества, оно стало пустое
print(colors)        # set() можно продолжить работу с пустым множеством


# работа с множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
print(c)             # {1, 2, 3, 5, 8}
u = a.union(b)       # объединение множеств а и б
print(u)             # {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)# пересечение а и б
print(i)             # {8, 2, 5}
dl = a.difference(b) # разность от а множества б
print(dl)            # {1, 3}
dr = b.difference(a) # разность от б множества а
print(dr)            # {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
print(q)              # {1, 21, 3, 13}

# работа с неизменяемыми (замороженными множествами)
# в них добавления, удаления работать не будут

s = frozenset(a) # заморозить множество


"""
Кортеж - это некий неизменяемый список. Используется в случае задиты каких-либо
данных от изменений (намеренных или случайных). Кортеж по сравнению со списком
занимает меньше места и работает быстрее.
"""

a, b = 3, 4      # это множественное присваивание значения переменных
(a) = (3, 4)     # а если все обрамим в скобочки, то получим кортеж
print(a)         # (3, 4)
print(a[0])      # можно обратиться по индексу, получим 3
(b) = (3, 1, 41, 4)
print(b[-2])     # 41

# но если мы пожелаем присвоить какому-то элементу другое значение,
# то это не получится, потому что это неизменяемый список !
# a[0] = 12 # не получится

t = ()
print(type(t))    # class 'tuple'
# если хотим создать кортеж из одного элемента, иначе t = (1) будет число
t = (1, )
print(type(t))    # class 'tuple'
t = (1)
print(type(t))    # class 'int'
t = (28, 9, 1990)
print(type(t))    # class 'tuple'
colors = ['red', 'green', 'blue']
print(colors)     # ['red', 'green', 'blue']
t = tuple(colors)
print(type(t))    # class 'tuple
print(t)          # ('red', 'green', 'blue')

# работа с кортежами в циклах

c = (3, 4, 5)
for item in c:
    print(item)
# 3 
# 4
# 5

# действия с кортежами из текстовых данных

t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green

for e in t:
    print(e)
# red
# green
# blue

# t[0] = 'black' # не даст переименовать так как это кортеж

# двойное преобразование (возможность "распаковать" кортеж в отдельные переменные)
t = tuple(['red', 'green', 'blue']) # создаем список [] преобразуем его в кортеж ()
red, green, blue = t # распаковываем кортеж, переводим в независимые переменные
# и далее с ними работаем, как с отдельными переменными
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# преобразование списка в кортеж
v = [1,8,9]
print(v)           # [1, 8, 9]
print(type(v))     # class 'list'

v=tuple(v)
print(v)           # (1, 8, 9)
print(type(v))     # class 'tuple'

# распаковка кортежа на переменные
a, b, c = v  
print(a,b,c)       # 1 8 9
print(type(a))     # class 'int'




# Lecture 3

'''
Очень важно понимать одну вещь, сколько аргументов мы передаем, столько и
принимаем. Или наоборот сколько аргументов мы принимаем, столько и передаем.
В нашем случае функция sum_numbers принимает 1 аргумент(n)
def sum_numbers(n, y='Hello'):  # вводим у по умолчанию, в print(n) не добавляем
    print(y)
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
n = int(input('Введите n: '))
print(sum_numbers(n))                # Hello
                                     # 15         
# print(sum_numbers(n, 'qwerty'))    # TypeError
'''

# а если необходимо добавить и в print(n)

def sum_numbers(n, y='Hello'):  
    print(y)
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


n = int(input('Введите n: '))

print(sum_numbers(n,'qwerty'))        # qwerty
                                      # 15


'''
Создать функцию sum_numbers которая будет считать сумму всех элементов от 1 до n.
решение без return (внутри функции)
def sum_numbers(n):      # def - указание на функцию, sum_numbers - название фукции, 
    sum = 0              # n - принимаемая переменная
    for i in range(1, n+1):
        sum += i
    print(sum)           # выводим результат
n = int(input('Введите n: '))  # запрашиваем переменную
sum_numbers(n)           # вызываем функцию
'''


# решение через return

def sum_numbers(n):       
    sum = 0              
    for i in range(1, n+1):
        sum += i
    return sum           # return возвращает значение и завершает работу функции


n = int(input('Введите n: ')) 

print(sum_numbers(n))    # следовательно результат выводим через print (иначе мы его не увидим), 
                         # после завершения работы функции

# a = sum_numbers(5)     # другой вариант вывода результата
# print(a)


# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1: # не создаем базис рекурсии, а показываем условие когда она выполняется (пока не останется по 1 элементу)
        mid = len(nums) // 2 # создаем переменную, путем деления размера списка на цело на 2
        left = nums[:mid]    # срез списка (левая часть от mid)
        right = nums[mid:]   # срез списка (правая часть от mid)
        merge_sort(left)     # создаем рекурсию для левой части (деление на 2)
        merge_sort(right)    # создаем рекурсию для правой части (деление на 2)
        i = j = k = 0        # создаем 3 переменных: i для left, j для rigth, k для общего списка
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i] # cоздаем пары чисел
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):   # если в каком-либо списке остались значения без пары
            nums[k] = left[i]  # c помощью двух этих условий добавляем их в конец
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)


# Алгоритм "быстрая сортировка". Отсортировать массив [10, 5, 3, 2]

def quick_sort(array):
    if len(array) <=1:   # базис рекурсии
       return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    # print(array)       # можно включить строку и посмотреть этапы рекурсии
    return quick_sort(less) + [pivot] + quick_sort(greater)
# pivot из int преобразовали в [] чтобы не показывало ошибку

print(quick_sort([5, 10, 3, 2])) # [2, 3, 5, 10]

'''
1-е повторение рекурсии:
    array = [5, 10, 3, 2]
    pivot = 5
    less = [3, 2]
    greater = [10]
    return quick_sort([3, 2] + [5] + quick_sort[10]) # [3, 2] [5] [10]
2-е повторение рекурсии:
    array = [3, 2]
    pivot = 3
    less = [2]
    greater = []
    return quick_sort([2] + [3] + quick_sort[]) # [2] [3] [5] [10]
# Важно! Помимо вызова рекурсии добавляются списки [5] и [10]
3- е повторение рекурсии:
    array = [2]
    return [2] # сработал базовый случай рекурсии и она остановилась
получаем список
[2, 3, 5, 10]  
'''


''' Рекурсия
Пользователь вводит число n. Необходимо вывести n - первых членов 
последовательности Фибоначчи. Решить задачу, используя рекурсию.
'''

def fib(n):           # создаем метод (рекурсию)
    if n in [1, 2]:    # базис рекурсии, т.е. условие выхода из нее
        return 1
    return fib(n-1) + fib(n-2) # сама рекурсия (формула расчета)

list_1 = []              # создаем список, в который будем записывать результат
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)               # [1, 1, 2, 3, 5, 8, 13, 21, 34]


'''
Передача неограниченного количества аргументов в функцию
def sum_str(*args):       # указание *, позваляет добавлять 
    res = ''              # неограниченное количество аргументов
    for i in args:
        res += i
    return res
print(sum_str('q', 'w', 'e', 'r', 't' ))
print(sum_str('q', 'w', 'e', 'r', 't', 'y' ))
'''
# работа с int

def sum_num(*args):       # указание *, позваляет добавлять 
    res = 0               # неограниченное количество элементов
    for i in args:
        res += i
    return res


print(sum_num(1, 2, 3, 4)) # 10
print(sum_num(1, 2, 3, 4, 5)) # 15




# Lecture 4

'''
Функция enumerate() применяется к итерируемому объекту и возвращает новый
итератор с кортежами из индекса и элементов входных данных.
Функция enumerate() позволяет пронумеровать набор данных.
'''
words = ['Казань', 'Смоленск', 'рыбки', 'Чикаго']
data = list(enumerate(words))
print(data)
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'рыбки'), (3, 'Чикаго')]


'''
Название функции filter() - говорящее, она фильтрует какие-либо
значения. На вход принимает 2 аргумента: 1 - сама функция, 2 - объект.
Функция filter() будет возвращать только те элементы объекта, для
которых вызов функции, которую мы передали, вернула значение thrue.
'''
data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)         # [15, 65, 175] фильтрует и отрбирает значения 
                   # элементов списка, оканчивающихся на 5


"""
lambda
"""

# def sum(a, b):
#     return a + b

def math(op, x, y):
    print(op(x, y))   

# заменим 1-2 строки кратким выражением, вводя lambda функцию
# она также будет называться sum, те же аргументы только без скобок
# далее после двоеточие, формулу получения результата функции

sum = lambda a, b: a + b


math(sum, 5, 45)

# можно еще больше сократить код, вообще не описывать функцию sum
# а сразу в вывозе функции math_1 описывать lambda функцию
# мы в оперативной памяти выделяем участок под эту функцию 
# и передаем ссылку сразу на этот участок, и затем с помощью
# переменной ор вызываем эту функцию


def math_1(op, x, y):
    print(op(x, y))  

math_1(lambda a, b: a + b, 5, 45)


# ИТОГО:
# 1 Сначала мы избавились от классического описания функций
# 2 Затем научились описывать лямбды, присваивая результат какой-то # переменной
# 3 После избавились от этой переменной, пробрасывая всю лямбду в качестве функции


def f(x):
    return x ** 2
            # g — это переменная, которая хранит в себе ссылку на функцию
g = f       # по сути мы переименовали f и создали ей новое имя. Теперь в оперативной 
            # памяти у нас есть участок, на который ссылаются переменные g и f
            # теперь в контексте этого приложения g может использоваться точно так же, как и f.

print(f(4)) # 16
print(g(4)) # 16

print(type(f)) # <class 'function'>
print(type(g)) # <class 'function'>

# У функции есть тип, значит мы можем создать переменную типа функции и
# положить в эту переменную какую-то другую функцию.


'''
Функция map() принимает на вход 2 аргумента: 1 - сама функция, которую мы передаем;
2 - объект. Функция map() применяет указанную функцию к каждому элементу
итерируемого объекта и возвращает итератор с новыми объектами.
'''

list_1 = [x for x in range(1, 20)] # заполним через генератор списков
print(list_1)  
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

list_1 = list(map(lambda x: x + 10, list_1)) 
# list_1 равен новому списку list в котором мы будем вызывать функцию map()
# и применять к ней функцию, которую мы опишем через функцию lambda
print(list_1)  
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]


"""
math
"""

def calc1(a):
    return a + a

def calc2(a):
    return a * a  # 100

# Если мы добавим в код еще умножение, деление и вычитание, то 
# внутри одного кода будем плодить одинаковую логику.

# Достаточно взять функцию math, которая будет в качестве аргумента
# принимать операцию и что-то выдавать


def math(op, x):
    print(op(x))   # вызываем и выводим на экран

math(calc2, 10)    # 100 передаем в функцию math функцию calc2,
                        # переменная op имеет ссылку на функцию calc2                

     # c несколькими переменными
     
def sum(a, b):
    return a + b

def mylt(a, b):
    return a * b

def math_1(op, x, y):
    print(op(x, y))   

math_1(sum, 5, 45)   # 50   


'''
В списке хранятся числа. Нужно выбрать только чётные числа и составить
список пар (число; квадрат числа).
Input:  [1, 2, 3, 5, 8, 15, 23, 38]
Output: [(2, 4), (8, 64), (38, 1444)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []       #  а можно list(); 
#                #  создали список res, в который будем выводить результа
# for i in data :
#     if i % 2 == 0:
#         res.append((i, i ** 2)) # передаем в список в виде кортежей
# print(res)
# запишем код с помощью применения lambda функции
def select(f, col):            # функция, в которую передаем фукнцию f и какое-то значение col
    return[f(x) for x in col]  # она будет возращать список, в котором каждому элементу будем применять
                               # функцию f(x), но мы должны будем пройти по всем элементам col
                               # (мы передаем список и функцию, она ко всем элементам применяет функцию)
def where(f, col):
    return[x for x in col if f(x)] # функция возвращает список из x,если мы пройдемся по всем элементам col                              
                                   # но возращать только те элементы, которые прошли проверку условия функции f(x)
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)           # список res создается вызовом функции select (int)-указывает, что мы желаем  
                                  # привести все к целочисленному типу, на вход принимает список data
print(res)   # [1, 2, 3, 5, 8, 15, 23, 38] возрващает все элементы списка
res = where(lambda x: x % 2 == 0, res) # вновь обращаемся к списку res, но уже будем делать выборку через вызов
                                   #  функции where. Cоздаем функцию lambda, которая принимает значение x  
                                   # и возвращает либо thrue либо false, условии деления на 2 на цело и так же передаем res
print(res) #[2, 8, 38] возвращает только четные значения x, но без возведения в квадрат
res = list(select(lambda x: (x, x**2), res))   # для того чтобы все ^2, вновь обращаемся к списку res и изменяем его
                                         # вновь обращаемся к функции select, в которую передаем первый аргумент:
                                         # функция lambda х, для кортежа из x и x**2 (х возведенный в квадрат), 
                                         # не забываем передать в функцию select список res
                                         # говоря проще: мы хотим преобразовать список res и вернуть значения в виде 
                                         # кортежей добавляем впереди select list(), чтобы получить в виде типа список
print(res)     # [(2, 4), (8, 64), (38, 1444)]
# c помощью map() можно сделать этот код лучше, он позволит избавиться от функции select()
# удалим строки, где мы задаем функцию select(), в оставшихся строках заменим функцию select()
# на map(). Map() это встроенная функция Python
# по сути функция select() эта таже функция map(), просто функцию select() мы прописали явно, 
# а функция map() прописана в модулях.
def where(f, col):
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)
'''
# фукнция where() похожа на функцию filter(), упростим вышенаписанный код

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = filter(lambda x: x % 2 == 0, data)
res = list(map(lambda x: (x, x ** 2), res))
print(res)         # [(2, 4), (8, 64), (38, 1444)]


'''
C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
функция .split() преобразует строку в список, используя в качестве разделителя по умолчанию
пробел, но можно по желанию указать любой разделитель, например запятая пробел (', ')
Результат работы map() — это итератор. По итератору можно пробежаться только один раз. 
Чтобы работать несколько раз с одними данными, нужно сохранить данные (например, в виде списка).
'''

data = '1 2 3 5 8 15 23 38' # пользователь вводит строку
# print(data)                 # 1 2 3 5 8 15 23 38  - строка
# print(type(data))           # <class 'str'>

# data=data.split()
# print(data)                 # ['1', '2', '3', '5', '8', '15', '23', '38'] - cписок строк
# print(type(data))           # <class 'list'>

# необходимо преобразовать список строк в список чисел
# с помощью функции map() и lambda() можно исключить к коде строки 9-14

data = list(map(int, data.split()))
# скажем, что это список, к которому будем вызывать функцию map() в которой к каждому объекту будем
# применять функцию int(). А какому объекту? указываем, строкУ data[], которую мы приобразовываем
# в список строк, с помощью функции split() (мы же закомментировали строки 9-14)
print(data)           # [1, 2, 3, 5, 8, 15, 23, 38]
print(type(data))     # <class 'list'> - список чисел


'''
Функция zip() применяется к набору итерируемых объектов и возвращает итератор
с кортежами из элементов входных данных.
На выходе получаем набор данных, состоящий из элементов соответствующих
исходному набору.
'''
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)
 # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]


# Функция zip () пробегает по минимальному входящему набору:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)
 # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]




 # Lecture 5 in 5.ipynb