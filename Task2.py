#Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите X: ')
x = int(input())
print('Введите Y: ')
y = int(input())
print('Введите Z: ')
z = int(input())


left_part = not (x or y or z)
right_part = not x and not y and not z


if left_part == right_part:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
