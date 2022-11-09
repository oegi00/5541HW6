import wave
import nltk

from nltk.corpus.reader import TimitCorpusReader
from nltk.corpus import timit
import numpy as np
import matplotlib.pyplot as plt
import time

# itemid = 'dr1-fvmh0/sx206'
# spkrid , sentid = itemid.split('/')
# item = TimitCorpusReader.utterance(spkrid, sentid)
# obj = TimitCorpusReader.wav(itemid) #does not read the object?
# print(TimitCorpusReader.audiodata(itemid))
# sampleRate = 16000.0 #16,000 hertz sample rate

#to find the # of samples for a given size and given frames, do sampling rate*size
def windowize(y_axis, step = 10, size = 25, sampling_rate = 16000):
    #number_of_samples = sampling_rate*size

    # 1 / 0.025 s = 40 hz

    windows = []
    for i in range(0, y_axis.size, step):
        windows.append(y_axis[i:i+size])

    # print(windows)
    return windows
        

def main():
    obj = wave.open("LDC93S1.wav")
    totalFrames = obj.getnframes()
    print(totalFrames)
    frames = obj.readframes(totalFrames)
    step = 100

    x_axis = np.array(range(0, totalFrames))
    y_axis = np.array([x for x in frames])

    max = np.amin(y_axis)
    min = np.amax(y_axis)

    standardize = lambda x: (x - min)/(max-min)
    y_axis = standardize(y_axis)

    # plt.plot(y_axis)
    # plt.show()
    # print(y_axis)
    print(y_axis.size)
    windows = windowize(y_axis)

    print(windows[0])
    print(windows[0][10])
    print(windows[1])

    obj.close()
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