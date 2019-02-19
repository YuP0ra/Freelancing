from pymining import seqmining

with open('reviews_sample.txt') as file:
    lines = file.read().split('\n')

for i, line in enumerate(lines):
    lines[i] = line.split(' ')

freq_seqs = sorted(seqmining.freq_seq_enum(lines, 100))

with open('patterns.txt', 'w') as file:
    for res in freq_seqs:
        file.write(str(res[1]) + ':' + ';'.join(res[0])+'\n')
