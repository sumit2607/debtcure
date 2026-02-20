import os
import glob
import re

def update_calc_labels(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    target = '<p>Potential Settlement Amount</p>'
    replacement = '<p>Potential Settlement Amount (30-40%)</p>'
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target in content:
            new_content = content.replace(target, replacement)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated calculator label in {os.path.basename(file_path)}")

if __name__ == '__main__':
    update_calc_labels('/Users/sumit/Downloads/debtCure')
