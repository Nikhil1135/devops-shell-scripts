# Day 13 - Python: *args, **kwargs, `if __name__ == "__main__"` and Custom Modules

## ✅ Topics Covered

1. **`*args` (Arbitrary Positional Arguments)**  
   - Allows passing a variable number of arguments to a function.
   - Syntax: `def func(*args):`

2. **`**kwargs` (Arbitrary Keyword Arguments)**  
   - Allows passing a variable number of keyword arguments (key=value).
   - Syntax: `def func(**kwargs):`

3. **`if __name__ == "__main__"` Block**  
   - Prevents code from being run when the file is imported as a module.
   - Common practice to define entry-point code.

4. **Creating and Importing a Custom Module**  
   - Wrote functions inside a separate file (`calculator.py`)
   - Imported and reused them in `main.py` using `import calculator`

---

## 🧪 Code Files

### 📄 `main.py`

```python
def greet_people(*args):
    for name in args:
        print(f"Hello, {name}!")

def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

import calculator

if __name__ == "__main__":
    greet_people("Nikhil", "Amit", "Riya")
    show_profile(name="Nikhil", role="DevOps Engineer", location="India")
    
    print("Addition:", calculator.add(10, 5))
    print("Subtraction:", calculator.subtract(10, 5))
