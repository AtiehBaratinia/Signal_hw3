import numpy as np
import matplotlib.pyplot as plt

def ak(k):
    step = 0.001
    # calculate -3 to -2
    integral1 = 0
    # calculate -2 to -1
    t2 = np.arange(-2, -1, step)
    result2 = (t2 + 2) * np.cos(k * w * t2)
    integral2 = np.sum(result2) * step
    # calculate -1 to 1
    t3 = np.arange(-1, 1, step)
    result3 = -t3 * np.cos(k * w * t3)
    integral3 = np.sum(result3) * step
    # calculate 1 to 2
    t4 = np.arange(1, 2, step)
    result4 = (t4 - 2) * np.cos(k * w * t4)
    integral4 = np.sum(result4) * step
    # calculate 2 to 3
    integral5 = 0
    # sum of five integrals
    integral = integral1 + integral2 + integral3 + integral4 + integral5
    a = integral / 3
    return a


def bk(k):
    step = 0.001
    # calculate -3 to -2
    integral1 = 0
    # calculate -2 to -1
    t2 = np.arange(-2, -1, step)
    result2 = (t2 + 2) * np.sin(k * w * t2)
    integral2 = np.sum(result2) * step
    # calculate -1 to 1
    t3 = np.arange(-1, 1, step)
    result3 = (-t3) * np.sin(k * w * t3)
    integral3 = np.sum(result3) * step
    # calculate 1 to 2
    t4 = np.arange(1, 2, step)
    result4 = (t4 - 2) * np.sin(k * w * t4)
    integral4 = np.sum(result4) * step
    # calculate 2 to 3
    integral5 = 0
    # sum of five integrals
    integral = integral1 + integral2 + integral3 + integral4 + integral5
    b = integral / 3
    return b


if __name__ == "__main__":

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
