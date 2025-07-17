# ✅ Day 16 – Python File Handling

## 📚 Topics Covered
- Reading from a file (`open()`, `read()`, `readlines()`)
- Writing to a file (`write()`, `writelines()`)
- Using `with open()` context manager
- File modes: `"r"`, `"w"`, `"a"`, `"r+"`
- Checking if a file exists using `os.path.exists()`
- Looping through lines in a file
- Creating a file copy using file operations

## 🛠️ Hands-on Tasks
- Created and wrote data to a file named `demo.txt`
- Read file content using different methods (`read()`, `readlines()`)
- Appended new lines to an existing file
- Copied contents from one file to another using:
  - Manual loop with `readlines()` and `write()`
  - `with open()` for safe file handling

## 🧠 Key Takeaways
- Always close files after opening, or use `with` to handle it automatically.
- File modes determine how the file is accessed.
- Handling file operations safely avoids data loss or errors.
- Real-world example: backing up logs or generating reports from one file to another.

## 🔁 To Practice Later
- Write a script to merge two text files into a third one.
- Create a file filter that copies only specific lines (e.g., those with a keyword) to a new file.
