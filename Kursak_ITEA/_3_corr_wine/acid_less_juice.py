

def main_less_acid_juice():
    print("ПРОГРАМА ВИЗНАЧАЄ СКІЛЬКИ ПОТРІБНО СОКУ З меншою КИСЛОТНІСТЮ ДОДАТТИ ДО 1л ОСНОВНОГО СОКУ,"
          " ЩОБ ОТРИМАТИ ПОТРІБНУ ЗМЕНШЕНУ КИСЛОТНІСТЬ ОСНОВНОГО СОКУ\n")
    while True:
        try:
            a = float(input("ВВЕДІТЬ КІЛЬКІСТЬ ТИТРОВАНОЇ КИСЛОТИ В ОСНОВНОМУ СОЦІ, %\t\t\t").replace(',','.'))
            b = float(input("ВВЕДІТЬ КІЛЬКІСТЬ ТИТРОВАНОЇ КИСЛОТИ В СОЦІ З меншою КИСЛОТНІСТЮ"
                    " (ТОЙ, ЯКИМ МАЄМО РОЗБАВЛЯТИ) %\t\t\t").replace(',','.'))
            c = float(input("\nВВЕДІТЬ ПОТРІБНУ ТИТРОВАНОЇ КИСЛОТНІСТЬ В КУПАЖОВАНОМУ СОЦІ %\t\t\t").replace(',','.'))
            if b <= c <= a:
                kil_juice = round((a - c) / (c - b), 2)
                break
            else:
                print("!!!!!!!ВВЕДІТЬ КОРЕКТНО ЗНАЧЕННЯ ТИТРОВАНОЇ КИСЛОТНОСТІ В СОКАХ!!!!!!!\n")
                continue
        except ValueError:
            print("ВВЕДІТЬ КОРЕКТНО ДАНІ")
    print(f"\nДЛЯ ОТРИМАННЯ ПОТРІБНОЇ КИСЛОТНОСТІ {c}% В КУПАЖНОМУ СОЦІ, ПОТРІБНО НА 1л ОСНОВНОГО СОКУ"
            f" ДОДАТИ {kil_juice}л СОКУ ІЗ меншою КИСЛОТНІСТЮ")
