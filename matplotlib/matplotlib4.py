#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
画图
1.坐标轴的label设置
2.标注每个点代表什么

'''

__author__ = 'Jackie Qiang'

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50) 
y1 = 2*x +1
y2 = x**2

plt.figure()
l1 = plt.plot(x, y2, label='up', linewidth=10) #可以赋给一个线条对象，同时可以添加标签
plt.ylim((-2,2))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

#读取出label
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)  #设置大小
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha= 0.7))   #设置坐标label的背景颜色，边框颜色，透明度
plt.show()
