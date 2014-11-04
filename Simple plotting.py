
# # Written by Duncan Forgan, 24/02/14
# # Simple script to demonstrate plotting of data in files
# # This uses the numpy and matplotlib modules, which are
# # extremely popular, and basically all you need to do
# # scientific computing in Python
# 
# # This code recreates the now-viral "Internet Explorer Use vs Murder Rate"
# # plot that has been circling the internet

import numpy as np
import matplotlib.pyplot as plt


data=np.genfromtxt('mydata.dat', dtype=None, names=True)

yearmin = np.amin(data['Year'])
yearmax = np.amax(data['Year'])

internetmin = np.amin(data['Internet_Explorer_Market_Share'])
internetmax = np.amax(data['Internet_Explorer_Market_Share'])

murdermin = np.amin(data['US_Murder_Rate'])
murdermax = np.amax(data['US_Murder_Rate'])

data.dtype.names[0]

plt.suptitle("Internet Explorer Use vs US Murder Rate", fontsize=12)
plt.plot(data['Year'], data['Internet_Explorer_Market_Share'])

plt.xlabel('Year', fontsize=12)
plt.ylabel('Internet Explorer Market Share', fontsize=12)

ax = plt.gca()

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

fig.suptitle("Internet Explorer Use vs US Murder Rate", fontsize=12)
ax1.plot(data['Year'], data['Internet_Explorer_Market_Share'], label="Internet Market Share")
#ax1.scatter(data['Year'], data['Internet_Explorer_Market_Share'], label="Internet Market Share")
ax1.xaxis.get_major_formatter().set_useOffset(False)

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Internet Explorer Market Share', fontsize=12)

ax2.bar(data['Year'], data['US_Murder_Rate'], facecolor='blue', alpha=0.1,  label="Murder Rate")
ax2.set_ylabel('US Murder Rate', fontsize=12)
ax2.set_ylim(murdermin, murdermax)

ax1.legend(loc=(0.4,0.85), frameon=0)
ax2.legend(loc=(0.4,0.75), frameon=0)


#fig.savefig('myPlot.ps') # works fine when no second axis but the right-hand y-axis gets cutoff

#change positions of axes plot wrt to plot area when saving a postscript
plt.gcf().subplots_adjust(right=0.8)
fig.savefig('myPlot2.ps')

#or save as .png
fig.savefig('myPlot2.png',dpi=100,bbox_inches='tight',pad_inches=0.2)


