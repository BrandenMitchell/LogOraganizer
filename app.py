

#--objective: process csv log data--
    #-how often networks are seen
    #-how often security types were seen
    #-what frequencies were most busy
    #-at what coordinates were networks found

#A,B,C,D,E,F paste at line one of any csv log


#Time,GPS/MAC,SSID/Latitude,Frequency/Longitude,Power,SecurityType --- key
from func import * # imports all from function file

import pandas as pd # using pandas framework 

while(True):
    try:

        print("welcome.")
        print("enter 1 -how often certain network seen")
        print("enter 2 -how often certain security type seen") 
        print("enter 3 -Frequency occurence ")
        print("enter 4 -what coordinate a given network can be found")
        print("enter q -quit")
        user = input("select option, press enter: ")
        if user == '1': 
            fname = input("enter csv file name: ")
            masterFrame = pd.read_csv(fname)
            find_net_occ(masterFrame)

        if user == '2':
            fname = input("enter csv file name: ")
            masterFrame = pd.read_csv(fname)
            masterFrame.columns = ['A','B','C','D','E','F'] #try to use this to automate headers
            find_sec_occ(masterFrame)

        if user == '3':
            fname = input("enter csv file name: ")
            masterFrame = pd.read_csv(fname)
            find_freq_occ(masterFrame)

        if user == '4':
            fname = input("enter csv file name: ")
            masterFrame = pd.read_csv(fname)
            Gps_network(masterFrame)
        
        elif user == 'q':
            break

    except(FileNotFoundError):
        print("File name incorrect or not in directory")

print("Done")



