class Solution:
    def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
        return -1
    start_station = 0
    tank_gas = 0
    for i in range(len(gas)):
        tank_gas += gas[i]-cost[i]
        if tank_gas < 0: # reset the start station
            tank_gas = 0
            start_station = i+1
    return start_station