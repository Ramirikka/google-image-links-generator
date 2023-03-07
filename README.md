# Google Image Links Generator

This is a Python script is a tool that converts a list of keywords into Google Image Search links. It takes a list of keywords as input and generates a set of links that can be used to search for images related to those keywords on Google.

## Instructions

1. Create an input file containing a list of keywords, with each keyword on a new line. For example:

```
• apple
• banana
• cherry
```

2. Save the input file as a text file (e.g. `input.txt`) in the same directory as the Python script.

3. Open the Python script in a Python IDE or text editor.

4. In the script, edit the values of the `input_file_path` and `output_file_path` variables to match the names and locations of your input and output files.

```python
input_file_path = "input.txt"
output_file_path = "output.txt"
```

Run the script. It will read in the list of keywords from the input file, generate a set of Google Image Search links based on those keywords, and write the links to the output file.

```python
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        modified_line = prefix + line.strip().replace(" ", "+") + suffix
        output_file.write(modified_line + "\n")
```


Open the output file (e.g. output.txt) to view the generated links.

```
https://www.google.com/search?q=apple&tbm=isch
https://www.google.com/search?q=banana&tbm=isch
https://www.google.com/search?q=cherry&tbm=isch
```

Note: By default, the generated links include the Google Images search options &tbm=isch which stands for "Image Search". If you want to customize your search parameters further, you can modify the prefix and suffix variables in the Python script.

## License

This script is open source and available under the MIT license. Feel free to use, modify, and distribute it as needed. If you have any questions or feedback, please don't hesitate to reach out.

![googlelogo_color_272x92dp](https://user-images.githubusercontent.com/19676135/223544008-4209ee6d-f2a9-45d0-b50e-411c6e665218.png)

