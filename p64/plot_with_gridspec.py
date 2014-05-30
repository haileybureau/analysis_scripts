#!/usr/bin/env python
import sys,os,pickle,shutil,fnmatch,itertools
import os.path,datetime,time
from glob import glob
from sys import argv
import numpy as np
from random import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import *
from matplotlib.gridspec import GridSpec

my_dir = os.path.abspath(os.path.dirname(__file__))
'''
#pmf_files = glob(os.path.join(my_dir,'pmf_*.dat'))
for f in glob(os.path.join(my_dir,'pmf_*.dat')):
    print f
    # example: asmd,400 tps,100 A/ns, implicit
    method      = f.split('_')[-1].split('.')[0]
    sample_size = f.split('_')[-2][1:]
    velocity    = f.split('_')[-3][1:]
    solvent     = f.split('_')[-4]
    print method,sample_size,velocity,solvent
'''

def plot_pmf(**kwargs):
    #for k,v in kwargs.iteritems():
    filename = 'pmf_NAMD_DANVT_%s_v%d_n%d_%s.dat' % (kwargs['solvent'], \
            kwargs['velocity'],kwargs['sample_size'],kwargs['method'])
    data = np.loadtxt(os.path.join(my_dir,filename))
    length = 30
    len_freq = data.shape[0]/length + 1
    ext = data[::len_freq,0]
    pmf = data[::len_freq,1]
    plt.plot(ext,pmf,kwargs['color_style'],linewidth=1.0,label=kwargs['label'])

# RESOURCES
# colors=['k','b','r','c','m','y','g','w']
# gray = '0.75'
# line_sty=['-','--','-.',':','.']
# line_sty=['.','^','d','p','+','-.',':','--']
# lst_colors=['k','y','c','b','r','y','g','w','0.75']
# COLOR CODE   ^^^   vvv  LINE STYLE
# lst_line_sty=['-','.',':','-.','--']

#_MATPLOTLIB_begin_____________________________________________________
gs = GridSpec(2,1,height_ratios=[4.5,2.5])
fig,(ax1,ax2)=plt.subplots(2, sharex=True,sharey=True)
plt.clf()
# FONTSIZE xx-small,x-small,small,medium,large,x-large,xx-large
fpropxxl=matplotlib.font_manager.FontProperties(size='xx-large')
fpropxl=matplotlib.font_manager.FontProperties(size='x-large')
fpropl=matplotlib.font_manager.FontProperties(size='large')
fpropm=matplotlib.font_manager.FontProperties(size='medium')
#FONTFAMILY
matplotlib.rcParams['font.family']='Times New Roman'
'''
# SUBPLOT 1
subplot(311)
#plt.xlabel('end-to-end distance ($\AA$)',fontproperties=fpropxxl)
#plt.ylabel('PMF (kcal/mol)',fontproperties=fpropxxl)
plt.yticks((0,10,20,30,40,50),fontproperties=fpropxl)
plt.xticks((15,20,25,30),fontproperties=fpropxl)
plt.ylim([-3,50])                 # manually define
plt.xlim([12.0,34.0])             # manually define
#to plot difference vels: added vel2 to variables for plot_vel
#    added differeent var (x) and in plot_pmf line use x instead
#    of v, at bottom, add vel2 to plot_vel call 
def plot_vel(vel,vel2):
    v = int(vel)
    x = int(vel2)
    #plot_pmf(**{'method':'smd','sample_size':800,'velocity':v, \
     #       'solvent':'vac','color_style':'k-','label':'SMD 800 at 10'})
    plot_pmf(**{'method':'asmd','sample_size':100,'velocity':v, \
            'solvent':'exp','color_style':'y.','label':'ASMD 100e at 100'})
    plot_pmf(**{'method':'asmd','sample_size':200,'velocity':v, \
            'solvent':'vac','color_style':'c:','label':'ASMD 200'})
    plot_pmf(**{'method':'asmd','sample_size':400,'velocity':v, \
            'solvent':'vac','color_style':'b-.','label':'ASMD 400'})
    plot_pmf(**{'method':'asmd','sample_size':400,'velocity':v, \
            'solvent':'exp','color_style':'r:','label':'ASMD 400e at 100'})
    plot_pmf(**{'method':'asmd','sample_size':800,'velocity':v, \
            'solvent':'exp','color_style':'r--','label':'ASMD 800e at 100'})
plot_vel('100','1')
# legend 1
plt.legend(loc='upper left',prop={'size':10})
leg = plt.gca().get_legend()
leg.draw_frame(False)
axis = plt.gca().yaxis.set_minor_locator(MultipleLocator(1))
plt.annotate('(a)', xy=(-10,10),
            xycoords='axes points',
            horizontalalignment='right', verticalalignment='bottom',
            fontsize=12)
'''
# SUBPLOT 2
ax2 = plt.subplot(gs[0])
#subplot(211)
#plt.xlabel('end-to-end distance ($\AA$)',fontproperties=fpropxxl)
#plt.ylabel('PMF (kcal/mol)',fontproperties=fpropxxl)
plt.yticks((0,5,10,15,20,25,30,35,40,45),fontproperties=fpropm)
plt.xticks((15,20,25,30),fontproperties=fpropm)
plt.ylim([-3,46])             # manually define
plt.xlim([12.0,34.0])           # manually define
def plot_vel(vel):
    v = int(vel)
    #plot_pmf(**{'method':'asmd','sample_size':800,'velocity':v, \
            #'solvent':'exp','color_style':'r--','label':'ASMD 800 tps'})
    #plot_pmf(**{'method':'asmd','sample_size':100,'velocity':x, \
     #       'solvent':'exp','color_style':'y.','label':'ASMD 100e at 1'})
    #plot_pmf(**{'method':'asmd','sample_size':400,'velocity':v, \
            #'solvent':'exp','color_style':'b-.','label':'ASMD 400 tps'})
    plot_pmf(**{'method':'asmd','sample_size':100,'velocity':v, \
            'solvent':'exp','color_style':'g--','label':'ASMD 100 tps'})
    plot_pmf(**{'method':'asmd','sample_size':400,'velocity':v, \
            'solvent':'exp','color_style':'b--','label':'ASMD 400 tps'})
    plot_pmf(**{'method':'asmd','sample_size':800,'velocity':v, \
            'solvent':'exp','color_style':'r--','label':'ASMD 800 tps'})
    plot_pmf(**{'method':'rsmd','sample_size':100,'velocity':v, \
            'solvent':'exp','color_style':'c--','label':'FR-ASMD 100 tps'})
