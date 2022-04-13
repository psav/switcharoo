import os
import random
import shutil
import json

files = os.listdir('source')
exts = set()
filenames = set()
for item in files:
    filename, ext = os.path.splitext(item)
    if "." not in ext:
        continue
    exts.add(ext)
    filenames.add(filename)

filenames_shuffle = list(filenames)
filenames_shuffle_dest = list(filenames)
random.shuffle(filenames_shuffle)
random.shuffle(filenames_shuffle_dest)

catalog = []

for i, name in enumerate(filenames_shuffle):
    print(name)
    for ext in exts:
        print("copy", 'source/' + name + ext, 'dest/' + filenames_shuffle_dest[i] + ext)
        shutil.copy('source/' + name + ext, 'dest/' + filenames_shuffle_dest[i] + ext)
        if ext == ".json":
            with open('source/' + name + ext) as f:
                data = json.load(f)
                catalog.append(data)

if len(catalog) != 0:
    with open('dest/catalog.json', "w") as f:
        json.dump(catalog, f)
