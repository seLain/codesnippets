import sys, os, fnmatch, re
from collections import defaultdict

def find_dict_to_defaultdict(root_dir):
	# recursively visit
	result = defaultdict(list)
	for root, sub_folders, files in os.walk(root_dir):
		for filename in fnmatch.filter(files, '*.py'):
			fpath = os.path.join(root, filename)
			with open(fpath, 'r') as content:
				counter = 0
				for line in content:
					counter += 1
					if dict_init_matched(line):
						result[fpath].append(counter)
	return result

def dict_init_matched(code_line):
	p = re.compile('\w*\s*=\s*\w*{\w*}\w*')
	if p.match(code_line.strip()):
		return True
	return False


if __name__ == '__main__':
	if len(sys.argv) > 1:
		result = find_dict_to_defaultdict(sys.argv[1])
		for key in result.keys():
			print(str(key)+' : lines '+str(result[key]))