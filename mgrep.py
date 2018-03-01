import sys

from gensim.models import KeyedVectors
word_vectors = KeyedVectors.load_word2vec_format('model', binary=False)

s = word_vectors.most_similar(sys.argv[1])

for x in range(0,int(sys.argv[2])):
    print(s[x][0])





