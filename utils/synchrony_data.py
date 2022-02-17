from os.path import exists

from convert_md_to_json import convert_md_to_json
from convert_json_to_md import convert_json_to_md
from update_latex_doc import update_latex_doc, read_json
from sort_json_by_word import sort_json_by_word


for ascii_num in range(65, 91):
    character = chr(ascii_num)

    md_path = 'collections/' + character + '.md'
    json_path = 'json_collections/' + character + '.json'
    tex_path = 'ebook/chapters/' + character + '.tex'

    # Convert markdown to JSON
    # to synchrony new changes
    if exists(md_path):
        convert_md_to_json(md_path, json_path, headers=["word", "reference", "status", "definition", "description", "figure", "tricks"])
    else:
        print(f"{md_path} does not exists. Proceeding ...")

    # Sort JSON and update the Latex version
    # of the dictionary
    sort_json_by_word(json_path)
    data = read_json(json_path)
    if data:
        update_latex_doc(tex_path, data)

    # Re-synchony to the markdown version
    # after sorting JSON
    convert_json_to_md(json_path, md_path)
