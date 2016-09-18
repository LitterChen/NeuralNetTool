#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
animation，动画
'''
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation    #引入动画模块

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))    #line返回是列表，所以注意加‘，’

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False) #fig,更新函数，帧数，最初的图像的函数，更新频率 x毫秒，是否更新整张图片
plt.show()
