file = open("output.txt", "w")
file.write("this is written from python !!  Thaggede le \n ")
file.write("Appending Anpther line.")
file.close()
print("Data written to output.txt")


with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


with open("output.txt", "a") as file:
    file.write("Appending using 'a' mode .\n")
