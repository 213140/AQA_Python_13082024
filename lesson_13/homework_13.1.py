from pathlib import Path
current_Path = Path.cwd()

def remove_duplicates_from_csv_file(path, file1_name, file2_name):
    """
    Function for checking duplicates from two files.
    Content without duplicates will be saved in new reuslt file.
    #######################Result file structure##################
    Result csv file name structure: result_ < your_second_name >.csv
    #######################Line example###########################
    Example of duplication in two files (random.csv as example):
    Los Angeles, CA  90057",(213) 480-1385,"161 S. Occidental Blvd. #19\n
    """
    if not (current_Path / 'result_mackevic.csv').exists():
        (current_Path / 'result_mackevic.csv').touch()
    with open(current_Path / 'result_mackevic.csv', 'w') as result_file:
        with open(path / file1_name, 'r') as file1:
            with open(path / file2_name, 'r') as file2:
                file1_content_as_lines = file1.readlines()
                file2_content_as_lines = file2.readlines()
                matches = set(file1_content_as_lines) & set(file2_content_as_lines)
                for match in matches:
                    file1_content_as_lines.remove(match)
                    file2_content_as_lines.remove(match)
                result_file.writelines([*file1_content_as_lines, *file2_content_as_lines])

# Example of usage with two files: 'r-m-c.csv' and 'random.csv'
remove_duplicates_from_csv_file(current_Path / 'ideas_for_test/work_with_csv',
                                'r-m-c.csv', 'random.csv')
