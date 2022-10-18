#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:52:54 2022

@author: weiqiyao
"""
from dnachisel import *
from dnachisel import biotools
import flametree

# loop for generating random reverse sequences for n times
Red = "MSKIKGEEDNMLIIKEFMRFKAHMEGSVNGHEFEIEGEGEGHPYEGTQTAKLKVTKGGPLPFAWDILSPQFMYGSKAYVKHPADIPDYLKLSFPEGFTWERVMNFEDGGVVTVTQDSSLQDGQFIYKVKLLGINFPSDGPVMQKKTMGWEASTERMYPEDGALKGEINQRLKLKDGGHYDAEVKTTYKAKKPVQLPGAYNVDIKLDITSHNEDYTIVEQYERAEGRHSTHHHHHH*"
num = 20
list_ID = []
list_seq = []
for i in range(0,num):
    Redram = biotools.reverse_translate(Red,True,table = 'Bacterial')
    ID = 'Red'+ str(i+1)
    #print(ID)
    list_ID.append(ID)
    list_seq.append(Redram)
    
# write into fasta file
ofile = open("Random_reverse.fasta", "w")

for i in range(len(list_seq)):

    ofile.write(">" + list_ID[i] + "\n" +list_seq[i] + "\n")

ofile.close()