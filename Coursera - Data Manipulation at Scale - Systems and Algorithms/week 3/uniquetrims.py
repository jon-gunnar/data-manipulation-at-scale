import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    # record: (sequence ID, string of nucleotides)
    value = record[1][:-10]
    mr.emit_intermediate('trimmed', value)


def reducer(key, list_of_values):
    # key: label
    # list_of_values: list of trimmed strings of nucleotides
    mr.emit(list(set(list_of_values)))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_data:
        mr.execute(input_data, mapper, reducer)
