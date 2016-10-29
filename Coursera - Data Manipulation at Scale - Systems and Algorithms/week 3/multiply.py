import sys
import numpy as np

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    # record: (matrix, row, col, value)
    value = record[3]
    for i in range(5):
        if record[0] == 'a':
            key = (record[1], i)
            mr.emit_intermediate(key, (record[0], record[2], value))
        elif record[0] == 'b':
            key = (i, record[2])
            mr.emit_intermediate(key, (record[0], record[1], value))


def reducer(key, list_of_values):
    # key: label
    sparse_arrays = {
        'a': np.zeros(5),
        'b': np.zeros(5),
    }

    for v in list_of_values:
        sparse_arrays[v[0]][v[1]] = v[2]

    mr.emit((key[0], key[1], int(np.dot(sparse_arrays['a'], sparse_arrays['b']))))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_data:
        mr.execute(input_data, mapper, reducer)
