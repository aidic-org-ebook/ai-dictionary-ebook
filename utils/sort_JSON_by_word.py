from os.path import exists
import json


def sort_json_by_word(path):
    """Sort the entries in the JSON file by the word alphabetically.

    Args:
        path (string): file path + file name of the Markdown file.
    """
    with open(path, encoding='utf8') as json_file:
        data = json.load(json_file)

    data.sort(key=lambda x: x['word'].lower())

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    for ascii_num in range(65, 91):
        character = chr(ascii_num)
        path = 'Collections/' + character + '.json'

        if exists(path):
            sort_json_by_word(path)
        else:
            print(f"{path} does not exists. Proceeding ...")
