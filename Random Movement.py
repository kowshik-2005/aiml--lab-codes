import matplotlib.pyplot as plt
import random

def random_walk(steps):
    x, y = [0], [0]
    
    for _ in range(steps):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            y.append(y[-1] + 1)
            x.append(x[-1])
        elif direction == 'down':
            y.append(y[-1] - 1)
            x.append(x[-1])
        elif direction == 'left':
            x.append(x[-1] - 1)
            y.append(y[-1])
        elif direction == 'right':
            x.append(x[-1] + 1)
            y.append(y[-1])

    plt.plot(x, y)
    plt.title("Random Movement")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

random_walk(100)
