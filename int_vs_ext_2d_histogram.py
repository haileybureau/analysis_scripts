#!/usr/bin/env python
#
#author: Hailey Bureau
#latest edits: 20 May 2014
#
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import *
from matplotlib import rcParams
from matplotlib.colors import LogNorm

# FONTSIZE xx-small,x-small,small,medium,large,x-large,xx-large
fpropxxl=matplotlib.font_manager.FontProperties(size='xx-large')
fpropxl=matplotlib.font_manager.FontProperties(size='x-large')
fpropl=matplotlib.font_manager.FontProperties(size='large')
fpropm=matplotlib.font_manager.FontProperties(size='medium')
#FONTFAMILY
matplotlib.rcParams['font.family']='Times New Roman'

#to not cut off bottom axes
rcParams.update({'figure.autolayout': True})

#load the data using the columns
frame,pep_only,solv_pep = np.loadtxt('both_hbonds', usecols=(0,1,2), unpack=True)
#frame_number = data[0,:]
#e, f = np.loadtxt('cor_pmf_NAMD_DANVT_exp_v100_n100_asmd9st.dat', unpack=True)
fig = plt.figure()

plt.xlabel(('peptide-solvent H bonds'),fontproperties=fpropl)
plt.ylabel(('peptide H bonds'),fontproperties=fpropl)
plt.title('H bonds (explicit solvent)')
plt.ylim([0,8])                 
plt.xlim([4,37])

# Estimate the 2D histogram
H, xedges, yedges = np.histogram2d(solv_pep,pep_only,bins=(35,9))

# H needs to be rotated and flipped
H = np.rot90(H)
H = np.flipud(H)

# Mask zeros
#Hmasked = np.ma.masked_where(H==0,H) # Mask pixels with a value of zero

# Plot 2D histogram using pcolor
#H was originally Hmasked 
#cmap=cm.gnuplot changes the color scheme of the data 
#use rasterized=True to raster the data points but not the lines and text of the figure 
plt.pcolormesh(xedges,yedges,H,cmap=cm.gnuplot, rasterized=True)

#set colorbar on the side
cbar = plt.colorbar()
cbar.ax.set_ylabel('Counts')

#show()
fig.set_size_inches(6.3,3.9) #define size of figure 
plt.draw()
plt.savefig('hbonds_exp_2dhist.eps')