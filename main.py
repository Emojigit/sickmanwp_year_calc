#!/usr/bin/python3
from datetime import datetime
from datetime import timedelta
import sys,os
def run():
    bdate = datetime(2019,7,3,0,0,0,0)
    modyear = int(sys.argv[1]) - 1
    adddate = int(modyear/2)
    addhour = 12
    if (modyear % 2) == 0:
        addhour = 0
    adddelta = timedelta(hours=addhour,days=adddate)
    return bdate + adddelta

if __name__ == '__main__':
    print(run())
