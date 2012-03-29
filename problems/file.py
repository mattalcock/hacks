def simplereadfile(filepath):
    with open(filepath, 'r') as f:
        return [line.rstrip(os.linesep) for line in f]
		
string_list=simplereadfile('/Users/mattalcock/Dev/tests/small.in')
for s in string_list:
    print s