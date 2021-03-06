# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os

from trace_viewer.build import check_common

GYPI_FILE = 'trace_viewer.gypi'

def GypiCheck():
  f = open(GYPI_FILE, 'r')
  gyp = f.read()
  f.close()

  data = eval(gyp)
  listed_files = []
  error = ''
  for group in check_common.FILE_GROUPS:
    filenames = map(os.path.normpath, data['variables'][group])
    error += check_common.CheckListedFilesSorted(GYPI_FILE, group, filenames)
    listed_files.extend(filenames)

  return error + check_common.CheckCommon(GYPI_FILE, listed_files)

if __name__ == '__main__':
  print GypiCheck()
