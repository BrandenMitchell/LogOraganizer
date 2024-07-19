#KEY--
#Time,GPS/MAC,SSID/Latitude,Frequency/Longitude,Power,SecurityType

#--objective: process csv log data--
    #-how often networks are seen
    #-how often security types were seen
    #-what frequencies were most busy
    #-at what coordinates were networks found using the times of the inputs

#ProgramInfo:
    #--Catchs filenotfound
    #--Auto generates headers
    #--Allows specific net/freq/sec type searching

#----------------------------------------------------------------#

from func import * # imports all from function file
import pandas as pd # using pandas framework 


print("CSV ORGANIZER")
while(True):
    try:

        print("enter 1 -how often certain network seen")
        print("enter 2 -how often certain security type seen") 
        print("enter 3 -Frequency occurence ")
        print("enter 4 -what coordinate a given network can be found")
        print("enter q -quit")
        user = input("select option, press enter: ")
        if user == '1': 
            fname = input("enter csv file name: ")
            masterFrame = pd.read_csv(fname,names= ['A','B','C','D','E','F'])
            find_net_occ(masterFrame)

        elif user == '2':
            fname = input("enter csv file name: ")
            masterFrame = pd.read_csv(fname,names= ['A','B','C','D','E','F']) #try to use this to automate headers

            find_sec_occ(masterFrame)

        elif user == '3':
            fname = input("enter csv file name: ")
            masterFrame = pd.read_csv(fname,names= ['A','B','C','D','E','F'])
            find_freq_occ(masterFrame)

        elif user == '4':
            fname = input("enter csv file name: ")
            masterFrame = pd.read_csv(fname,names= ['A','B','C','D','E','F'])
            Gps_network(masterFrame)
        
        elif user == 'q':
            break

        else:
            print("Not valid option")
    except(FileNotFoundError):
        print("File name incorrect or not in directory")

print("Done")



