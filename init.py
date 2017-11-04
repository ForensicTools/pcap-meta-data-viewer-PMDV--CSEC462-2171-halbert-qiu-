__author__ = 'Patrick Qiu', "Christian Halbert"
import logging
import os

from scapy.all import *
    #This will be the storage for the SourceIP addresses that store the destination addresses of those
    #Uses a dictionary to process information

def grabber():
    #pass
    # Attempt at creating a tshark parser to grab IP's

    # This will grab the pcap file that is being processed
    pkts = rdpcap("capture.pcap")

    test = ""
    for pkt in pkts:
        temp = pkt.sprintf("%IP.src%,%IP.dst%,")
        test = test + temp



def parsethrough(list):             #Prints out the destinations for the sourceIPs
    # By using the dictionaries we can sort the sourceIP with new destination IPs
    # Then scan them through and make sure there are no clones
    counter=0
    counter2=0
    for x in range(0,len(list)):
        pass
    print(list)



def saveToFile(self):
    print(self)



def processLocation(self):
    pass






def main():
    srcIP={}
    srcIP["192.168.100.1"]=["1","2"]    #Testing Dictionary entry adding
    srcIP["192.168.100.1"].append("3")  #Testing nested lists in a Dictionary
    print(len(srcIP["192.168.100.1"]))  #Making sure list is extendable
    parsethrough(srcIP["192.168.100.1"])
main()


