""""
Дано ромб (на картинці) зі стороною величиною n. Знайти площу такого робму зі стороною n.
"""
try:
    n = int(input("Введіть сторону ромба   "))
    if n <= 0:
        print ("\nВВедіть сторону робма більше нуля")
except ValueError:
    print ("\nВВедене значення сторони ромба не число")

# формула для розрахунку площі s = 2(n**2 -n)+1
s = 2 * (n**2 - n) + 1
print("\nПлоща ромба становить {}".format(s))