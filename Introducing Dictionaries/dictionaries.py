course = {'teacher':'Ashley','title':'Introducing Doctionaries','level':'Beginner'}

print(course['teacher'])

course.keys() # gets a list of all keys in the dictionary

course.values() # gets a list of all values
course['teacher'] = 'Nikita'

print(course['teacher'])
course['stages'] = 2
print(course['stages'])
del(course['stages'])


for item in course:
    print(item)

for key, value in course.items():
    print(key)
    print(value)


