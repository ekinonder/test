import numpy as np

f=open("linsp.txt","r")
result=np.loadtxt(f)
print(result)
x=result[1,:]
y=result[2,:]

z=np.sin(x*y)

f=open('linsp2.txt',"w")
f.write(str(z))

plt.plot(sqrt(z),x*y)
plt.show()
