class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) != len(cost):
            return -1

        if len(gas) == 0:
            return -1
        elif len(gas) == 1 and gas[0] < cost[0]:
            return -1
        elif len(gas) == 1 and gas[0] >= cost[0]:
            return 0

        # calculate gas income from i to i+1 station
        gas_income = []
        for i in range(0, len(gas)):
            gas_income.append(gas[i]-cost[i])

        # try each station
        for i in range(0, len(gas)):
            new_income = gas_income[i:] + gas_income[0:i]
            tank_gas = 0
            success = True
            for j in range(0, len(new_income)):
                tank_gas += new_income[j]
                if tank_gas < 0:
                    success = False
                    break # fail
            if success is True:
                return i

        return -1   # if there is no station that works

