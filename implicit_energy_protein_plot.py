#!/usr/bin/python
#
#author: Hailey Bureau 
#latest edits: 2 May 2014
#

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import *
from matplotlib import rcParams

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

data = np.loadtxt('implicit_energy_protein_notitles', unpack=True)
frame_number = data[0,:]
time = data[1,:]
bond = data[2,:]
angle = data[3,:]
dihedral = data[4,:]
improper = data[5,:]
electrostatic = data[6,:]
vdw = data[7,:]
conformational = data[8,:]
nonbonded = data[9,:]
total_energy = data[10,:]
#print 'total_energy', total_energy
#exit() 
#a, b = np.loadtxt('pmf_NAMD_DANVT_imp_v1_n100_asmd.dat', unpack=True)
#c, d = np.loadtxt('pmf_NAMD_DANVT_exp_v1_n100_asmd.dat', unpack=True)
#e, f = np.loadtxt('cor_pmf_NAMD_DANVT_exp_v100_n100_asmd9st.dat', unpack=True)
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
#ax3 = fig.add_subplot(111)
#ax4 = fig.add_subplot(111)
#exit()
#ax1.set_title("Plot title...")    
ax1.set_xlabel(('Frame number'),fontproperties=fpropl)
ax1.set_ylabel(('Energy (kcal/mol)'),fontproperties=fpropl)

plt.title('Implicit solvent protein only')
plt.yticks((0,50,100,150,200,250),fontproperties=fpropm)
plt.xticks((0,100,200,300,400,500,600,700,800,900,1000),fontproperties=fpropm)
plt.ylim([0,250])                 # manually define
plt.xlim([0,1000])

ax1.plot(time,total_energy,'r-',linewidth = 0.5,label='Total Energy')
ax2.plot(time, electrostatic, 'k-', linewidth = 0.5,label='Electrostatic')
#ax3.plot(time,d, 'b--',linewidth = 3.0,label='explicit 100 tps')
#ax4.plot(e,f,'g--', label='9 stages')
leg = ax1.legend(loc=2,prop={'size':10})
#leg = ax2.legend(loc=2,prop={'size':10})
#leg = ax3.legend(loc=2,prop={'size':10})
#leg = ax4.legend(loc=4)
#plt.legend(loc='upper left',prop={'size':10})
#leg = plt.gca().get_legend()
leg.draw_frame(False)

fig.set_size_inches(6.3,3.9)
plt.draw()
plt.savefig('energies_implicit_protein.eps')
#plt.savefig('mixed_vie_final.png')
#plt.savefig('mixed_vie_final.svg')
#plt.show()
