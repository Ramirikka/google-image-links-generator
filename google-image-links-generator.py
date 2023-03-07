input_file_path = "input.txt"
output_file_path = "output.txt"

prefix = "https://www.google.com/search?q="
suffix = "&tbm=isch"

with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        modified_line = prefix + line.strip().replace(" ", "+") + suffix
        output_file.write(modified_line + "\n")
