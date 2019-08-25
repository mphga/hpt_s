import yaml

# open the file first - read for load, write for dump
with open('save.yaml', 'r') as f:

	mydict = yaml.load(f)


# to load (read) use <var> = yaml.load(<openfileobject>)
# to dump (save) use yaml.dump(<existingdictname>, <openfileobject>)