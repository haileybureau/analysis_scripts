#!/usr/bin/env python
import sys,os,fnmatch,itertools,pickle,re
import os.path,datetime,time
from glob import glob
import numpy as np
from random import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import *
from matplotlib import rcParams

my_dir = os.path.abspath(os.path.dirname(__file__))

count = 0
for path in glob(os.path.join(my_dir,'*-sfwf.pkl*')):
    count +=1
num = str(count).zfill(2)
if '00' == num:
    print num,'no data acquired'
    sys.exit()

# load AsmdMethod_solv_vel_stage.pkl
# ex.: AsmdMethod_vac_02_10.pkl
solvent = my_dir.split('/')[-2].split('.')[1]
vel_dir = my_dir.split('/')[-1]
total_stages = '10'
asmd_pkl_name = 'AsmdMethod_%s_%s_%s.pkl' % (solvent,vel_dir,total_stages)
dir_loc_AsmdMethod_pkl = '/'.join(my_dir.split('/')[0:-2])
asmd_pkl = os.path.join(dir_loc_AsmdMethod_pkl,asmd_pkl_name)
sys.path.append(dir_loc_AsmdMethod_pkl)
from asmd.asmdwork import *
c_asmd = pickle.load(open(asmd_pkl,'r'))

print dir(c_asmd)

vel  = c_asmd.v
dist = c_asmd.dist
ts   = c_asmd.ts
path_seg   = c_asmd.path_seg
path_svel  = c_asmd.path_svel
path_vel   = c_asmd.path_vel
path_steps = c_asmd.path_steps
dt         = c_asmd.dt
path_v_aps = c_asmd.pv_aps
domain     = np.cumsum(((path_steps*ts)/1000)*path_v_aps)

print vel
print dist
print ts
print path_seg
print path_svel
print path_vel
print path_steps
print dt
print path_v_aps
print domain

spos=13.0
kb  =-0.001987
temp=300
beta=1/(kb*temp) # 1/kb*T
quota=100*1
quota = []

#_____________________________________________________________________________
def pack(stage):
    seed_bond={}
    wght_bond={}
    wrk_pkl={}
    wrk_pkl=pickle.load(open('%s-sfwf.pkl' % stage,'rb'))
    for path in glob(os.path.join(my_dir,'%s/*/*-hb_pr*pr*.pkl.*' % stage)):
        seed = path.split('.')[-1]
        sample_i = pickle.load(open(path,'rb'))
        bond_clist=[]
        for i in range(len(sample_i)):
            cnt = len(sample_i[i])
            bond_clist.append(cnt)
        seed_bond[seed]=np.array(bond_clist)
    seeds = wrk_pkl[stage].keys()
    for s in seeds:
        sample_w = np.exp(wrk_pkl[stage][s][1][::,3]*beta).astype(float)
        sample_b = (seed_bond[s]).astype(float)
        lenf_w = len(sample_w)/100
        lenf_b = len(sample_b)/100
        print lenf_w,lenf_b
        B_list=[]
        W_list=[]
        for b in range(len(sample_b)):
            wv = int(((b+1)/lenf_b)*lenf_w)
            sum_B=(sample_b[b]*np.exp(beta*sample_w[wv]))
            sum_W=(np.exp(beta*sample_w[wv]))
            print sum_B,sum_W
            B_list.append(sum_B)
            W_list.append(sum_W)
        avg_B=np.array(B_list).cumsum()/np.array(W_list).cumsum()
        wght_bond[s]=avg_B
        #plot_hb_bluedot(avg_B[::2],stage,'b.',0.1)
    wb_vecs = np.array(wght_bond.values()).mean(axis=0)
    plot_hb(wb_vecs,stage,'k-',2)
    print type(wb_vecs)
    print len(wb_vecs)
#____________________________________________________________________________
def iter_pickle(filename):
    with open(filename) as fp:
        while True:
            try:
                entry = pickle.load(fp)
            except EOFError:
                break
            yield entry

