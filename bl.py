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
    def __init__(self):
        self.xlate = {}
        self.xlate['dev'] = {}
        self.xlate['sasid'] = {}
        self.xlate['loc'] = {}

        self.get_lsscsi()
        for expander in self.list_expanders():
            if expander == 'expander-2:1':
                self.xlate['loc'][expander] = self.supermicro_sc847_e26_front()
                self.xlate['loc'][expander]['side'] = 'Front'
            else:
                self.xlate['loc'][expander] = self.supermicro_sc847_e26_back()
                self.xlate['loc'][expander]['side'] = 'Back'
            self.get_smpdiscover(expander)



    def pretty_print(self):

        for expander in self.xlate['loc']:
            print "------------ [ %-6s ] -------------" % self.xlate['loc'][expander]['side'] 
            for y in xrange(0, 6):
                for x in xrange(0, 4):
                    found = False
                    for l in self.xlate['loc'][expander]:
                        loc = self.xlate['loc'][expander][l]
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
        res = {}

        res[99] = {}
        res[99]['pos_x'] = 0
        res[99]['pos_y'] = 0

        res[98] = {}
        res[98]['pos_x'] = 0
        res[98]['pos_y'] = 1

        res[97] = {}
        res[97]['pos_x'] = 0
        res[97]['pos_y'] = 2

        res[10] = {}
        res[10]['pos_x'] = 0
        res[10]['pos_y'] = 3

        res[9] = {}
        res[9]['pos_x'] = 0
        res[9]['pos_y'] = 4

        res[8] = {}
        res[8]['pos_x'] = 0
        res[8]['pos_y'] = 5


        res[16] = {}
        res[16]['pos_x'] = 1
        res[16]['pos_y'] = 0

        res[15] = {}
        res[15]['pos_x'] = 1
        res[15]['pos_y'] = 1

        res[14] = {}
        res[14]['pos_x'] = 1
        res[14]['pos_y'] = 2

        res[13] = {}
        res[13]['pos_x'] = 1
        res[13]['pos_y'] = 3

        res[12] = {}
        res[12]['pos_x'] = 1
        res[12]['pos_y'] = 4

        res[11] = {}
        res[11]['pos_x'] = 1
        res[11]['pos_y'] = 5


        res[22] = {}
        res[22]['pos_x'] = 2
        res[22]['pos_y'] = 0

        res[21] = {}
        res[21]['pos_x'] = 2
        res[21]['pos_y'] = 1

        res[20] = {}
        res[20]['pos_x'] = 2
        res[20]['pos_y'] = 2

        res[19] = {}
        res[19]['pos_x'] = 2
        res[19]['pos_y'] = 3

        res[18] = {}
        res[18]['pos_x'] = 2
        res[18]['pos_y'] = 4

        res[17] = {}
        res[17]['pos_x'] = 2
        res[17]['pos_y'] = 5


        res[28] = {}
        res[28]['pos_x'] = 3
        res[28]['pos_y'] = 0

        res[27] = {}
        res[27]['pos_x'] = 3
        res[27]['pos_y'] = 1

        res[26] = {}
        res[26]['pos_x'] = 3
        res[26]['pos_y'] = 2

        res[25] = {}
        res[25]['pos_x'] = 3
        res[25]['pos_y'] = 3

        res[24] = {}
        res[24]['pos_x'] = 3
        res[24]['pos_y'] = 4

        res[23] = {}
        res[23]['pos_x'] = 3
        res[23]['pos_y'] = 5

        return res



    def supermicro_sc847_e26_front(self):

        #y x0   1   2   3
        #0  17  23  29  35
        #1  16  22  28  34
        #2  15  21  27  33
        #3  14  20  26  32
        #4  13  19  25  31
        #5  12  18  24  30
        res = {}

        res[17] = {}
        res[17]['pos_x'] = 0
        res[17]['pos_y'] = 0

        res[16] = {}
        res[16]['pos_x'] = 0
        res[16]['pos_y'] = 1

        res[15] = {}
        res[15]['pos_x'] = 0
        res[15]['pos_y'] = 2

        res[14] = {}
        res[14]['pos_x'] = 0
        res[14]['pos_y'] = 3

        res[13] = {}
        res[13]['pos_x'] = 0
        res[13]['pos_y'] = 4

        res[12] = {}
        res[12]['pos_x'] = 0
        res[12]['pos_y'] = 5


        res[23] = {}
        res[23]['pos_x'] = 1
        res[23]['pos_y'] = 0

        res[22] = {}
        res[22]['pos_x'] = 1
        res[22]['pos_y'] = 1

        res[21] = {}
        res[21]['pos_x'] = 1
        res[21]['pos_y'] = 2

        res[20] = {}
        res[20]['pos_x'] = 1
        res[20]['pos_y'] = 3

        res[19] = {}
        res[19]['pos_x'] = 1
        res[19]['pos_y'] = 4

        res[18] = {}
        res[18]['pos_x'] = 1
        res[18]['pos_y'] = 5


        res[29] = {}
        res[29]['pos_x'] = 2
        res[29]['pos_y'] = 0

        res[28] = {}
        res[28]['pos_x'] = 2
        res[28]['pos_y'] = 1

        res[27] = {}
        res[27]['pos_x'] = 2
        res[27]['pos_y'] = 2

        res[26] = {}
        res[26]['pos_x'] = 2
        res[26]['pos_y'] = 3

        res[25] = {}
        res[25]['pos_x'] = 2
        res[25]['pos_y'] = 4

        res[24] = {}
        res[24]['pos_x'] = 2
        res[24]['pos_y'] = 5


        res[35] = {}
        res[35]['pos_x'] = 3
        res[35]['pos_y'] = 0

        res[34] = {}
        res[34]['pos_x'] = 3
        res[34]['pos_y'] = 1

        res[33] = {}
        res[33]['pos_x'] = 3
        res[33]['pos_y'] = 2

        res[32] = {}
        res[32]['pos_x'] = 3
        res[32]['pos_y'] = 3

        res[31] = {}
        res[31]['pos_x'] = 3
        res[31]['pos_y'] = 4

        res[30] = {}
        res[30]['pos_x'] = 3
        res[30]['pos_y'] = 5

        return res



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



    def get_smpdiscover(self, expander):
        """ Run smpdiscover on our disk enclosures and get output
        """
        p = subprocess.Popen(['smp_discover', '--multiple', '/dev/bsg/' + expander], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdoutdata, stderrdata) = p.communicate(None)
        for line in stdoutdata.splitlines():
            if not re.search('^ *phy.*attached', line):
                continue
            data = line.split()[1]
            slot = int(data.split(':')[0])
            sas_id = data.split(':')[3].strip('[]')

            # update location information
            if expander not in self.xlate['loc']:
                self.xlate['loc'][expander] = {}

            if slot not in self.xlate['loc'][expander]:
                self.xlate['loc'][expander][slot] = {}
            self.xlate['loc'][expander][slot]['sasid'] = sas_id

            # update sasid information
            if sas_id not in self.xlate['sasid']:
                self.xlate['sasid'][sas_id] = {}
            self.xlate['sasid'][sas_id]['slot'] = slot
            self.xlate['sasid'][sas_id]['expander'] = expander



    def light(self, dev, on = True):
        """
        """
        dev = '/dev/' + dev

        if on is True:
            cmd = 'set'
        else:
            cmd = 'clear'

        sas_id = self.xlate['dev'][dev]['sasid']
        expander = self.xlate['sasid'][sas_id]['expander']
        slot = self.xlate['sasid'][sas_id]['slot']

