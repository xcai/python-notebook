#!/usr/bin/env python3
#
# python3 disk.py / /aegi /aegis /agdisk
#
import os
import time
from datetime import datetime
import sys
from sys import stdout, stderr

LOG_FILE = '~/monitor/disk.log'

def disk_stat(path):
    disk = os.statvfs(path)
    percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks -disk.f_bfree + disk.f_bavail) + 1
    return percent

paths = sys.argv[1:]
stdout.write('Start to monitor: %s'% paths)
print("Start to monitor: %s", ', '.join(paths))
while True:
    now = str(datetime.now())
    for p in paths:
        used = round(disk_stat(p))
        if used > 96:
            msg = "\033[7;31m %s！！！警告：磁盘（%s）使用率已到%s%%\033[1;31;40m"%(now, p, used)
            os.system('wall "'+msg+'"')
            stdout.write(msg)
#            with open(LOG_FILE, 'a') as f:
#                f.write(msg+'\n')
    time.sleep(5)
