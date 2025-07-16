# 📘 Day 10 – Python Loops & DevOps Tools Menu (Basics)

## ✅ Topics Covered

- Python `for` loops using lists
- `for` loop with `range(len(...))`
- `while` loop basics
- Working with lists and indexes
- Logic building with iteration
- DevOps tools list and display

---

## 🔁 Practiced Script

```python
devops_tools = ["Docker", "Git", "Jenkins", "k8s"]

# For loop - direct iteration
for tool in devops_tools:
    print(tool)

# For loop - using index access
for i in range(len(devops_tools)):
    print(f"Index {i} --> Value {devops_tools[i]}")

# While loop - limited iteration
count = 0
while count < 3:
    print(f"tool is {devops_tools[count]}")
    count += 1
