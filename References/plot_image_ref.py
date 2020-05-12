import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('TkAgg')
%matplotlib notebook
from time import sleep

fig = plt.figure()
ax = fig.gca()
fig.show()
a=1
for i in range(10):
    fig.clf()
    plt.imshow(background, interpolation='None', alpha=a)
    a=a-0.1
    fig.canvas.draw()
    sleep(0.01)