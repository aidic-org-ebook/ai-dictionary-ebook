import json
from os.path import exists

def convert_json_to_md():
    for ascii_num in range(65, 91):
        character = chr(ascii_num)

        json_path = 'Collections/' + character + '.json'
        if exists(json_path):
            with open(json_path, encoding='utf8') as json_file:
                data = json.load(json_file)
        else:
            print(f"{json_path} does not exists. Proceeding ...")

        md_path = 'Collections/' + character + '.md'
        with open(md_path, 'w', encoding='utf8') as md_file:
            for word in data:
                md_file.write(f"# {word['word']}\n")

                md_file.write(f"### Reference\n")
                if word['reference']:
                    md_file.write(f"{word['reference']}\n")

                md_file.write(f"### Status\n")
                if word['status']:
                    md_file.write(f"{word['status']}\n")

                md_file.write(f"### Definition\n")
                if word['definition']:
                    md_file.write(f"{word['definition']}\n")

                md_file.write(f"### Desciption\n")
                if word['desciption']:
                    md_file.write(f"{word['desciption']}\n")

                md_file.write(f"### Figure\n")
                if word['figure']:
                    md_file.write(f"{word['figure']}\n")

                md_file.write(f"### Tricks\n")
                if word['tricks']:
                    md_file.write(f"{word['tricks']}\n")

                md_file.write("\n")


if __name__ == "__main__":
    convert_json_to_md()
