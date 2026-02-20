import os
import glob
import re

def update_js(directory):
    js_files = glob.glob(os.path.join(directory, 'js', '*.js'))
    for file_path in js_files:
        if 'app.js' in file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'document.getElementById(\'page-loader\')' not in content:
                loader_js = """
// Loader removal
window.addEventListener('load', () => {
    const loader = document.getElementById('page-loader');
    if (loader) {
        loader.style.opacity = '0';
        loader.style.visibility = 'hidden';
        setTimeout(() => {
            loader.style.display = 'none';
        }, 500); // Wait for transition
    }
});
"""             
                content += "\n" + loader_js
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added loader JS to {os.path.basename(file_path)}")

if __name__ == '__main__':
    update_js('/Users/sumit/Downloads/debtCure')
