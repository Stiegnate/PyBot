# Coding Style

# Windows
as pseudo_example.py

# macOS

- `MouseAction` class example:

```python
from mac import MouseAction

action = MouseAction(0, 0)
action.mouseClick() # click at (x, y) = (0, 0) loc
action.mouseMove(100, 100) # move mouse to (x, y) = (100, 100) loc
action.mouseClick() # click at (x, y) = (100, 100) loc
```

# Ubuntu

# Develope note
- try to deal with different operating system
- build test_function.py
- build standard pytest
