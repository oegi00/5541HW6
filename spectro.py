import wave
import numpy as np
import matplotlib.pyplot as plt
import struct
import math # ask about library restriction
from PIL import Image #is this one usable?


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
    
    for number in fourier:
        magnitude = math.pow(number.real, 2) + math.pow(number.imag, 2)
        square_magnitude = math.pow(magnitude, 0.5) 
        log_scaled = 10 * math.log(square_magnitude,10) 
        # print(log_scaled) # are they all supposed to be negative?

        ls.append(log_scaled)
        
    return ls

#to find the # of samples for a given size and given frames, do sampling rate*size
def windowize(y_axis, step = 10, size = 25, sampling_rate = 16000):
    number_of_samples = int(sampling_rate*(size/1000))
    step = int(sampling_rate*(step/1000))
    # 1 / 0.025 s = 40 hz
    windows = []
    for i in range(0, y_axis.size, step):
        if ((i + number_of_samples) > y_axis.size): #attempt to ensure array is completely square
            first = np.copy(y_axis[i:i+(number_of_samples)])

            filled = first.resize(400)

            #diff = (i + number_of_samples) - y_axis.size

            windows.append(filled)

        else:
            windows.append(y_axis[i:i+(number_of_samples)])

    return windows

# def visualization():
    # obj = wave.open("LDC93S1.wav")
    # totalFrames = obj.getnframes()
   
    # # step = 100

    # x_axis = np.array(range(0, totalFrames))
    # y_axis = []

    # for i in range(totalFrames):   
    #     frames = obj.readframes(1)
    #     y_axis.append(struct.unpack("<h", frames)[0])

    # obj.close()

    # y_axis = np.array(y_axis)

    # max = np.amin(y_axis)
    # min = np.amax(y_axis)

    # standardize = lambda x: (x - min)/(max-min)
    # y_axis = standardize(y_axis)

    # windows = windowize(y_axis)

    # plt.specgram(test,Fs=16000)
    # plt.show()


def main(filename = "LDC93S1.wav"):
    obj = wave.open(filename) #how to accept arguments
    totalFrames = obj.getnframes()
    print(totalFrames)

    x_axis = np.array(range(0, totalFrames))
    y_axis = []

    for i in range(totalFrames):   
        frames = obj.readframes(1)
        y_axis.append(struct.unpack("<h", frames)[0])
    obj.close()
    # y_axis = np.array(struct.iter_unpack("<h",frames))

    y_axis = np.array(y_axis)

    max = np.amin(y_axis)
    min = np.amax(y_axis)

    standardize = lambda x: (x - min)/(max-min)
    y_axis = standardize(y_axis)


    print(y_axis.size)
    windows = windowize(y_axis)
    
    print(len(windows))


    print(windows[293-1])

    # print(len(windows))
    # print(len(windows[0]))

    #transformed is the list of lists of frequency magnitude
    transformed = np.array(transform_all(windows)) 
    # windows are not uniform; later windows are shorter as they are cut off

    # for i in transformed:
    #     print(len(i))

    # print(transformed[0])

        
    #normalize
    norm = []

    tr_max = transformed[0][0]
    tr_min = transformed[0][0]

    for window in transformed:
        temp_max = np.max(window)
        temp_min = np.min(window)

        if (temp_max > tr_max):
            tr_max = temp_max
        
        if (temp_min < tr_min):
            tr_min = temp_min

    print(tr_min)
    print(tr_max)

    for transformed_window in transformed:
        temp = []
        for data in transformed_window:
            # temp.append((float(data))*-1) #ask prof/ta about weird coloring?
            temp.append(abs((data - tr_max) / (tr_max - tr_min)) * 255) #check with the ta if we're doing this correctly
        norm.append(temp)

    norm = np.array(norm)

    print(norm[0])
    
    
    #plt.specgram(test,Fs=16000)

    # img = Image.fromarray(norm) #is using img fine?
    # img.show()

    plt.imshow(norm)
    # plt.figure()
    plt.title(f"Spectrogram of {filename}")
    plt.ylabel("Frequency")
    plt.xlabel("Time")
    
    plt.show()

    # obj.setframerate(sampleRate)
    # print( "Number of channels",obj.getnchannels())
    # print ( "Sample width",obj.getsampwidth())
    # print ( "Frame rate.",obj.getframerate())
    # print ("Number of frames",obj.getnframes())
    # print ( "parameters:",obj.getparams())
    # should we make it take command line arguments?


if __name__ == '__main__':
    main()

    