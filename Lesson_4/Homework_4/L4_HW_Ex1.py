
Nkard = input("Введіть номер своєї кредитної карти(16  цифр)   ")

print ("Введіть термін дії кредитної карти у форматі (місяць/рік)) у форматі dd/yy")

#ВВодяться дані щодо терміну дії картки
dd = input("Введіть день dd:   ")
Ldd = len (dd)# рахує скільки символів було введено
yy = input("Введіть день /yy:   ")
Lyy= len (yy)# рахує скільки символів було введено

# Вводимо значення CVV
CVV = input ("ВВедіть номер CVV - 3 числа   ")


# перевіряємо чи в номері карти введені лише цілі числа
try:
    intNkard = int(Nkard)
except ValueError: #  працює і без ValueError Чому?
    print ('Не всі символи в номері карти цифри. Номер карти повинен містити лише цифри!')
if len(Nkard)<16:
    print (" \nУ номер карти введено менше 16 цифр")
if len(Nkard)>16:
    print (" \nУ номер карти введено більше 16 цифр")

# перевіряємо на правильність введення формату дня (dd) в терміну дії карти в int, якщо правда, то помилки не буде
if len (dd) ==2:
    try:
        idd = int(dd)
    except :
        print ('\n НЕ правильно введений формат дня. Правильно введіть формат дня!')
else:
    print("                 Потрібно вірно ввести формат ДНЯ - 2 цифри")


# перевіряємо на правильність введення формату року (yy)в терміну дії карти в int, якщо правда, то помилки не буде
if len (yy) ==2:
    try:
        iyy = int(yy)
    except :
        print ('\n НЕ правильно введений формат року. Правильно введіть формат дня!')
else:
    print("                 Потрібно вірно ввести формат Року - 2 цифри")


# перевірка правильності введення CVV
if len(CVV)==3:
    try:
        iCVV = int(CVV)
    except:
        print("                 Введене число CVV НЕ відповідного формату")

if (len (Nkard) ==16 and intNkard == int(Nkard)) \
        and (len (dd) ==2 and idd == int (dd))\
        and (len (yy) ==2 and iyy == int(yy)) \
        and (len(CVV)==3 and iCVV == int(CVV)):

    print ("Ha-ha-ha.Now I will use your credit card! А людською мовою- Було Ваше стало Наше")
else:
    print (" Перелік даних, що ти ввів не вірно зазначено вище")







