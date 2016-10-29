import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    # record: (document name, document contents)
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)


def reducer(key, list_of_values):
    # key: word
    # list_of_values: list of documents it appears in
    mr.emit((key, list(set(list_of_values))))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_data:
        mr.execute(input_data, mapper, reducer)
