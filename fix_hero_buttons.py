import os
import glob
import re

def fix_buttons(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the hero section and replace btn-outline with btn-outline-white within it
        # Patterns for hero section can vary slightly, so we look for patterns
        
        changed = False
        
        # Look for the "Talk to Expert Now" button specifically
        target = 'btn btn-outline large">📞 Talk to Expert Now</a>'
        replacement = 'btn btn-outline-white large">📞 Talk to Expert Now</a>'
        
        if target in content:
            content = content.replace(target, replacement)
            changed = True
            
        # Also check for other hero buttons that might be using btn-outline
        # We can look for sections with class="hero-section" or "page-header" 
        
        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed hero button visibility in {os.path.basename(file_path)}")

if __name__ == '__main__':
    fix_buttons('/Users/sumit/Downloads/debtCure')
