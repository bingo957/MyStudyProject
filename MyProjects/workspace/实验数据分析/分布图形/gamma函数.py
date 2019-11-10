#
#                 God Bless No Bugs!
#
#                       _ooOoo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      O\  =  /O
#                   ____/`---'\____
#                 .'  \\|     |//  `.
#                /  \\|||  :  |||//  \
#               /  _||||| -:- |||||-  \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |   |
#               \  .-\__  `-`  ___/-. /
#             ___`. .'  /--.--\  `. . __
#          ."" '<  `.___\_<|>_/___.'  >'"".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `-.   \_ __\ /__ _/   .-` /  /
#    ======`-.____`-.___\_____/___.-`____.-'======
#                       `=---='
#    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# coding: utf-8 #
#  author:李斌  #

"""
Beta 分布
@date 2019-05-09
@author wangxianpeng
"""

import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 8))
# Gamma函数（Gamma function）
x = np.linspace(-1, 10, 1000)
plt.plot(x, gamma(x), ls='-', c='k', label='$\Gamma(x)$')

# (x-1)! for x = 1, 2, ..., 6
x2 = np.linspace(1, 6, 6)
y2 = np.array([1, 1, 2, 6, 24, 120])
plt.plot(x2, y2, marker='*', markersize=12, markeredgecolor='r', markerfacecolor='r', ls='', c='r', label='$(x-1)!$')

plt.title('Gamma Function')
plt.ylim(0, 25)
plt.xlim(0, 6)
plt.xlabel('$x$')
plt.ylabel('$\Gamma(x)$')

plt.legend()
plt.show()
