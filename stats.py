import os
import numpy as np

f=os.listdir("n256")
#print(f) 

os.chdir('n256')

for nm in f:
	x=np.loadtxt(nm,usecols=(2))
	print(nm,x.mean(),x.std(),np.median(x))
