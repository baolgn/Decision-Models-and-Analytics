import numpy as np
import matplotlib.pyplot as plt
import pulp

# Problem Definition
trans = pulp.LpProblem('TransportCo_Distribution_Problem', pulp.LpMinimize)

# Decision Variables (Positive and Integer Constraints)
DN = pulp.LpVariable('Dallas–Nashville', lowBound=0, cat='Integer')
DC = pulp.LpVariable('Dallas–Cleveland', lowBound=0, cat='Integer')
DO = pulp.LpVariable('Dallas–Omaha', lowBound=0, cat='Integer')
DS = pulp.LpVariable('Dallas–St. Louis', lowBound=0, cat='Integer')
AN = pulp.LpVariable('Atlanta–Nashville', lowBound=0, cat='Integer')
AC = pulp.LpVariable('Atlanta–Cleveland', lowBound=0, cat='Integer')
AO = pulp.LpVariable('Atlanta–Omaha', lowBound=0, cat='Integer')
AS = pulp.LpVariable('Atlanta–St. Louis', lowBound=0, cat='Integer')
PN = pulp.LpVariable('Pittsburgh–Nashville', lowBound=0, cat='Integer')
PC = pulp.LpVariable('Pittsburgh–Cleveland', lowBound=0, cat='Integer')
PO = pulp.LpVariable('Pittsburgh–Omaha', lowBound=0, cat='Integer')
PS = pulp.LpVariable('Pittsburgh–St. Louis', lowBound=0, cat='Integer')

# Objective Function (Minimize)
trans += (
    30 * DN + 55 * DC + 35 * DO + 35 * DS +
    10 * AN + 35 * AC + 50 * AO + 25 * AS +
    35 * PN + 15 * PC + 40 * PO + 30 * PS
), 'Total Shipping Cost'

# Constraints
trans += DN + AN + PN == 25, 'Nashville Demand'
trans += DC + AC + PC == 35, 'Cleveland Demand'
trans += DO + AO + PO == 40, 'Omaha Demand'
trans += DS + AS + PS == 20, 'St. Louis Demand'

trans += DN + DC + DO + DS <= 50, 'Dallas Supply'
trans += AN + AC + AO + AS <= 20, 'Atlanta Supply'
trans += PN + PC + PO + PS <= 50, 'Pittsburgh Supply'

# Problem Solver
trans.solve()

# Optimal Solution
optimal_DN = pulp.value(DN)
optimal_DC = pulp.value(DC)
optimal_DO = pulp.value(DO)
optimal_DS = pulp.value(DS)
optimal_AN = pulp.value(AN)
optimal_AC = pulp.value(AC)
optimal_AO = pulp.value(AO)
optimal_AS = pulp.value(AS)
optimal_PN = pulp.value(PN)
optimal_PC = pulp.value(PC)
optimal_PO = pulp.value(PO)
optimal_PS = pulp.value(PS)
optimal_cost = pulp.value(trans.objective)

# Print Optimal Solution
print(f'Optimal Shipping Quantities of Dallas-Nashville: {optimal_DN:.0f} {'units' if optimal_DN != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Dallas-Cleveland: {optimal_DC:.0f} {'units' if optimal_DC != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Dallas-Omaha: {optimal_DO:.0f} {'units' if optimal_DO != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Dallas-St. Louis: {optimal_DS:.0f} {'units' if optimal_DS != 1 else 'unit'}')

print(f'Optimal Shipping Quantities of Atlanta-Nashville: {optimal_AN:.0f} {'units' if optimal_AN != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Atlanta-Cleveland: {optimal_AC:.0f} {'units' if optimal_AC != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Atlanta-Omaha: {optimal_AO:.0f} {'units' if optimal_AO != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Atlanta-St. Louis: {optimal_AS:.0f} {'units' if optimal_AS != 1 else 'unit'}')

print(f'Optimal Shipping Quantities of Pittsburgh-Nashville: {optimal_PN:.0f} {'units' if optimal_PN != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Pittsburgh-Cleveland: {optimal_PC:.0f} {'units' if optimal_PC != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Pittsburgh-Omaha: {optimal_PO:.0f} {'units' if optimal_PO != 1 else 'unit'}')
print(f'Optimal Shipping Quantities of Pittsburgh-St. Louis: {optimal_PS:.0f} {'units' if optimal_PS != 1 else 'unit'}')

print(f'\nMinimum cost: ${optimal_cost:.2f}')

# Charts Data
warehouses = np.array(['Dallas', 'Atlanta', 'Pittsburgh'])
cities = np.array(['Nashville', 'Cleveland', 'Omaha', 'St. Louis'])
shipping_to = np.array([
    [optimal_DN, optimal_DC, optimal_DO, optimal_DS],  # Dallas
    [optimal_AN, optimal_AC, optimal_AO, optimal_AS],  # Atlanta
    [optimal_PN, optimal_PC, optimal_PO, optimal_PS]   # Pittsburgh
])
shipping_from = shipping_to.T

city_requirements = [25, 35, 40, 20]
warehouse_capacities = [50, 20, 50]

# Stacked Bar Chart: Shipping to Cities
fig, ax = plt.subplots(figsize=(10, 7), dpi=300, facecolor='w', edgecolor='w', clear=True)
plt.ylim(0, 41)
plt.yticks(np.arange(0, 41, 5))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))
plt.grid(False)
plt.tick_params(axis='y', which='both', length=5)

bottom = np.zeros(len(cities))
for i, warehouse in enumerate(warehouses):
    ax.bar(cities, shipping_to[i], bottom=bottom, label=warehouse)
    bottom += shipping_to[i]

for i, constraint in enumerate(city_requirements):
    ax.hlines(constraint, xmin=i - 0.4, xmax=i + 0.4, colors='r', linestyles='dashed', color='green', label=f'Demand' if i == 0 else None)

ax.set_xlabel('Cities')
ax.set_ylabel('Units Shipped')
ax.set_title('Shipping Quantities to Cities')
ax.legend()

plt.grid(False)
plt.savefig('Trans 2.png')
plt.show()

# Stacked Bar Chart: Shipping from Warehouses
fig, ax = plt.subplots(figsize=(10, 7), dpi=300, facecolor='w', edgecolor='w', clear=True)
plt.ylim(0, 51)
plt.yticks(np.arange(0, 51, 5))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))
plt.tick_params(axis='y', which='both', length=5)

bottom = np.zeros(len(warehouses))
for i, city in enumerate(cities):
    ax.bar(warehouses, shipping_from[i], bottom=bottom, label=city)
    bottom += shipping_from[i]

for i, constraint in enumerate(warehouse_capacities):
    ax.hlines(constraint, xmin=i - 0.4, xmax=i + 0.4, colors='r', linestyles='dashed', color='red', label=f'Capacity' if i == 0 else None)

ax.set_xlabel('Warehouses')
ax.set_ylabel('Units Shipped')
ax.set_title('Shipping Quantities from Warehouses')
ax.legend()

plt.grid(False)
plt.savefig('Trans 1.png')
plt.show()
