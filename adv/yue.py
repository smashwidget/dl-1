import adv.adv_test
import adv
from slot.a import *
from slot.d import *

def module():
    return Yue

class Yue(adv.Adv):
    #comment = 'Arctos'
    conf = {}
    conf['acl'] = """
        `s3, not this.s3_buff_on
        `s1
        `s2,seq=4
        `fs,seq=5
        """



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

