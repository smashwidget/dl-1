import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Mitsuhide

class Mitsuhide(Adv):
    a1 = ('a',0.2,'hit15')
    a3 = ('k_paralysis',0.3)

    conf = {}
    conf['slot.a'] = TB()+SotS()
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=4
    """
    conf['cond_afflict_res'] = 0

    def init(this):
        this.s1_stance = 1

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.paralysis.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.paralysis.resist=100

    def s1_proc(this, e):
        this.afflics.paralysis('s1',120, 0.97)
        for _ in range(11):
            this.dmg_make('o_s1',0.61,'s')
            this.hits += 1

    def s2_proc(this, e):
        if(this.hits >= 5):
            this.dmg_make('o_s2_boost',0.4725,'s')
        if(this.hits >= 10):
            this.dmg_make('o_s2_boost',0.4725,'s')
        if(this.hits >= 15):
            this.dmg_make('o_s2_boost',0.945,'s')
        if(this.hits >= 20):
            this.dmg_make('o_s2_boost',0.945,'s')
        if(this.hits >= 25):
            this.dmg_make('o_s2_boost',0.945,'s')
        if(this.hits >= 30):
            this.dmg_make('o_s2_boost',0.945,'s')

        Spdbuff('s2',0.1,10).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)




