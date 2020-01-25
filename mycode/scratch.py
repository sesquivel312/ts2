import thinkstats2 as ts
import thinkplot as tp

seq = [1,0,2,7,2,0,9,11,10,9,4,5,3,4,2,2,2]

h = ts.Hist(seq)
tp.Hist(h)
tp.Show()

