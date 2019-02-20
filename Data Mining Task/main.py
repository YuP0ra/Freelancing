from pymining import seqmining
from libs import ContiguousSequentialPatterns


SAMPLES_PATH = 'reviews_sample.txt'
SUPPORT = 100

with open(SAMPLES_PATH) as file:
    lines = file.read().split('\n')

for i, line in enumerate(lines):
    lines[i] = line.split(' ')

freq_seqs = ContiguousSequentialPatterns(lines, SUPPORT, 10).patterns()

with open('patterns.txt', 'w') as file:
    for k in freq_seqs:
        file.write(str(freq_seqs[k]) + ':' + ';'.join(k.split(' '))+'\n')
