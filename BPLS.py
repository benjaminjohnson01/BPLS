import os
from datetime import datetime
import pandas as pd

working_directory = '/Users/ben/Desktop/Ben Path Length Scanner'

def set_working_directory(directory):
    original_working_directory = os.getcwd()
    print(original_working_directory)
    os.chdir(directory)
    new_working_directory = os.getcwd()
    print(new_working_directory)

def find_long_paths(directory, max_length, output_file):
    set_working_directory(working_directory)

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    output_file_with_timestamp = f"{output_file}_{timestamp}.txt"
    
    with open(output_file_with_timestamp, 'w') as file:
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if len(file_path) > max_length:
                    file.write(f"{len(file_path)}: {file_path}\n")

# Usage example
directory = '/Users/ben/Downloads'  # Replace with the root directory you want to scan
max_length = 20  # Maximum path length
output_file = 'long_paths'  # Output file name (without extension)

find_long_paths(directory, max_length, output_file)

def text_file_to_dataframe(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                length, path = line.split(': ')
                data.append({'Length': int(length), 'Path': path})
    
    df = pd.DataFrame(data)
    return df

df = text_file_to_dataframe('long_paths_20240122232412.txt')

print(df.head())