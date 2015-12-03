#!/usr/bin/env python
import re

print "Welcome: lets get started"

hand = open('excel_input_stream.md')
for line in hand:
    line = line.rstrip()
    if re.search('^##_', line) :
        print line
