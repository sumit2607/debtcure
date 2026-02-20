import os
import glob
import re

GTAG_SCRIPT = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-T1SSM5TR15"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-T1SSM5TR15');
    </script>
"""

def add_gtag(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'G-T1SSM5TR15' not in content and '<head>' in content:
            # Inject immediately after <head>
            content = content.replace('<head>', '<head>' + GTAG_SCRIPT, 1)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added gtag to {os.path.basename(file_path)}")

if __name__ == '__main__':
    add_gtag('/Users/sumit/Downloads/debtCure')
