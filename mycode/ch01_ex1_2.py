import gzip
from pathlib import Path

import thinkstats2 as ts2

base_dir = Path(r'C:\Users\steve\dev\stats\ts2')
code = base_dir.joinpath('code')
mycode = base_dir.joinpath('mycode')
fem_resp_dct = code.joinpath('2002FemResp.dct')
fem_resp_dat = code.joinpath('2002FemResp.dat.gz')

databook = ts2.ReadStataDct(fem_resp_dct)
df = databook.ReadFixedWidth(fem_resp_dat, compression='gzip')

print(df.pregnum.value_counts())