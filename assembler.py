import os
import argparse
import sys


def readFile(f): 
  # read each file and get each line
  if os.access(f, os.R_OK):
    with open(f) as fp: 
      file = fp.read()
  i = 0
  file = file.split('\n')
  for line in file: 
    print i,line
    i += 1

def getfile(f):
  print "getting file",f 
  # check if file is present
  path = os.path
  if path.exists(f): 
    readFile(f)  
  else :
    print "File Not Found!"

if __name__ == "__main__":
  # get file from current path
  # start parsing line by line
  # we want to generate 8 bits
  # write generated bits to newfile
  print "Assembler running..." 
  flag = sys.argv[1] 
  fileName = sys.argv[2]
  if flag == "-f": 
    getfile(fileName)

