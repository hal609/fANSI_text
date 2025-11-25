# fansi_text

A Python module for formatting text with ANSI escape codes.

## Installation

```
pip install fansi_text
```

## Usage

```python
from fansi_text import Red

print(Red("Red text"))
```

```python
from fansi_text import RGBColor

print(RGBColor("RGB Text", 200, 130, 60))
```

You can also form complex combinations of overlapping effects.
```python
from fansi_text import *

print(
    Bold("Bold, " +
         Green("green and bold. ")) + 
    "Then normal text. Then " +
    Underline(Overline("under and over lined. ")) +
    "Next " + 
    Italic("italics. Add " + 
           Yellow("yellow " + 
                  Bold("and bold too! ") +
                  "Then back to yellow and italics, ") + 
           "then just italics, ") + 
    "and finally back to normal."
)
```