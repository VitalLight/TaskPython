""""
Написати контактний довідник. Має бути реалізовано такі класи: Person, Address, Contact, Notebook.
Клас Contact повинен одночасно наслідуватися від класу Address та Person.
Після запуску програми користувач повинен мати змогу додавати нові контакти, переглядати існуючі, робити пошук по імені.
 Всі ці методи пошуку, додавання, перегляду мають бути розміщені у класі Notebook.
 Контактну інформацію зберігати у файлі у довільному форматі.
 При запуску програми із файлу зчитувати всі контактні дані.
Для кожного контакту створювати динамічно об’єкт типу Contact і додавати його до масиву всіх контактів.
Масив контактів зберігати як поле contacts всередині класу Notebook.
"""
import json
print("КОНТАКТНИЙ ДОВІДНИК")

class Person():
    def __init__(self, f_name, l_name, mail, n_phone):
        self.name = f_name
        self.prizv = l_name
        self.email = mail
        self.phone = n_phone

class Address:
    def __init__(self, streete, n_house, touwn):
        self.streete = streete
        self.house = n_house
        self.misto = touwn


class Contact(Person, Address):
    def __init__(self, f_name, l_name, mail, n_phone, streete, n_house, touwn):
        Person.__init__(self, f_name, l_name, mail, n_phone)
        Address.__init__(self, streete, n_house, touwn)

    def read_contact(self):
        with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json', 'r') as f:
            masiv_contact = json.loads(f.read())  # з файлу записується рядок
            print(masiv_contact)
            contacts = list()
            for i in range(len(masiv_contact)):
                contact = cont
                #  обєкту контакт не бачить
                contacts.append(contact)
        print(contacts)
        return contacts

    #  це щось теж не працює? не розумію принцип як сюди передати дані, щоб П мене розумів, які дані я хочу побачити.
    #  та як при потребі ці дані перетворити в інший формат
    def __str__(self):
        return self.read_contact()  #

class Notebok (Contact):
    mas_dict = list()
    def __init__(self):
        pass

    def add_new_contact(self, new_cont):
        with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json', 'r') as f:
            dict_contact = json.loads(f.read())

            #  по new_cont виникає помилка, що не хоче ітеруватися. Я не розумію для чого воно йому треба.
            #  чому він не може просто взяти переданий обєкт?
            #  при такому записі має ствритися словник.
            dict_contact.update(new_cont)

            #  а так я хочу цей словник запистаи в масив, і в мене це не виходить! що мені потрібно почитати?
            #  щоб зрозуміти свої помилки
            dict_in_mas = dict_in_mas.append(dict_contact)

            #  і мені воно не записує
            with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json', 'w') as f:
                json.dump(dict_in_mas, f)

            print(dict_in_mas)
            return dict_in_mas


#  додає нові контакти
# dict_contact = {}
while True:
    f_name = input("enter first name     ")
    l_name = input("enter last name     ")
    mail = input("enter number mail    ")
    n_phone = input ("enter number phone    ")
    streete = input("enter street           ")
    n_house = input("enter number house    ")
    touwn = input("enter touwn    ")
    break

#  dinamic object
#  створення обєкту cont класу Contact та звернення до його методу read_contact
cont = Contact(f_name, l_name, mail, n_phone, streete, n_house, touwn)

cont.read_contact()
#  підозрюю що десь тут я не правильно розумію запис та передачу даних
new_cont = Notebok()
new_cont.add_new_contact(new_cont)


