# switcharoo
File mixer-upper

Put the files in `source`, and run `python ./switcharoo`.

# Features
* Takes input files and randomly changes their names, if two files have different extensions but the same name they will still be associated.
* If one extension is JSON, a catalog.json will be generated in the dest folder.

# Recatalog
* If user namkes changes to the ordering in the dest folder `python recatalog.py` can be used to regenerate the catalog. Note, this only works
  if filenames are numeric.