from os.path import exists
import json


def remove_stars(file_name):
    """Remove any star "*" character from the json file.

    Args:
        file_name (string): path to the json file.
    """
    with open(file_name, encoding='utf8') as json_file:
        data = json.load(json_file)

        for entry in data:
            entry['word'] = entry['word'].strip('*')

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def add_header(file_name, headers):
    """Add headers to existing json format.

    Args:
        file_name (string): path to the json file.
        header (list): list of headers.
    """
    with open(file_name, encoding='utf8') as json_file:
        data = json.load(json_file)

        for entry in data:
            for header in headers:
                entry[header] = ''

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    for ascii_num in range(65, 91):
        character = chr(ascii_num)
        path = 'Collections/' + character + '.json'

        if exists(path):
            remove_stars(path)
            add_header(path, ['definition', 'desciption', 'figure', 'tricks'])
        else:
            print(f"{path} does not exists. Proceeding ...")
