import seaborn as sbn
import numpy as np
import matplotlib.pylab as plt
import scipy as sci
import functions
from scipy import signal
from scipy.io import wavfile
import librosa

def frequency_detector(time_loop, freq_loop, amplitudes, time, freq, dB):
    notes = []
    for i in range (0, time_loop): #time loop
        for j in range (0,freq_loop):
            if (amplitudes[j,i] > dB) and (librosa.hz_to_note(freq[j]) not in notes):
                notes.append(librosa.hz_to_note(freq[j]))

    return notes

def frequency_presence_detector(time_loop, freq_loop, amplitudes, time, freq, dB):
    notes = []
    notes_amplitudes = []
    biggest_amps = []
    index = np.array([])
    for i in range (0, time_loop): #time loop
        for j in range (0,freq_loop):
            if (amplitudes[j,i] > dB) and (freq[j] not in notes):
                notes.append(freq[j])
                notes_amplitudes.append(amplitudes[j,i])
                for k in range(i, time_loop):
                    if amplitudes[j,k] > notes_amplitudes[len(notes_amplitudes)-1]:
                        notes_amplitudes[len(notes_amplitudes)-1] = amplitudes[j,k]
    for i in range(0, len(notes)):
        notes[i] = librosa.hz_to_note(notes[i])
    uninotes = np.unique(notes)
    for i in range(0, len(uninotes)):
        index = np.where(np.asarray(notes) == uninotes[i])[0]
        intermittent = 0
        for j in range (0, len(index)):
            if notes_amplitudes[index[j]] > intermittent:
                intermittent = notes_amplitudes[index[j]]
        biggest_amps.append(intermittent)
    return uninotes, biggest_amps

def frequency_time_detector(time_loop, freq_loop, amplitudes, time, freq, dB):
    notes = []
    when = []
    note = ['0']
    for i in range (0, time_loop): #time loop
        for j in range (0,freq_loop):
            if (amplitudes[j,i] > dB) and (librosa.hz_to_note(freq[j]) not in notes or time[i]not in when):
                notes.append(librosa.hz_to_note(freq[j]))
                when.append(time[i])
                amplitudes[j,i] = 100
            else:
                amplitudes[j,i] = 0
    for i in range(1,freq_loop):
        note.append(librosa.hz_to_note(freq[i]))
    plt.pcolormesh(time, freq, amplitudes)
    plt.show()
    return