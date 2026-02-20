import os
import glob

def defer_scripts(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False
        if '<script src="js/app.js"></script>' in content:
            content = content.replace('<script src="js/app.js"></script>', '<script src="js/app.js" defer></script>')
            changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Deferred app.js in {os.path.basename(file_path)}")

if __name__ == '__main__':
    defer_scripts('/Users/sumit/Downloads/debtCure')
