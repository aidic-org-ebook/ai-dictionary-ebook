from os.path import exists
import json


def convert_mdtable_to_json(path):
    """Convert Markdown table into json format file.
    This funtion will create a "{path}.json".

    There will be no Markdown table format checking, so please be precise.

    Args:
        path (string): file path + file name of the Markdown file.
    """
    line_number = 0
    with open(path, encoding="utf8") as md_file:
        result = []

        for line in md_file:
            data = {}
            if line_number == 0:
                header = [t.strip() for t in line.split('|')[1:-1]]
            if line_number > 1:
                if line != "\n":
                    values = [t.strip() for t in line.split('|')[1:-1]]
                    for col, value in zip(header, values):
                        data[col] = value
                    result.append(data)

            line_number += 1

    with open(path[:-3] + '.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    for ascii_num in range(65, 91):
        character = chr(ascii_num)
        path = 'Collections/' + character + '.md'

        if exists(path):
            convert_mdtable_to_json(path)
        else:
            print(f"{path} does not exists. Proceeding ...")
