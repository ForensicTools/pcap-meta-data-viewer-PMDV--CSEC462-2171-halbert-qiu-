__author__ = 'Patrick Qiu', "Christian Halbert"
import logging
import os
import socket
import pip
import csv
import pygeoip

#-------------------------------------------------------------------------------------------------------------------
# Method: getIp
# Parameters; Self
# Inputs: CSV file, User IP input
# Exports: CSV file with IP addresses mapped to longitude and latitude
#   This method will take a csv file that orginated from a pcap without IPv6 addresses in it. Then it will parse through
#       this file and look for the desintation and source IP addresses and put them into a dictionary to sort the
#       network traffic between source and IP addesswer. The key will be the Source IP while the data stored will be
#       the destination IP. Then the program will remove all interneal traffic from the dictionary and display
#       all the IP's that have traffic that is not only internal traffic as they are non-routable Then match them to
#       longitude and latitude locations. Then save the data in a csv file called locationfile.csv.
#-------------------------------------------------------------------------------------------------------------------
def getIPs():
    #chrome --allow-file-access-from-files
    g=pygeoip.GeoIP("GeoLiteCity.dat")
    print("Please enter file name, must be a CSV taken from a PCAP:")
    filename = input()
    with open(filename) as file:
        holderOfIPs = {}                                        # create an empty dictionary
        filereadlist = []                                       # create an empty list
        filereadlist = file.readlines()                         # get every line of the file and add to a list
        filereadlist = [item.strip() for item in filereadlist]  # strip each line in the file of newline characters and etc.
        lineNum = 0                                             # Checks line number being processed.
        for line in filereadlist:                               # go through each line in the file
            fields = []
            fields = line.split(',')                            # split each line into a list
            i = 0
            for item in fields:                                 #go through each item in the line list
                fields[i] = item[1:-1]                          # remove the first and last characters with are " and "
                i = i + 1
            src_ip = fields[2]                                  # source ip is at the 2nd index
            dst_ip = fields[3]                                  # destination ip is at 3rd index

            if (src_ip not in holderOfIPs):                     # check if the source ip is already in Dictionary
                holderOfIPs[src_ip] = []                        # add the source ip with an empty list value

            if (dst_ip not in holderOfIPs[src_ip]):             # check if destination ip is already mapped to source ip
                holderOfIPs[src_ip].append((dst_ip))            # add destination ip to value list of source ip
            lineNum = lineNum + 1
    for key in holderOfIPs:
        destCounter=0
        for x in range(0, len(holderOfIPs[key])):               # Print keys of IP's that dont only have private routing
            destcheck=holderOfIPs[key][x]
            #print(destcheck)
            #print(destcheck)
            try:
                 g.record_by_addr(destcheck)['latitude']        # Check to see if the key is routable by checking latitude
        #         g.record_by_addr(destcheck)['longitude']
            except (TypeError, AttributeError):                 # Used to check if all dests are internal or just some
                 destCounter=destCounter+1

        if(len((holderOfIPs[""+key]))!=destCounter):            # If all internal then dont print that key
            print("IP: " +key)
            #print((holderOfIPs[""+key]))

        #print("\n")


    #print("Testing Location")
    #ip='172.16.255.1'
    print("Input IP you wish to track:")                        #Used to determine which IP user wants to track
    iptrack=input()
    #print(holderOfIPs[iptrack])
    #print(len(holderOfIPs[iptrack]))
    with open('locationfile.csv', 'w', newline='') as locfile:  # Creates file to store the locations ie. Long and lat
        wr = csv.writer(locfile)
        wr.writerow(["Destination_IP","Latitude",'Longitude','city','country'])
        for x in range(0, len(holderOfIPs[iptrack])):
                destcheck=holderOfIPs[iptrack][x]
                #print(destcheck)
                #print('IP address: '+destcheck)
                try:
                    wr.writerow([destcheck,g.record_by_addr(destcheck)['latitude'],g.record_by_addr(destcheck)['longitude'],g.record_by_addr(destcheck)['city'],g.record_by_addr(destcheck)['country_code3']])
                except (TypeError, AttributeError):
                    pass
                #print(str(g.record_by_addr(destcheck)['longitude'])+'\n')
                #(g.record_by_addr(destcheck)['latitude'])

def main():
    getIPs()

main()