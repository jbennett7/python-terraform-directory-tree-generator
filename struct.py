import sys, os

root_directory = sys.argv[1]
structure_file = sys.argv[2]
suffixes =  ['tf']

with open(structure_file) as f:
    items = f.read().splitlines()

for item in items:
    if item.split('.')[-1:][0] in suffixes:
        try:
            open(item, 'a').close()
        except Exception as e:
            print(str(e))
    if item[-1:] == '/':
        try:
            os.makedirs(root_directory + '/' + item)
        except OSError as e:
            if e.errno == 17:
                continue
            print(str(e))
        except Exception as e:
            print(str(e))
