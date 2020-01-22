import os
import numpy as np
f=os.listdir("n256")
#print(f) 
os.chdir('n256')
print("# 3SAT_results")
print("| Input | Mean | Std | Median | Min | Max |")
print("| ----- | -----| ---- |  ----- | ----- | ----- |")
for nm in sorted(f, key=lambda a : int(a.split('_')[-1])):
  x = np.loadtxt(nm, usecols=(2))
  #print(nm,x.mean(),x.std(),np.median(x),x.min(),x.max())
  idx = int(nm.split('_')[-1])
  vals = [idx, x.mean(), x.std(), np.median(x), x.min(), x.max()]
  print("| " + " | ".join([str(x) for x in vals]) + " |")
