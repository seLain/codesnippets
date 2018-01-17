
#
# Smells
#
example = {} # {key:[], ...}
def add_element(k, v):
	if k in example.keys():
		example[k].append(v)
	else:
		example[k] = [v]

#
# Refactored
#
from collections import defaultdict
example = defaultdict(list)	# {key:[], ...}
def add_element(k, v):
	example[k].append(v)