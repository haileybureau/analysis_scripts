#!/usr/bin/python

## Author: Hailey Bureau 
## Latest edits: 28 May 2014

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import *
from matplotlib import rcParams

# FONTSIZE xx-small,x-small,small,medium,large,x-large,xx-large
fpropxxl=matplotlib.font_manager.FontProperties(size='xx-large')
fpropxl=matplotlib.font_manager.FontProperties(size='x-large')
fpropl=matplotlib.font_manager.FontProperties(size='large')
fpropm=matplotlib.font_manager.FontProperties(size='medium')
#FONTFAMILY
matplotlib.rcParams['font.family']='Times New Roman'

#to not cut off bottom axes
rcParams.update({'figure.autolayout': True})

filename=raw_input('What file would you like to plot? (Ex: 1residue.txt):  ')
residue,sasa_value,frame = np.loadtxt(filename, usecols=(0,1,2),unpack=True)
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_ylabel(('SASA ($\AA^2$)'),fontproperties=fpropl)
ax1.set_xlabel(('Frame number'), fontproperties=fpropl)
plt.title('Implicit SASA values per residue')
#plt.yticks((0,50,100,150,200,250),fontproperties=fpropm)
#plt.xticks((0,100,200,300,400,500,600,700,800,900,1000),fontproperties=fpropm)
#plt.ylim([0,250])                 # manually define
#plt.xlim([0,1000])

ax1.plot(frame,sasa_value,'r-',linewidth = 0.5)
#plt.legend(loc='upper left',prop={'size':10})
#leg = plt.gca().get_legend()
#leg.draw_frame(False)

fig.set_size_inches(6.3,3.9)
plt.draw()
figname=raw_input('What would you like the figure filename to be? (Ex: 1res.eps) ')
plt.savefig(figname)
