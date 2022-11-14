import seaborn as sbn
import numpy as np
import matplotlib.pylab as plt
import scipy as sci

from scipy.io import wavfile

sr, aud_array = wavfile.read(r'C:\Users\jackk\OneDrive - South East Technological University (Waterford Campus)\college backup\semester 7\Digital Signal Processing\mini project\python files\vivaldi_V1.wav')

time = len(aud_array)/sr
x = np.linspace(0,time,len(aud_array))
#print(np.shape(aud_array))
if 0:
    plt.plot(x, aud_array,)
    plt.xlabel("time (s)"); plt.ylabel("Amplitude")
    plt.show()


if 0:
    #for i in range(0,2):
    aud_array[:,1] = abs(np.fft.fft(aud_array[:,1]))
    plt.plot(aud_array[:,1])
    plt.show()




#frequency domain
if 1:
    sig0 = aud_array[:,0]
    sig0 = abs(np.fft.fft(sig0/len(sig0)))
    sig1 = aud_array[:,1]
    sig1 = abs(np.fft.fft(sig1/len(sig1)))
    freqax = sci.fftpack.fftfreq(len(sig1),1.0/sr) #look into this
    plt.plot(freqax, 20*np.log10(sig0), label = 'channel 1')
#    plt.plot(freqax, 20*np.log10(sig1), label = 'channel 2')
    plt.xlabel("Frequency (Hz)"); plt.ylabel("Amplitude (dB)")
    plt.legend(loc="upper left")
    #plt.yscale("log")
    plt.show()




#own attempt of freq domain
if 0:
    sig0 = aud_array[:,0]
    sig0 = abs(np.fft.fft(sig0/len(sig0)))
    sig1 = aud_array[:,1]
    sig1 = abs(np.fft.fft(sig1/len(sig1)))
    freqax = np.linspace(-sr/2,sr/2,len(sig0))
    plt.plot(freqax, sig0)
    #plt.plot(freqax, sig1)
    #plt.yscale("log")
    plt.show()
    print(freqax)
    