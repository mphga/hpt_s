import yaml

with open('save.yaml', 'r') as f:

	mydict = yaml.load(f)


print(mydict['k2'])