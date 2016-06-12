#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import subprocess
import sys
import re
import time

def main(args=None):

    try:
        while True:
            filename = time.strftime("%Y%m%d%H%M%S") + ".wav"
            proc = subprocess.Popen(['sh','sox.sh', filename, '5' ], stdout=subprocess.PIPE)
            result,errors = proc.communicate()
            amplitude=float(result)
            print amplitude
            if amplitude > 0.15:
                print 'Sound detected'
                #os.rename(filename, "data/" + filename)
            else:
                print 'No sound detected'
                #os.remove(filename)
    except KeyboardInterrupt:
        print('')
    finally:
        print('Program over')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