def find_seed(seq,seed):
    for dct in seq:
        if dct['seed']==seed:
            return dct
#____________________________________________________________________________
def plot_pkl(stage,sel,acc_d,acc_b,index=0,color='k-',b_label='hydrogen bonds'):
    phase=int(stage)-1
    def residue_index(label):
        return int(re.sub("[^0-9]","",label))
    def charac_bond2(trajectory,distance_target):
        acc_count_frames = []
        for frame in trajectory:
            acc_count = 0
            for bond in frame:
                distance = residue_index(bond[2])-residue_index(bond[3])
                if distance == distance_target:
                    acc_count += 1
            acc_count_frames.append(acc_count)
        return acc_count_frames
    #_________________________________________________________________________
    if sel != 'ihb':     # sel ==  'wp', 'hb'
        dct_sd_hb={}
        pfile = '%s-sd_%s.pkl' %(stage,sel)     # pkl: sd_hb or sd_wp
        for hb_seq in iter_pickle(pfile):
            dct_sd_hb.update(hb_seq)
        seeds = dct_sd_hb.keys()
        print seeds
        quota.append(len(seeds))
        acclens=[]
        for s in seeds:
            acc=[]
            sample_i = dct_sd_hb[s]  # trajectory,dcd-length list with
            for c in range(len(sample_i[0])):     # width of bonds per frame
                hbc=len(sample_i[0][c]) # hbc-hydrogen-bond-count, 1 frame
                acc.append(hbc)      # acc: counts over full trajectory
            acclens.append(acc)      # acclens: all trajectories
        data = np.array(acclens).mean(axis=0)
        if stage=='01':
            d = np.linspace(spos,spos+domain[phase],data.shape[0])
        elif stage !='01':
            d = np.linspace(spos+domain[phase-1],spos+domain[phase],data.shape[0])
        # establish domain, by linspacing - vector same length as data(frames)
        acc_d.append(d)              # acc_d.append(d[2:-2])
        acc_b.append(data)           # acc_b.append(data[2:-2])
    else: # sel == 'ihb'
        pfile = '%s-sd_%s.pkl' %(stage,sel[1:3])
        dct_sd_hb={}
        for hb_seq in iter_pickle(pfile):
            dct_sd_hb.update(hb_seq)
        seeds = dct_sd_hb.keys()
        print seeds
        quota.append(len(seeds))
        b_data = np.array([[charac_bond2(dct_sd_hb[s][0],n) for s in seeds] \
                     for n in [3,4,5]])
        acc_b.append(b_data)
