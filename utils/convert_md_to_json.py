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

            data["word"] = line.strip(" #\n")
            line = md_file.readline()

            if line == "### Reference\n":
                data["reference"] = []

                line = md_file.readline()

                while line[:3] != "###":
                    data["reference"].append(line.strip(" \n"))
                    line = md_file.readline()

            if line == "### Status\n":
                line = md_file.readline()
                if line[:3] != "###":
                    data["status"] = line.strip(" \n")
                    line = md_file.readline()
                else:
                    data["status"] = "Pending"  # Default to Pending status

            if line == "### Definition\n":
                line = md_file.readline()
                if line[:3] != "###":
                    data["definition"] = line.strip(" \n")
                    line = md_file.readline()
                else:
                    data["definition"] = ""  # Default to empty

            if line == "### Description\n":
                data["description"] = []

                line = md_file.readline()

                while line[:3] != "###":
                    data["description"].append(line.strip(" \n"))
                    line = md_file.readline()

            if line == "### Figure\n":
                content = []
                line = md_file.readline()
                while line[:3] != "###":
                    content.append(line.strip(" \n"))
                    line = md_file.readline()
                data['figure'] = ' '.join(content)

                if data['figure']:
                    data['figure'] = json.loads(data['figure'])

            if line == "### Tricks\n":
                data["tricks"] = []

                line = md_file.readline()

                while line != "\n":
                    data["tricks"].append(line.strip(" \n"))
                    line = md_file.readline()

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
            convert_md_to_json(md_path, json_path, headers=["word", "reference", "status", "definition", "description", "figure", "tricks"])
        else:
            print(f"{md_path} does not exists. Proceeding ...")
