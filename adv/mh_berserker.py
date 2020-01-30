if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return MH_Berserker

class MH_Berserker(Adv):
    a1 = ('fs', 0.30)
    conf ={}
    conf['slot.a'] = Stellar_Show()+Resounding_Rendition()   
    conf['slot.d'] = Arctos() 
    conf['acl'] = """
        #fs=None
        #fs1=this.fs1
        #fs3=this.fs3
        `s1, fsc
        `s2, fsc
        `dodge, fsc
        `fs3
        """
    
    def init(this):
        conf_alt_fs = {
            1: {
                'dmg': 296 / 100.0,
                'sp': 600,
                'startup': (30+10) / 60.0,
                'recovery': 30 / 60.0,
            },
            # 2: {
            #     'fs.dmg': 424 / 100.0,
            #     'fs.sp': 960,
            #     # 'fs.startup'     : 19      / 60.0  ,
            #     # 'fs.recovery'    : 21      / 60.0  ,
            # },
            3: {
                'dmg': 548 / 100.0,
                'sp': 1400,
                'startup': 120 / 60.0,
                'recovery': 30 / 60.0,
                'hit': 1,
            }
        }

        this.conf['fs1'] = Conf(conf_alt_fs[1])
        this.a_fs1 = Action('fs1', this.conf['fs1'])
        this.a_fs1.atype = 'fs'
        this.a_fs1.interrupt_by = ['s']
        this.a_fs1.cancel_by = ['s','dodge']
        this.l_fs1 = Listener('fs1',this.l_fs1)

        this.conf['fs3'] = Conf(conf_alt_fs[3])
        this.a_fs3 = Action('fs3', this.conf['fs3'])
        this.a_fs3.atype = 'fs'
        this.a_fs3.interrupt_by = ['s']
        this.a_fs3.cancel_by = ['s','dodge']
        this.l_fs3 = Listener('fs3',this.l_fs3)
    
    def l_fs1(this, e):
        this.a_fs1.getdoing().cancel_by.append('fs1')
        this.a_fs1.getdoing().interrupt_by.append('fs1')
        this.fs_before(e)
        this.update_hits('fs')
        this.dmg_make('fs', this.conf.fs1.dmg, 'fs')
        this.fs_proc(e)
        this.think_pin('fs')
        this.charge('fs1',this.conf.fs1.sp)

    def fs1(this):
        return this.a_fs1()

    def l_fs3(this, e):
        this.a_fs3.getdoing().cancel_by.append('fs3')
        this.a_fs3.getdoing().interrupt_by.append('fs3')
        this.fs_before(e)
        this.update_hits('fs')
        this.dmg_make('fs', this.conf.fs3.dmg, 'fs')
        this.fs_proc(e)
        this.think_pin('fs')
        this.charge('fs3',this.conf.fs3.sp)

    def fs3(this):
        return this.a_fs3()

    def prerun(this):
        this.s1_debuff = Debuff('s1', 0.05, 10)

        this.s2_fs_boost = Selfbuff('s2', 0.80, -1, 'fs', 'buff')

        this.a3_crit = Modifier('a3', 'crit', 'chance', 0)
        this.a3_crit.get = this.a3_crit_get
        this.a3_crit.on()

    def a3_crit_get(this):
        return (this.mod('def') != 1) * 0.20

    def s1_proc(this, e):
        this.s1_debuff.on()

    def s2_proc(this, e):
        if not this.s2_fs_boost.get():
            this.s2_fs_boost.on()
    
    def fs_proc(this, e):
        this.s2_fs_boost.off()
    

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf)

