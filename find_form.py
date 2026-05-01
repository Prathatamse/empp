from bs4 import BeautifulSoup

with open(r'e:\New folder\website-export\index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

forms = soup.find_all('form')
with open('form_debug.txt', 'w', encoding='utf-8') as out:
    for i, form in enumerate(forms):
        out.write(f"Form {i}:\n")
        out.write(f"  Action: {form.get('action')}\n")
        out.write(f"  Method: {form.get('method')}\n")
        out.write("  Inputs:\n")
        for inp in form.find_all('input'):
            out.write(f"    - name={inp.get('name')} type={inp.get('type')}\n")
        for tb in form.find_all('textarea'):
            out.write(f"    - name={tb.get('name')}\n")
        for btn in form.find_all('button'):
            out.write(f"    - type={btn.get('type')}\n")
        out.write("-" * 20 + "\n")
