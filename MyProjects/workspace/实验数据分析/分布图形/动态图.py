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



from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd

df = pd.read_csv('data.csv')
data_list = list(df['close'])
length = len(df) - 1
index_lst = []
for j in range(len(df)):
    index_lst.append(j)
fig = plt.figure()

ax1 = fig.add_subplot(1, 1, 1, xlim=(0, length - 1), ylim=(0, 5000))
line, = ax1.plot([], [], lw=2)
xdata, ydata = [], []

def run(data):
  x,y = data
  xdata.append(x)
  ydata.append(y)
  line.set_data(xdata, ydata)
  return line,

def data_gen():
  cnt = 0
  while cnt < length:
    cnt+=1
    yield cnt, data_list[cnt]

# anim1 = animation.FuncAnimation(fig, animate, init_func=init, interval=2000)
ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=1, repeat=False)
plt.show()
