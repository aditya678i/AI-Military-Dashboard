import os
import re

directory = 'C:/Users/adity/Downloads/project/pages'
cols = set()

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(r'df\[["\'](.*?)["\']\]', content)
                cols.update(matches)

print("Columns used:", cols)
