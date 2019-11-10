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

import numpy as np
from scipy.stats import gamma
from matplotlib import pyplot as plt
# Gamma分布（Gamma Distribution）

# 例子
# alpha_values = [1, 2, 3, 3, 3]
# beta_values = [0.5, 0.5, 0.5, 1, 2]
# color = ['b', 'r', 'g', 'y', 'm']

labels = ['3K', '6K', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K', '90K', '100K']

font1 = {'family': 'Times New Roman',

         'weight': 'normal',

         'size': 30, }

# 112#参数
# alpha_values = [0.235, 0.276, 0.992, 0.827, 0.961, 1.074, 0.806, 0.696, 0.788, 0.774, 0.779, 0.969]
# beta_values = [1/14.35, 1/11.53, 1/20.44, 1/17.89, 1/19.13, 1/19.11, 1/16.59, 1/16.28, 1/16.38, 1/16.82, 1/16.63, 1/18.22]

# 113#参数
alpha_values = [1.512, 1.641, 1.719, 0.503, 0.637, 0.733, 0.802, 0.804, 0.761, 0.75, 0.797, 0.769]
beta_values = [1/302.9, 1/248.1, 1/224.9, 1/13.58, 1/15.1, 1/14.71, 1/16.12, 1/15.95, 1/15.66, 1/15.76, 1/15.46, 1/14.88]
color = ['b', 'r', 'g', 'y', 'm', 'darkcyan', 'darkorange', 'coral', 'orchid', 'goldenrod', 'olive', 'violet']
x = np.linspace(0.02, 1, 1000)

fig, ax = plt.subplots(figsize=(12, 10))
i = 0
for k, t, c in zip(alpha_values, beta_values, color):
    dist = gamma(k, 0, t)
    l1 = plt.plot(x, dist.pdf(x), linewidth=3, c=c, label=labels[i])
    plt.legend(loc='upper right', prop=font1)
    i += 1
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.xlim(0.02, 1)
plt.ylim(0, 15)

plt.xlabel('$x$', fontsize=25)
plt.ylabel(r'$p(x|\alpha,\beta)$', fontsize=25)
plt.title('3.3mm-Gamma Distribution', fontsize=30)

plt.legend(loc=0)
plt.show()
