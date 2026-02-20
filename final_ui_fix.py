import os
import glob

def fix_stuff(directory):
    # 1. Add missing layout classes to style.css
    css_path = os.path.join(directory, 'css', 'style.css')
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        
        layout_adds = """
/* Layout Helpers */
.justify-center { justify-content: center !important; }
.align-center { align-items: center !important; }
.flex-wrap { flex-wrap: wrap !important; }
.gap-20 { gap: 20px !important; }

@media (max-width: 768px) {
    .floating-whatsapp {
        width: 50px;
        height: 50px;
        bottom: 20px;
        right: 20px;
    }
    .hero-buttons {
        flex-direction: column;
        width: 100%;
    }
    .hero-buttons .btn {
        width: 100%;
    }
}
"""
        if '.justify-center' not in css:
            css += layout_adds
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css)
            print("Added layout helpers and mobile fixes to style.css")

    # 2. Convert any remaining btn-outline to btn-outline-white in hero sections
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Target buttons specifically in hero/header containers
        new_content = content.replace('class="btn btn-outline large"', 'class="btn btn-outline-white large"')
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed button visibility in {os.path.basename(file_path)}")

if __name__ == '__main__':
    fix_stuff('/Users/sumit/Downloads/debtCure')
