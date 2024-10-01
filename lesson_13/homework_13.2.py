import json
from pathlib import Path
import logging

logging.basicConfig(filename='result_mackevic.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

current_path = Path.cwd()

def check_file_in_dir_with_invalid_json(path):
    """
    Function checks if all json files in directory are valid.
    If not return information about not valid json files.
    """
    for json_file_path in path.iterdir():
        with open(json_file_path, 'r') as json_file:
            try:
                content_from_file = json.load(json_file)
                print(f"The File {json_file_path} contains valid JSON content", content_from_file)
            except (UnicodeDecodeError, json.decoder.JSONDecodeError) as e:
                logging.error(f"The File {json_file_path} does NOT contain valid JSON. Error found: {e}")
                # print(f"The File {json_file_path} does NOT contain valid JSON. Error found: {e}")

# Example of usage
check_file_in_dir_with_invalid_json(current_path / 'ideas_for_test/work_with_json')
