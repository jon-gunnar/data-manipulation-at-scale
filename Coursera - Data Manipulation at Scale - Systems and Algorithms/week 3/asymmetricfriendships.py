import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    # record: (person, person's friend)
    key = tuple(sorted(record))
    mr.emit_intermediate(key, record)


def reducer(key, list_of_values):
    # key: people in relationship in alphabetical order
    # list_of_values: 1 for each relationship
    if len(list_of_values) == 1:
        mr.emit(list_of_values[0])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_data:
        mr.execute(input_data, mapper, reducer)
