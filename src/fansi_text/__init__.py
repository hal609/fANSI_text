
"""
fansi_text: A Python library for applying ANSI text effects and colors.

Features:
- Text styles: Bold, Italic, Underline, Blink, etc.
- Colors: Standard, Bright, RGB foreground and background.
- Font variations and special effects.

Usage:
    ```python
    from fansi_text import Bold, Red
    print(Bold(Red("Hello World")))
    ```
Run `fansi_text.demo_all()` to see all available effects.
"""
__version__ = "0.1.0"


from .ANSI_effects import *
from .demo import demo_all

__all__ = [
    "Reset", "Bold", "Faint", "Italic", "Underline", "SlowBlink", "FastBlink", "Invert", "Conceal", "Strikethrough",
    "Font0", "Font1", "Font2", "Font3", "Font4", "Font5", "Font6", "Font7", "Font8", "Font9", "FrakturFont", "DoubleUnderline",
    "ProportionalSpacing", "Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White", "RGBColor", "BgBlack", "BgRed",
    "BgGreen", "BgYellow", "BgBlue", "BgMagenta", "BgCyan", "BgWhite", "RGBBgColor", "Framed", "Encircled", "Overline", 
    "UnderlineColor", "IdeogramUnderline", "IdeogramDoubleUnderline", "IdeogramOverline", "IdeogramDoubleOverline", 
    "IdeogramStressMarking", "Superscript", "Subscript", "BrightBlack", "BrightRed", "BrightGreen", "BrightYellow", 
    "BrightBlue", "BrightMagenta", "BrightCyan", "BrightWhite", "BgBrightBlack", "BgBrightRed", "BgBrightGreen", "BgBrightYellow",
    "BgBrightBlue", "BgBrightMagenta", "BgBrightCyan", "BgBrightWhite",
    "demo_all"
]
