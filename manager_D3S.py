#!/usr/bin/env python
import argparse

import kromek

import numpy as np

class Manager_D3S(object):
    
    def __init__(self,
                 interval=int(args.interval)
                 count=int(args.count)
                ):
    
        self.total = None
        self.lst = None
        self.create_structures = True
        
        self.interval = interval
        self.count = count
        
    def run():
        done_devices = set()
        with kromek.Controller(devs, interval) as controller:
            for reading in controller.read():
                if create_structures:
                    total = np.array(reading[4])
                    lst = np.array([reading[4]])
                    flag = False
                else:
                    total += np.array(reading[4])
                    lst = np.concatenate((lst, [np.array(reading[4])]))
                serial = reading[0]
                dev_count = reading[1]
                if serial not in done_devices:
                    print reading[4]
                if dev_count >= count > 0:
                    done_devices.add(serial)
                    controller.stop_collector(serial)
                if len(done_devices) >= len(devs):
                    break

    @classmethod
    def from_argparse(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument('--transport', '-t', dest='transport', default='any')
        parser.add_argument('--interval', '-i', dest='interval', default=30)
        parser.add_argument('--count', '-c', dest='count', default=0)
        parser.add_argument('--device', .'-d', dest='device', default='all')
        parser.add_argument('--log-bytes', '-b', dest='log_bytes', default=False, action='store_true')
        args = parser.parse_args()
        
        if args.transport == 'any':
            devs = kromek.discover()
        else:
            devs = kromek.discover(args.transport)
        print 'Discovered %s' % devs
        if len(devs) <= 0:
            return
        
        filtered = []
        
        for dev in devs:
            if args.device == 'all' or dev[0] in args.device:
                filtered.append(dev)
    
        devs = filtered
        if len(devs) <= 0:
            return

        arg_dict = vars(args)
        mgr = Manager(**arg_dict)

        return mgr

if __name__ == '__main__':
    mgr = Manager_D3S.from_argparse()
    mgr.run()