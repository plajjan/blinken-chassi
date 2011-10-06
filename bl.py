#!/usr/bin/python

import subprocess
import curses

import sqlite3
import re

class NcurseUi:
    def __init__(self):
        self.scr = curses.initscr()

    def test(self):

        pass

class TextUi:
    def __init__(self):
        self.slots = {}

    def box_init(self, x, y):
        for a in xrange(0, x):
            if a not in self.slots:
                self.slots[a] = {}
            for b in xrange(0, y):
                if b not in self.slots[a]:
                    self.slots[a][b] = {}


    def display(self):
        for x in self.slots:
            for y in self.slots[x]:
                print str(x) + ',' + str(y),
            print ""

class Smp:
    def __init__(self, bla):
        self.expander = bla

        self.xlate = {}
        self.xlate['dev'] = {}
        self.xlate['sasid'] = {}
        self.xlate['loc'] = {}

        if self.expander == '4:1':
            self.supermicro_sc847_e26_front()
        else:
            self.supermicro_sc847_e26_back()

        self.get_lsscsi()
        self.get_smpdiscover()

        for y in xrange(0, 6):
            for x in xrange(0, 4):
                found = False
                for l in self.xlate['loc']:
                    loc = self.xlate['loc'][l]
                    if 'pos_y' not in loc or 'sasid' not in loc:
                        continue

                    if loc['pos_y'] == y and loc['pos_x'] == x:
                        sas_id = self.xlate['sasid'][loc['sasid']]
                        if 'dev' in sas_id:
                            dev = re.sub('/dev/', '', self.xlate['sasid'][loc['sasid']]['dev'])
                        else:
                            dev = '--'
                        found = True
                        print "%-10s" % dev,
                if not found:
                    print "%-10s" % 'PSU',
            print ""




    def supermicro_sc847_e26_back(self):
        self.xlate['loc'][99] = {}
        self.xlate['loc'][99]['pos_x'] = 0
        self.xlate['loc'][99]['pos_y'] = 0

        self.xlate['loc'][98] = {}
        self.xlate['loc'][98]['pos_x'] = 0
        self.xlate['loc'][98]['pos_y'] = 1

        self.xlate['loc'][97] = {}
        self.xlate['loc'][97]['pos_x'] = 0
        self.xlate['loc'][97]['pos_y'] = 2

        self.xlate['loc'][10] = {}
        self.xlate['loc'][10]['pos_x'] = 0
        self.xlate['loc'][10]['pos_y'] = 3

        self.xlate['loc'][9] = {}
        self.xlate['loc'][9]['pos_x'] = 0
        self.xlate['loc'][9]['pos_y'] = 4

        self.xlate['loc'][8] = {}
        self.xlate['loc'][8]['pos_x'] = 0
        self.xlate['loc'][8]['pos_y'] = 5


        self.xlate['loc'][16] = {}
        self.xlate['loc'][16]['pos_x'] = 1
        self.xlate['loc'][16]['pos_y'] = 0

        self.xlate['loc'][15] = {}
        self.xlate['loc'][15]['pos_x'] = 1
        self.xlate['loc'][15]['pos_y'] = 1

        self.xlate['loc'][14] = {}
        self.xlate['loc'][14]['pos_x'] = 1
        self.xlate['loc'][14]['pos_y'] = 2

        self.xlate['loc'][13] = {}
        self.xlate['loc'][13]['pos_x'] = 1
        self.xlate['loc'][13]['pos_y'] = 3

        self.xlate['loc'][12] = {}
        self.xlate['loc'][12]['pos_x'] = 1
        self.xlate['loc'][12]['pos_y'] = 4

        self.xlate['loc'][11] = {}
        self.xlate['loc'][11]['pos_x'] = 1
        self.xlate['loc'][11]['pos_y'] = 5


        self.xlate['loc'][22] = {}
        self.xlate['loc'][22]['pos_x'] = 2
        self.xlate['loc'][22]['pos_y'] = 0

        self.xlate['loc'][21] = {}
        self.xlate['loc'][21]['pos_x'] = 2
        self.xlate['loc'][21]['pos_y'] = 1

        self.xlate['loc'][20] = {}
        self.xlate['loc'][20]['pos_x'] = 2
        self.xlate['loc'][20]['pos_y'] = 2

        self.xlate['loc'][19] = {}
        self.xlate['loc'][19]['pos_x'] = 2
        self.xlate['loc'][19]['pos_y'] = 3

        self.xlate['loc'][18] = {}
        self.xlate['loc'][18]['pos_x'] = 2
        self.xlate['loc'][18]['pos_y'] = 4

        self.xlate['loc'][17] = {}
        self.xlate['loc'][17]['pos_x'] = 2
        self.xlate['loc'][17]['pos_y'] = 5


        self.xlate['loc'][28] = {}
        self.xlate['loc'][28]['pos_x'] = 3
        self.xlate['loc'][28]['pos_y'] = 0

        self.xlate['loc'][27] = {}
        self.xlate['loc'][27]['pos_x'] = 3
        self.xlate['loc'][27]['pos_y'] = 1

        self.xlate['loc'][26] = {}
        self.xlate['loc'][26]['pos_x'] = 3
        self.xlate['loc'][26]['pos_y'] = 2

        self.xlate['loc'][25] = {}
        self.xlate['loc'][25]['pos_x'] = 3
        self.xlate['loc'][25]['pos_y'] = 3

        self.xlate['loc'][24] = {}
        self.xlate['loc'][24]['pos_x'] = 3
        self.xlate['loc'][24]['pos_y'] = 4

        self.xlate['loc'][23] = {}
        self.xlate['loc'][23]['pos_x'] = 3
        self.xlate['loc'][23]['pos_y'] = 5



    def supermicro_sc847_e26_front(self):

        #y x0   1   2   3
        #0  17  23  29  35
        #1  16  22  28  34
        #2  15  21  27  33
        #3  14  20  26  32
        #4  13  19  25  31
        #5  12  18  24  30


        self.xlate['loc'][17] = {}
        self.xlate['loc'][17]['pos_x'] = 0
        self.xlate['loc'][17]['pos_y'] = 0

        self.xlate['loc'][16] = {}
        self.xlate['loc'][16]['pos_x'] = 0
        self.xlate['loc'][16]['pos_y'] = 1

        self.xlate['loc'][15] = {}
        self.xlate['loc'][15]['pos_x'] = 0
        self.xlate['loc'][15]['pos_y'] = 2

        self.xlate['loc'][14] = {}
        self.xlate['loc'][14]['pos_x'] = 0
        self.xlate['loc'][14]['pos_y'] = 3

        self.xlate['loc'][13] = {}
        self.xlate['loc'][13]['pos_x'] = 0
        self.xlate['loc'][13]['pos_y'] = 4

        self.xlate['loc'][12] = {}
        self.xlate['loc'][12]['pos_x'] = 0
        self.xlate['loc'][12]['pos_y'] = 5


        self.xlate['loc'][23] = {}
        self.xlate['loc'][23]['pos_x'] = 1
        self.xlate['loc'][23]['pos_y'] = 0

        self.xlate['loc'][22] = {}
        self.xlate['loc'][22]['pos_x'] = 1
        self.xlate['loc'][22]['pos_y'] = 1

        self.xlate['loc'][21] = {}
        self.xlate['loc'][21]['pos_x'] = 1
        self.xlate['loc'][21]['pos_y'] = 2

        self.xlate['loc'][20] = {}
        self.xlate['loc'][20]['pos_x'] = 1
        self.xlate['loc'][20]['pos_y'] = 3

        self.xlate['loc'][19] = {}
        self.xlate['loc'][19]['pos_x'] = 1
        self.xlate['loc'][19]['pos_y'] = 4

        self.xlate['loc'][18] = {}
        self.xlate['loc'][18]['pos_x'] = 1
        self.xlate['loc'][18]['pos_y'] = 5


        self.xlate['loc'][29] = {}
        self.xlate['loc'][29]['pos_x'] = 2
        self.xlate['loc'][29]['pos_y'] = 0

        self.xlate['loc'][28] = {}
        self.xlate['loc'][28]['pos_x'] = 2
        self.xlate['loc'][28]['pos_y'] = 1

        self.xlate['loc'][27] = {}
        self.xlate['loc'][27]['pos_x'] = 2
        self.xlate['loc'][27]['pos_y'] = 2

        self.xlate['loc'][26] = {}
        self.xlate['loc'][26]['pos_x'] = 2
        self.xlate['loc'][26]['pos_y'] = 3

        self.xlate['loc'][25] = {}
        self.xlate['loc'][25]['pos_x'] = 2
        self.xlate['loc'][25]['pos_y'] = 4

        self.xlate['loc'][24] = {}
        self.xlate['loc'][24]['pos_x'] = 2
        self.xlate['loc'][24]['pos_y'] = 5


        self.xlate['loc'][35] = {}
        self.xlate['loc'][35]['pos_x'] = 3
        self.xlate['loc'][35]['pos_y'] = 0

        self.xlate['loc'][34] = {}
        self.xlate['loc'][34]['pos_x'] = 3
        self.xlate['loc'][34]['pos_y'] = 1

        self.xlate['loc'][33] = {}
        self.xlate['loc'][33]['pos_x'] = 3
        self.xlate['loc'][33]['pos_y'] = 2

        self.xlate['loc'][32] = {}
        self.xlate['loc'][32]['pos_x'] = 3
        self.xlate['loc'][32]['pos_y'] = 3

        self.xlate['loc'][31] = {}
        self.xlate['loc'][31]['pos_x'] = 3
        self.xlate['loc'][31]['pos_y'] = 4

        self.xlate['loc'][30] = {}
        self.xlate['loc'][30]['pos_x'] = 3
        self.xlate['loc'][30]['pos_y'] = 5



    def get_lsscsi(self):
        """ Run lsscsi -t and parse its output
        """
        p = subprocess.Popen(['lsscsi', '-t'], stdout=subprocess.PIPE)
        (stdoutdata, _) = p.communicate(None)
        for line in stdoutdata.splitlines():
            if not re.search('sas:0x', line):
                continue
            sas_id = line.split()[-2].split('sas:0x')[1]
            dev_name = line.split()[-1]

            if dev_name not in self.xlate['dev']:
                self.xlate['dev'][dev_name] = {}
            self.xlate['dev'][dev_name]['sasid'] = sas_id

            if sas_id not in self.xlate['sasid']:
                self.xlate['sasid'][sas_id] = {}
            self.xlate['sasid'][sas_id]['dev'] = dev_name



    def get_smpdiscover(self):
        """ Run smpdiscover on our disk enclosures and get output
        """
        expander = '/dev/bsg/expander-' + self.expander
        p = subprocess.Popen(['smp_discover', '--multiple', expander], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdoutdata, _) = p.communicate(None)
        for line in stdoutdata.splitlines():
            if not re.search('^ *phy.*attached', line):
                continue
            data = line.split()[1]
            loc = int(data.split(':')[0])
            sas_id = data.split(':')[3].strip('[]')

            if loc not in self.xlate['loc']:
                self.xlate['loc'][loc] = {}
            self.xlate['loc'][loc]['sasid'] = sas_id

            if sas_id not in self.xlate['sasid']:
                self.xlate['sasid'][sas_id] = {}
            self.xlate['sasid'][sas_id]['loc'] = loc


    def light(self, dev, on = True):
        if not re.match('/dev', dev):
            dev = '/dev/' + dev
        sas_id = self.xlate['dev'][dev]['sasid']
        loc = self.xlate['sasid'][sas_id]['loc']
        if self.expander == '4:0':
            exp = '/dev/bsg/4:0:11:0'
            slot = "%02d" % (loc - 7)
        else:
            exp = '/dev/bsg/4:0:35:0'
            slot = "%02d" % (loc - 11)
        if on is True:
            cmd = 'set'
        else:
            cmd = 'clear'
        subprocess.Popen(['sg_ses', '-D', 'Slot ' + slot, '--' + cmd + '=locate', '/dev/bsg/4:0:11:0'])






    def list(self):
        pass



