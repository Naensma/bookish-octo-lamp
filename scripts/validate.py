import sys

def validate():
    print("Validating app...")
    with open('app/main.py') as f:
        code = f.read()
    if 'def' not in code:
        print("No functions found.")
        sys.exit(1)
    print("Validation complete.")

validate()
