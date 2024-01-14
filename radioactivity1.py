import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import loadtxt
import math
filename="G:\\My Drive\\University Year 2\\exponential.txt"

data=loadtxt(filename, usecols=(0,1,2,3), skiprows=1, unpack=True)
xdata = data[0]
ydata = data[1]
xerror = data[2]
yerror = data[3]   

def least_square(t, R, A_obs_0, t2):
  eb=0.8
  ec=0.95
  wc=0.693147181/(27*60)#0.00042786863# 27 minutes
  wb=0.693147181/(20*60)#0.0005776226505#20 minutes
  ratio=ec/eb
  wratio=wc/(wc-wb)
  print("wratio", wratio)
  eeb=np.exp(-wb*(t+t2))
  eec=np.exp(-wc*(t+t2))
  return A_obs_0 *(1+ratio*R+ratio*wratio*(eeb-eec))

def decay(t, A, t2):
   w=0.00001750371668
   return A*np.exp(-w*(t-t2))

def decay1(t, A, t2, w):
   return A*np.exp(-w*(t-t2))

resd,dc = curve_fit(decay, xdata[-20:-1], ydata[-20:-1],p0=(1.0, 7000))
#print(xdata[-40:-1], ydata[-40:-1])
print(resd)
yfdata=ydata-(decay(xdata, resd[0], resd[1]))

resdt,dc = curve_fit(decay1, xdata, ydata,p0=(1.0, 7000,0))
resdf,dc = curve_fit(decay1, xdata, yfdata,p0=(1.0, 7000,0))
plt.plot(xdata,(decay(xdata, resd[0], resd[1])),'-')
plt.plot(xdata,(decay1(xdata, resdt[0], resdt[1], resdt[2])),'-', color='green')
#plt.plot(xdata, ydata,  alpha=0.3, color='green')
plt.plot(xdata, decay1(xdata, resdf[0], resdf[1], resdf[2]), '-', color='red')
#plt.plot(xdata, yfdata,  alpha=0.3, color='red')
plt.errorbar(xdata, yfdata, alpha=0.3, color='red', xerr=xerror, yerr=yerror, fmt='.')
plt.errorbar(xdata, ydata, xerr=xerror, yerr=yerror, fmt='.',  alpha=0.3, color='green')
plt.xlabel('time')
plt.ylabel('beta decays detected (N)')
plt.title("Beta decays detected over time")
plt.legend(['thoron decay', 'beta decay detected', 'radon decay detected'], loc='upper right')
plt.grid()
plt.show()
plt.xlabel('time')
plt.ylabel('beta decays detected (N)')
plt.title("Beta decays detected over time")
plt.legend(['thoron decay', 'beta decay detected', 'radon decay detected'], loc='upper right')
plt.grid()
plt.plot(xdata, decay1(xdata, resdf[0], resdf[1],resdf[2]), '-', color='green')
plt.plot(xdata, decay(xdata, resd[0], resd[1]), '-', color='red')
plt.legend(['radon decay detected','thoron decay'], loc='upper right')

plt.yscale('log')  
plt.show()


resfit, pcov = curve_fit(least_square, xdata, yfdata, p0=(1.5,200,1000),maxfev=100000000)


R=resfit[0]
A_obs_0=resfit[1]

print("R=",R, "A_obs_0 = ", A_obs_0, "t2 = ", resfit[2])
curvey=least_square(xdata, R, A_obs_0, resfit[2])
#plt.plot(xdata,yfdata,'*')
plt.errorbar(xdata, yfdata, alpha=0.3,xerr=xerror, yerr=yerror, fmt='.')
plt.plot(xdata,curvey,'r')
plt.grid()
plt.xlabel('time')
plt.ylabel('beta decays detected (N)')
plt.title("Beta decays detected over time fitted to RaB-RaC equation (6)")
plt.legend(['radon decay', 'least square fit'], loc='upper right')
plt.show()
print("first=", curvey[0])
#res= curve_fit(least_square, xdata, ydata,p0=(1,10))
print(ydata[1], yerror[1])
yaerror=np.sqrt(abs(yfdata))
print(yfdata[1], "yerror=", yaerror[1])
residuals = yfdata - curvey
#print('residuals:', residuals)

chi_squared = 0
for i in range(len(yaerror)):
  chi_squared += ((residuals[i])**2 / (yaerror[i])**2)
print('Chi squared:', chi_squared)

degrees_of_freedom = len(yfdata) - 2
reduced_chi_squared = chi_squared / degrees_of_freedom
print("Reduced chi squared = ", reduced_chi_squared)

fig, ax = plt.subplots()

# Plot the residuals against the current
ax.scatter(xdata, residuals, marker='o', color='blue')
ax.axhline(y=0, color='red', linestyle='--')  # Add a horizontal line at y=0 for reference

# Set the labels and title
ax.set_xlabel('time (s)')
ax.set_ylabel('Beta decay count of radon (N)')
ax.set_title('Residuals of Beta decay count of radon (N) as a Function of time (s)')

# Add grid lines
ax.grid(True)

# Display the plot
plt.show()

#print(popt)

xd=np.linspace(-4200, 10000, 1000)
plt.plot(xd, least_square(xd, resfit[0], resfit[1], resfit[2]), alpha=0.3)
plt.plot(xdata,curvey,'r')
plt.grid()
plt.xlabel('time')
plt.ylabel('beta decays detected (N)')
plt.title("Beta decays detected over time fitted to RaB-RaC equation (6)")
plt.legend(['radon decay', 'least square fit'], loc='upper right')
plt.show()
#res= curve_fit(least_square, xdata, ydata,p0=(1,10))