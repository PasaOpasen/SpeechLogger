# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:31:00 2020

@author: qtckp
"""


import pyaudio 

# detect devices:
p = pyaudio.PyAudio()
host_info = p.get_host_api_info_by_index(0)    
device_count = host_info.get('deviceCount')
devices = []

# iterate between devices:
for i in range(0, device_count):
    device = p.get_device_info_by_host_api_device_index(0, i)
    devices.append(device['name'])

print(devices)

