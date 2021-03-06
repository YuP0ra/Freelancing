from collections import defaultdict


class ContiguousSequentialPatterns:
    def __init__(self, seq_lines, min_support, max_seq_len=3):
        self.seq_lines = seq_lines
        self.min_support = min_support
        self.max_seq_len = max_seq_len

    def patterns(self):
        full_lookup_dict = defaultdict(int)
        final_dict = defaultdict(int)

        for line in self.seq_lines:
            for cegment_len in range(1, self.max_seq_len + 1):
                temp_line_set = []
                for i in range(len(line) - cegment_len + 1):
                    segment = ' '.join(line[i: i + cegment_len])
                    if not segment in temp_line_set:
                        temp_line_set.append(segment)
                        full_lookup_dict[segment] += 1

        for key in full_lookup_dict:
            if full_lookup_dict[key] >= self.min_support:
                final_dict[key] = full_lookup_dict[key]

        return final_dict
