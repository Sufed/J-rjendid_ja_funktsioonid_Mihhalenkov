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
        print("6. Выйти")
        valik = int(input("Сделайте выбор (1-6): "))
        if valik == 1:
            nimi = input("Введите имя спортсмена: ")
            sportlased.append(nimi)
            tulemus = []
            for i in range(3):
                tulemus.append(random.randint(1, 100))
            parim_tulemus = max(tulemus)
            tulemused.append(parim_tulemus)
        elif valik == 2:
            n = int(input("Введите, сколько лучших результатов показать: "))
            show_top_scores(tulemused)
        elif valik == 3:
            sort_scores(sportlased, tulemused)
        elif valik == 4:
            show_individual_scores(sportlased, tulemused)
        elif valik == 5:
            remove_below_criteria(sportlased, tulemused)
        elif valik == 6:
            break
        else:
            print("Неверный выбор")
