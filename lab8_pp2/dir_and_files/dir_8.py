import os
a = r'C:\Users\Admin\E.txt'
os.remove(a)

import os
fname = input()
if os.path.exists(fname):
    if os.access(fname, os.W_OK):
        os.remove(fname)
        print("Deleted")
    else:
        print("No permission")
else:
    print("File does not exist!")