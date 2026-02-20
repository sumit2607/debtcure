import os
import glob
import re

FAVICON_TAG = '<link rel="icon" href="favicon.svg" type="image/svg+xml">'

def add_favicon(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # Replace existing .ico favicon or inject new one
        if 'rel="icon"' in content and 'favicon.ico' in content:
            new_content = re.sub(r'<link[^>]*rel=["\']icon["\'][^>]*>', FAVICON_TAG, content)
            if new_content != content:
                content = new_content
                changed = True
        elif 'favicon.svg' not in content:
            # Inject just before </head>
            if '</head>' in content:
                content = content.replace('</head>', f'    {FAVICON_TAG}\n</head>')
                changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added favicon to {os.path.basename(file_path)}")

if __name__ == '__main__':
    add_favicon('/Users/sumit/Downloads/debtCure')
