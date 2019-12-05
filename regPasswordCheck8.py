import re

pattern = re.compile(r'(^[a-zA-Z0-9_,+-]+@[a-zA-Z0-9_,+-]+\.[a-zA-Z0-9-.]+$)')
string = 'Glen'
pattern2=re.compile(r'[a-zA-Z0-9$%#@]{8,}\d')
password = 'hdklklk9jhgjklbhj8'

a=pattern.search(string)
check=pattern2.fullmatch(password)
print(check)