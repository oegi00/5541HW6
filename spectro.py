#written by Angie Chen (chen7313) and Omonigho (egi00002)

import wave
import numpy as np
import matplotlib.pyplot as plt
import struct
import math
import sys

hamming_scale = np.hamming(400) #hamming function

#apply fourier transformation on all of the windows
def transform_all(windows):
    transformed = []
    for window in windows:
        transformed_info = transform(window)
        if not(transformed_info is None):
            transformed.append(transformed_info)
    return transformed

#fourier transform on a single window
def transform(window):
    for i, wi in enumerate(window): #apply the hamming function
        window[i] = wi * hamming_scale[i]

    if (window is None): 
        return None
    try:
        fourier = np.fft.fft(window)
    except:
        print(window)
        print(type(window))
    ls = []

    #grab the first half of the array
    fourier = fourier[:200]
    
    for number in fourier: #log of square magnitude
        magnitude = math.pow(number.real, 2) + math.pow(number.imag, 2)
        square_magnitude = math.sqrt(magnitude) 
        
        try:
            log_scaled = 10 * math.log(square_magnitude,10) 
        except:
            print(square_magnitude)
            log_scaled = 0 #if error (typically value error, subsitute with a 0)
        ls.append(log_scaled)

    return ls

#to find the # of samples for a given size and given frames, do sampling rate*size
def windowize(y_axis, step = 10, size = 25, sampling_rate = 16000):
    number_of_samples = int(sampling_rate*(size/1000))
    step = int(sampling_rate*(step/1000))
    windows = []

    for i in range(0, y_axis.size, step):
        if (i+number_of_samples > y_axis.size): #hits the boundaries; data not worth including
            break
        else:
            windows.append(y_axis[i:i+(number_of_samples)])

    return windows


def main():
    filename = sys.argv[1]
    obj = wave.open(filename) 
    totalFrames = obj.getnframes()
    print(totalFrames)

    y_axis = []

    for i in range(totalFrames):   #read file
        frames = obj.readframes(1)
        y_axis.append(struct.unpack("<h", frames)[0])
    obj.close()

    y_axis = np.array(y_axis)

    print(y_axis.size)
    windows = windowize(y_axis)
    print(len(windows))

    #transformed is the list of lists of frequency magnitude
    transformed = np.array(transform_all(windows)) 
        
    #normalize
    norm = []
    #get max, min of all of transformed
    tr_max = transformed[0][0]
    tr_min = transformed[0][0]
    for window in transformed:
        temp_max = np.max(window)
        temp_min = np.min(window)
        if (temp_max > tr_max):
            tr_max = temp_max
        if (temp_min < tr_min):
            tr_min = temp_min

    print(tr_min) #debugging
    print(tr_max)

    #normalize and scale all values to 0-255
    for transformed_window in transformed:
        temp = []
        for data in transformed_window: #normalize the value, then scale to 0-255 and flip
            temp.append(255- abs((data - tr_min) / (tr_max - tr_min)*255))
        norm.append(temp)

    norm = np.array(norm).T #rotate the graph
    norm = np.flip(norm,axis=0) #reflect the graph (to be right side up)

    #graphing spectrogram
    plt.imshow(norm, cmap='gray', vmin=0, vmax=255)
    plt.title(f"Spectrogram of {filename}")
    plt.ylabel("Frequency")
    plt.xlabel("Window")
    plt.show()
    

if __name__ == '__main__':
    main()

    