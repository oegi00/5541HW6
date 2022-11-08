import wave
import nltk

from nltk.corpus.reader import TimitCorpusReader
from nltk.corpus import timit
import numpy

itemid = 'dr1-fvmh0/sx206'
spkrid , sentid = itemid.split('/')

# item = TimitCorpusReader.utterance(spkrid, sentid)
obj = TimitCorpusReader.wav(itemid) #does not read the object?
print(TimitCorpusReader.audiodata(itemid))

sampleRate = 16000.0 #16,000 hertz sample rate
obj = wave.open("LDC93S1.wav")
#find min and max values
#turn them into floats; scale them to -1 to 1 scale
# need to figure out what should be the 0 or negative part of the graph

# obj.setframerate(sampleRate)
# print( "Number of channels",obj.getnchannels())
# print ( "Sample width",obj.getsampwidth())
# print ( "Frame rate.",obj.getframerate())
# print ("Number of frames",obj.getnframes())
# print ( "parameters:",obj.getparams())

totalFrames = obj.getnframes()
print(totalFrames)

frames = obj.readframes(totalFrames)
step = 100
x_axis = range(0, totalFrames, step)
y_axis = []

for i in x_axis:
    y_axis.append(frames[i])

print(len(x_axis))
print(len(y_axis))

import matplotlib.pyplot as plt
import time

plt.plot(x_axis, y_axis)
plt.show()
#time.sleep(5)
#plt.close()

obj.close()