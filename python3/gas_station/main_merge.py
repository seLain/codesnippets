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
            gas_income.append([i, gas[i]-cost[i]])

        # minimize and check route
        return  self.minimize_check(gas_income)

    def minimize_check(self, gas_income):
        

        # check length of merged stations when left length == 1 or 2
        if len(gas_income) == 2:
            if gas_income[0][1] + gas_income[1][1] < 0:
                return -1
            elif gas_income[0][1] >= gas_income[1][1]:
                return gas_income[0][0]
            else:
                return gas_income[1][0]
        elif len(gas_income) == 1:
            if gas_income[0][1] >= 0:
                return gas_income[0][0]
            else:
                return -1

        # merge continues + or -
        new_gas_income = [[gas_income[0][0], gas_income[0][1]]]
        for i in range(1, len(gas_income)):
            if gas_income[i][1] >= 0:
                if new_gas_income[-1][1] >= 0:
                    new_gas_income[-1][1] += gas_income[i][1]
                else:
                    new_gas_income.append([gas_income[i][0], gas_income[i][1]])
            else:
                if new_gas_income[-1][1] < 0:
                    new_gas_income[-1][1] += gas_income[i][1]
                else:
                    new_gas_income.append([gas_income[i][0], gas_income[i][1]])
                    
        # deal with last and first income cases: + + or - -
        if (new_gas_income[0][1] < 0 and new_gas_income[-1][1] < 0) or \
           (new_gas_income[0][1] >= 0 and new_gas_income[-1][1] >= 0):
            new_gas_income[-1][1] += new_gas_income[0][1]
            del new_gas_income[0]
        
        # merge +,- pair
        new_gas_income2 = []
        if len(new_gas_income) > 2:
            ## find fist not negative and reorganize the list
            for i in range(0, len(new_gas_income)):
                if new_gas_income[i][1] >= 0:
                    reordered = new_gas_income[i:] + new_gas_income[0:i]
                    new_gas_income = reordered
            ## regular merge
            for i in range(0, len(new_gas_income), 2):
                if i < len(new_gas_income)-1:
                    new_gas_income2.append([new_gas_income[i][0], 
                                            new_gas_income[i][1] + new_gas_income[i+1][1]])
                elif i == len(new_gas_income)-1:
                    new_gas_income2.append([new_gas_income[i][0], 
                                            new_gas_income[i][1]])
        else:
            new_gas_income2 = new_gas_income
        
        # next tier
        return self.minimize_check(new_gas_income2)