# Function to check if a link ends with '.pdf'
def is_pdf_link(link):
    return link.strip().lower().endswith('.pdf')

# Input file containing the links (replace 'input.txt' with your file name)
input_file = 'unfiltered_output_links.txt'

# Output file to store the filtered PDF links
output_file = 'pdf_links_final_filtered_nepali.txt'

with open(input_file, 'r') as file:
    with open(output_file, 'w') as output:
        for line in file:
            link = line.strip()
            if is_pdf_link(link):
                output.write(link + '\n')

print("PDF links filtered and saved in 'pdf_links.txt' file.")

