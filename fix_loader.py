import os
import re

directory = 'C:/Users/adity/Downloads/project/pages'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Remove local load_data
            content = re.sub(r'@st\.cache_data\s+def load_data\(\):.*?return df', '', content, flags=re.DOTALL)
            
            # Remove direct df = pd.read_csv
            content = re.sub(r'df\s*=\s*pd\.read_csv\(.*?nrows=15000\)', '', content, flags=re.DOTALL)
            
            # Remove duplicate df = load_data()
            content = re.sub(r'df\s*=\s*load_data\(\)', '', content)
            
            # Remove existing from utils.data_loader import load_data
            content = re.sub(r'from utils\.data_loader import load_data', '', content)
            
            # Add the correct import and assignment at the top after standard imports
            import_block = "from utils.data_loader import load_data\ndf = load_data()\n"
            
            # Find a safe place to insert (after last standard import)
            matches = list(re.finditer(r'^(import|from) .+', content, flags=re.MULTILINE))
            if matches:
                last = matches[-1].end()
                content = content[:last] + "\n\n" + import_block + content[last:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
