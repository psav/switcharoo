import os
import json

files = os.listdir('dest')
exts = set()
filenames = set()
for item in files:
    if 'catalog' in item:
        continue
    filename, ext = os.path.splitext(item)
    if "." not in ext:
        continue
    exts.add(ext)
    filenames.add(filename)

print(filenames)
filenames = sorted(filenames, key=int)
print(filenames)

catalog = []

for i, name in enumerate(filenames):
    print(name)
    for ext in exts:
        if ext == ".json" and name != "catalog":
            with open('dest/' + name + ext) as f:
                data = json.load(f)
                catalog.append(data)

if len(catalog) != 0:
    with open('dest/catalog.json', "w") as f:
        json.dump(catalog, f)
