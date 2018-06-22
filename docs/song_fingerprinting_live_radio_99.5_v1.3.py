#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:52:47 2018

@author: ajit
"""
#import iglob
import os
import numpy as np
import time
from time import sleep
#import matplotlib.pyplot as plt
from matplotlib.mlab import specgram
from scipy.io import wavfile
from skimage.feature import peak_local_max

os.chdir("/home/ajit/Documents/adskipper/LiveRadioStreams/Radio_99.5/wav")

def cut_specgram(min_freq, max_freq, spec, freqs):
    spec_cut = spec[(freqs >= min_freq) & (freqs <= max_freq)]
    freqs_cut = freqs[(freqs >= min_freq) & (freqs <= max_freq)]
    Z_cut = 10.0 * np.log10(spec_cut)
    Z_cut = np.flipud(Z_cut)
    return Z_cut, freqs_cut

dict_995 = np.load('../Ads_fingerprint_99.5.npy').item()

while 1!=2:
    sleep(2)
    #onlyfiles = [f for f in os.listdir() if os.path.isfile(str(f))]
    time_stamp_list = []
    for k in os.listdir(): #onlyfiles:
        time_stamp_list.append(time.ctime(os.path.getmtime(str(k) )))
    Latest_Stream = os.listdir()[time_stamp_list.index(max(time_stamp_list))]

    rate1, song_array1 = wavfile.read(Latest_Stream)
    #rate2, song_array2 = wavfile.read('Josh-Woodward--I-Want-To-Destroy-Something-Beautiful_21sec_cut.wav')
    spec1, freqs1, t1 = specgram(song_array1[:,0], NFFT=4096, Fs=rate1, noverlap=2048)
    #spec2, freqs2, t2 = specgram(song_array2[:,0], NFFT=4096, Fs=rate2, noverlap=2048)
    spec1[spec1 == 0] = 1e-6
    #spec2[spec2 == 0] = 1e-6
    min_freq = 0
    max_freq = 15000
    Z1, freqs1 = cut_specgram(min_freq, max_freq, spec1, freqs1)
    #Z2, freqs2 = cut_specgram(min_freq, max_freq, spec2, freqs2)
    coordinates1 = peak_local_max(Z1, min_distance=20, threshold_abs=20)
    #coordinates2 = peak_local_max(Z2, min_distance=20, threshold_abs=20)
    #len(song_array2)/len(song_array1)
    ad_vec = 0
    tvec = {}
    for ix in dict_995.keys():
        idx = 0
        for i in range(0,coordinates1.shape[0]):
                       if coordinates1[i] in dict_995[ix]:
                           idx += 1    
        #print(idx,coordinates1.shape[0],coordinates2.shape[0])
        tvec[ix]=idx/coordinates1.shape[0]
        if idx/coordinates1.shape[0]>0.90:
            ad_vec += 1

    
    if ad_vec>0:
        print("----------------------There is an Ad on 99.5!!----------------------------------")
    else:
        print("There is NO Ad on 99.5!!")


