import os
import glob
import re

def upgrade_heros(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    # Button HTML to insert
    hero_buttons_html = """
            <div class="hero-buttons justify-center mt-20">
                <a href="#contact" class="btn btn-primary large">Get Free Legal Consultation</a>
                <a href="tel:+919076573857" class="btn btn-outline-white large">📞 Talk to Expert Now</a>
            </div>"""

    for file_path in html_files:
        if 'index.html' in file_path:
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # If it has a hero-subtitle but no hero-buttons, add them
        if '<p class="hero-subtitle">' in content and 'hero-buttons' not in content:
            content = content.replace('</p>', '</p>' + hero_buttons_html, 1)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added hero buttons to {os.path.basename(file_path)}")

    # Add mobile padding fix to CSS
    css_path = os.path.join(directory, 'css', 'style.css')
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        
        mobile_fix = """
/* Hero Mobile Spacing Fix */
@media (max-width: 768px) {
    .hero-section, .page-header {
        padding-bottom: 120px !important; /* Space for WhatsApp icon */
    }
    .hero-buttons {
        gap: 12px !important;
    }
}
"""
        if 'Hero Mobile Spacing Fix' not in css:
            css += mobile_fix
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css)
            print("Added mobile spacing fix to style.css")

if __name__ == '__main__':
    upgrade_heros('/Users/sumit/Downloads/debtCure')
