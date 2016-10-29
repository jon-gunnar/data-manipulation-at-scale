import itertools
import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    # key: order id
    key = record[1]
    mr.emit_intermediate(key, record)


def reducer(key, list_of_values):
    # key: order id
    # list_of_values: order details
    joined = [p[0] + p[1] for p
              in itertools.combinations(list_of_values, 2)
              if p[0][0] != p[1][0]]

    for line in joined:
        mr.emit(line)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_data:
        mr.execute(input_data, mapper, reducer)
