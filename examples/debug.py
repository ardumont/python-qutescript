#!/usr/bin/env python3.6
# coding=utf-8
import json

from qutescript import qutescript


@qutescript
def dump_to_log(request):
    with open('qutescript.debug.log', 'a') as logfile:
        line = json.dumps(request.dump())
        logfile.writelines([line])

if __name__ == '__main__':
    dump_to_log()