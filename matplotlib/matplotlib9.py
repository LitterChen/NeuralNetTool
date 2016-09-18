#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
主次坐标轴
'''
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x ** 2
y2 = -1 * y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()   #镜面将y轴对应到第二个

ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1', color='g')
ax2.set_xlabel('X data')
ax2.set_ylabel('Y2', color='b')
plt.show()
