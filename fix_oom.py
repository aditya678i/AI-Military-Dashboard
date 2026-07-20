import os
import re

directory = 'C:/Users/adity/Downloads/project'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace pd.read_csv calls to include nrows=15000 to prevent OOM
            new_content = re.sub(
                r'pd\.read_csv\(\s*(.*?globalterrorism\.csv.*?),\s*encoding=["\']latin1["\'],\s*low_memory=False\s*\)',
                r'pd.read_csv(\1, encoding="latin1", low_memory=False, nrows=15000)',
                content,
                flags=re.DOTALL
            )
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
