import os
import fnmatch

def markdown_files_list(directory):
    markdown_files = []
    pattern = "*.md"

    for current_path, directories, files in os.walk(directory):
        for file in fnmatch.filter(files, pattern):
            markdown_files.append(file)

    return markdown_files

def convert_to_image_format(line):
    return f"![[{line.strip()}]]"

def file_convert(input_file, output_file):
    with open(input_file, 'r') as input:
        lines = input.readlines()

    converted_lines = [convert_to_image_format(line) for line in lines]

    with open(output_file, 'w') as output:
        for converted_line in converted_lines:
            output.write(converted_line + '\n')

# Change the directory path that you want to analyze
analysis_directory = input("Enter the path to .md files folder: ")

markdown_files = markdown_files_list(analysis_directory)

if markdown_files:
    # Save files' names in 'files.md'
    with open("files.md", "w") as output_file:
        for file in markdown_files:
            output_file.write(file + "\n")
    print("Names of files saved in 'files.md'.")
else:
    print("No Markdown files in the directory.")

final_file = analysis_directory+"/markdown_list.md"

file_convert('files.md', final_file)
print(f"Converted and saved at {final_file}.")