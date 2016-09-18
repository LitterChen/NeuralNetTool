#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
画图
1.坐标轴设置
2.改变坐标轴的方式

'''

__author__ = 'Jackie Qiang'

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50) 
y1 = 2*x +1
y2 = x**2

plt.figure()   
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1, 2))    #x轴的取值范围
plt.ylim((-2,3))    #y轴的取值范围
plt.xlabel('a\sdf')
plt.ylabel('i am y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)   #修改角标，范围从-1到2.共有5个点
plt.yticks([-2, -1.8, -1, 1.22, 3,],
    [r'$really\ bad$', r'$bad\ \alpha$', 'normal', 'good', 'really good']) #修改y轴的角标

#gca = 'get current axis'
ax =plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0)) # outward, axis
ax.spines['left'].set_position(('data', 0))

plt.show()
