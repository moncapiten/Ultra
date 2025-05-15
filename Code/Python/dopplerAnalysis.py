import numpy as np
import matplotlib
matplotlib.use('TKAgg')  # Use a non-interactive backend for matplotlib
import matplotlib.pyplot as plt
import pastamarkers

from scipy.optimize import curve_fit





#path = '../../Data/doppler_20250513_123343/'
#filename = 'dopplerShift-0-80000'
path = '../../Data/dopplerWithAngle_20250515_112543/'
filename = 'dopplerShift_0-0-80000'
numFiles = 20

movingtt, _, movingrx = [], [], []

for i in range(0, numFiles):
    specificFilename = filename + '_' + str(i) + '.txt'
    print(specificFilename)
    # Load the data from the file
    # The data is assumed to be in three columns: time, tx, rx  
    _tt, _tx, _rx = np.loadtxt(path+specificFilename, unpack=True)
    movingtt = movingtt + _tt.tolist()
#    tx = tx + _tx.tolist()
    movingrx = movingrx + _rx.tolist()









# fourier transform
movingfreqs = np.fft.rfftfreq(len(movingtt), np.mean(np.diff(movingtt)))
movingfrx = np.abs(np.fft.rfft(movingrx))

movingfrx /= np.max(movingfrx)

#print(np.max(ftx), np.max(frx))

# plot the data



















path1 = '../../Data/doppler_20250513_121050/'
filename1 = 'dopplerShift-0-0'

numFiles1 = 20

stoppedtt, _, stoppedrx = [], [], []

for i in range(0, numFiles1):
    specificFilename = filename1 + '_' + str(i) + '.txt'
    print(specificFilename)
    # Load the data from the file
    # The data is assumed to be in three columns: time, tx, rx  
    _tt, _tx, _rx = np.loadtxt(path1+specificFilename, unpack=True)
    stoppedtt = stoppedtt + _tt.tolist()
#    tx = tx + _tx.tolist()
    stoppedrx = stoppedrx + _rx.tolist()









# fourier transform
stoppedfreqs = np.fft.rfftfreq(len(stoppedtt), np.mean(np.diff(stoppedtt)))
stoppedfrx = np.abs(np.fft.rfft(stoppedrx))

stoppedfrx /= np.max(stoppedfrx)


























































from pastamarkers import pasta

# plot the data
plt.figure()
#plt.scatter(stoppedfreqs, stoppedfrx, marker = pasta.tortellini, s=1000, label='stoppedrx', linewidth=0.1)
#plt.scatter(movingfreqs, movingfrx, marker = pasta.farfalle, s=1000, label='stoppedrx', linewidth=0.1)
plt.scatter(stoppedfreqs, stoppedfrx, label='stoppedrx')
plt.scatter(movingfreqs, movingfrx, label='movingrx')


#plt.xlim(1, 5e4)
#plt.xscale('log')


plt.xlim(40.965e3, 40.97e3)
plt.legend()
plt.title('Fourier Transform of the received signals')

#plt.yscale('log')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude (normalized) [V/Hz]')

plt.grid(which='both', linestyle='-.', linewidth=0.5)

plt.show()




