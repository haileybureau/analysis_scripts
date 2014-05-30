#!/usr/bin/python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import *
from matplotlib import rcParams

#_________________RYAN_______________#
#you should only have to change the file name in the x,y variable
#you'll need to change the x and y axis limits 
#________________RYAN________________#

#with open("res10-d.dat") as f:
#    data = f.readlines()

#data = data.split('\n')
'''
x = []
y = []
for row in data:
    tmp=row.split()
    print tmp
    x.append(float(tmp[0]))
    y.append(float(tmp[1]))
'''
#x = [row.split(' ')[0] for row in data]
#print x
##exit()

#y = [row.split(' ')[1] for row in data]

# FONTSIZE xx-small,x-small,small,medium,large,x-large,xx-large
fpropxxl=matplotlib.font_manager.FontProperties(size='xx-large')
fpropxl=matplotlib.font_manager.FontProperties(size='x-large')
fpropl=matplotlib.font_manager.FontProperties(size='large')
fpropm=matplotlib.font_manager.FontProperties(size='medium')
#FONTFAMILY
matplotlib.rcParams['font.family']='Times New Roman'

#to not cut off bottom axes
rcParams.update({'figure.autolayout': True})

x, y = np.loadtxt('pmf_NAMD_DANVT_vac_v1_n100_asmd.dat', unpack=True)
a, b = np.loadtxt('pmf_NAMD_DANVT_imp_v1_n100_asmd.dat', unpack=True)
c, d = np.loadtxt('pmf_NAMD_DANVT_exp_v1_n100_asmd.dat', unpack=True)
#e, f = np.loadtxt('cor_pmf_NAMD_DANVT_exp_v100_n100_asmd9st.dat', unpack=True)
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
ax3 = fig.add_subplot(111)
#ax4 = fig.add_subplot(111)
#exit()
#ax1.set_title("Plot title...")    
ax1.set_xlabel(('end-to-end distance ($\AA$)'),fontproperties=fpropl)
ax1.set_ylabel(('PMF (kcal/mol)'),fontproperties=fpropl)

plt.yticks((0,5,10,15,20,25),fontproperties=fpropm)
plt.xticks((15,20,25,30),fontproperties=fpropm)
plt.ylim([-3,26])                 # manually define
plt.xlim([12,34])

ax1.plot(x,y, 'r--',linewidth = 3.0,label='vacuum 100 tps')
ax2.plot(a,b, 'k--', linewidth = 3.0,label='implicit 100 tps')
ax3.plot(c,d, 'b--',linewidth = 3.0,label='explicit 100 tps')
#ax4.plot(e,f,'g--', label='9 stages')
leg = ax1.legend(loc=2,prop={'size':10})
leg = ax2.legend(loc=2,prop={'size':10})
leg = ax3.legend(loc=2,prop={'size':10})
#leg = ax4.legend(loc=4)
#plt.legend(loc='upper left',prop={'size':10})
#leg = plt.gca().get_legend()
leg.draw_frame(False)

fig.set_size_inches(6.3,3.9)
plt.draw()
plt.savefig('mixed_vie_final.eps')
plt.savefig('mixed_vie_final.png')
plt.savefig('mixed_vie_final.svg')
#plt.show()