print "-------[Front]-------"
sf = Smp('4:1')
print "-------[Back]-------"
sb = Smp('4:0')
#sb.light('sdm', True)

    #def locate(self, ):

# turn on LED for slot $I on backside
# sg_ses -D "Slot $I" --clear=locate /dev/bsg/4:0:11:0
# turn on LED for slot $I on frontside
# sg_ses -D "Slot $I" --clear=locate /dev/bsg/4:0:25:0
# 4:0:25:0 is a SAS expander / chassis thing, which one is which?

# lsscsi -t
# phy numbers maps up like this:
#
#   17  23  29  35
#   16  22  28  34
#   15  21  27  33
#   14  20  26  32
#   13  19  25  31
#   12  18  24  30

# lsscsi -t 
#   phy  28:T:attached:[5003048000abd95c:00  t(SATA)]  6 Gbps
# would be second from the top in the third row (from left)


# MAPPING
# Chassis slot to Chassis element (kinda!?)
# sg_ses -p 0x7 --verbose /dev/bsg/4:0:25:0

# Chassis Element to SAS address
# sg_ses -p 0xa --verbose /dev/bsg/4:0:25:0


#
#if __name__ == '__main__':
#    tu = TextUi()
#    tu.box_init(4,6)
#    tu.display()
#
