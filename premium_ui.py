import os
import glob
import re

CSS_ROOT_REPLACEMENT = """:root {
    --primary-color: #0F172A; /* Deep Premium Navy */
    --primary-hover: #1E293B;
    --accent-color: #10B981; /* Premium Emerald */
    --accent-hover: #059669; 
    --white: #FFFFFF;
    --soft-white: #F8FAFC;
    --light-grey: #E2E8F0;
    --text-primary: #0F172A;
    --text-secondary: #475569;
    --text-muted: #94A3B8;
    --font-heading: 'Outfit', 'Poppins', sans-serif;
    --font-body: 'Inter', sans-serif;
    --card-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04);
    --card-hover-shadow: 0 20px 40px -5px rgba(16, 185, 129, 0.12), 0 10px 10px -5px rgba(15, 23, 42, 0.04);
    --btn-shadow: 0 6px 16px -2px rgba(16, 185, 129, 0.4);
}"""

CSS_BTN_REPLACEMENT = """.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 14px 28px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.05rem;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    border: 2px solid transparent;
    letter-spacing: 0.5px;
}

.btn-primary {
    background: linear-gradient(135deg, var(--accent-color), var(--accent-hover));
    color: var(--white);
    box-shadow: var(--btn-shadow);
}

.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(16, 185, 129, 0.5);
    background: linear-gradient(135deg, var(--accent-hover), var(--accent-color));
}

.btn-secondary {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-hover));
    color: var(--white);
    box-shadow: 0 6px 16px -2px rgba(15, 23, 42, 0.3);
}

.btn-secondary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.4);
}

.btn-outline {
    border-color: var(--primary-color);
    color: var(--primary-color);
    background: transparent;
}

.btn-outline:hover {
    background-color: var(--primary-color);
    color: var(--white);
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.2);
}"""

def upgrade_ui(directory):
    css_path = os.path.join(directory, 'css', 'style.css')
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()

        # Replace root variables
        css = re.sub(r':root\s*\{[^}]+\}', CSS_ROOT_REPLACEMENT, css, count=1)

        # Enhance headings
        css = re.sub(r'h1,\s*h2,\s*h3,\s*h4,\s*h5,\s*h6\s*\{([^}]+)\}', 
                     r'h1, h2, h3, h4, h5, h6 {\1 letter-spacing: -0.02em;}', css)

        # Replace button base styles
        btn_regex = r'\.btn\s*\{[^}]+\}\s*\.btn-primary\s*\{[^}]+\}\s*\.btn-primary:hover\s*\{[^}]+\}\s*\.btn-secondary\s*\{[^}]+\}\s*\.btn-secondary:hover\s*\{[^}]+\}\s*\.btn-outline\s*\{[^}]+\}\s*\.btn-outline:hover\s*\{[^}]+\}'
        
        # Simple string replacement for safety since regex matching CSS can fail if structured differently
        # We will instead replace specific class bodies individually
        
        btn_replacements = {
            r'\.btn\s*\{[^}]+\}': ".btn {\n    display: inline-flex;\n    align-items: center;\n    justify-content: center;\n    padding: 14px 28px;\n    border-radius: 50px;\n    font-weight: 600;\n    font-size: 1.05rem;\n    cursor: pointer;\n    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);\n    border: 2px solid transparent;\n    letter-spacing: 0.5px;\n}",
            r'\.btn-primary\s*\{[^}]+\}': ".btn-primary {\n    background: linear-gradient(135deg, var(--accent-color), var(--accent-hover));\n    color: var(--white);\n    box-shadow: var(--btn-shadow);\n}",
            r'\.btn-primary:hover\s*\{[^}]+\}': ".btn-primary:hover {\n    transform: translateY(-3px);\n    box-shadow: 0 10px 25px rgba(16, 185, 129, 0.5);\n    background: linear-gradient(135deg, var(--accent-hover), var(--accent-color));\n}",
            r'\.btn-outline\s*\{[^}]+\}': ".btn-outline {\n    border-color: var(--primary-color);\n    color: var(--primary-color);\n    background: transparent;\n}",
            r'\.btn-outline:hover\s*\{[^}]+\}': ".btn-outline:hover {\n    background-color: var(--primary-color);\n    color: var(--white);\n    transform: translateY(-3px);\n    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.2);\n}",
            r'\.btn-outline-white\s*\{[^}]+\}': ".btn-outline-white {\n    border-color: var(--white);\n    color: var(--white);\n    background: transparent;\n}",
            r'\.btn-outline-white:hover\s*\{[^}]+\}': ".btn-outline-white:hover {\n    background-color: var(--white);\n    color: var(--primary-color);\n    transform: translateY(-3px);\n    box-shadow: 0 10px 25px rgba(255, 255, 255, 0.3);\n}"
        }

        for pattern, replacement in btn_replacements.items():
            css = re.sub(pattern, replacement, css, count=1)

        # Enhance Service Cards
        css = re.sub(r'\.service-card\s*\{[^}]+\}', 
                     ".service-card {\n    background: rgba(255, 255, 255, 0.7);\n    backdrop-filter: blur(12px);\n    -webkit-backdrop-filter: blur(12px);\n    padding: 36px 32px;\n    border-radius: 20px;\n    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);\n    border: 1px solid rgba(255, 255, 255, 0.5);\n    box-shadow: var(--card-shadow);\n}", css)
                     
        # Testimonial Cards
        css = re.sub(r'\.testimonial-card\s*\{[^}]+\}', 
                     ".testimonial-card {\n    background: var(--white);\n    padding: 36px 32px;\n    border-radius: 20px;\n    box-shadow: var(--card-shadow);\n    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);\n    position: relative;\n    border: 1px solid var(--light-grey);\n}", css)

        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css)
        print("Premium injected into style.css")

    # Update HTML font links
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add Outfit font
        if 'Outfit' not in content:
            content = content.replace('family=Inter:', 'family=Outfit:wght@400;500;600;700;800&family=Inter:')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added premium font to {os.path.basename(file_path)}")

if __name__ == '__main__':
    upgrade_ui('/Users/sumit/Downloads/debtCure')
