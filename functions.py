import seaborn as sbn
import numpy as np
import matplotlib.pylab as plt
import scipy as sci
import functions
from scipy import signal
from scipy.io import wavfile
import librosa
import math

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
    timing_list = []
    intermittent = []
    first = 1
    for i in range (0, time_loop): #time loop
        for j in range (0,freq_loop):
            if amplitudes[j,i] > dB:
                amplitudes[j,i] = 100
                if librosa.hz_to_note(freq[j]) not in notes:
                    notes.append(librosa.hz_to_note(freq[j]))
                    timing_list.append([time[i]])
                else:
                    timing_list[notes.index(librosa.hz_to_note(freq[j]))].append(time[i])
            else:
                amplitudes[j,i] = 0
    #plotting
    if 1:
        plt.figure(figsize=(10,6))
        plt.pcolormesh(time, freq, amplitudes)
        plt.xlabel("Time (sec)"); plt.ylabel("frequency (Hz)")
        plt.title('STFT Channel 1 - present frequencies')
        plt.show()
    # sub plots of timing graphs and longest time a note is present
    if 0:
        figure, axis = plt.subplots(math.ceil(len(notes)/3),1)
        notes_time_period = []
        for i in range(0,len(notes)):
            num = 0
            max_consec = 0
            for j in range(0,len(time)):
                if time[j] in timing_list[i]:
                    intermittent.append(1+i)
                    num = num + 1
                    if num > max_consec:
                        max_consec = num
                        
                else:
                    intermittent.append(0)
                    num = 0

            time_period = (time[j] - time[j-max_consec])*1000
            notes_time_period.append(time_period)
            axis[int(i/3)].step(time, intermittent, label = notes[i])
            intermittent.clear()
        for ax in axis:
            ax.set(xlabel= "time (sec)", ylabel = "present or not")
            ax.legend(loc = "upper right")
        print(notes, notes_time_period)
    #plot one timing graph with dictionary value
    if 0:
        search_note = "E6"
        for each_time in time:
                if each_time in timing_list[notes.index(search_note)]:
                    intermittent.append(1)
                else:
                    intermittent.append(0)
        plt.step(time,intermittent)
        plt.title("timing diagram for presence of - " + search_note)
        plt.xlabel("Time (sec)"); plt.ylabel("Present or not")
    plt.show()
    return
