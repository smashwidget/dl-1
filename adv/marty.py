import adv.adv_test
import adv
from slot.a import *

def module():
    return Marty

class Marty(adv.Adv):
    a1 = ('sp',0.05)
    conf = {}
    conf['slots.a'] = TSO()+BN()
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1,fsc
        `fs, seq=3
        """



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

