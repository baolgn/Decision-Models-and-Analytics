profit_coefficients = [-13; -23];  

constraint_matrix = [5 15; 4 4; 35 20];   
constraint_rhs = [480; 160; 1190];        

lower_bounds = [0; 0];

[optimal_solution, max_profit] = linprog(profit_coefficients, constraint_matrix, constraint_rhs, [], [], lower_bounds, []);

max_profit = -max_profit;

optimal_ale = optimal_solution(1);
optimal_beer = optimal_solution(2);

fprintf('Optimal number of Ale barrels: %.0f\n', optimal_ale);
fprintf('Optimal number of Beer barrels: %.0f\n', optimal_beer);
fprintf('Maximum profit: $%.2f\n', max_profit);

ale_barrels = linspace(0, 100, 500);  

corn_constraint_beer = (480 - 5 * ale_barrels) / 15;
hops_constraint_beer = (160 - 4 * ale_barrels) / 4;
malt_constraint_beer = (1190 - 35 * ale_barrels) / 20;

figure('Position', [100, 100, 800, 600], 'Color', 'w');
hold on;

plot(ale_barrels, corn_constraint_beer, 'r', 'LineWidth', 2, 'DisplayName', 'Corn Capacity');
plot(ale_barrels, hops_constraint_beer, 'y', 'LineWidth', 2, 'DisplayName', 'Hops Capacity');
plot(ale_barrels, malt_constraint_beer, 'b', 'LineWidth', 2, 'DisplayName', 'Malt Capacity');

feasible_beer = min([corn_constraint_beer; hops_constraint_beer; malt_constraint_beer]);

fill([ale_barrels, fliplr(ale_barrels)], [feasible_beer, zeros(1, 500)], 'g', 'FaceAlpha', 0.2, 'DisplayName', 'Feasible Region');

plot(optimal_ale, optimal_beer, 'r.', 'MarkerSize', 25, 'DisplayName', sprintf('Optimal Solution (Ale = %.0f, Beer = %.0f)', optimal_ale, optimal_beer));

xlabel('Barrels of Ale', 'FontSize', 12);
ylabel('Barrels of Beer', 'FontSize', 12);
title('Bland Brewery Production Possibility Frontier', 'FontSize', 14);

xlim([0 100]);
ylim([0 60]);

set(gca, 'XTick', 0:10:100, 'YTick', 0:10:60);
set(gca, 'XMinorTick', 'on', 'YMinorTick', 'on');
set(gca, 'XMinorGrid', 'on', 'YMinorGrid', 'on');

grid on;

legend('show', 'Location', 'Best');
hold off;
