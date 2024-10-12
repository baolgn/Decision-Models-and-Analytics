cost_coefficients = [80; 45];  

constraint_matrix = [
    96 * 0.15, 30 * 0.20;  
    96 * 0.10, 30 * 0.30;  
    96 * 0.10, 30 * 0.15;  
    96 * 0.10, 30 * 0.20   
];   

constraint_rhs = [240; 180; 210; 160];        

lower_bounds = [0; 0]; 

upper_bounds = [20; 20]; 

[optimal_solution, optimal_cost] = linprog(cost_coefficients, -constraint_matrix, -constraint_rhs, [], [], lower_bounds, upper_bounds);

optimal_daytime = optimal_solution(1);
optimal_evening = optimal_solution(2);

fprintf('Optimal number of Daytime Hires: %.0f\n', optimal_daytime);
fprintf('Optimal number of Evening Hires: %.0f\n', optimal_evening);
fprintf('Minimum cost: $%.2f\n', optimal_cost);

daytime_workers = linspace(0, 20, 500);  

evening_workers_wives = (240 - 96 * 0.15 * daytime_workers) / (30 * 0.20);
evening_workers_husbands = (180 - 96 * 0.10 * daytime_workers) / (30 * 0.30);
evening_workers_males = (210 - 96 * 0.10 * daytime_workers) / (30 * 0.15);
evening_workers_females = (160 - 96 * 0.10 * daytime_workers) / (30 * 0.20);

figure('Position', [100, 100, 800, 600], 'Color', 'w');
hold on;

plot(daytime_workers, min(evening_workers_wives, 20), 'r', 'LineWidth', 2, 'DisplayName', 'Wives');
plot(daytime_workers, min(evening_workers_husbands, 20), 'g', 'LineWidth', 2, 'DisplayName', 'Husbands');
plot(daytime_workers, min(evening_workers_males, 20), 'b', 'LineWidth', 2, 'DisplayName', 'Single Adult Males');
plot(daytime_workers, min(evening_workers_females, 20), 'm', 'LineWidth', 2, 'DisplayName', 'Single Adult Females');

feasible_evening_workers = min([evening_workers_wives; evening_workers_husbands; evening_workers_males; evening_workers_females]);

fill([daytime_workers, fliplr(daytime_workers)], [min(evening_workers_wives, 20), zeros(1, 500)], 'r', 'FaceAlpha', 0.1, 'HandleVisibility', 'off');
fill([daytime_workers, fliplr(daytime_workers)], [min(evening_workers_husbands, 20), zeros(1, 500)], 'g', 'FaceAlpha', 0.1, 'HandleVisibility', 'off');
fill([daytime_workers, fliplr(daytime_workers)], [min(evening_workers_males, 20), zeros(1, 500)], 'b', 'FaceAlpha', 0.1, 'HandleVisibility', 'off');
fill([daytime_workers, fliplr(daytime_workers)], [min(evening_workers_females, 20), zeros(1, 500)], 'm', 'FaceAlpha', 0.1, 'HandleVisibility', 'off');

plot(optimal_daytime, optimal_evening, 'r.', 'MarkerSize', 25, 'DisplayName', sprintf('Optimal Solution (Daytime = %.0f, Evening = %.0f)', optimal_daytime, optimal_evening));

xlabel('Daytime Workers (D)', 'FontSize', 12);
ylabel('Evening Workers (E)', 'FontSize', 12);
title('Telephone Staffing Optimization', 'FontSize', 14);

xlim([0 20]);
ylim([0 20]);

set(gca, 'XTick', 0:2:20, 'YTick', 0:2:20);
set(gca, 'XMinorTick', 'on', 'YMinorTick', 'on');
set(gca, 'XMinorGrid', 'on', 'YMinorGrid', 'on');

grid on;

legend('show', 'Location', 'Best');
hold off;
