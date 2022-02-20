import json
from os.path import exists

def convert_json_to_md(json_path, md_path):

    with open(json_path, encoding='utf8') as json_file:
        data = json.load(json_file)

    with open(md_path, 'w', encoding='utf8') as md_file:
        for word in data:
            md_file.write(f"# {word['word']}\n")

            md_file.write(f"### Reference\n")
            if word['reference']:
                for reference in word["reference"]:
                    md_file.write(f"{reference}\n")

            md_file.write(f"### Status\n")
            if word['status']:
                md_file.write(f"{word['status']}\n")

            md_file.write(f"### Definition\n")
            if word['definition']:
                md_file.write(f"{word['definition']}\n")

            md_file.write(f"### Description\n")
            if word['description']:
                for sentence in word["description"]:
                    md_file.write(f"{sentence}\n")

            md_file.write(f"### Figure\n")
            if word['figure']:
                md_file.write(f"{word['figure']}\n".replace("'", '"'))

            md_file.write(f"### Tricks\n")
            if word['tricks']:
                for sentence in word["tricks"]:
                    md_file.write(f"{sentence}\n")

            md_file.write("\n")


if __name__ == "__main__":
    for ascii_num in range(65, 91):
        character = chr(ascii_num)
        md_path = 'collections/' + character + '.md'
        json_path = 'json_collections/' + character + '.json'

        if exists(json_path):
            convert_json_to_md(json_path, md_path)
        else:
            print(f"{json_path} does not exists. Proceeding ...")
