import os
import glob
import re

def generate_html_sitemap(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    sitemap_path = os.path.join(directory, 'sitemap.html')
    
    links = []
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename in ['sitemap.html']: # Skip sitemap itself
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else filename
        
        # Simplify title
        title = title.split('|')[0].strip()
        
        links.append(f'                            <li><a href="{filename}">{title}</a></li>')

    links.sort()
    
    sitemap_content = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sitemap | DebtCure</title>
    <meta name="description" content="Complete sitemap and directory of all pages on the DebtCure website.">
    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
    <!-- Google Site Verification -->
    <meta name="google-site-verification" content="04yGYdu6A6_jEy0ohwNoGZPe7XmgMEuFVFpmMNixd08" />
</head>

<body>

    <!-- Header -->
    <header class="header" id="main-header">
        <div class="container header-container">
            <a href="index.html" class="logo" aria-label="DebtCure Home">
                <svg class="logo-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 22C12 22 20 18 20 12V5L12 2L4 5V12C4 18 12 22 12 22Z" fill="var(--primary-color)" stroke="var(--primary-color)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M9 12L11 14L15 10" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
                <div class="logo-text-wrapper">
                    <span class="logo-part-1">Debt</span><span class="logo-part-2">Cure</span>
                </div>
            </a>
            <nav class="nav">
                <ul class="nav-list">
                    <li><a href="index.html">Home</a></li>
                    <li class="dropdown">
                        <a href="services.html" class="dropbtn">Services ▾</a>
                        <div class="dropdown-content">
                            <a href="personal-loan-settlement.html">Personal Loan Settlement</a>
                            <a href="credit-card-loan-settlement.html">Credit Card Loan Settlement</a>
                            <a href="anti-harassment-service.html">Anti-Harassment Service</a>
                            <a href="credit-score-builder.html">Credit Score Builder</a>
                            <a href="education-loan-settlement.html">Education Loan Settlement</a>
                            <a href="additional-services.html">Additional Services</a>
                            <a href="loan-segregation.html">Loan Segregation</a>
                        </div>
                    </li>
                    <li><a href="your-rights.html">Your Rights</a></li>
                    <li><a href="steps.html">Steps</a></li>
                    <li><a href="stories.html">Stories</a></li>
                </ul>
            </nav>
            <div class="header-actions">
                <a href="index.html#contact" class="btn btn-primary small">Get Legal Help</a>
            </div>
            <button class="mobile-menu-toggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <!-- Page Header -->
    <section class="page-header" style="background: radial-gradient(circle at 50% 50%, #1a2e47 0%, var(--primary-color) 100%); padding: 120px 0 60px; color: white; text-align: center;">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb" style="margin-bottom: 20px; font-size: 0.9rem;">
                <a href="index.html" style="color: rgba(255,255,255,0.8); text-decoration: none;">Home</a>
                <span style="margin: 0 10px; color: rgba(255,255,255,0.5);">/</span>
                <span style="color: white;">Sitemap</span>
            </nav>
            <h1 class="hero-title" style="font-size: 2.5rem;">Sitemap</h1>
            <p class="hero-subtitle">Directory of all DebtCure pages.</p>
        </div>
    </section>

    <!-- Sitemap Content -->
    <section class="section">
        <div class="container">
            <div class="box p-30 bg-light" style="border-radius: 12px; box-shadow: var(--shadow-sm); max-width: 800px; margin: 0 auto;">
                <h2>All Pages</h2>
                <ul class="check-list mt-20" style="columns: 2; column-gap: 40px; list-style: circle !important; padding-left: 20px;">
""" + "\n".join(links) + """
                </ul>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h3 class="footer-logo">DebtCure</h3>
                    <p>Empowering you with legal protection against unfair loan recovery practices.</p>
                    <div class="social-icons">
                        <span>📘</span> <span>🐦</span> <span>📷</span>
                    </div>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="your-rights.html">Know Your Rights</a></li>
                        <li><a href="steps.html">Steps</a></li>
                        <li><a href="stories.html">Stories</a></li>
                        <li><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="sitemap.html">Sitemap</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact Us</h4>
                    <p>📧 debtcureindia@gmail.com</p>
                    <p>📍 Patiala House Court & Saket Court, New Delhi</p>
                    <p>📞 +91-9076573857</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 DebtCure. All Rights Reserved.</p>
                <p class="disclaimer">Disclaimer: This platform provides consultation and legal support. We are not a bank or NBFC.</p>
            </div>
        </div>
    </footer>
    <script type="module" src="js/firebase-init.js"></script>
    <script src="js/app.js"></script>
</body>
</html>"""

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print("Generated HTML Sitemap at sitemap.html")

def add_sitemap_to_footer(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '<li><a href="sitemap.html">Sitemap</a></li>' not in content and '<li><a href="privacy-policy.html">Privacy Policy</a></li>' in content:
            changed_content = content.replace('<li><a href="privacy-policy.html">Privacy Policy</a></li>', '<li><a href="privacy-policy.html">Privacy Policy</a></li>\n                        <li><a href="sitemap.html">Sitemap</a></li>')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(changed_content)
            print(f"Added sitemap link to {os.path.basename(file_path)}")

if __name__ == '__main__':
    directory = '/Users/sumit/Downloads/debtCure'
    generate_html_sitemap(directory)
    add_sitemap_to_footer(directory)
