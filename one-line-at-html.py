import re

def extract_links(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    links = []
    for line in lines:
        match = re.search(r'(https?://\S+)', line)
        if match:
            links.append(match.group())

    with open(output_file, 'w') as file:
        file.write('\n'.join(links))

# Usage example
input_file = 'input_unfiltered_data_points.txt'  # Replace with your input file path
output_file = 'unfiltered_output_links.txt'  # Replace with your output file path
extract_links(input_file, output_file)

