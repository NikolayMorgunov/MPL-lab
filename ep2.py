import matplotlib.pyplot as plt

with open('data2.txt', 'r') as f:
    s = list(filter(lambda el: el, f.read().split('\n')))
    fig, axs = plt.subplots(len(s) // 6, 3)
    n = len(s)
    min_x = float(s[0].split()[0])

    max_x = min_x
    min_y = float(s[1].split()[0])
    max_y = min_y

    for i in range(n // 2):
        x = [float(j) for j in s[2 * i].split()]
        y = [float(j) for j in s[2 * i + 1].split()]
        min_x = min(min_x, min(x))
        max_x = max(max_x, max(x))
        min_y = min(min_y, min(y))
        max_y = max(max_y, max(y))

    for i in range(n // 2):
        x = [float(j) for j in s[2 * i].split()]
        y = [float(j) for j in s[2 * i + 1].split()]
        axs[i // 3, i % 3].plot(x, y)

        axs[i // 3, i % 3].minorticks_on()
        axs[i // 3, i % 3].grid(which='major',
                                color='k',
                                linewidth=1)
        axs[i // 3, i % 3].grid(which='minor',
                                color='grey',
                                linestyle=':')

        axs[i // 3, i % 3].set_title('Frame ' + str(i + 1))
        axs[i // 3, i % 3].set_xlim((min_x, max_x))
        axs[i // 3, i % 3].set_ylim((min_y - 1, max_y + 1))

    plt.show()
