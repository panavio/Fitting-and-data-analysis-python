import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import loadtxt
import math

eb=0.8
ec=0.95
wc=0.693147181/(27*60)#0.00042786863# 27 minutes
wb=0.693147181/(20*60)#0.0005776226505#20 minutes
wa=0.693147181/(3.1*60)#0.003726597745 #3.1 minutes
ratio=ec/eb
wratio=wc/wa
k=0.0130
ans=k*(wratio+1)
ans=ans/wb
ans=ans*(wb)
ans=-17/ans
print("wratio", ans)
