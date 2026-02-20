import os
import glob
import re

def update_files(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # update base URLs
        if 'debtcurein.online' in content:
            content = content.replace('https://debtcurein.online', 'https://www.debtcure.online')
            content = content.replace('https://www.debtcurein.online', 'https://www.debtcure.online')
            content = content.replace('debtcurein.online', 'www.debtcure.online')
            changed = True

        # replace remaining Unsplash URLs
        if 'unsplash.com' in content:
            # specifically the ones in Schema and Slider
            content = re.sub(r'https://images\.unsplash\.com/[^\s"]+', 'https://www.debtcure.online/assets/lawyer_1.png', content)
            changed = True

        # make sure og:image and twitter:image use the correct new absolute URL
        content = re.sub(r'(<meta property="?og:image"?\s*content=")[^"]+(")', r'\g<1>' + 'https://www.debtcure.online/assets/lawyer_1.png' + r'\g<2>', content)
        content = re.sub(r'(<meta name="?twitter:image"?\s*content=")[^"]+(")', r'\g<1>' + 'https://www.debtcure.online/assets/lawyer_1.png' + r'\g<2>', content)
        content = re.sub(r'(<meta property="?twitter:image"?\s*content=")[^"]+(")', r'\g<1>' + 'https://www.debtcure.online/assets/lawyer_1.png' + r'\g<2>', content)

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file_path)}")

if __name__ == '__main__':
    update_files('/Users/sumit/Downloads/debtCure')
