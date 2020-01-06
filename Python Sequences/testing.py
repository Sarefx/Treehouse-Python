docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'


if 'tuple' in docs:
    print('tuple is here')
else:
    print('tuple is not here')

print(docs.count('tuple'))


teachers = ['alena', 'ashley', 'nicole']

print(teachers.index('nicole'))