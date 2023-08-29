# Создание множества со случайными элементами
my_set1 = {1, 2, 3, 'a', 'b', 'c'}
my_set2 = {3, 4, 5, 'b', 'c', 'd'}

# Вывод первого множества
print("Первое множество:", my_set1)

# Создание кортежа из пересечения множеств
intersection_tuple = tuple(my_set1.intersection(my_set2))
print("Кортеж из пересечения множеств:", intersection_tuple)

# Создание кортежа из разности множеств
difference_tuple = tuple(my_set1.difference(my_set2))
print("Кортеж из разности множеств:", difference_tuple)

# Срез первых 3 символов из кортежа
sliced_tuple = intersection_tuple[:3]
print("Срез первых 3 символов из кортежа:", sliced_tuple)

# Вывод символов с числами из второго множества
numbers_symbols = {item for item in my_set2 if isinstance(item, int)}
print("Символы с числами из второго множества:", numbers_symbols)

# Развертывание кортежа с помощью среза
reversed_tuple = difference_tuple[::-1]
print("Развернутый кортеж:", reversed_tuple)

# Преобразование кортежей в списки
intersection_list = list(intersection_tuple)
difference_list = list(difference_tuple)

print("Список из кортежа пересечения:", intersection_list)
print("Список из кортежа разности:", difference_list)

