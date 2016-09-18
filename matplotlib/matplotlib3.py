#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
画图
1.添加图例
2.标注每个点代表什么

'''

__author__ = 'Jackie Qiang'

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50) 
y1 = 2*x +1
y2 = x**2

plt.figure()   
l1 = plt.plot(x, y2, label='up') #可以赋给一个线条对象，同时可以添加标签
l2 = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
plt.xlim((-1, 2))
plt.ylim((-2,3)) 
plt.xlabel('asdf')
plt.ylabel('i am y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks) 
plt.yticks([-2, -1.8, -1, 1.22, 3,],
    [r'$really\ bad$', r'$bad\ \alpha$', 'normal', 'good', 'really good'])

plt.legend(handles=[l1, l2,], labels=['aaa','bbb'], loc='best') #画的线，标签名，位置

#标注每个点 Annotation
x0 = 0.5
y0 = 2*x0 + 1
plt.scatter(x0, y0,s=50, color='b')   #画的是点，而不是线.x坐标，y坐标，尺寸颜色
plt.plot([x0, x0],[y0, 1], 'k--', lw=2.5)

#method1
plt.annotate(r'$2x+1=%s$'%y0, xy=(x0, y0), xycoords='data',xytext=(+30,-30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
#method2
plt.text(-3.7, 3, r'$jkh$', fontdict={'size':16, 'color':'r'})
plt.show()
