#! /usr/bin/python

import os
import zipfile

for root, dirs, files in os.walk('.'):
  for file in files:
    if file.endswith('.zip'):
      try:
        zfile = zipfile.ZipFile(file)
      except zipfile.BadZipfile as ex:
        print("%s not a zip file" % file)
        continue

      ret = zfile.testzip()

      if ret is not None:
        print("%s bad zip file, error: %s" % file, ret)
      else:
        print("%s OK" % file)