#        if self.expander == '4:0':
#            exp = '/dev/bsg/2:0:11:0'
#            slot = "%02d" % (loc - 7)
#        else:
#            exp = '/dev/bsg/2:0:35:0'
#            slot = "%02d" % (loc - 11)

        print "expander:", expander, "  slot:", slot
        if expander == 'expander-2:1':
            sg = '/dev/sg43'
            slot -= 7
        else:
            sg = '/dev/sg18'
            slot -= 11
        print "expander:", expander, "  slot:", slot
        subprocess.Popen(['sg_ses', '-D', 'Slot ' + str(slot), '--' + cmd + '=locate', sg])



    def list_expanders(self):
        import os
        entries = os.listdir('/dev/bsg/')
        result = []
        for entry in entries:
            if re.match('expander-', entry):
                result.append(entry)

        return result





if __name__ == '__main__':
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--print', dest = 'pretty_print', action = 'store_true')
    parser.add_option('--locate', dest = 'light', action = 'store_true')
    parser.add_option('--locate-off', dest = 'light', action = 'store_false')

    (options, args) = parser.parse_args()

    s = Smp()

    if options.pretty_print:
        s.pretty_print()

    if options.light is True:
        for dev in args:
            s.light(dev, True)

    if options.light is False:
        for dev in args:
            s.light(dev, False)



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
