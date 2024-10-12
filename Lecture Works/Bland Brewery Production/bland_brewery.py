import numpy as np
import matplotlib.pyplot as plt
import pulp

bland_brewery = pulp.LpProblem('Bland_Brewery', pulp.LpMaximize)

ale = pulp.LpVariable('Barrels of Ale', lowBound=0, cat='Integer')
beer = pulp.LpVariable('Barrels of Beer', lowBound=0, cat='Integer')

bland_brewery += 13 * ale + 23 * beer, 'Total Profit'

bland_brewery += 5 * ale + 15 * beer <= 480, 'Corn Capacity'
bland_brewery += 4 * ale + 4 * beer <= 160, 'Hops Capacity'
bland_brewery += 35 * ale + 20 * beer <= 1190, 'Malt Capacity'

bland_brewery.solve()

optimal_ale = pulp.value(ale)
optimal_beer = pulp.value(beer)
optimal_profit = pulp.value(bland_brewery.objective)

print(f'Optimal number of Ale barrels: {optimal_ale}')
print(f'Optimal number of Beer barrels: {optimal_beer}')
print(f'Maximum profit: {optimal_profit}')

corn_constraint_ale = np.linspace(0, 100, 500)
corn_constraint_beer = (480 - 5 * corn_constraint_ale) / 15
hops_constraint_ale = np.linspace(0, 100, 500)
hops_constraint_beer = (160 - 4 * hops_constraint_ale) / 4
malt_constraint_ale = np.linspace(0, 100, 500)
malt_constraint_beer = (1190 - 35 * malt_constraint_ale) / 20

plt.figure(figsize=(10, 7), dpi=300, facecolor='w', edgecolor='w', clear=True)

plt.plot(corn_constraint_ale, corn_constraint_beer, label='Corn', color='red')
plt.plot(hops_constraint_ale, hops_constraint_beer, label='Hops', color='yellow')
plt.plot(malt_constraint_ale, malt_constraint_beer, label='Malt', color='blue')

plt.fill_between(corn_constraint_ale, 0, corn_constraint_beer, where=(corn_constraint_beer >= 0), alpha=0.1, color='red')
plt.fill_between(hops_constraint_ale, 0, hops_constraint_beer, where=(hops_constraint_beer >= 0), alpha=0.1, color='yellow')
plt.fill_between(malt_constraint_ale, 0, malt_constraint_beer, where=(malt_constraint_beer >= 0), alpha=0.1, color='blue')

plt.xlim(0, 100)
plt.ylim(0, 60)

plt.xlabel('Barrels of Ale')
plt.ylabel('Barrels of Beer')
plt.title('Bland Brewery Production Possibility Frontier')

plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 61, 10))
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))
plt.grid(which='both', axis='both', linestyle='solid', linewidth=0.5)

plt.plot(optimal_ale, optimal_beer, 'ro', label=f'Optimal Solution (Ale = {optimal_ale:.0f}, Beer = {optimal_beer:.0f})')

plt.grid(True)
plt.legend()
plt.savefig('Bland Brewery.png')
plt.show()
