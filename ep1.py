import matplotlib.pyplot as plt
import os

file_numb = input('File number = ')
with open(os.path.join('data1', f'00{file_numb}.dat'), 'r') as f:
    s = f.read().split('\n')
    n = int(s[0])
    x, y = [], []
    for i in s[1:n + 1]:
        x.append(float(i.split()[0]))
        y.append(float(i.split()[1]))
    size = [int(input('Points size = '))] * n
    plt.scatter(x, y, size)
    plt.axis('scaled')
    plt.title('Number of points: ' + str(n))
    plt.show()
