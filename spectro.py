import wave
import nltk

from nltk.corpus.reader import TimitCorpusReader
from nltk.corpus import timit
import numpy

# itemid = 'dr1-fvmh0/sx206'
# spkrid , sentid = itemid.split('/')

# # item = TimitCorpusReader.utterance(spkrid, sentid)
# obj = TimitCorpusReader.wav(itemid)
# print(TimitCorpusReader.audiodata(item))

sampleRate = 16000.0 #16,000 hertz sample rate
obj = wave.open("LDC93S1.wav")

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