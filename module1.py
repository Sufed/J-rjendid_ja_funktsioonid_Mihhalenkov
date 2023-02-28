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
        print("1. Добавить спортсмена")
        print("2. Узнать n лучших результатов")
        print("3. Упорядочить результаты в порядке возрастания баллов.")
        print("4. Найти результат(ы) спортсмена")
        print("5. Дисквалифицировать спортсменов")
        print("0. Свой вариант")
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
        elif valik == 6:
            break
        else:
            print("Неверный выбор")



#Код снизу будет изменятся т.к. я не знаю как его объяснять, но он работает.    
def generate_scores(tulemused):
    for i in range(len(tulemused)):
        score1 = random.randint(0, 100)
        score2 = random.randint(0, 100)
        score3 = random.randint(0, 100)
        max_score = max(score1, score2, score3)
        tulemused[i] = max_score

def show_top_scores(tulemused):
    n = int(input("Введите количество лучших результатов, которые вы хотите узнать: "))
    if n > len(tulemused):
        n = len(tulemused)
    top_scores = sorted(tulemused, reverse=True)[:n]
    print("Топ-{} результатов:".format(n))
    for i in range(n):
        print("{}. {}".format(i+1, top_scores[i]))

def sort_scores(sportlased, tulemused):
    tuples = [(sportlased[i], tulemused[i]) for i in range(len(sportlased))]
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    print("Отсортированный список:")
    for i in range(len(sorted_tuples)):
        print("{}. {} - {} баллов".format(i+1, sorted_tuples[i][0], sorted_tuples[i][1]))

def found_scores(sportlased, tulemused):
    names = input("Введите имена спортсменов через запятую: ")
    names_list = names.split(",")
    for name in names_list:
        if name in sportlased:
            index = sportlased.index(name)
            print("{} - {} баллов".format(name, tulemused[index]))
        else:
            print("{} не найден".format(name))

def remove(sportlased, tulemused):
    criteria = int(input("Введите критерий: "))
    new_sportlased = []
    new_tulemused = []
    for i in range(len(sportlased)):
        if tulemused[i] >= criteria:
            new_sportlased.append(sportlased[i])
            new_tulemused.append(tulemused[i])
            print("Удалены спортсмены с результатами хуже {} баллов".format(criteria))
            for i in range(len(new_sportlased)):
                print("{} - {} баллов".format(new_sportlased[i], new_tulemused[i]))
                sportlased.clear()
                tulemused.clear()
                sportlased.extend(new_sportlased)
                tulemused.extend(new_tulemused)
