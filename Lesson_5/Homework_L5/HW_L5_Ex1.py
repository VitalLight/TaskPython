""""
Alarm clock manager. Уявіть, що на протязі трьох наступних тижнів ви плануєте щодня прокидатися на 15 хвилин раніше,
 ніж попереднього дня. Проте на вихідних ви хочете прокидатися не раніше, а поспати стільки ж, скільки у п`ятницю.
  Напишіть програму, яка порахує і виведе на екран, на котру годину вам потрібно поставити будильник,
  щоб прокинутися вчасно протягом наступних трьох тижнів, якщо зазвичай ви просиналися о 08:00 ранку.
  Формат виводу наступний: http://i.imgur.com/SNDo2GO.png
"""
try:
        n_week =int (input ("Введіть кількість тижнів:   "))
except ValueError:
        print ("Введіть кількість тижнів числом")
        exit()
d_week = ["ПОНЕДІЛОК","ВІВТОРОК","СЕРЕДА","ЧЕТВЕР","ПЯТНИЦЯ","СУБОТА","НЕДІЛЯ"]
n_d = 7  # кількість днів в масиві d_week

t_st = input ("Введіть час(години: хвилини) у форматі --hh/mm-- від якого розпочати розрахунок  :   ")
a = t_st.split('/',2)  #  створюється масив -а- з елеметів "hh" та "mm"
if len(a)>2 or len(a)<2 :
    print("НЕ вірний формат введення --hh/mm-. Повторіть спробу")
    exit()

try:  #  перетворюємо стрічку в число з перевіркою на правильність формату введених даних
    t_zatr = int(input("Введіть час (t_zatr) на скільки хочете прокидатися раніше, хв:   "))
    hh = int(a[0])  # години перетворення str to int
    mm = int (a[1])  # хвилини перетворення str to int

    if hh>24 and mm >60:
        print (" Дані мають бути з такими показниками hh =<24 mm<=60 ")
        exit()
except  ValueError:
    print ("Введенні дані не цілі числа. Введіть дані hh, mm, t_zatr числами!")
    exit ()

e_time = hh*60+mm  # введений початковий час переведений в хвилини
d_mm = 24*60 # кількість хвилин в одній добі - 24 години

for i in range (n_week):  # цикл розрахунку починаємо в тиждні
    space_ = " "  # стрічка для відступу назв днів
    print("\n")  # щоб тижні розділити стрічкою

    for j in range(8):  # цикл по днях тижня

        if j<=4:  #  якщо індекс масиву менше вказаного - це дні з Пн по Пт
            t_Wake_up = e_time-t_zatr  # наступний час прокидання
            HH = t_Wake_up//60  # розрахунок цілих годин в часі для пробудження
            MM = t_Wake_up - HH*60  #  розрахунок хвилин в часі для пробудження
            if MM<=9:  #  якщо хвилини менше 10
                MM= ("0%s"%MM)  # такий запис працює! ставить нуль і потрібну хвилину!!!
            print ("%s %s  %s:%s" %(space_*j, d_week[j], HH, MM))  # друкує день з годинами
            e_time = t_Wake_up  # e_time переприсвоюємо час, щоб мати нову точку відліку часу пробудження

        elif 4<j<=6:
            print ("%s %s  %s:%s" %(space_*j, d_week[j], HH, MM))  # друкує день з годинами