#_____________________________________________________________________________
def main_bond(sel,indx_clr=[(0,'k-','')]):
    # matplotlib
    fig,(ax1)=plt.subplots(1)
    plt.clf()
    subplot(111)
    # FONTSIZE
    fpropxxl=matplotlib.font_manager.FontProperties(size='xx-large')
    fpropxl=matplotlib.font_manager.FontProperties(size='x-large')
    fpropl=matplotlib.font_manager.FontProperties(size='large')
    fpropm=matplotlib.font_manager.FontProperties(size='medium')
    rcParams.update({'figure.autolayout':True})

    #FONTFAMILY
    matplotlib.rcParams['font.family']='Times New Roman'
    # AXES labels
    plt.xlabel('end-to-end distance ($\AA$)',fontproperties=fpropl)
    plt.ylabel('Average H-bond count',fontproperties=fpropl)
    # TICKS
    # list = [0,10,20,30]
    # plt.yticks(list,fontproperties=fpropxl)
    # plt.yticks((0,10,20,30),fontproperties=fpropxl)
    plt.yticks((0,1,2,3,4,5,6),fontproperties=fpropl)
    plt.xticks((15,20,25,30),fontproperties=fpropl)
    plt.xlim([spos,spos+dist])
    #plt.ylim([-.1,6.5])
    # sub calls - list dirs 01,02, ... 10; call plot_pkl
    dirs = []
    for i in range(1,int(num)+1):
        dirs.append(str(i).zfill(2))
    acc_domain=[]
    acc_bond  =[]
    sel = 'hb'
    #else: # 'hb','wp'
    if sel == 'hb':
        [plot_pkl(st,sel,acc_domain,acc_bond,indx_clr[0][0],indx_clr[0][1],\
                   ) for st in sorted(dirs)]
        print acc_bond[0].shape
        acc_count_traj = []
        for ab in acc_bond:
            print ab.shape
            acc_count_traj.append(ab.shape[0])
        min_val = min(acc_count_traj)
        print type(min_val),'min_val',min_val
        acc_count_trim_traj = []
        for ab in acc_bond:
            print ab.shape
            b = ab[:min_val]
            print b.shape
            acc_count_trim_traj.append(b)
        bnd2 = np.concatenate(acc_bond,axis=0)
        y_d = len(bnd2)/100
        ext2 = np.linspace(spos,spos+dist,bnd2.shape[0])
        x_d = len(ext2)/100
        #plt.plot(ext2[::x_d],bnd2[::y_d],'k-',linewidth=1.0,label='hydrogen bonds')
    ####
    acc_domain=[]
    acc_bond  =[]
    sel = 'ihb'
    if sel == 'ihb':
        [plot_pkl(st,sel,acc_domain,acc_bond,indx_clr[0][0],indx_clr[0][1],\
                  indx_clr[0][2]) for st in sorted(dirs)]
        print acc_bond[0].shape
        acc_count_traj = []
        for ab in acc_bond:
            print ab.shape
            print ab.shape[1]
            acc_count_traj.append(ab.shape[1])
        min_val = min(acc_count_traj)
        print type(min_val),'min_val',min_val
        acc_count_trim_traj = []
        for ab in acc_bond:
            b = ab[:,:min_val,:]
            print b.shape
            acc_count_trim_traj.append(b)
        bnd = np.concatenate(acc_count_trim_traj,axis=2)
        y_d = bnd.shape[2]/100
        ext = np.linspace(spos,spos+dist,bnd.shape[2])
        x_d = len(ext)/100
        print bnd.shape,'x',x_d,'y',y_d
        
        #plt.errorbar(ext[::x_d],bnd[0,::,::y_d].mean(axis=0), yerr=bnd[0,::,::y_d].std(axis=0))
        for i in range(len(bnd[0,::,::y_d])):
            if i == 0:
                plt.plot(ext[::x_d],bnd[0,::,::y_d][i], 'r:',linewidth=0.5)#, label=r"i$\rightarrow$i+3")	
                plt.plot(ext[::x_d],bnd[1,::,::y_d][i], 'b:',linewidth=0.5)#, label=r"i$\rightarrow$i+4")
                plt.plot(ext[::x_d],bnd[2,::,::y_d][i], 'g:',linewidth=0.5)#, label=r"i$\rightarrow$i+5")
            else:
                plt.plot(ext[::x_d],bnd[0,::,::y_d][i], 'r:',linewidth=0.5) 
                plt.plot(ext[::x_d],bnd[1,::,::y_d][i], 'b:',linewidth=0.5)
                plt.plot(ext[::x_d],bnd[2,::,::y_d][i], 'g:',linewidth=0.5)
        #print "SASHA "+ str(len(bnd[0,::,::y_d]))
        plt.plot(ext[::x_d],bnd[0,::,::y_d].mean(axis=0),'w-',linewidth=4.0)#label=r"i$\rightarrow$i+3")
        # ,'r-',linewidth=1.0, label=r"i$\rightarrow$i+3"
        plt.plot(ext[::x_d],bnd[1,::,::y_d].mean(axis=0),'w-',linewidth=4.0)#, \
                                              #label=r"i$\rightarrow$i+4")
        plt.plot(ext[::x_d],bnd[2,::,::y_d].mean(axis=0),'w-',linewidth=4.0)#, \
                                              #label=r"i$\rightarrow$i+5")

        plt.plot(ext[::x_d],bnd[0,::,::y_d].mean(axis=0),'r-',linewidth=1.0,label=r"i$\rightarrow$i+3")
        # ,'r-',linewidth=1.0, label=r"i$\rightarrow$i+3"
        plt.plot(ext[::x_d],bnd[1,::,::y_d].mean(axis=0),'b-',linewidth=1.0, \
                                              label=r"i$\rightarrow$i+4")
        plt.plot(ext[::x_d],bnd[2,::,::y_d].mean(axis=0),'g-',linewidth=1.0, \
                                              label=r"i$\rightarrow$i+5")

    tup_data = (ext,bnd2,bnd[0,::,::].mean(axis=0),bnd[1,::,::].mean(axis=0), \
                    bnd[2,::,::].mean(axis=0))
    bond_data = np.transpose(np.array(tup_data))
    sel = 'hb'
    # LEGEND
    plt.legend(loc='upper right',prop={'size':12})
    plt.gca().set_ylim(ymin=-0.3,ymax=6.5)
    plt.yticks((0,1,2,3,4,5,6),fontproperties=fpropl)
    #plt.xticks((15,20,25,30),fontproperties=fpropl)
    #plt.gca().set_ylim(ymax=+0.3) #doesn't seem to work, may18
    leg = plt.gca().get_legend()
    leg.draw_frame(False)

    plt.subplots_adjust(left=0.11,right=0.99,top=0.97,bottom=0.16)
    fig.set_size_inches(4.2,3.0)
    # DRAW
    plt.draw()

    lst_name=['','','','','','']
    velcode=my_dir.split('/')[-1]
    dct_vel={'01':'1000','02':'100','03':'10','04':'1','05':'p1'}
    dct_case={100:'100',150:'150',200:'200',250:'250',400:'400',600:'600',800:'800'}
    print quota
    if quota[0] > 99:
        n = dct_case.get(quota[0],dct_case[min(dct_case.keys(), \
                                 key=lambda k:abs(k-quota[0]))])
    else:
        n = str(quota[0])

    # TITLE
    #plt.title('DANVT - NAMD - ASMD \n vac 1.0 $\AA$/ns')
    lst_name[0]=('bond_NAMD_DANVT_')
    lst_name[1]=my_dir.split('/')[-2].split('.')[1]+'_'
    lst_name[2]='v'+dct_vel[velcode]+'_'
    lst_name[3]='n'+n+'_'
    if int(num) > 1:
        lst_name[4]='asmd_'
    else:
        lst_name[4]='smd_'
    lst_name[5]=sel
    print ''.join(lst_name)
    name = ''.join(lst_name)

    def save_pic_data(i,subdir,fname):
        content_dir = os.path.join('/'.join(my_dir.split('/')[0:i]),subdir)
        if not os.path.exists(content_dir): os.makedirs(content_dir)
        abs_file_name = os.path.join(content_dir,fname)
        plt.savefig('%s.png' % abs_file_name)
        plt.savefig('%s.eps' % abs_file_name)
        plt.savefig('%s.svg' % abs_file_name)
        os.chdir(content_dir)
        pickle.dump(bond_data,open('%s.pkl' % fname,'w'))
        np.savetxt('%s.dat' % fname,bond_data,fmt='%3.4f',delimiter=' ')

    # levels back, -4:beyond,-3:default,-2:count,-1:env,'':cwd
    # save_pic_data(levels_back,subdir,name)
    # example: save_pic_data(-4,'fig',name)
    save_pic_data(-3,'bond',name)
    #save_pic_data(-3,'',name)

#___main_call_'hb','wp','ihb'_________________________________________________
main_bond('hb')
#main_bond('ihb')
if my_dir.split('/')[-2].split('.')[1]=='exp':
    main_bond('wp')
