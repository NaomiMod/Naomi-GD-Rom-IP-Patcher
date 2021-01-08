#-------------------------------------------------
# Naomi GD-Rom IP patcher by VincentNL 08/01/2021
#-------------------------------------------------

import tkinter as tk
from tkinter import filedialog
import shutil

root = tk.Tk()
root.withdraw()

# create a backup
my_file = filedialog.askopenfilename(initialdir = ".",title = "Select Naomi GD - IP.BIN file",filetypes=[("IP.bin", "IP.bin")])
my_file2 = (my_file[0:-3]+"bak")
shutil.copy2(my_file, my_file2)

# patch bytes
bytes = bytearray(b'\x4E\x41\x4F\x4D\x49\x47\x44\x2E\x42\x49\x4E\x20\x20\x20\x20\x20')
f = open(my_file, 'r+b')
f.seek(0x60)
f.write(bytes)
f.close()
