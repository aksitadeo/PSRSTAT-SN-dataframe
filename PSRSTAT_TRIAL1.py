#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:37:00 2022

@author: deo010
"""

#%% 
import os
import subprocess as sp
import pandas as pd

#%%

out = os.system('psrstat -c snr ARCHIVEs/t160114_192200.sfARCH.ar.zap.F')

#%%

output = sp.getoutput('psrstat -Q -c snr t160114_192200.sfARCH.ar.zap.F')

#%%
file = []
DM = []
SNR = []
x = []

for i in range(0,5):
#print(output)
    xs = output.split()
    x += [xs]
#print(x)

#%%
for thing in x:
    thing[1] = float(thing[1])
print(x)

#%% Main Loop

x =[]

for filename in os.listdir():
    if filename.endswith(".ar.zap.F"):
        print("")
        print('Now working on: {}'.format(filename))
        output = sp.getoutput('psrstat -Q -c snr {}'.format(filename))
        xs = output.split()
        x += [xs]
        
#%%

print(x)
        
#%% Convert to float

for thing in x:
    thing[1] = float(thing[1])
    print(thing)
print(x)       

# lst2 = [item[0] for item in lst]

#%%

#x[1].sort(reverse=True)
#print(x)

#%% Create dataframe

df = pd.DataFrame(x)
df.columns = ['filename','S/N']

#%%

df

#%%
final_df = df.sort_values(by=['S/N'], ascending=False)

#%%

final_df

#%%
top10 = final_df.head(20)

#%%

for file in top10['filename']:
    files = file[0:17]
    print("Now working on: {}".format(files))
    # /DATA/MENSA_1/deo010/dir/J1550-5418/F_s130416_212545.sf
    os.system('gv /DATA/MENSA_1/deo010/dir/J1550-5418/F_{}/{}TEST_rfifind.ps'.format(files,files))

#%% Averaging in polarisation

for filename in os.listdir():
    if filename.endswith(".ar.zap.F"):
        print("")
        print('Now working on: {}'.format(filename))
        os.system('pam -p {} -e Fp'.format(filename))

#%%

for filename in os.listdir():
    if filename.endswith(".ar.zap.Fp"):
        print("")
        print('Now working on: {}'.format(filename))
        os.system('pdv -t {} >> {}.txt'.format(filename,filename))

#%%

print('test')


os.system('psrplot ARCHIVEs/t160114_192200.sfARCH.ar.zap.F')

#%% 

stri = "TEST"
stri[0:3]






