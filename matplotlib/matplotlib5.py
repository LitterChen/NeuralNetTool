#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
plot不同的类型
1.散点图
2.柱状图
'''
__author__ = 'Jackie Qiang'

import matplotlib.pyplot as plt
import numpy as np

#散点图
n=1024
X = np.random.normal(0, 1, n)   #设置多个x值
Y = np.random.normal(0, 1, n)   #设置多个y值
T = np.arctan2(Y, X)    #为了颜色变化

plt.scatter(X, Y, s=75, c=T, alpha=0.5) #x值，y值，尺寸， 颜色，透明度
plt.scatter(np.arange(5), np.arange(5)) #设置图片


plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
plt.xticks(())
plt.yticks(())

#柱状图
n = 12  #柱状图的个数
X = np.arange(n)
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')    #X,Y,背景色，边框色
plt.bar(X,-Y2,facecolor='#ff9900',edgecolor='white')

for x,y in zip(X,Y1):
    #ha:horizontal alignment 对齐方式
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x,y in zip(X,Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.xlim((-.5, n))
plt.ylim((-1.25, 1.25))
plt.xticks(())
plt.yticks(())
plt.show()
