""""
Обчислити перимерт квадрата за стороною, що вводиться користувачем.
Результат вивести на екран.
"""
try:
    n = float(input("Введіть сторону квадрата:   "))
    if n <= 0:
        print("\nВВедіть сторону квадрата більше нуля")
except ValueError:
    print("\nВВедене не числове значення сторони квадрата")
    exit()

# формула для розрахунку периметру квадрата p = 4*n
p = 4 * n
print("\n Периметр квадрата становить {}".format(p))