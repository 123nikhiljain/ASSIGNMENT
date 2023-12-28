#!/usr/bin/env python
# coding: utf-8

# In[1]:


def can_complete_circuit(gas, cost):
    total_gas = 0
    current_gas = 0
    start_station = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        # If the current gas becomes negative, start from the next station
        if current_gas < 0:
            start_station = i + 1
            current_gas = 0

    # If total gas is greater than or equal to 0, return the start station index
    if total_gas >= 0:
        return start_station % len(gas)
    else:
        return -1

# Example usage:
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
result = can_complete_circuit(gas, cost)
print("Starting gas station index:", result)


# In[ ]:




