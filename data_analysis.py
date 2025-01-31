import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors 





file = 'Nemo_6670.dat'


data_names = pd.read_csv(file,delim_whitespace= True, header = 0, nrows = 1)
names = data_names.columns.delete(0)

data = pd.read_csv(file,delim_whitespace= True,names = names,skiprows=1)



M_ass = data['M_ass']
b_y = data['b-y']
age_parent_Gyr = data['age_parent']


plt.figure(figsize=(16,8)) 
plt.title('M_ass vs b-y',fontsize = 20)

min_val, max_val = min(age_parent_Gyr), max(age_parent_Gyr)


value = 0.0
intervals = [value]
starting_increment = 0.05
increment = 0.015
while (value + starting_increment)<max_val:
    value+= starting_increment
    intervals.append(np.round(value,2))
    starting_increment+= increment
intervals.append(np.round(max_val,2))

cmap = mpl.cm.gist_ncar
norm = colors.Normalize(vmin = min_val,vmax = max_val)

im = plt.scatter(b_y,-M_ass,c = age_parent_Gyr,s = 5,cmap = cmap,norm = norm)

handles,labels = im.legend_elements(num= intervals,fmt =None)
labels = [u"{}Gyr - {}Gyr".format(intervals[i], intervals[i+1]) for i in range(len(intervals)-1)]

leg = plt.legend(handles = handles,labels = labels,fontsize = 7, loc="upper right")

plt.xlabel('b-y',fontsize = 15)
plt.ylabel('M_ass',fontsize = 15)
plt.xlim(-0.2,1)



plt.figure(figsize=(16,8)) 
plt.title('MsuH Distribution',fontsize = 20)

MsuH = data['MsuH']

set_1_met =[]   # < 1 Gyr
set_2_met =[]   # tra 1 Gyr e 5 Gyr
set_3_met =[]   # > 5 vGyr

for i in range(len(age_parent_Gyr)):
    if age_parent_Gyr[i]<1:
        set_1_met.append(MsuH[i])
    elif age_parent_Gyr[i]>5:
        set_3_met.append(MsuH[i])
    else:
        set_2_met.append(MsuH[i])
  
        
mean_1 = np.mean(set_1_met)
mean_2 = np.mean(set_2_met)
mean_3 = np.mean(set_3_met)


median_1 = np.median(set_1_met)
median_2 = np.median(set_2_met)
median_3 = np.median(set_3_met)


lower_limit_bins = min(np.min(set_1_met),np.min(set_2_met),np.min(set_3_met))
upper_limit_bins = max(np.max(set_1_met),np.max(set_2_met),np.max(set_3_met))


set_1_met_data,set_1_met_bins = np.histogram(a = set_1_met,bins = 20,range= [lower_limit_bins,upper_limit_bins] )
set_2_met_data,set_2_met_bins = np.histogram(a = set_2_met,bins = 20 ,range= [lower_limit_bins,upper_limit_bins])
set_3_met_data,set_3_met_bins = np.histogram(a = set_3_met,bins = 20,range= [lower_limit_bins,upper_limit_bins] )


max_value_for_hist = max(np.max(set_1_met_data),np.max(set_2_met_data),np.max(set_3_met_data))
plt.hist(x = set_1_met,bins = set_1_met_bins,label ='< 1Gyr',color = 'green',alpha = 0.5)
plt.hist(x = set_2_met,bins = set_2_met_bins, label = '> 1Gyr and < 5Gyr',color = 'red',alpha =0.5)
plt.hist(x = set_3_met,bins = set_3_met_bins,label = '< 5Gyr',color = 'blue',alpha = 0.5)


plt.vlines(mean_1,0,max_value_for_hist,color = 'green', ls = '--',label ='(mean)  < 1Gyr')
plt.vlines(mean_2,0,max_value_for_hist,color = 'red',ls = '--',label = ' (mean)  > 1Gyr and < 5Gyr')
plt.vlines(mean_3,0,max_value_for_hist,color = 'blue',ls = '--',label = '(mean)  < 5Gyr')

plt.vlines(median_1,0,max_value_for_hist,color = 'green',ls = ':',label ='(median)  < 1Gyr')
plt.vlines(median_2,0,max_value_for_hist,color = 'red',ls = ':',label = ' (median)  > 1Gyr and < 5Gyr')
plt.vlines(median_3,0,max_value_for_hist,color = 'blue',ls = ':',label = '(median)  < 5Gyr')

plt.xlabel('MsuH', fontsize = 15)
plt.ylabel('Number of el.')

plt.legend(loc = 'upper left',fontsize = 10)





plt.figure(figsize=(16,8)) 
plt.title('MsuH vs m_ini',fontsize = 20)

m_ini  = data['m_ini']

set_1_mass =[]   # < 1 Gyr
set_2_mass =[]   # tra 1 Gyr e 5 Gyr
set_3_mass =[]   # > 5 vGyr

for i in range(len(age_parent_Gyr)):
    if age_parent_Gyr[i]<1:
        set_1_mass.append(m_ini[i])
    elif age_parent_Gyr[i]>5:
        set_3_mass.append(m_ini[i])
    else:
        set_2_mass.append(m_ini[i])

plt.scatter(set_1_mass,set_1_met,color = cmap(0.15),s = 15, label ='< 1Gyr',alpha = 1 )
plt.scatter(set_2_mass,set_2_met,color = cmap(0.55),s = 15, label = '> 1Gyr and < 5Gyr',alpha = 0.2 )
plt.scatter(set_3_mass,set_3_met,color = cmap(0.75),s = 15,label = '< 5Gyr',alpha = 0.2)
plt.xlabel('m_ini', fontsize = 15)
plt.ylabel('MsuH', fontsize = 15)

plt.xlim(0,7)
plt.ylim(-2.3,1)

plt.legend(loc = 'lower right',fontsize = 10)

