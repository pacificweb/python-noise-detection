#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import subprocess
import sys
import re
import time

def main(args=None):

    #todo offset,root via param
    root = "/mnt/flash/capture/"
    offset = 0.15 # user defined

    try:
        while True:
            filedate = time.strftime("%Y%m%d-%H%M%S")
            filename = root + filedate + ".wav"
            #if not root current then uncomment
            #filename = filedate + ".wav"
            proc = subprocess.Popen(['/bin/bash','sox.sh', filename, '5' ], stdout=subprocess.PIPE)
            result,errors = proc.communicate()
            amplitude = float(result)
            print amplitude
            if amplitude >= offset:
                print 'Sound detected - amplitude was ' + str(amplitude)
            else:
                os.remove(filename)
    #todo other except handler
    except KeyboardInterrupt:
        print('')
    finally:
        print('')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
