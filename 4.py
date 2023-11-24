import numpy as np
from numpy import sin, cos, arctan, sqrt
import matplotlib.pyplot as plt
import matplotlib.widgets as w

plt.ion()
fig, ax = plt.subplots(2,1, figsize=(8, 1), label="Волна 1")
fig1, ax1 = plt.subplots(2, 1, figsize=(8, 1), label="Волна 2")
fig2, ax2 = plt.subplots()
t = np.linspace(1, 200)
frSl1 = w.Slider(ax[0], "Частоста", 0, 100)
ampSl1 = w.Slider(ax[1], "Амплитуда", 0, 100)
freSl2 = w.Slider(ax1[0], "Частоста", 0, 100)
ampSl2 = w.Slider(ax1[1], "Амплитуда", 0, 100)


def fi(freq1, amp1, freq2, amp2, t):
    return arctan((amp1 * sin(freq1 * t) + amp2 * sin(freq2 * t))/(amp1 * cos(freq1 * t) + amp2 * cos(freq2 * t)))


def amp(freq1, amp1, freq2, amp2, t):
    return sqrt((amp1 ** 2) + (amp2 ** 2) + amp1 * amp2 * 2 * cos((freq2 - freq1) * t))


def sum_v(freq1, amp1, freq2, amp2, ta):
    temp = []
    for i in ta:
        temp.append(amp(freq1, amp1, freq2, amp2, i) * sin(fi(freq1, amp1, freq2, amp2, i)))
    return np.array(temp)


while True:
    ax2.cla()
    ax2.plot(t, sum_v(frSl1.val, ampSl1.val, freSl2.val, ampSl2.val, t))
    plt.draw()
    plt.gcf().canvas.flush_events()
