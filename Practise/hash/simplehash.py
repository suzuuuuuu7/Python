import json
import hashlib

filepath="E:\Python\Practise\index.py"

def calculate_hash(filepath):
    sha256=hashlib.sha256()
    return sha256.hexdigest()
    
hash_value = calculate_hash(filepath)
print(hash_value)