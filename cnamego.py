import sys
import dns
import dns.resolver
import colorama
import time
from colorama import Fore, Style
from requests.exceptions import ConnectionError

outname = input('Output Save To file name ==> ')

print(Fore.WHITE + '''

                          _                _           _ _ 
 ___ _ __ ___   __ _  ___| | _____ _ __ __| | ___   __| (_)
/ __| '_ ` _ \ / _` |/ __| |/ / _ \ '__/ _` |/ _ \ / _` | |
\__ \ | | | | | (_| | (__|   <  __/ | | (_| | (_) | (_| | |
|___/_| |_| |_|\__,_|\___|_|\_\___|_|  \__,_|\___/ \__,_|_|

''')
print(Fore.GREEN + '''              CODED BY     : DAOUD YOUSSEF 
	      SOME EDIT BY : MoamEn Go         


''')                                              
print (Fore.RED + 'PREPARING FOR BEGIN SCRIPT')
for i in range(5,0,-1):
    time.sleep(1)
    print(str(i) + i * " . ")
sublist=sys.argv[1]
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8']
subfile=open(sublist, 'r')
for sub in subfile:
        try:
                subd=sub.strip()
                answer=my_resolver.query(sub.strip(), 'CNAME')
                for data in answer:
                        print(Fore.WHITE + (subd))
                        print(Fore.GREEN + ' CNAME_IS ==> ' + Fore.YELLOW + str(data))
                        save = open(outname, 'a')
                        save.write((subd) + ' CNAME_IS ==> ' + str(data) + '\n\n')
                        
        except :    
                print(Fore.WHITE + (sub) + Fore.RED + (' has no cname'))
subfile.close()
