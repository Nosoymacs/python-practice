# 1. YOUR OWN MODULE
# Any .py file can be a module. text_tools.py lives in the same folder as this file.
# To import it, use the file name WITHOUT the .py extension.
# Python runs the whole module from top to bottom the FIRST time it is imported.
# That is why a line from text_tools.py is printed when you run this guide.

import text_tools

print(text_tools.count_vowels("Programming"))  
print(text_tools.shout("python"))              
print(text_tools.VOWELS)                      

# 2. IMPORT ONLY WHAT YOU NEED, AND ALIASES
# The same options you used with the standard modules.

from text_tools import count_vowels as vowels

print(vowels("Education")) 

# 3. __name__ AND THE "MAIN" BLOCK
# Python gives every file a variable called __name__.
# - When you run a file directly, its __name__ is "__main__".
# - When another file imports it, its __name__ is the module name.
# That is why the block "if __name__ == '__main__':" in text_tools.py did NOT run here,
# but it does run when you open text_tools.py and run it directly.

print(__name__)  # __main__ (this file is being run directly)

# 4. WHERE PYTHON LOOKS FOR YOUR MODULE
# Python looks first in the folder of the file you run.
# That is why this works even though your VS Code task runs from python/.

# 5. THINGS TO AVOID
# - Never name your module like a standard one (math.py, random.py, datetime.py).
# - Use lowercase names with underscores, no spaces or hyphens: text_tools.py, not text-tools.py.
# - After the first import, Python creates a __pycache__/ folder with compiled files.