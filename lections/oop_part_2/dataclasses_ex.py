import dataclasses


@dataclasses.dataclass
class Article:
    topic: str
    contributor: str
    language: str
    likes: int
    tag: list


python_classes = Article('Python Classes', 'Rostyslav', 'Ukrainian', 20, ['Python'])
python_classes_1 = Article('Python Classes', 'Rostyslav', 'Ukrainian', 20, ['Python'])

python_classes_dict = {
    'topic': 'Python Classes',
    'contributor': 'Rostyslav',
    'language': 'Ukrainian',
    'likes': 20,
    'tag': ['Python']
}
python_classes_dict_1 = {
    'topic': 'Python Classes',
    'contributor': 'Rostyslav',
    'language': 'Ukrainian',
    'likes': 20,
    'tag': ['Python']
}
print(python_classes)
print(python_classes.topic, python_classes.contributor)
print(python_classes.contributor)
python_classes.likes = 40
print(python_classes.likes)
python_classes.test = 'hello'
print(python_classes.test)

print(python_classes_dict['topic'], python_classes_dict.get('likes'))
is_frozen = True
def change_dataclass_type(is_frozen):
    return is_frozen

@dataclasses.dataclass(frozen=is_frozen)
class Book:
    title: str
    author: str
    pages: int

python_book = Book('Python Lecture', 'Rostyslav', 15)
print(python_book.title, python_book.author, python_book.pages)
python_book.pages = 20
python_book.test = 'test'

@dataclasses.dataclass
class Configuration:
    debug: bool
    environment: str
    configs: list

stage_config = Configuration(True, 'Stage', [])
qa_config = Configuration(True, 'QA', [])
production = Configuration(True, 'Production', [])