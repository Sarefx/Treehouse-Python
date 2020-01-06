import re

names_file = open("names.txt")
data = names_file.read()
names_file.close()

#print(data)

#last_name = r'Love'

#print(re.match(r'Love',data))
#print(re.search(r'Kenneth',data))
#print(re.search(r'\(\d{3}\) \d\d\d-\d\d\d\d',data))
#print(re.search(r'\w+, \w+',data))
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}',data))
#print(re.findall(r'\w*, \w+',data))

#print(re.findall(r'[-\w\d+.]+@[-\w\d+.]+' , data))
#print(re.findall(r'[trehous]{9}\b' , data , re.I))

print(re.findall(r"""
  \b[-\w]+,
  \s
  [-\w ]+
  [^\t\n]
""", data, re.X))

print(re.findall(r'''
([-\w ]+,\s[-\w ]+)\t
([-\w\d.+]+@[-\w\d.]+)\t
(\(?\d{3}\)?-?\s?\d{3}-\d{4})\t # phone
([\w\s]+,\s[\w\s]+)\t 
(@[\w\d]+)
''', data, re.X | re.M))

print(re.findall(r'''
^(?P<name>[-\w ]*,\s[-\w ]+)\t
(?P<email>[-\w\d.+]+@[-\w\d.]+)\t
(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t
(?P<job>[\w\s]+,\s[\w\s.]+)\t?
(?P<twitter>@[\w\d]+)?$
''', data, re.X | re.M))

print(re.search(r'''
(?P<email>[-\w\d.+]+@[-\w\d.]+),\s
(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})
''', data, re.X | re.M))
