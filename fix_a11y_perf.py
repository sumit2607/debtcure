import os
import glob
import re

def optimize_html(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # --- Performance / Layout Shift (CLS) Fixes ---
        # Add dimensions to all our newly generated images (16:9 ratio -> e.g., 1920x1080 or 800x450, we'll use 1920x1080)
        if 'lawyer_1.png' in content and 'width=' not in content:
            content = re.sub(r'(src="[^"]*lawyer_1\.png"[^>]*)>', r'\1 width="1920" height="1080">', content)
            changed = True
        if 'lawyer_2.png' in content and 'width=' not in content:
            content = re.sub(r'(src="[^"]*lawyer_2\.png"[^>]*)>', r'\1 width="1920" height="1080">', content)
            changed = True
        if 'lawyer_3.png' in content and 'width=' not in content:
            content = re.sub(r'(src="[^"]*lawyer_3\.png"[^>]*)>', r'\1 width="1920" height="1080">', content)
            changed = True

        # Ensure all SVGs are aria-hidden
        if '<svg ' in content and 'aria-hidden' not in content:
            content = content.replace('<svg ', '<svg aria-hidden="true" ')
            changed = True

        # --- Accessibility Fixes ---
        # Lead form inputs
        content = content.replace('<input type="text" placeholder="Your Name" required>', '<input type="text" placeholder="Your Name" aria-label="Your Name" required>')
        content = content.replace('<input type="tel" placeholder="Phone Number" required>', '<input type="tel" placeholder="Phone Number" aria-label="Phone Number" required>')
        content = content.replace('<textarea placeholder="Briefly describe your issue" rows="3"></textarea>', '<textarea placeholder="Briefly describe your issue" aria-label="Briefly describe your issue" rows="3"></textarea>')
        
        # Social Icons
        content = content.replace('<span>📘</span>', '<span role="img" aria-label="Facebook">📘</span>')
        content = content.replace('<span>🐦</span>', '<span role="img" aria-label="Twitter">🐦</span>')
        content = content.replace('<span>📷</span>', '<span role="img" aria-label="Instagram">📷</span>')

        # Mobile Menu Button missing aria expanded
        if 'mobile-menu-toggle' in content and 'aria-expanded' not in content:
            content = content.replace('aria-label="Menu">', 'aria-label="Menu" aria-expanded="false">')
            changed = True
            
        # Add meta theme-color for PWA and better mobile display
        if 'theme-color' not in content:
            content = content.replace('</title>', '</title>\n    <meta name="theme-color" content="#0E1A2B">')
            changed = True

        if changed or ('aria-label="Your Name"' in content):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed a11y & perf on {os.path.basename(file_path)}")

if __name__ == '__main__':
    optimize_html('/Users/sumit/Downloads/debtCure')
