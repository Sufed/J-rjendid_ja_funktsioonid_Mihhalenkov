import random
"""Напишите функцию sport(), при запуске которой происходит заполнение двух списков: sportlased[], tulemused[].  Список sportlased[] - заполняет пользователь, а список результаты[] – заполняется автоматически: оздаеются случайные 3 числа и наибольшее из них заносится в список.
После заполнения списков появляется меню с выбором действий:
• Узнать n лучших результатов;
• Упорядочить список в порядке возрастания баллов. Отобразить спортсменов их баллы и места;
• Ввести имя одного или нескольких спортсменов и показать его/их результат;
• Дисквалифицировать(удалить из списка)  спортсменов, у которых результаты хуже чем придуманный вами критерий;
• Свой вариант.
Для описания действий создайте необходимые функции."""

def sport():
    sportlased = []
    tulemused = []
    while True:
        print("")
        print("1. Добавить спортсмена")
        print("2. Узнать n лучших результатов")
        print("3. Упорядочить результаты в порядке возрастания баллов.")
        print("4. Найти результат(ы) спортсмена")
        print("5. Дисквалифицировать спортсменов")
        print("0. Упорядочить результаты в порядке убывания баллов.")
        print("6. Выйти")
        valik = int(input("Сделайте выбор (0-6): "))
        if valik == 1:
            nimi = input("Введите имя спортсмена: ")
            sportlased.append(nimi)
            tulemus = []
            for i in range(3):
                tulemus.append(random.randint(1, 100))
            parim_tulemus = max(tulemus)
            tulemused.append(parim_tulemus)
#С  22 строчки по 29 происходит добавление спортсмена в списки. Пользователь вписывает его имя и для него рандомно присваиваются результаты в количестве,
#3-ех штук.
        elif valik == 2:
            show_top_scores(tulemused)
        elif valik == 3:
            sort_scores(sportlased, tulemused)
        elif valik == 4:
            found_scores(sportlased, tulemused)
        elif valik == 5:
            remove(sportlased, tulemused)
        elif valik == 0:
            sort_scores_убывание(sportlased, tulemused)
        elif valik == 6:
            break
        else:
            print("Неверный выбор")
def show_top_scores(tulemused):
    n = int(input("Введите количество лучших результатов, которые вы хотите узнать: "))
    if n > len(tulemused):
        n = len(tulemused)
    top_scores = sorted(tulemused, reverse=True)[:n]
    print("Топ-{} результатов:".format(n))
    for i in range(n):
        print("{}. {}".format(i+1, top_scores[i]))


def sort_scores(sportlased, tulemused):    
    n = len(tulemused) #Функция len показывает кол-во элементов. Длинну.
    for i in range(n):
        for j in range(0, n-i-1): #0 начальная цифра. От чего будет отсчет. n-i-1 это до чего оно должно дойти.
            #Цикл будет повторяться n-i-1 раз для каждого значения i, которое определяется во внешнем цикле,
            #Значение j будет изменяться в каждой итерации цикла в соответствии с заданным диапазоном значений range().
            if tulemused[j] > tulemused[j+1]: # Перестановка элементов
                tulemused[j], tulemused[j+1] = tulemused[j+1], tulemused[j] 
                sportlased[j], sportlased[j+1] = sportlased[j+1], sportlased[j]
    for i in range(n): # Вывод информации о каждом спортсмене, его баллах и месте
        print(f"{i+1}. {sportlased[i]} - {tulemused[i]} punkti")


def found_scores(sportlased, tulemused): 
    names = input("Введите имена спортсменов через запятую: ")
    names_list = names.split(",")
    for name in names_list:
        if name in sportlased:
            index = sportlased.index(name)
            print("{} - {} баллов".format(name, tulemused[index]))
        else:
            print("{} не найден".format(name))


def sort_scores_убывание(sportlased, tulemused):
    n = len(tulemused) #Функция len показывает кол-во элементов. Длинну.
    for i in range(n):
        for j in range(0, n-i-1): #0 начальная цифра. От чего будет отсчет. n-i-1 это до чего оно должно дойти.
            #Цикл будет повторяться n-i-1 раз для каждого значения i, которое определяется во внешнем цикле,
            #Значение j будет изменяться в каждой итерации цикла в соответствии с заданным диапазоном значений range().
            if tulemused[j] < tulemused[j+1]: # Перестановка элементов
                tulemused[j], tulemused[j+1] = tulemused[j+1], tulemused[j] 
                sportlased[j], sportlased[j+1] = sportlased[j+1], sportlased[j]
    for i in range(n): # Вывод информации о каждом спортсмене, его баллах и месте
        print(f"{i+1}. {sportlased[i]} - {tulemused[i]} punkti")

def remove(sportlased, tulemused):
    kriteerium = int(input("Введите критерий (кол-во баллов): "))
    for i in range(len(tulemused)-1, -1, -1):
        if tulemused[i] < kriteerium:
            del sportlased[i]
            del tulemused[i]
    print("Sportlased, чьи результаты не дисквалифицированы: ", sportlased)
    print("Их результаты: ", tulemused)
