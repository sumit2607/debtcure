import os
import glob
import re

def update_loader(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    # Target the loader SVG
    loader_svg_pattern = r'<svg aria-hidden="true" class="loader-icon pulse".*?</svg>'
    
    # New loader img
    new_loader_img = '<img src="assets/logo.png" alt="Loading..." class="loader-icon pulse" width="80" height="80" style="animation: pulse-animation 1.5s infinite ease-in-out; border-radius: 12px; margin-bottom: 20px;">'

    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace loader icon
        new_content = re.sub(loader_svg_pattern, new_loader_img, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated loader logo in {os.path.basename(file_path)}")

if __name__ == '__main__':
    update_loader('/Users/sumit/Downloads/debtCure')
