
""""
2. Послідовність Фібоначчі. Користувач вводить число n. Вивести на екран перші n елементів послідовності фібоначчі.
 Тобто, якщо було введено число “6”, то на екрані має бути виведено “1, 1, 2, 3, 5, 8”.
  Детальніше про послідовність можна почитати у Вікіпедії.
"""
n = int(input (" Введіть потрібну кількість чисел в послідовності Фібоначчі:  "))
f_arr = [1, 1]  # перші два початкові числа для послідовності Фібоначі
i=1 #  перший індекс елементу
for i in range (n):  #
    k_i =f_arr[i]+f_arr[i-1]  # третє число це сума значень двох попередніх чисел
    f_arr.append (k_i)  # заповнення масиву числами

print ("Послідовність Фібоначі з %s елементів має такий вигляд %s " %(n, f_arr))