import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    # record: (person, person's friend)
    key = tuple(sorted(record))
    mr.emit_intermediate(key, record)


def reducer(key, list_of_values):
    # key: (person, person's friend)
    # list_of_values: 1 for each relationship
    print(list_of_values)
    # if sum(list_of_values) == 1:
    #     mr.emit(key)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_data:
        mr.execute(input_data, mapper, reducer)
