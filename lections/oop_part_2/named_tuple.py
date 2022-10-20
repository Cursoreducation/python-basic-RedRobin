import collections

Article = collections.namedtuple('Article', ['topic', 'contributor', 'likes', 'tags', 'language'])

python_classes = Article('Python', 'Rostyslav', 30, [['Python', 'Hello', ['Hi']], 'Lecture'], 'Ukrainian')

# Доступ через крапочку
print(python_classes.contributor)

# Доступ по індексу
print(python_classes[1])
print(python_classes[3][0][2][0])