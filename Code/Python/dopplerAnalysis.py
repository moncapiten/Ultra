import numpy as np
import matplotlib
matplotlib.use('TKAgg')  # Use a non-interactive backend for matplotlib
import matplotlib.pyplot as plt
import pastamarkers
from pastamarkers import pasta

from scipy.optimize import curve_fit





#path = '../../Data/doppler_20250513_123343/'
#filename = 'dopplerShift-0-80000'
path = '../../Data/dopplerWithAngle_20250515_112543/'
filename = 'dopplerShift_0-0-80000'
numFiles = 20

lowth = 40965
highth = 40970











plt.figure()


paths = [ '../../Data/doppler_20250513_121050/',  '../../Data/dopplerWithAngle_20250515_112543/', '../../Data/dopplerWithAngle_20250515_112543/', '../../Data/dopplerWithAngle_20250515_112543/', '../../Data/dopplerWithAngle_20250515_112543/' ]
filenames = [ 'dopplerShift-0-0', 'dopplerShift_0-0-80000', 'dopplerShift_66-0-80000', 'dopplerShift_133-0-80000', 'dopplerShift_200-0-80000' ]

names = [ 'Stationary transmitter', '0° inclination', '29.7° inclination', '59.8° inclination', '90° inclination' ]
pastas = [ pasta.tortellini, pasta.farfalle, pasta.fusilli2, pasta.rigatoni, pasta.penne ]



for j in range(0, len(paths)):
    print(j)
    path1 = paths[j]
    filename1 = filenames[j]

    numFiles1 = 20

    tt, _, rx = [], [], []

    for i in range(0, numFiles1):
        specificFilename = filename1 + '_' + str(i) + '.txt'
        print(specificFilename)
        # Load the data from the file
        # The data is assumed to be in three columns: time, tx, rx  
        _tt, _tx, _rx = np.loadtxt(path1+specificFilename, unpack=True)
        tt = tt + _tt.tolist()
    #    tx = tx + _tx.tolist()
        rx = rx + _rx.tolist()





    # fourier transform
    freqs = np.fft.rfftfreq(len(tt), np.mean(np.diff(tt)))
    frx = np.abs(np.fft.rfft(rx))

    frx /= np.max(frx)

    tt, _, rx = [], [], []

    # mask the data
    mask = (freqs > lowth) & (freqs < highth)
    freqs = freqs[mask]
    frx = frx[mask]

#    plt.scatter(freqs, frx, label=names[j])
    plt.scatter(freqs, frx, marker = pastas[j], s=500, label=names[j], linewidth=0.1)
























































#from pastamarkers import pasta

# plot the data
#plt.figure()
#plt.scatter(stoppedfreqs, stoppedfrx, marker = pasta.tortellini, s=1000, label='rx', linewidth=0.1)
#plt.scatter(movingfreqs, movingfrx, marker = pasta.farfalle, s=1000, label='rx', linewidth=0.1)
#plt.scatter(stoppedfreqs, stoppedfrx, label='rx')
#plt.scatter(movingfreqs, movingfrx, label='rx')


#plt.xlim(1, 5e4)
#plt.xscale('log')


plt.xlim(40.965e3, 40.97e3)
plt.legend()
plt.title('Fourier Transform of the received signals')

#plt.yscale('log')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude (normalized) [pure]')

plt.grid(which='both', linestyle='-.', linewidth=0.5)

plt.show()
'''




import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=stoppedfreqs,
    y=stoppedfrx,
    mode='markers',
    name='rx'
))

fig.add_trace(go.Scatter(
    x=movingfreqs,
    y=movingfrx,
    mode='markers',
    name='rx'
))

fig.update_layout(
    title='Fourier Transform of the received signals',
    xaxis_title='Frequency [Hz]',
    yaxis_title='Amplitude (normalized) [V/Hz]',
    xaxis=dict(
        range=[40.965e3, 40.97e3],
        showgrid=True,
        gridwidth=0.5,
        gridcolor='lightgray'
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=0.5,
        gridcolor='lightgray'
    ),
    legend=dict(title='Signals')
)

fig.show()



'''



