import sys
import re

file = open(sys.argv[1], 'r')
text = file.read()

data = re.search('(.+)\n\n(.+)((?:\n.+:.+){2,})', text)

name, spell_type, header = data.groups()

out = open(sys.argv[1], 'w')

print = lambda x: out.write(x + "\n")

print(f"# {name}")
print("")
print("|||")
print('|---|---|')
print(f"|Тип|{spell_type}|")

for line in header.split('\n'):
    if not line:
        continue
    key, value = re.search('(.+):(.+)', line).groups()

    print(f'|{key}|{value}|')
print("")
print(text[data.span()[1]+1:].replace("-\n", "").replace("\n", " "))


out.close()
