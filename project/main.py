import json


data = json.load(open('../data/dictionary.json'))


def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return ['No such word in a dictionary!']


if __name__ == '__main__':
    key = input('Enter a word: ')
    definition_list = get_definition(key)
    for definition in definition_list:
        print(definition)
