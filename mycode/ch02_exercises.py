import pathlib
import sys

import thinkstats2 as ts

base = pathlib.Path(r'C:\Users\steve\dev\stats\ts2')
code = base.joinpath('code')
mycode = base.joinpath('mycode')
ts2 = base.joinpath('thinkstats2')
sys.path.insert(0, ts2)
sys.path.insert(0, mycode)
sys.path.insert(0, code)

from code.nsfg import ReadFemPreg, ReadFemResp

l = [1, 2, 3, 1, 4, 1, 2, 1, 5, 3, 1, 1, 1, 2, 6, 4, 9]

h = ts.Hist(l)

# ex 2-3
def all_modes(hist):
    """
    takes a ts.Hist object and returns a list of value, freq pairs, in descending order

    :param hist:
    :return:
    """

    return sorted(hist.Items(), key=lambda t: t[1], reverse=True)


def mode(hist):

    t = all_modes(hist)

    return t[0]


print(all_modes(h))

print(mode(h))

# ex 2-4
dct = code.joinpath('2002FemPreg.dct')
dat = code.joinpath('2002FemPreg.dat.gz')

preg = ReadFemPreg(dct_file=dct, dat_file=dat)

print


