import json
from os.path import exists


def convert_md_to_json(md_path, json_path, headers):
    """Convert Markdown syntax into json format file.
    This funtion will create a "{path}.json".

    Args:
        md_path (string): file path + file name of the Markdown file.
        json_path (string): file path + file name of the new Json file.
        headers (list): list of header for json format.
    """
    with open(md_path, encoding="utf8") as md_file:
        result = []

        line = md_file.readline()
        while line:
            data = {}

            data[headers[0]] = line.strip(" #\n")
            line = md_file.readline()
            for header in headers[1:]:
                content = []
                line = md_file.readline()
                while line[:3] != "###" and line != "\n":
                    content.append(line.strip(" \n"))
                    line = md_file.readline()
                data[header] = ' '.join(content)

            if data['figure']:
                data['figure'] = json.loads(data['figure'])

            if data['status'] == 'Translated':
                result.append(data)

            line = md_file.readline()

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    for ascii_num in range(65, 91):
        character = chr(ascii_num)
        md_path = 'collections/' + character + '.md'
        json_path = 'json_collections/' + character + '.json'

        if exists(md_path):
            convert_md_to_json(md_path, json_path, headers=["word", "reference", "status", "definition", "desciption", "figure", "tricks"])
        else:
            print(f"{md_path} does not exists. Proceeding ...")
