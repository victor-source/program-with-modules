import re
def message(text):
    (input(text))
def title(text):
    print(f'======= {(text)} =========')
def extract_email(email):
    pattern = r'([\W\.-]+)@([\W\-]+)(\.[\W\.]+)'
    match = re.search(email, pattern)
    print(match)