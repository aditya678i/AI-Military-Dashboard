import os
import re

directory = 'C:/Users/adity/Downloads/project/pages'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove the current import and load
            content = content.replace("from utils.data_loader import load_data\ndf = load_data()\n", "")
            content = content.replace("from utils.data_loader import load_data\r\ndf = load_data()\r\n", "")
            
            # Find the set_page_config block
            matches = list(re.finditer(r'st\.set_page_config\(.*?\)', content, flags=re.DOTALL))
            if matches:
                last = matches[-1].end()
                content = content[:last] + "\n\nfrom utils.data_loader import load_data\ndf = load_data()\n" + content[last:]
            else:
                # If no set_page_config, just put it after imports
                import_matches = list(re.finditer(r'^(import|from) .+', content, flags=re.MULTILINE))
                if import_matches:
                    last = import_matches[-1].end()
                    content = content[:last] + "\n\nfrom utils.data_loader import load_data\ndf = load_data()\n" + content[last:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
