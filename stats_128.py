import os
import numpy as np
f=os.listdir("n128")
#print(f) 
os.chdir('n128')

print("# 3SAT_results")
print("## Statistics on time 128 bits ")
print("| Input | Mean | Std | Median | Min | Max | Total time (m)|")
print("| -----: | -----:| ----: |  -----: | -----: | -----: | ----: |")
for nm in sorted(f, key=lambda a : int(a.split('_')[-1])):
  x = np.loadtxt(nm, usecols=(2))
  #print(nm,x.mean(),x.std(),np.median(x),x.min(),x.max())
  idx = int(nm.split('_')[-1])
  vals = [ x.mean(), x.std(), np.median(x), x.min(), x.max(),x.sum()/60]
  #print("| " + " | ".join([str(x) for x in vals]) + " |")
  entry = "| "+str(idx)
  for v in vals:
    entry += " | {:7.5f} ".format(v)
  entry += "|"
  print(entry)

print("## Statistics on iterations 128 bits")
print("| Input | Mean | Std | Median | Min | Max |")
print("| -----: | -----:| ----: |  -----: | -----: | -----: |")
for nm in sorted(f, key=lambda a : int(a.split('_')[-1])):
  it = np.loadtxt(nm, comments=None, usecols=(4),converters={4: lambda s: int(s[6:])},unpack=True)
  idx = int(nm.split('_')[-1])
  vals = [ it.mean(), it.std(), np.median(it), it.min(), it.max()]
  entry = "| "+str(idx)
  for v in vals:
    entry += " | {:10.0f} ".format(v)
  entry += "|"
  print(entry)
