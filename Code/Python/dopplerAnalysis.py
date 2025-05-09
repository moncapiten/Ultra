import numpy as np
import matplotlib
matplotlib.use('TKAgg')  # Use a non-interactive backend for matplotlib
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

path = '../../Data/doppler_20250509_102751/'
filename = 'dopplerShift-0-80000.txt'
tt, tx, rx = np.loadtxt(path+filename, unpack=True)


# fourier transform
freqs = np.fft.rfftfreq(len(tt), np.mean(np.diff(tt)))
ftx = np.abs(np.fft.rfft(tx))
frx = np.abs(np.fft.rfft(rx))

ftx /= np.max(ftx)
frx /= np.max(frx)

print(np.max(ftx), np.max(frx))

# plot the data
plt.figure(figsize=(10, 5))
plt.plot(freqs, ftx, label='tx')
plt.plot(freqs, frx, label='rx')


plt.xlim(5e6, 1e7)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (Hz)')

plt.show()