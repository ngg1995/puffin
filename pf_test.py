from app import *
from antlr4 import *

file = 'test.py'
language = 'Python3'
outfile = 'test.pf'


with open(file,'r') as f:
    file_text = InputStream(f.read())
    
out = generate_puffin_file(file_text,'Python3')
print(out)