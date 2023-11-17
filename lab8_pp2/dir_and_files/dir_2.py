import os

print('Testing:', 'raw.txt')
print('Exists:', os.access('raw.txt', os.F_OK))
print('Readable:', os.access('raw.txt', os.R_OK))
print('Writable:', os.access('raw.txt', os.W_OK))
print('Executable:', os.access('raw.txt', os.X_OK))
