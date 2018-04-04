#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

# input comes from STDIN (standard input)
with sys.stdin as csvfile:
    reader = csv.reader(csvfile, delimiter =',')
    reader.next()
    for line in reader:
        line = line[-5:]
        line = filter(None, line)
        for items in line:
            print '%s\t%s' % (items,1)

