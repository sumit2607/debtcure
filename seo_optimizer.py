import os
import glob
import re
from datetime import datetime

BASE_URL = "https://www.debtcurein.online"

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(file_path)
    if filename == "index.html":
        url = f"{BASE_URL}/"
    else:
        url = f"{BASE_URL}/{filename}"

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "Stop Loan Recovery Harassment | DebtCure"
    
    # Extract description
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', content, re.IGNORECASE | re.DOTALL)
    desc = desc_match.group(1).strip() if desc_match else "Facing harassment from loan recovery agents? Get legal consultation and stop harassment legally."

    changed = False

    # 1. Canonical Tag
    canonical_tag = f'<link rel="canonical" href="{url}" />'
    if 'rel="canonical"' not in content:
        # insert after <head> or similar
        content = content.replace('</title>', f'</title>\n    {canonical_tag}')
        changed = True

    # 2. Open Graph Tags
    if 'property="og:title"' not in content:
        og_tags = f"""
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{BASE_URL}/images/og-image.jpg">
"""
        content = content.replace('</head>', f'{og_tags}\n</head>')
        changed = True

    # 3. Twitter Card Tags
    if 'name="twitter:card"' not in content:
        tw_tags = f"""
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="{url}">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{desc}">
    <meta property="twitter:image" content="{BASE_URL}/images/og-image.jpg">
"""
        content = content.replace('</head>', f'{tw_tags}\n</head>')
        changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated SEO tags in {filename}")

def generate_sitemap(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    sitemap_path = os.path.join(directory, 'sitemap.xml')
    
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename == "index.html":
            loc = f"{BASE_URL}/"
            priority = "1.0"
        else:
            loc = f"{BASE_URL}/{filename}"
            priority = "0.8"
            
        xml.append('  <url>')
        xml.append(f'    <loc>{loc}</loc>')
        xml.append(f'    <lastmod>{now}</lastmod>')
        xml.append(f'    <changefreq>weekly</changefreq>')
        xml.append(f'    <priority>{priority}</priority>')
        xml.append('  </url>')
        
    xml.append('</urlset>')
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(xml))
    print(f"Generated sitemap.xml with {len(html_files)} URLs")

if __name__ == '__main__':
    directory = '/Users/sumit/Downloads/debtCure'
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for f in html_files:
        process_file(f)
    generate_sitemap(directory)
