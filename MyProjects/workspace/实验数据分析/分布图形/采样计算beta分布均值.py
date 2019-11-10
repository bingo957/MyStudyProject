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
均值 E（x）= α /（α+β）
"""
import numpy as np
import numpy.random as nprnd
import scipy.stats as spstat
import matplotlib.pyplot as plt

# Beta 分布的平均数
N = (np.arange(200) + 3) ** 2 * 20

betamean = np.zeros_like(N, dtype=np.float64)
for idx, i in enumerate(N):
    betamean[idx] = np.mean(nprnd.beta(2, 1, i))

plt.plot(N, betamean, color='steelblue', lw=2)
plt.xscale('log')
plt.show()

print(spstat.beta(2, 1).mean(), 2.0 / (2 + 1))
