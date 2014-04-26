import smtplib as soc
import dns.resolver
import string
import optparse
import re

###### dnspython must be installed before using smtptls_checker 
###### You can download dnspython from http://www.dnspython.org/




def Server(ip):
            try:
                        p = soc.SMTP(ip)
                        p.set_debuglevel(0)
                        try:
                                    resp , null = p.starttls()
                                    if resp == 220:
                                                print('TLS Supported\n')
                                                p.quit()
                        except:
                                    print ('TLS not Supported\n')
                                    p.quit()
            except:
                        print ('SMTP Server Not Responding\n')

            
def UserINP(domain):
    
            try:
       #         if c == '' : break
                        mx = dns.resolver.query(domain, 'MX')        
                        for data in mx:
                                    hey = str(data.exchange)
                                    dev = data.preference
                                    ipx = hey[:-1]
                                    print "Domain Name===>",domain
                                    print "MX Preferance ==> Name" ,dev, "===>" ,ipx
                                    Server(ipx)
            except:
                        print 'Domain Name not resolved =>' , domain
           

def  FileINP(filepath):
    
            try:
                        red  = open(filepath)
                        for c in red.read().split('\n'):
                                    try:
                                                mx = dns.resolver.query(c, 'MX')        
                                                for data in mx:
                                                            hey = str(data.exchange)
                                                            dev = data.preference
                                                            ipx = hey[:-1]
                                                            print "Domain Name===>",c
                                                            print "MX Preferance ==> Name" ,dev, "===>" ,ipx
                                                            Server(ipx)
                                    except:
                                                print 'Domain Name not resolved =>' , c
            except:
                        print 'File could not be opened !!! '

def Start():
            p = optparse.OptionParser("usage: %prog [options] arg")
            p.add_option("-d" , "--domain", dest="domain", type="string",
                  help="Enter Only Domain name")
            p.add_option("-f", "--filepath", dest="filepath", type="string",
                   help="Enter Host Name File Destination")
            options, arguments = p.parse_args()
            domain = options.domain
            filepath = options.filepath
            helps = help
            if options.domain is not None:
                        UserINP(domain)
            elif options.filepath is not None:
                        FileINP(filepath)
            else :p.print_help()
                       
Start()


