import os
import glob
import re

LOADER_HTML = """
    <!-- Full Screen Shimmer Loader -->
    <div id="page-loader" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background-color: #F8FAFC; z-index: 999999; display: flex; align-items: center; justify-content: center; flex-direction: column; transition: opacity 0.5s ease, visibility 0.5s ease;">
        <div class="loader-content" style="text-align: center;">
            <svg class="loader-icon pulse" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" width="60" height="60" style="animation: pulse-animation 1.5s infinite ease-in-out;">
                <path d="M12 22C12 22 20 18 20 12V5L12 2L4 5V12C4 18 12 22 12 22Z" fill="#10B981" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M9 12L11 14L15 10" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <div class="shimmer-text" style="margin-top: 15px; font-weight: 600; font-family: 'Poppins', sans-serif; color: #0E1A2B; font-size: 1.2rem; background: linear-gradient(90deg, #0E1A2B 0%, #94A3B8 50%, #0E1A2B 100%); background-size: 200% auto; color: transparent; -webkit-background-clip: text; background-clip: text; animation: shimmer 2s linear infinite;">Loading DebtCure...</div>
        </div>
        <style>
            @keyframes pulse-animation {
                0% { transform: scale(0.95); opacity: 0.8; }
                50% { transform: scale(1.05); opacity: 1; }
                100% { transform: scale(0.95); opacity: 0.8; }
            }
            @keyframes shimmer {
                to { background-position: 200% center; }
            }
        </style>
    </div>
"""

def add_loader(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        if '<div id="page-loader"' not in content and '<body' in content:
            # Inject immediately after the <body> tag
            content = re.sub(r'(<body[^>]*>)', r'\1\n' + LOADER_HTML, content, count=1)
            changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added loader to {os.path.basename(file_path)}")

if __name__ == '__main__':
    add_loader('/Users/sumit/Downloads/debtCure')
