# Задача:
# 2. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка
# l = [1, 2, 3]
# a = 'abc'
# result = [1, 2, 3, 'a', 'b', 'c']

# Решение:
l = [1, 2, 3]
a = 'abc'
l.extend(list(map(str, a)))
print(l)
