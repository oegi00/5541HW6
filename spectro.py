import wave
import numpy as np
import matplotlib.pyplot as plt
import struct
import math # ask about library restriction
import sys


def transform_all(windows):
    transformed = []
    for window in windows:
        transformed_info = transform(window)
        if not(transformed_info is None):
            transformed.append(transformed_info)
    return transformed

def transform(window):
    if (window is None): 
        return None
    try:
        fourier = np.fft.fft(window)
    except:
        print(window)
        print(type(window))
    ls = []
    
    for number in fourier: #CHECK HERE
        magnitude = math.pow(number.real, 2) + math.pow(number.imag, 2)
        square_magnitude = math.sqrt(magnitude) 
        log_scaled = 10 * math.log(square_magnitude,10) 
        ls.append(log_scaled)

    return ls

#to find the # of samples for a given size and given frames, do sampling rate*size
def windowize(y_axis, step = 10, size = 25, sampling_rate = 16000):
    number_of_samples = int(sampling_rate*(size/1000))
    step = int(sampling_rate*(step/1000))
    windows = []

    for i in range(0, y_axis.size, step): #CHECK HERE?
        # if ((i + number_of_samples) > y_axis.size): #attempt to ensure array is completely square
        #     first = np.copy(y_axis[i:i+(number_of_samples)])
        #     filled = first.resize(400)
        #     #diff = (i + number_of_samples) - y_axis.size
        #     windows.append(filled)
        if (i+number_of_samples > y_axis.size):
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

    for i in range(totalFrames):   
        frames = obj.readframes(1)
        y_axis.append(struct.unpack("<h", frames)[0])
    obj.close()

    y_axis = np.array(y_axis)
    max = np.amin(y_axis)
    min = np.amax(y_axis)

    #CHECK HERE
    standardize = lambda x: (x - min)/(max-min) #standardizing here makes the constrast slightly higher
    y_axis = standardize(y_axis)

    print(y_axis.size)
    windows = windowize(y_axis)
    print(len(windows))

    #transformed is the list of lists of frequency magnitude
    transformed = np.array(transform_all(windows)) 

    # transformed = transformed.T[200:,:] #attempt to lighten up the graph, comment out later
        
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

    # tr_min += 30 #manual changing, delete later
    # tr_max -= 20
    print(tr_min)
    print(tr_max)

    #normalize and scale all values to 0-255
    for transformed_window in transformed: #CHECK HERE
        temp = []
        for data in transformed_window:
            # temp.append((float(data))*-1) #ask prof/ta about weird coloring?
            # fix the coloring????
            temp.append(255 - abs((data - tr_min) / (tr_max - tr_min)*255)) #check with the ta if we're doing this correctly
        norm.append(temp)

    
    norm = np.array(norm).T[200:,:]
    # norm = np.array(norm) #comment out
     
    print(norm[0]) #one or two random values that are 0, everything else is light??
    plt.imshow(norm, cmap='gray', vmin=0, vmax=255) #0 should be black, not white like specified in the warmup?
    plt.title(f"Spectrogram of {filename}")
    plt.ylabel("Frequency")
    plt.xlabel("Window")
    # ax = plt.axes()
    # ax.set_facecolor("white")
    plt.show()
    

if __name__ == '__main__':
    main()

    