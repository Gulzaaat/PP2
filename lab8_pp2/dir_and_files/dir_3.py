import os 

def exists(fname):
    if os.path.exists(fname):
        return True
    else:
        return False

a = r'C:\Users\Admin\raw.txt'
print(exists(a))
print(a)