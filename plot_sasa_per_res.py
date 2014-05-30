#!/usr/bin/python

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

data = np.loadtxt('sasa_trajectory', unpack=True)
residue1 = data[0::10]
residue2 = data[1::10]
residue3 = data[2::10]
residue4 = data[3::10]
residue5 = data[4::10]
residue6 = data[5::10]
residue7 = data[6::10]
residue8 = data[7::10]
residue9 = data[8::10]
residue10 = data[9::10]

#print 'residue9',residue9
#print 'residue10',residue10
#exit()
data2= np.loadtxt('explicit_energy_protein_notitles',unpack=True)
frame_number = data2[1,:]
#print len(frame_number)
#exit()
#bond = data[2,:]
#angle = data[3,:]
#dihedral = data[4,:]
#improper = data[5,:]
#electrostatic = data[6,:]
#vdw = data[7,:]
#conformational = data[8,:]
#nonbonded = data[9,:]
#total_energy = data[10,:]
#print 'total_energy', total_energy
#exit() 
#a, b = np.loadtxt('pmf_NAMD_DANVT_imp_v1_n100_asmd.dat', unpack=True)
#c, d = np.loadtxt('pmf_NAMD_DANVT_exp_v1_n100_asmd.dat', unpack=True)
#e, f = np.loadtxt('cor_pmf_NAMD_DANVT_exp_v100_n100_asmd9st.dat', unpack=True)
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
ax3 = fig.add_subplot(111)
ax4 = fig.add_subplot(111)
ax5 = fig.add_subplot(111)
ax6 = fig.add_subplot(111)
ax7 = fig.add_subplot(111)
ax8 = fig.add_subplot(111)
ax9 = fig.add_subplot(111)
ax10 = fig.add_subplot(111)
#exit()
#ax1.set_title("Plot title...")    
ax1.set_xlabel(('Frame number'),fontproperties=fpropl)
ax1.set_ylabel(('SASA ($\AA^2$)'),fontproperties=fpropl)

plt.title('Explicit SASA values per residue')
#plt.yticks((0,50,100,150,200,250),fontproperties=fpropm)
#plt.xticks((0,100,200,300,400,500,600,700,800,900,1000),fontproperties=fpropm)
#plt.ylim([0,250])                 # manually define
#plt.xlim([0,1000])

ax1.plot(frame_number,residue1,'r-',linewidth = 0.5,label='residue 1')
ax2.plot(frame_number, residue2, 'k-', linewidth = 0.5,label='residue 2')
ax3.plot(frame_number, residue3, 'b-',linewidth = 0.5,label='residue 3')
ax4.plot(frame_number, residue4, 'g-',linewidth = 0.5,label='residue 4')
ax5.plot(frame_number, residue5, 'y-',linewidth = 0.5,label='residue 5')
ax6.plot(frame_number, residue6, 'c-',linewidth = 0.5,label='residue 6')
ax7.plot(frame_number, residue7, 'm-',linewidth = 0.5,label='residue 7')
ax8.plot(frame_number, residue8, color='0.75', linestyle ='-',linewidth = 0.5,label='residue 8')
ax9.plot(frame_number, residue9, color='#31B404',linestyle='-',linewidth = 0.5,label='residue 9')
ax10.plot(frame_number, residue10, color='#086A87',linestyle='-',linewidth = 0.5,label='residue 10')
#ax4.plot(e,f,'g--', label='9 stages')
leg = ax1.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax2.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax3.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax4.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax5.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax6.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax7.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax8.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax9.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
leg = ax10.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.,prop={'size':10})
#legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#leg = ax4.legend(loc=4)
#plt.legend(loc='upper left',prop={'size':10})
#leg = plt.gca().get_legend()
leg.draw_frame(False)

fig.set_size_inches(6.3,3.9)
plt.draw()
plt.savefig('SASA_explicit_per_residue.eps')
#plt.savefig('mixed_vie_final.png')
#plt.savefig('mixed_vie_final.svg')
#plt.show()
