# Простой словарь
fio={'firstName':'nina','secondName':'Alexandrovna','lastName':'chekalina'}




# Доступ к значению
print("Полное имя/фамилия: " + fio['firstName'] + fio['lastName'])


# Перебор всех пар ключ-значение
fio={'firstName':'nina','secondName':'Alexandrovna','lastName':'chekalina','date':'2022-09-10','period':14}
for name,s in fio.items():
 print(name + ':' + str(s) )



# преобразую представление в список, списокявляется последовательностью кортежей (ключ, значение) - то, что получает dict для создания словаря
list(fio.items())



# функция sorted возвращает новый отсортированный список 
for name in sorted(fio.items()):
    print(name)



# противоположный порядок вывода
for name in sorted(fio.keys(),
                   reverse=True):
     print(name)
   

for name in sorted(fio.items(),
                   reverse=True):
     print(name)


# Перебираем все ключи
fio={'firstName':'nina','secondName':'Alexandrovna','lastName':'chekalina','date':'2022-09-10','period':14}
for name in fio.keys():
 print(name + '')



# Перебор всех значений
# Результат вызова .values также является представлением. Он отражает
# # # текущее состояние значений, находящихся в словаре
for number in fio.values():
 print(str(number) + ' ' + 'статус:по совместительству')



# Для вставки значений в словарь используют индексные операции:
fio['occupation'] = 'programming'



# поиск индексной операцией:
fio['occupation']



# Метод .get словаря получает значение, соответствующее ключу
staff = fio.get('Должность', 'преподаватель')
staff
 



# операции подсчета
import collections
count = collections.Counter(['Чернова', 'Семенов', 'Ветров', 'Чернова'])
count




# только Чернова
count['Чернова']




# Задание: Связать фамилию участника с двумя группами
surnamesGroup = ['Чернова', 'Семенов', 'Ветров', 'Мостовой']
candidate = ['Чернова']
surnames = {}
for name in surnamesGroup:
                 surnames.setdefault(name, []).append('DKMO-21')
for name in candidate:
                 surnames.setdefault(name,[]).append('DKMO-22')
print(surnames['Чернова'])




# Python не позволяет добавлять и удалять данные из словаря во время егоперебора.
# В таких ситуациях Python выдает исключение RuntimeError:
data = {'surname':'Чернова', 'surname':'Семенов','surname': 'Ветров', 'surname':'Мостовой'}
for key in dict(data):
    del data[key]



print("\n\nЗАДАЧА:")


from collections import Counter
phone = {'xiaomi': {'size': '1920:1080', 'память': '64', 'ОС': 'android', 'firms': 'xiaomi'},
         'Samsung': {'size': '1920:1080', 'память': '64', 'ОС': 'android', 'firms': 'Samsung'},
         'iPhone 8': {'size': '1920:1080', 'память': '64', 'ОС': 'ios', 'firms': 'Apple'},
         'iPhone x': {'size': '1820:760', 'память': '32', 'ОС': 'ios', 'firms': 'Apple'},}

s = {}
x = set()
for i in phone.values():
    for j, k in i.items():
        if not k in x:
            s[j] = 1
            x.add(k)
        else: s[j] += 1
print('Одинаковых фирм:', s['firms'])
print('Одинаковых ОС:', s['ОС'])
print('Ключи отсортированные по убыванию;', sorted(s.values(), reverse=True))
# Результат: https://clck.ru/328chc