plot_vel('100')
# legend 2
plt.legend(loc='upper left',prop={'size':8})
leg = plt.gca().get_legend()
leg.draw_frame(False)
axis = plt.gca().yaxis.set_minor_locator(MultipleLocator(1))
plt.annotate('(a)', xy=(-10, 10),
            xycoords='axes points',
            horizontalalignment='right', verticalalignment='bottom',
            fontsize=12)
# SUBPLOT 3
ax2 = plt.subplot(gs[1])
#subplot(212)
#plt.xlabel('end-to-end distance ($\AA$)',fontproperties=fpropxxl)
#plt.ylabel('PMF (kcal/mol)',fontproperties=fpropxxl)
plt.yticks((0,5,10,15,20,25),fontproperties=fpropm)
plt.xticks((15,20,25,30),fontproperties=fpropm)
plt.ylim([-3,26])             # manually define
plt.xlim([12.0,34.0])           # manually define
def plot_vel(vel,vel2):
    v = int(vel)
    x = int(vel2)
    #plot_pmf(**{'method':'smd','sample_size':10,'velocity':x, \
     #       'solvent':'exp','color_style':'c--','label':'FR-ASMD 100 tps'})
    plot_pmf(**{'method':'asmd','sample_size':100,'velocity':v, \
            'solvent':'exp','color_style':'g--','label':'ASMD 100 tps'})
    plot_pmf(**{'method':'asmd','sample_size':400,'velocity':v, \
            'solvent':'exp','color_style':'b--','label':'ASMD 400 tps'})
    plot_pmf(**{'method':'asmd','sample_size':800,'velocity':v, \
            'solvent':'exp','color_style':'r--','label':'ASMD 800 tps'})
    plot_pmf(**{'method':'rsmd','sample_size':100,'velocity':v, \
            'solvent':'exp','color_style':'c--','label':'FR-ASMD 100 tps'})
    plot_pmf(**{'method':'asmd','sample_size':100,'velocity':x, \
            'solvent':'exp','color_style':'k--','label':'ASMD 100 tps (1 $\AA$/ns) '})
    plot_pmf(**{'method':'smd','sample_size':10,'velocity':x, \
            'solvent':'exp','color_style':'y--','label':'SMD 10 tps (0.1 $\AA$/ns)'})
plot_vel('10','1')
# legend 3
plt.legend(loc='upper left',prop={'size':8})
leg = plt.gca().get_legend()
leg.draw_frame(False)
axis = plt.gca().yaxis.set_minor_locator(MultipleLocator(1))
plt.annotate('(b)', xy=(-10, 10),
            xycoords='axes points',
            horizontalalignment='right', verticalalignment='bottom',
            fontsize=12)
# EXTRA
fig.subplots_adjust(hspace=0)
fig.set_size_inches(4.0,7.0)
#plt.xlabel('end-to-end distance ($\AA$)',fontproperties=fpropxxl)
#plt.ylabel('PMF (kcal/mol)',fontproperties=fpropxxl)
fig.text(0.55,0.03,'end-to-end distance ($\AA$)',ha='center',va='center',fontproperties=fpropl)
fig.text(0.09,0.5,'PMF (kcal/mol)',ha='center',va='center', \
                 rotation='vertical',fontproperties=fpropl)
plt.subplots_adjust(left=0.175,right=0.90,top=0.90,bottom=0.085)
# DRAW__________________________________________________
plt.draw()
#plt.show()
#plt.savefig('test.png')
#plt.savefig('test.svg')
plt.savefig('FR-ASMDexp10and100final.png')
plt.savefig('FR-ASMDexp10and100final.svg')
plt.savefig('FR-ASMDexp10and100final.eps')
