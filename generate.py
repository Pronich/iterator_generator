import hashlib

def generate(filename):
    with open(filename, 'r') as f:
        data = f.read().split('\n')

    for line in data:
        yield hashlib.md5(line.encode()).hexdigest()
