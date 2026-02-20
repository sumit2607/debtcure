import os
import re
import glob

def optimize_html_files(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # Add loading="lazy" to all images that don't already have a loading attribute
        new_content = re.sub(r'<img\s+(?![^>]*\bloading\s*=)', r'<img loading="lazy" ', content)
        if new_content != content:
            content = new_content
            changed = True

        # Inject Firebase init module script just before closing body tag
        if 'firebase-init.js' not in content and '</body>' in content:
            content = content.replace('</body>', '    <script type="module" src="js/firebase-init.js"></script>\n</body>')
            changed = True

        # Inject Google Site Verification meta tag
        meta_tag = '<meta name="google-site-verification" content="04yGYdu6A6_jEy0ohwNoGZPe7XmgMEuFVFpmMNixd08" />'
        if meta_tag not in content and '</title>' in content:
            content = content.replace('</title>', '</title>\n    ' + meta_tag)
            changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Optimized {os.path.basename(file_path)}")

if __name__ == '__main__':
    optimize_html_files('/Users/sumit/Downloads/debtCure')
