names = ['Sam', 'Don', 'Daniel']

def hash_name(name):
    return hash(name)

hashed_names = list(map(hash_name, names))

print(hashed_names)