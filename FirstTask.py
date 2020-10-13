# coding: utf-8

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

x = np.arange(0, 1, 0.02)
s = ((6*x-2)**2 * np.sin(12*x-4))

i=0
while i<=49:
        print("%.1f    %.1f"%(x[i],s[i]))
        i+=1
fig, ax = plt.subplots()
ax.plot(x, s,'r')

ax.set(xlabel='(x)', ylabel='(y)',
       title='График заданной функции')
ax.grid()

newpath = r'C:\result'
if not os.path.exists(newpath):
        os.mkdir(newpath)
fig.savefig(r"C:\result\result.png")
plt.show()

