def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
        print(f"Content has been written to file : {filename}")

def append_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
        print(f" Appended to file : {filename}")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(f"Reading from file {filename}:\n ")
            #printing using 
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                print(f"{idx} : {line.strip()}")
            #print(file.read())
    except FileNotFoundError:
        print(f" File '{filename}' not found !!")


if __name__ == "__main__":
    write_to_file("sample.txt", "This is line one.\n")
    append_to_file("sample.txt", "This is line two.\n")
    read_file("sample.txt")