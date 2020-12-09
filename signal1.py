import numpy as np
import matplotlib.pyplot as plt

def ak(k):
    step = 0.001
    # calculate -3 to 0
    t1 = np.arange(-3, 0, step)
    result1 = np.cos(k*w*t1)
    integral1 = np.sum(result1) * step
    # calculate 0 to 3
    t2 = np.arange(0, 3, step)
    result2 = -1 * np.cos(k * w * t2)
    integral2 = np.sum(result2) * step
    # sum of two integrals
    integral = integral1 + integral2
    a = integral / 3
    return a


def bk(k):
    step = 0.001
    # calculate -3 to 0
    t1 = np.arange(-3, 0, step)
    result1 = np.sin(k*w*t1)
    integral1 = np.sum(result1) * step
    # calculate 0 to 3
    t2 = np.arange(0, 3, step)
    result2 = -1 * np.sin(k * w * t2)
    integral2 = np.sum(result2) * step
    # sum of two integrals
    integral = integral1 + integral2
    b = integral/3
    return b


if __name__ == "__main__":
    xt = []
    w = np.pi / 3
    time = np.arange(-3, 3, 0.005)
    for j in range(11):
        xt = []
        for t in time:
            x = 0
            for k in range(j):
                a = ak(k)
                b = bk(k)
                x += a * np.cos(k * w * t)
                x += b * np.sin(k * w * t)
            xt.append(x)
        plt.plot(time, xt)
    plt.show()
