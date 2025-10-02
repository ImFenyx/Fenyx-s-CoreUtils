import sys

PROGRAM_NAME = "basename"

if len(sys.argv) != 2:
    print(f"Usage: {PROGRAM_NAME} <path>")
    sys.exit(1)
    
def remover_sufixo(name):
    name = name.split('.')[0]
    return name

def adicionar_sufixo(name):
    return f"{name}"

print(remover_sufixo(sys.argv[1]))
print(adicionar_sufixo(sys.argv[1]))
