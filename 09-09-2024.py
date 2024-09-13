import matplotlib.pyplot as plt    #matplotlib is an visualization library.

x = [1,2,3,4,5]
y = [6,7,8,9,10]

plt.plot(x,y,marker = 'o', ms=30)   #plotting x & y coordinates. marker isused to indicate the datapoints with custom shapess
plt.title('sample plot')
plt.show()

