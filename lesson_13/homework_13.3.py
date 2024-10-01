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
    number_as_string = str
    if type(group_number) != '<str>':
        number_as_string = str(group_number)
    else:
        number_as_string = group_number

    for child in root.findall('group'):
        child_group_number = str(child.find('number').text)
        if child_group_number == number_as_string:
            timing_exbytes = child.find('timingExbytes')
            if timing_exbytes is not None:
                bbo = timing_exbytes.find('bbo')
                if bbo is not None:
                    logging.info(bbo.text)

# Example of usage for file groups.xml and group number 2
search_in_xml_by_group_number(Path.cwd() / 'ideas_for_test/work_with_xml/groups.xml', 2)