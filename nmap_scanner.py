#!/usr/ python
import csv
import nmap
try:
    nm = nmap.PortScanner()         # init portscanner object
except :
    print("Unexpected error:", sys.exe_info()[0])
    sys.exit(1)

# using namp scan all active hosts
nm.scan(hosts='192.168.1.1/24', arguments='-sP')

csvfile='Mac Address List.csv'
val = {}
vendorLst = []

for host in nm.all_hosts():         # get all scanned hosts
    all_hosts = nm[host].keys() 
    for h in all_hosts:             # iterate all the keys
        print('~~~~', h, ' :-' , nm[host][h])
    # we need to get <key,value> pair containing <MAC,Vendor Name>  
        if h == 'vendor':           
            vendorLst.append(nm[host][h])

for vl in vendorLst:
    for vlKey, vlVal in vl.items():
        val[vlKey] = vlVal
        print('__________' + vlKey + '  ' + vlVal )

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(val.items())
