import wave

import numpy as np
import matplotlib.pyplot as plt
import struct
import math # ask about library restriction

# itemid = 'dr1-fvmh0/sx206'
# spkrid , sentid = itemid.split('/')
# item = TimitCorpusReader.utterance(spkrid, sentid)
# obj = TimitCorpusReader.wav(itemid) #does not read the object?
# print(TimitCorpusReader.audiodata(itemid))
# sampleRate = 16000.0 #16,000 hertz sample rate

def transform_all(windows):
    print(len(windows))
    # print("f")
    transformed = []

    for window in windows:
        # print(i)
        transformed.append(transform(window))

    return transformed


def transform(window):
    fourier = np.fft.fft(window)
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
        windows.append(y_axis[i:i+(number_of_samples)])

    # print(windows)
    return windows
        

def main():
    obj = wave.open("LDC93S1.wav")
    totalFrames = obj.getnframes()
    print(totalFrames)
   
    step = 100

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

    # plt.plot(y_axis)
    # plt.show()
    # print(y_axis)
    print(y_axis.size)
    windows = windowize(y_axis)

    # print(windows[0])
    # print(windows[0][10])
    # print(windows[1])
    print(len(windows))
    print(len(windows[0]))

    test = np.array(transform_all(windows)) 
    # windows are not uniform; later windows are shorter as they are cut off

    plt.plot(test)
    # plt.show()

    # print(test)
    # imgplot = plt.imshow(test)

    # print(tranform_test)
    # print(len(tranform_test))

    
    #find min and max values
    #turn them into floats; scale them to -1 to 1 scale
    # need to figure out what should be the 0 or negative part of the graph

    # obj.setframerate(sampleRate)
    # print( "Number of channels",obj.getnchannels())
    # print ( "Sample width",obj.getsampwidth())
    # print ( "Frame rate.",obj.getframerate())
    # print ("Number of frames",obj.getnframes())
    # print ( "parameters:",obj.getparams())

if __name__ == '__main__':
    main()