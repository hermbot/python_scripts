"""
Created on Tue Jan 12 08:30:11 2016

@author: mhermes
"""

from os import listdir, rename

orig = ['_7_', '_8_', '_9_', '_10_', '_11_', '_12_', '_13_', '_14_', '_15_',
        '_16_', '_17_', '_18_', '_19_', '_20_', '_21_', '_22_']

new = ['_1_', '_2_', '_3_', '_4_', '_5_', '_6_', '_7_', '_8_', '_9_', '_10_',
       '_11_', '_12_', '_13_', '_14_', '_15_', '_16_']


for file_name in listdir('.'):
    for i in orig:
        if i in file_name:
            j = orig.index(i)
            rename(file_name, file_name.replace(orig[j], new[j]))
            print(file_name, ' -> ', new_name)
