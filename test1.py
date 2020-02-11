import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,10)
print(x)
print("------")
f=open("linsp.txt","w")
y=-x*np.sin(2*x)*2
print (y)
for ii in range(len(x)):
	f.write(str(x[ii])+'   '+str(y[ii])+'\n')

plt.plot(x,y)
plt.show()
plt.close()

