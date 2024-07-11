import json


def get_tokens():
    f = open('Tokens/tokens.json')
    data = json.load(f)
    f.close()
    return data