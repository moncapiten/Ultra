import numpy as np
import matplotlib
matplotlib.use('TKAgg')  # Use a non-interactive backend for matplotlib
import matplotlib.pyplot as plt
import pastamarkers

from scipy.optimize import curve_fit

#path = '../../Data/doppler_20250509_102751/'
#filename = 'dopplerShift-0-80000'
#path1 = '../../Data/doppler_20250513_090948/'
#filename1 = 'dopplerShift-0-0'
#path = '../../Data/doppler_20250513_091749/'
#filename = 'dopplerShift-0-80000'
#numFiles = 6
#numFiles1 = 8



path = '../../Data/doppler_20250513_123343/'
filename = 'dopplerShift-0-80000'
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


#movingnewtt = []
#movingshift = 0
#for i in range(len(movingtt)):

#    movingnewtt.append( ( movingtt[i] ) + movingshift )

#    if( i != len(movingtt)-1 and movingtt[i] > 0 and movingtt[i+1] < 0):
#        movingshift = movingnewtt[-1] - movingtt[i+1]

#movingtt = movingnewtt







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


#stoppednewtt = []
#stoppedshift = 0
#for i in range(len(stoppedtt)):
#    stoppednewtt.append( ( stoppedtt[i] ) + stoppedshift )

#    if( i != len(stoppedtt)-1 and stoppedtt[i] > 0 and stoppedtt[i+1] < 0):
#        stoppedshift = stoppednewtt[-1] - stoppedtt[i+1]

#stoppedtt = stoppednewtt







# fourier transform
stoppedfreqs = np.fft.rfftfreq(len(stoppedtt), np.mean(np.diff(stoppedtt)))
stoppedfrx = np.abs(np.fft.rfft(stoppedrx))

stoppedfrx /= np.max(stoppedfrx)

#print(np.max(ftx), np.max(frx))

























































from pastamarkers import pasta

# plot the data
plt.figure()
plt.scatter(stoppedfreqs, stoppedfrx, marker = pasta.tortellini, s=1000, label='stoppedrx')
plt.scatter(movingfreqs, movingfrx, marker = pasta.farfalle, s=1000, label='stoppedrx')

#plt.xlim(1, 5e4)
#plt.xscale('log')


plt.xlim(40.95e3, 40.98e3)
plt.legend()
plt.title('Fourier Transform of the received signals')

#plt.yscale('log')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude (normalized) [V/Hz]')

plt.grid(which='both', linestyle='-.', linewidth=0.5)

plt.show()









#from scipy.signal import correlate
#def calcola_sfasamento(ch1, ch2):
#    # Calcolare la correlazione incrociata
#    correlation = correlate(ch1, ch2, mode='full')
#    sfasamento = (np.argmax(correlation) - len(ch1) + 1)*10**(3-int(np.floor(np.log10(np.abs(5e5)))))
#    return sfasamento, correlation




#smallwindowstopped = [ i for i in stoppedfreqs if i > 39.9e3 and i < 40.1e3 ]
#smallwindowmoving = [ i for i in movingfreqs if i > 39.9e3 and i < 40.1e3 ]

#print( calcola_sfasamento(smallwindowmoving, smallwindowstopped) )


#calcola_sfasamento(movingrx, stoppedrx)














