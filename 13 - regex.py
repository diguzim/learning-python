import re

pattern = r"spam"
text = "eggspamsausagespam"

match = re.search(pattern, text)
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

# group

pattern = r"(\d+)-(\d+)-(\d+)"
text = "Today is 2018-04-28, whay a day!"

match = re.search(pattern, text)
if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.groups())

# replacing

text = "My name is David. Hi David."
pattern = r"David"

newtext = re.sub(pattern, "Rodrigo", text)
print(newtext)