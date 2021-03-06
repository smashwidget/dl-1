import adv.adv_test
import adv
from slot.d import *

def module():
    return Eleonora

class Eleonora(adv.Adv):
    a3 = ('prep','50%')
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['slot.d'] = Garland()
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.poison.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.poison.resist=100
        if this.condition('fullhp=poison'):
            this.fullhp = 1
        else:
            this.fullhp = 0

    def s1_proc(this, e):
        this.afflics.poison('s1',110+50*this.fullhp,0.53)

    def s2_proc(this, e):
        this.afflics.poison('s2',100+50*this.fullhp,0.396)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)
