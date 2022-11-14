import seaborn as sbn
import numpy as np
import matplotlib.pylab as plt
import scipy as sci

from scipy import signal
from scipy.io import wavfile

sr, aud_array = wavfile.read(r'C:\Users\jackk\OneDrive - South East Technological University (Waterford Campus)\college backup\semester 7\Digital Signal Processing\mini project\python files\vivaldi_V1.wav')

time = len(aud_array)/sr
x = np.linspace(0,time,len(aud_array))
#print(np.shape(aud_array))
if 0:
    plt.plot(x, aud_array,)
    plt.xlabel("time (s)"); plt.ylabel("Amplitude")
    plt.show()





#my periodogram
if 0:
    sig2 = aud_array[:,1]
    sig2 = ((abs(np.fft.fft(sig2)))**2)/(len(sig2)*sr)
    freqax = sci.fftpack.fftfreq(len(sig2),1.0/sr) #look into this
    plt.plot(freqax, 10*np.log10(sig2), label = 'channel 3')

if 0:
    sig0 = aud_array[:,0]
    freqax, power_spec_dens = signal.periodogram(sig0, sr,window='boxcar', detrend = False, return_onesided = False, scaling = "density")
    plt.plot(freqax, 10*np.log10(power_spec_dens), label = 'channel 1')
    plt.xlabel("Frequency (Hz)"); plt.ylabel("Amplitude (V^2/Hz)")
    plt.legend(loc="upper left")
    #plt.yscale("log")

# FFT
if 0:
    sig0 = aud_array[:,0]
    sig0 = abs(np.fft.fft(sig0/len(sig0)))
    freqax = sci.fftpack.fftfreq(len(sig0),1.0/sr) #look into this
    plt.plot(freqax, 20*np.log10(sig0), label = 'channel 1 - FFT')
    #plt.plot(freqax, 20*np.log10(sig1), label = 'channel 2')
    #plt.xlabel("Frequency (Hz)"); plt.ylabel("Amplitude (dB)")
    plt.legend(loc="upper left")
    #plt.yscale("log")

#welch
if 1:
    sig0 = aud_array[:,0]
    sig1 = aud_array[:,0]
    freqax0, power_spec_dens0 = signal.welch(x = sig0, fs = sr, window= 'hann',noverlap = 1024, nperseg = 2048, detrend = False, average='mean')
    freqax1, power_spec_dens1 = signal.welch(x = sig1, fs = sr, window= 'hann',noverlap = 0, nperseg = 2048, detrend = False, average='mean')
    print(np.shape(power_spec_dens0))
    plt.plot(freqax0, 10*np.log10(power_spec_dens0), label = 'channel 1 - Periodogram')
    #plt.plot(freqax1, 10*np.log10(power_spec_dens1), label = 'channel 2')
    plt.xlabel("Frequency (Hz)"); plt.ylabel(f"Amplitude (dB)")
    plt.legend(loc="upper right")
    #plt.yscale("log")
plt.show()
    
