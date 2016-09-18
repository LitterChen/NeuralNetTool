#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
画图
1.画出简单函数图像
2.figure 的使用
'''

__author__ = 'Jackie Qiang'

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)  #-1到1，共50个点
y1 = 2*x +1
y2 = x**2

plt.figure(num=3, figsize=(8, 5))    #第一个figure,figure名称，figsize()长宽
plt.plot(x,y1)
plt.show()

plt.figure()    #第二个figure
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--') #颜色，线宽，线条性状
plt.show()
