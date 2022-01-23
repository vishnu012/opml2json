from xml.etree import ElementTree

def opml_to_dic(file_path):
    final_data = {}
    with open(file_path,'rt') as f:
        tree = ElementTree.parse(f)
        root = tree.getroot()
        folder_names = []
        for child in root[1]:
            folder_names.append(child)
        for folder_name in folder_names:
            rss_data_folder_wise = []
            for rss_data in folder_name:
                rss_data_folder_wise.append(rss_data.attrib)
            final_data[folder_name.attrib['text']] = rss_data_folder_wise
    return final_data
