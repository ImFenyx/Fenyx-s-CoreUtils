import sys

if len(sys.argv) < 2:
    print("Usage: touch <file1> <file2> ...")
    sys.exit(1)

def touch(file_path):
    try:
        with open(file_path, 'a'):
            pass
    except Exception as e:
        print(f"Error touching file {file_path}: {e}")
        
        
for file in sys.argv[1:]:
    touch(file)
    