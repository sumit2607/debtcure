import os
import glob
import re

def update_og_images(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    new_image_url = "https://debtcurein.online/assets/lawyer_1.png"

    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # Replace og:image content
        orig_content = content
        content = re.sub(r'(<meta property="og:image"\s*content=")[^"]+(")', r'\g<1>' + new_image_url + r'\g<2>', content)
        content = re.sub(r'(<meta name="twitter:image"\s*content=")[^"]+(")', r'\g<1>' + new_image_url + r'\g<2>', content)
        content = re.sub(r'(<meta property="twitter:image"\s*content=")[^"]+(")', r'\g<1>' + new_image_url + r'\g<2>', content)

        if content != orig_content:
            changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated OG/Twitter image in {os.path.basename(file_path)}")

if __name__ == '__main__':
    update_og_images('/Users/sumit/Downloads/debtCure')
