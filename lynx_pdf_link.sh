#!/bin/bash

# Input file containing links
input_file="unfiltered_output_links.txt"

# Output file to store the PDF links
output_file="links_nepali_epics.txt"

# Temporary file to store individual link files
temp_file="temp.txt"

# Loop through each link in the input file
while IFS= read -r link; do
    # Use lynx with the -listonly -dump options to extract links from each webpage
    lynx -listonly -dump "$link" | awk '/http/{print $2}' >> "$temp_file"
done < "$input_file"

# Extract PDF links from the temporary file and remove duplicates
grep -i '\.pdf$' "$temp_file" | sort -u > "$output_file"



