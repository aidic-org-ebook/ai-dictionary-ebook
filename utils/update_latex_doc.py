import json
from os.path import exists
from sort_json_by_word import sort_json_by_word


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
            if word['status'] == 'Translated':
                line = []
                line.append(
                    f"\\section*{{\\huge \\textcolor{{Red}}{{ {word['word']} }} \\small \\textit{{ {word['definition']} }} }}"
                )

                if word['reference']:
                    references = "Tham khảo:"
                    for reference in word["reference"]:
                        references += f" \\footnote{{ \\url{{{ reference }}} }}"
                    line.append(references)

                if word['description']:
                    descriptions = "\\subsection*{Định nghĩa:}"
                    for sentence in word["description"]:
                        descriptions += f"\n{sentence}"
                    line.append(descriptions)

                if word['figure']:
                    for idx, fig in enumerate(word['figure']):
                        figure_format = "\\begin{{figure}}[!h]\n\t\\centering\n"
                        figure_format += f"\t\\includegraphics[width={fig['width'] if 'width' in fig else 0.75}\\linewidth]{{ {fig['path']} }}\n"
                        if 'caption' in fig:
                            figure_format += f"\t\\caption{{ {fig['caption']} }}"
                        figure_format += f"\\label{{fig:{word['word'].lower()}_{idx+1}}}\n\\end{{figure}}"
                        line.append(figure_format)

                if word['tricks']:
                    tricks = "\\subsection*{Mẹo nhỏ:}"
                    for sentence in word["tricks"]:
                        tricks += f"\n{sentence}"
                    line.append(tricks)

                tex_file.write('\n'.join(line))
                tex_file.write('\n')
                tex_file.write('\n')


if __name__ == "__main__":

    word_collections_path = 'json_collections'
    ebook_path = 'ebook/chapters'

    for ascii_num in range(65, 91):
        character = chr(ascii_num)
        # Each .json file is corressponding to a .tex file with the same name.
        json_path = word_collections_path + '/' + character + '.json'
        tex_path = ebook_path + '/' + character + '.tex'

        if exists(json_path):
            sort_json_by_word(json_path)

            data = read_json(json_path)

            if data:
                update_latex_doc(tex_path, data)

        else:
            print(f"{json_path} does not exists. Proceeding ...")
