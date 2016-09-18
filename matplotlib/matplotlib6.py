#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
plot不同的类型
1.等高线图

'''
__author__ = 'Jackie Qiang'

import matplotlib.pyplot as plt
import numpy as np

#等高线图
#高度的函数
def f(x, y):
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n= 256
x = np.linspace(-3, 3, n)   #设置多个x值
y = np.linspace(-3, 3, n)   #设置多个y值

X,Y = np.meshgrid(x, y) #定义网格

#
plt.contourf(X, Y, f(X,Y), 8, alpha=0.75, cmap=plt.cm.hot)  #等高线着色,X,Y,Z,将等高线分为几段,透明度，色相

#使用plt.contour添加等高线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
#添加标签
plt.clabel(C, inline=True, fontsize=10) #

plt.xticks(())
plt.yticks(())

#图片数据
a = np.array([0.31, 0.36, 0.42,
    0.36, 0.43, 0.52,
    0.42, 0.54, 0.65]).reshape(3, 3)

'''
关于参数‘interpolation’可以查看
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
'''

plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower') #绘图，输入数据，清晰度， ， 
plt.colorbar(shrink=0.9)  #颜色标注
plt.show()
