# read_write.py
with open("copy.txt", "w") as outfile:
    with open("sample.txt", "r") as infile:
        for line in infile:
            outfile.write(line.upper())  # Convert to UPPERCASE and copy
