import numpy as np
import matplotlib.pyplot as plt
import pulp

staffing = pulp.LpProblem('Telephone_Staffing_Optimization', pulp.LpMinimize)

D = pulp.LpVariable('Daytime Workers', lowBound=0, upBound=20, cat='Integer')
E = pulp.LpVariable('Evening Workers', lowBound=0, upBound=20, cat='Integer')

staffing += 80 * D + 45 * E, 'Total Cost'

staffing += 96 * 0.15 * D + 30 * 0.20 * E >= 240, 'Wives'
staffing += 96 * 0.10 * D + 30 * 0.30 * E >= 180, 'Husbands'
staffing += 96 * 0.10 * D + 30 * 0.15 * E >= 210, 'Single Adult Males'
staffing += 96 * 0.10 * D + 30 * 0.20 * E >= 160, 'Single Adult Females'

staffing.solve()

optimal_D = pulp.value(D)
optimal_E = pulp.value(E)
optimal_cost = pulp.value(staffing.objective)

print(f'Optimal number of Daytime Hires: {optimal_D}')
print(f'Optimal number of Evening Hires: {optimal_E}')
print(f'Minimum cost: {optimal_cost}')

D_vals = np.linspace(0, 20, 500)
E_vals_wives = (240 - 96 * 0.15 * D_vals) / (30 * 0.20)
E_vals_husbands = (180 - 96 * 0.10 * D_vals) / (30 * 0.30)
E_vals_males = (210 - 96 * 0.10 * D_vals) / (30 * 0.15)
E_vals_females = (160 - 96 * 0.10 * D_vals) / (30 * 0.20)

plt.figure(figsize=(10, 7), dpi=300, facecolor='w', edgecolor='w', clear=True)

plt.plot(D_vals, np.minimum(E_vals_wives, 20), label='Wives', color='red')
plt.plot(D_vals, np.minimum(E_vals_husbands, 20), label='Husbands', color='green')
plt.plot(D_vals, np.minimum(E_vals_males, 20), label='Single Adult Males', color='blue')
plt.plot(D_vals, np.minimum(E_vals_females, 20), label='Single Adult Females', color='purple')
plt.axvline(x=20, color='black', linestyle='--')
plt.axhline(y=20, color='black', linestyle='--')

plt.fill_between(D_vals, 0, np.minimum(E_vals_wives, 20), where=(E_vals_wives >= 0), alpha=0.1, color='red')
plt.fill_between(D_vals, 0, np.minimum(E_vals_husbands, 20), where=(E_vals_husbands >= 0), alpha=0.1, color='green')
plt.fill_between(D_vals, 0, np.minimum(E_vals_males, 20), where=(E_vals_males >= 0), alpha=0.1, color='blue')
plt.fill_between(D_vals, 0, np.minimum(E_vals_females, 20), where=(E_vals_females >= 0), alpha=0.1, color='purple')

plt.xlim(0, 21)
plt.ylim(0, 21)

plt.xlabel('Daytime Workers (D)')
plt.ylabel('Evening Workers (E)')
plt.title('Telephone Staffing Problem')

plt.xticks(np.arange(0, 21, 2))
plt.yticks(np.arange(0, 21, 2))
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))
plt.grid(which='both', axis='both', linestyle='solid', linewidth=0.5)

plt.plot(optimal_D, optimal_E, 'ro', label=f'Optimal Solution (Daytime Hires = {optimal_D:.0f}, Evening Hires = {optimal_E:.0f})')

plt.grid(True)
plt.legend()
plt.savefig('Staffing.png')
plt.show()
