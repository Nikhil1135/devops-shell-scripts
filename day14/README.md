# ✅ Day 14 – Python File Handling (Advanced)

## 📌 Topics Covered

Today, we deepened our understanding of **file handling** in Python. We explored:

- Writing to a file
- Appending to a file
- Reading from a file
- Reading line-by-line with line numbers
- Using `if __name__ == "__main__"` block for modular code execution

---

## 📂 Files Created

### `file_handler.py`

This script performs all major file operations:
- Writes initial content
- Appends new lines
- Reads content line-by-line, showing line numbers

---

## 🧠 Concepts Learned

### 1. Writing to a File (`write_to_file`)
```python
def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

######   Appending to a File (append_to_file)
def append_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
=======================================================
############Reading from a File with Line Numbers (read_file)
def read_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                print(f"{idx}: {line.strip()}")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")
=================================================================
########### Using __main__ Block
if __name__ == "__main__":
    write_to_file("sample.txt", "This is line one.\n")
    append_to_file("sample.txt", "This is line two.\n")
    append_to_file("sample.txt", "This is line three.\n")
    read_file("sample.txt")
================================================================
#############################OUTPUT###########################
✅ Written to sample.txt
➕ Appended to sample.txt
➕ Appended to sample.txt
📄 Reading from sample.txt:

1: This is line one.
2: This is line two.
3: This is line three.
