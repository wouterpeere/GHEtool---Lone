import numpy as np
import matplotlib.pyplot as plt

Ts_avg = 11.9
Ts_ampl1 = 6.9
Ts_ampl2 = -0.6
PL1 = 20
PL2 = 28
a_s = 2 / (2.4*10**6) * 3600*24  #k_s/C
t_p = 365

def func(z, t):
    return Ts_avg - np.exp(-z*np.sqrt(np.pi/(a_s*t_p)))*Ts_ampl1*np.cos(2*np.pi/365*(t-PL1)-z*np.sqrt(np.pi/(a_s*t_p))) \
    + np.exp(-z*np.sqrt(2*np.pi/(a_s*t_p)))*Ts_ampl2*np.cos(4*np.pi/t_p*(t-PL2)-z*np.sqrt(2*np.pi/(a_s*t_p)))

z = 30
t = np.arange(0, 365)
print(t)

res = func(t, z)

plt.figure()
plt.plot(res)
plt.show()