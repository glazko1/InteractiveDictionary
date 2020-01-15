import json
from difflib import get_close_matches


data = json.load(open('../data/dictionary.json'))


def get_definition(word):
    word = word.lower()
    close_matches = get_close_matches(word, data.keys(), cutoff=0.8)
    if word in data:
        return data[word]
    elif len(close_matches) > 0:
        close_match = close_matches[0]
        if suggest_close_match(close_match):
            return data[close_match]
    return ['No such word in a dictionary!']


def suggest_close_match(predicted_word):
    agree = input('Maybe you\'ve meant "' + predicted_word + '"? Type Y if yes, N otherwise: ')
    return agree == 'Y'


if __name__ == '__main__':
    key = input('Enter a word to get its definition: ')
    definition_list = get_definition(key)
    for definition in definition_list:
        print(definition)
