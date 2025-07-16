def extract_errors(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if "ERROR" in line:
                    outfile.write(line)

                 

        print(f"Error lines written to {output_file}")
    
    except FileNotFoundError:
        print(f" The file {input_file} was not found...")


if __name__ == "__main__":
    extract_errors("app.log", "error.log")