import os
filepath = '/home/runner/work/SP/SP/data/test.txt'
print(filepath)
print('Script working directory', os.getcwd())

# save news data
import json
with open(filepath, 'w') as f:
  f.write('\nhello')
print('File Created', filename)
