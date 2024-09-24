#!/usr/bin/python3

import sys

try:
 # do something
 sum = 1 + "3"
except Exception as e:
 # pring out the error
 print(e)

 #story the process and exit with a non-zero status
 sys.exit(75)
