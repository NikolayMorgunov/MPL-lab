import csv
import matplotlib.pyplot as plt
from collections import defaultdict

with open('data3.csv', 'r') as f:
    reader = list(csv.reader(f, delimiter=';', quotechar='\n'))
    # по преподавателям
    preps = set()
    for i in reader:
        preps.add(i[0])

    preps = sorted(list(preps))
    marks = [[0 for j in range(len(preps))] for i in range(10)]
    mark_exist = [False] * 10

    for i in reader:
        marks[int(i[2]) - 1][preps.index(i[0])] += 1
        mark_exist[int(i[2]) - 1] = True

    for i in range(10):
        if mark_exist[i]:
            first_mark = i + 1
            break

    marks_to_draw = dict()
    for i in range(10):
        if mark_exist[i]:
            marks_to_draw[i + 1] = marks[i]

    fig, axs = plt.subplots(2, 1)
    a = [0 for i in range(len(preps))]
    for i in marks_to_draw.keys():
        if i == first_mark:
            axs[0].bar(preps, marks_to_draw[i])
        else:
            axs[0].bar(preps, marks_to_draw[i], bottom=a)
        for j in range(len(preps)):
            a[j] += marks_to_draw[i][j]
    axs[0].legend([str(i) for i in marks_to_draw.keys()])
    axs[0].set_title("Marks per prep")
    # по группам
    groups = set()
    for i in reader:
        groups.add(i[1])
    groups = sorted(list(groups))
    marks = [[0 for j in range(len(groups))] for i in range(10)]
    mark_exist = [False] * 10

    for i in reader:
        marks[int(i[2]) - 1][groups.index(i[1])] += 1
        mark_exist[int(i[2]) - 1] = True

    for i in range(10):
        if mark_exist[i]:
            first_mark = i + 1
            break

    marks_to_draw = dict()
    for i in range(10):
        if mark_exist[i]:
            marks_to_draw[i + 1] = marks[i]


    a = [0 for i in range(len(groups))]
    for i in marks_to_draw.keys():
        if i == first_mark:
            axs[1].bar(groups, marks_to_draw[i])
        else:
            axs[1].bar(groups, marks_to_draw[i], bottom=a)
        for j in range(len(groups)):
            a[j] += marks_to_draw[i][j]
    axs[1].legend([str(i) for i in marks_to_draw.keys()])
    axs[1].set_title("Marks per group")

    # статистика

    preps = defaultdict(list)
    groups = defaultdict(list)
    for i in reader:
        preps[i[0]].append(int(i[2]))
        groups[i[1]].append(int(i[2]))

    preps_avr = dict()
    for i in preps.items():
        preps_avr[i[0]] = sum(i[1])/len(i[1])
        groups_avr = dict()
    for i in groups.items():
        groups_avr[i[0]] = sum(i[1])/len(i[1])

    print("Самый халявный препод:", max(preps_avr.items(), key=lambda i: i[1])[0])
    print("Самый нехалявный препод:", min(preps_avr.items(), key=lambda i: i[1])[0])
    print()
    print("Самая трудолюбивая группа:", max(groups_avr.items(), key=lambda i: i[1])[0])
    print("Самая раздолбайская группа:", min(groups_avr.items(), key=lambda i: i[1])[0])

    plt.show()
