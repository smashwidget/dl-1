import adv.adv_test
import adv

def module():
    return Taro

class Taro(adv.Adv):
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=1)

