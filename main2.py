from matplotlib.pyplot import figure, show, cm
from numpy import arange
from numpy.random import rand
import pandas

df1 = pandas.read_csv("QAC3.csv")

def gbar(ax, x, y, width=0.5, bottom=0):
    X = [[.6, .6], [.7, .7]]
    for left, top in zip(x, y):
        right = left + width
        ax.imshow(X, interpolation='bicubic', cmap=cm.copper,
                  extent=(left, right, bottom, top), alpha=1)

fig = figure()

xmin, xmax = xlim = 0, 10
ymin, ymax = ylim = 0, 1
ax = fig.add_subplot(111, xlim=xlim, ylim=ylim,
                     autoscale_on=False)
X = [[.6, .6], [.17, 1.7]]

ax.imshow(X, interpolation='bicubic', cmap=cm.Greens,
          extent=(xmin, xmax, ymin, ymax), alpha=1)

y = df1["Group"]
x = df1["Log"]
gbar(ax, x, y, width=0.7)
ax.set_aspect('auto')
show()