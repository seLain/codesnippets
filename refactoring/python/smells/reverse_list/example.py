
#
# Smells
#
s = [1,2,3,4,5,6]
r = [s[i] for i in range(len(s)-1, -1, -1)]

#
# Refactored
#
r = s[::-1]

#
# explanation:
# notation "[a:b:c]" means "count in increments of c starting 
# at a inclusive, up to b exclusive". If c is negative you count 
# backwards, if omitted it is 1. If a is omitted then you start 
# as far as possible in the direction you're counting from (so 
# that's the start if c is positive and the end if negative). 
# If b is omitted then you end as far as possible in the direction 
# you're counting to (so that's the end if c is positive and the 
# start if negative). If a or b is negative it's an offset from 
# the end (-1 being the last character) instead of the start.