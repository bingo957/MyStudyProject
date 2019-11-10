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

# Beta 分布（Beta distribution）
import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt

labels = ['3K', '6K', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K', '90K', '100K']

font1 = {'family': 'Times New Roman',

         'weight': 'normal',

         'size': 15, }

# 112# 参数
alpha_values = [0.215, 0.246, 0.895, 0.743, 0.862, 0.958, 0.718, 0.623, 0.702, 0.693, 0.696, 0.864]
beta_values = [12.9, 10.01, 17.55, 15.32, 16.3, 16.08, 14.06, 13.96, 13.88, 14.35, 14.16, 15.39]

# 113# 参数
# alpha_values = [1.499, 1.623, 1.698, 0.447, 0.568, 0.647, 0.713, 0.713, 0.675, 0.666, 0.705, 0.677]
# beta_values = [298.9, 243.9, 220.5, 11.63, 12.89, 12.33, 13.61, 13.43, 13.23, 13.35, 12.96, 12.43]

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'coral', 'darkcyan', 'goldenrod']
x = np.linspace(0.015, 1, 1002)[1:-1]

fig, ax = plt.subplots(figsize=(12, 10))
i = 0
for a, b, c in zip(alpha_values, beta_values, colors):
    dist = beta(a, b)
    plt.plot(x, dist.pdf(x), linewidth=3, c=c, label=labels[i])
    plt.legend(loc='upper right', prop=font1)
    i += 1
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.xlim(0.015, 1)
plt.ylim(0, 15)

plt.xlabel('$x$', fontsize=25)
plt.ylabel(r'$p(x|\alpha,\beta)$', fontsize=25)
plt.title('3.3mm-Beta Distribution', fontsize=30)

"""
ax.annotate('Beta(1/3,1)', xy=(0.014, 5), xytext=(0.04, 5.2),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(10,30)', xy=(0.276, 5), xytext=(0.3, 5.4),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(20,20)', xy=(0.5, 5), xytext=(0.52, 5.4),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(1,3)', xy=(0.06, 2.6), xytext=(0.07, 3.1),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(2,6)', xy=(0.256, 2.41), xytext=(0.2, 3.1),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(4,4)', xy=(0.53, 2.15), xytext=(0.45, 2.6),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(1,1)', xy=(0.8, 1), xytext=(0.7, 2),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(2,1)', xy=(0.9, 1.8), xytext=(0.75, 2.6),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
ax.annotate('Beta(2/3,2/3)', xy=(0.99, 2.4), xytext=(0.86, 2.8),
            arrowprops=dict(facecolor='black', arrowstyle='-'))
"""

# plt.legend(loc=0)
plt.show()
