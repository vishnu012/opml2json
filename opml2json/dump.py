import json
from opml2json.otoj import opml_to_dic

def write_json(file_path):
    dic = opml_to_dic(file_path)
    with open("sample.json", "w") as output:
        json.dump(dic, output,indent=4,sort_keys=True)
