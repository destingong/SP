import os
filepath = '/home/runner/work/SP/SP/data/test.txt'
# print('Script working directory', os.getcwd())

# save news data
import json
with open(filepath, 'w') as f:
  f.write('\nhello')

# Traverse up the directory tree
while current_dir != os.path.dirname(current_dir):  # Stop at the root directory
    print(current_dir)
    current_dir = os.path.dirname(current_dir)
  
print('File Created', filepath)
