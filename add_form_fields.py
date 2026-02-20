import os
import glob

def add_inputs(directory):
    html_files = glob.glob(os.path.join(directory, '*.html'))
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        target = '<input type="tel" placeholder="Phone Number" aria-label="Phone Number" required>'
        new_inputs = """
                    <input type="text" placeholder="Total Loan Outstanding (₹)" aria-label="Total Loan Outstanding" required>
                    <input type="text" placeholder="EMI Due From (Months/Date)" aria-label="EMI Due From" required>"""
        
        if target in content and 'Total Loan Outstanding' not in content:
            content = content.replace(target, target + new_inputs)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file_path)}")

if __name__ == '__main__':
    add_inputs('/Users/sumit/Downloads/debtCure')
