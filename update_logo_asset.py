import os
import glob
import re

def update_logo(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    # 1. Header Logo
    # Current SVG pattern
    svg_pattern = r'<svg aria-hidden="true" class="logo-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">.*?</svg>'
    
    # New image logo - adding a bit of styling to make it look clean
    logo_img_html = '<img src="assets/logo.png" alt="DebtCure Logo" class="logo-icon" style="width: 42px; height: 42px; object-fit: contain; border-radius: 8px;">'

    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace occurrences of the logo SVG
        new_content = re.sub(svg_pattern, logo_img_html, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated logo in {os.path.basename(file_path)}")

if __name__ == '__main__':
    update_logo('/Users/sumit/Downloads/debtCure')
