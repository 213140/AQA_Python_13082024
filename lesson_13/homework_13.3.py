import xml.etree.ElementTree as ET
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def search_in_xml_by_group_number(file_path, group_number):
    """
    Function returns incoming value based on group number
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    for child in root:
        if child.tag == 'group':
            for subchild in child:
                if subchild.tag == 'number':
                    number_as_string = str
                    if type(group_number) != '<str>':
                        number_as_string = str(group_number)
                    else:
                        number_as_string = group_number
                    if subchild.text == number_as_string:
                        for subchild in child:
                            if subchild.tag == 'timingExbytes':
                                for subsubchild in subchild:
                                    if subsubchild.tag == 'incoming':
                                        logging.info(subsubchild.text)

# Example of usage for file groups.xml and group number 2
search_in_xml_by_group_number(Path.cwd() / 'ideas_for_test/work_with_xml/groups.xml', 2)