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

#%% Main Loop

x =[]

for filename in os.listdir():
    if filename.endswith(".ar.zap.F"):
        print("")
        print('Now working on: {}'.format(filename))
        output = sp.getoutput('psrstat -Q -c snr {}'.format(filename))
        xs = output.split()
        x += [xs]
        
#%% Check the output

print(x)
        
#%% Convert to float

for thing in x:
    thing[1] = float(thing[1])
    print(thing)
print(x)       

#%% Create dataframe

df = pd.DataFrame(x)
df.columns = ['filename','S/N']

#%% Sort by highest to lowest S/N
final_df = df.sort_values(by=['S/N'], ascending=False)

#%% Display top 10 S/N
top10 = final_df.head(20)

#%% View the top 10 S/N by plotting

for file in top10['filename']:
    files = file[0:17]
    print("Now working on: {}".format(files))
    os.system('gv /DATA/MENSA_1/deo010/dir/J1550-5418/F_{}/{}TEST_rfifind.ps'.format(files,files))

#%% Averaging in polarisation

for filename in os.listdir():
    if filename.endswith(".ar.zap.F"):
        print("")
        print('Now working on: {}'.format(filename))
        os.system('pam -p {} -e Fp'.format(filename))

#%% Convert averaged data to text files

for filename in os.listdir():
    if filename.endswith(".ar.zap.Fp"):
        print("")
        print('Now working on: {}'.format(filename))
        os.system('pdv -t {} >> {}.txt'.format(filename,filename))






