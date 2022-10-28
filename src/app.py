#!/usr/bin/python

import sys, getopt

from mailer import *
def main(argv):
   configfile = ''
   addressfile = ''
   messagefile = ''
   try:
      opts, args = getopt.getopt(argv,"hc:a:m:",["config=", "address=","message="]) #getopt.getopt(args, options, [long_options])
   except getopt.GetoptError:
      print ('app.py ->e -c <config> -a <addresses> -m <message>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('app.py ->h -c <config> -a <addresses> -m <message>')
         sys.exit()
      elif opt in ("-c", "--config"):
         configfile = arg
      elif opt in ("-a", "--address"):
         addressfile =  arg
      elif opt in ("-m", "--message"):
         messagefile = arg
   #c = open(configfile).read()
   #print(c)
   bulk_mail_sender(configfile, addressfile, messagefile)
if __name__ == "__main__":
   main(sys.argv[1:])
