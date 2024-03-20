
import cantools
import can
import csv
from pprint import pprint

file = open('output.csv', 'w')

with can.BLFReader('test.blf') as can_log:
  for msg in can_log:
      #print(msg)
      content = str(msg) + "\r"
      file.write(content)

file.close()


