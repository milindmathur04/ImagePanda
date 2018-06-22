#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:02:34 2018

@author: ajit
"""
'''
import vlc
p = vlc.MediaPlayer("http://your_mp3_url")
p.play()

important links:
https://stackoverflow.com/questions/4247248/record-streaming-and-saving-internet-radio-in-python
https://github.com/DirkR/podhorst
https://github.com/beedaddy/radiorec
http://people.csail.mit.edu/hubert/pyaudio/#docs
https://stackoverflow.com/questions/892199/detect-record-audio-in-python
http://python-sounddevice.readthedocs.io/en/0.3.10/

'''

import os
import requests
from time import sleep
import subprocess

os.chdir("/home/ajit/Documents/adskipper/LiveRadioStreams/Radio_99.5/mp3")


while 1!=2:
    for i in range(0,21):
        #4
        sleep(4)
        stream_url = 'http://14833.live.streamtheworld.com/WUSNFMAAC_SC'
        r = requests.get(stream_url, stream=True)
        
        
        idx = 0
        with open('radio1_stream'+str(i)+'.mp3', 'wb') as f:
            #16
                for block in r.iter_content(16):
                    idx += 1
                    f.write(block)
                    #3000
                    if(idx==3000):
                        print(i)
                        break
        if os.path.isfile('/home/ajit/Documents/adskipper/LiveRadioStreams/Radio_99.5/wav/radio1_stream'+str(i)+'.wav') :
            os.remove('/home/ajit/Documents/adskipper/LiveRadioStreams/Radio_99.5/wav/radio1_stream'+str(i)+'.wav')
        subprocess.call(['ffmpeg', '-i', 'radio1_stream'+str(i)+'.mp3','/home/ajit/Documents/adskipper/LiveRadioStreams/Radio_99.5/wav/radio1_stream'+str(i)+'.wav'])

