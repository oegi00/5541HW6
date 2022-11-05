import wave
import nltk

from nltk.corpus.reader import TimitCorpusReader
from nltk.corpus import timit

itemid = 'dr1-fvmh0/sx206'
spkrid , sentid = itemid.split('/')

item = TimitCorpusReader.utterance(spkrid, sentid)
obj = TimitCorpusReader.wav(itemid)


# print(TimitCorpusReader.audiodata(item))