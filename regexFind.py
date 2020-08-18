import re

string = "This is a very important import you see here"

find = re.findall("import", string)

print(len(find))

for each in find:
    print(each)

for each in re.finditer("import", string):
    lookup = each.span()
    print(lookup)
print("----------------")

# Match
collection = "now, wow, how, mow, bow"
catch = re.findall("[nwhm]ow", collection)

for each in catch:
    print(each)
print("----------------")

 # Pattern
pattern = re.findall("[^a-i]ow", collection)

for each in pattern:
    print(each)
print("----------------")


# Replace
check = "My naam is Billa"
regex = re.compile("[n]aam")

replaced = regex.sub("name", check)
print(replaced)
print("----------------")

# Back slash problem
back = "This is a double \\slash"
print(re.search(r"\\slash", back))
print("----------------")

# Remove items
sentence = '''
Corona is
gonna be
around for
many more
years to come
unfortunately!!!
'''

trim = re.compile("\n")

newSentence = trim.sub(" ", sentence)
print(newSentence)
print("----------------")


check = "123 1234 12345 123456 1234567 12345678"

search = re.findall("\d{7,8}", check)

print("Matches found: " + str(len(search)))