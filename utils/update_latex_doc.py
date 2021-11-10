from os.path import exists
import json


def read_json(json_path):
    if not exists(json_path):
        print(f"{json_path} does not exists. Proceeding ...")
        return

    with open(json_path, encoding='utf8') as json_file:
        json_data = json.load(json_file)

    return json_data


def update_latex_doc(tex_path, data):
    """Update the Latex document based on json data.

    Args:
        tex_path (string): path to the latex source code.
        data (json object (dict)): a dictionary that contains the json data format to parse into latex.
    """
    with open(tex_path, mode='w', encoding='utf8') as tex_file:
        for word in data:
            if word['status'] != 'Translated':
                continue

            line = []
            line.append(
                f"\\section*{{\\huge \\textcolor{{Red}}{{ {word['word']} }} \\small \\textit{{ {word['definition']} }} }}"
            )

            if word['reference']:
                line.append(
                    f"Tham khảo: \\footnote{{ \\url{{{word['reference']}}} }}"
                )

            if word['desciption']:
                line.append(
                    f"\\subsection*{{Định nghĩa:}}\n{word['desciption']}"
                )

            if word['figure']:
                for idx, fig in enumerate(word['figure']):
                    line.append(
                        f"""
                        \\begin{{figure}}[!h]
                            \\centering
                            \\includegraphics[width=1.0\\linewidth]{{ {fig['path']} }}
                            \\caption{{ {fig['Caption']} }}
                            \\label{{fig:{word['word'].lower()}_{idx+1}}}
                        \\end{{figure}}
                        """
                    )

            if word['tricks']:
                line.append(
                    f"\\subsection*{{Mẹo nhỏ:}}\n{word['tricks']}"
                )

            tex_file.write('\n'.join(line))
            tex_file.write('\n')


if __name__ == "__main__":

    word_collections_path = 'collections'
    ebook_path = 'ebook/chapters'

    for ascii_num in range(65, 91):
        character = chr(ascii_num)

        # Each .json file is corressponding to a .tex file with the same name.
        json_path = word_collections_path + '/' + character + '.json'
        tex_path = ebook_path + '/' + character + '.tex'

        data = read_json(json_path)

        if data:
            update_latex_doc(tex_path, data)