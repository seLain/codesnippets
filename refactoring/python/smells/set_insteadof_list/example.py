import random
#
# Smells
#
data = []
for i in range(0, 100):
	x = random.randint(0, 10)
	if x not in data:
		data.append(x)

#
# Refactored
#
data = set()
for i in range(0, 100):
	data.add(random.randint(0, 10))