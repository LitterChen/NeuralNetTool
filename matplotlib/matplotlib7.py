#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
3D图像
1.一幅3D图像
2.多幅图像结合在一起 method1
3.多幅图像结合在一起 method2

'''
__author__ = 'Jackie Qiang'

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec

#3D绘图
fig = plt.figure()
ax = Axes3D(fig)
#X,Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)    #Z的高度值
#高度值
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))    # X, Y, Z, 黑线的密集度，黑线德 的密集度，颜色
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')   #X, Y, Z, 从那个坐标轴作投影，开始坐标，颜色

ax.set_zlim(-2, 2)

#method1 : subplot2grid
#在一个figure中显示多个图片
plt.figure()

plt.subplot(2, 1, 1)
plt.plot([0,1], [0,1])

plt.subplot(2, 3, 4)
plt.plot([0,1], [0,2])

plt.subplot(2, 3, 5)
plt.plot([0,1], [0,3])

plt.subplot(2, 3, 6)
plt.plot([0,1], [0,4])

############
plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3, rowspan=1)
ax1.plot([1,2], [1,2])
ax1.set_title('ax1')
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2, rowspan=1)
ax3 = plt.subplot2grid((3,3), (1,2), colspan=1, rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0), colspan=1, rowspan=1)
ax5 = plt.subplot2grid((3,3), (2,1), colspan=1, rowspan=1)
ax1.plot([1,2], [1,2])
ax1.set_title('ax1')

#method2 : gridspec

plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])

#method3 : easy define structure
##########################################3
f, ((ax11, ax12),(ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=False)
ax11.scatter([1, 2],[1, 2])
ax12.scatter([1, 2],[1, 2])
ax21.scatter([1, 2],[1, 2])

plt.tight_layout()
plt.show()
ax21.scatter([1, 2],[1, 2])
