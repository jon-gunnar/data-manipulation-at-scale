import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    # record: (person, person's friend)
    key = record[0]
    mr.emit_intermediate(key, 1)


def reducer(key, list_of_values):
    # key: person
    # list_of_values: 1 for each friend
    mr.emit((key, sum(list_of_values)))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_data:
        mr.execute(input_data, mapper, reducer)
