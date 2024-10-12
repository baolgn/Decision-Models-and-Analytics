cost_coefficients = [
    30; 55; 35; 35;
    10; 35; 50; 25;
    35; 15; 40; 30
];

constraint_matrix = [
    1 0 0 0 1 0 0 0 1 0 0 0;
    0 1 0 0 0 1 0 0 0 1 0 0;
    0 0 1 0 0 0 1 0 0 0 1 0;
    0 0 0 1 0 0 0 1 0 0 0 1;
    1 1 1 1 0 0 0 0 0 0 0 0;
    0 0 0 0 1 1 1 1 0 0 0 0;
    0 0 0 0 0 0 0 0 1 1 1 1
];

constraint_rhs = [25; 35; 40; 20; 50; 20; 50];

lower_bounds = zeros(12, 1);

[optimal_solution, optimal_cost] = linprog(cost_coefficients, [], [], constraint_matrix, constraint_rhs, lower_bounds, []);

optimal_DN = optimal_solution(1);
optimal_DC = optimal_solution(2);
optimal_DO = optimal_solution(3);
optimal_DS = optimal_solution(4);
optimal_AN = optimal_solution(5);
optimal_AC = optimal_solution(6);
optimal_AO = optimal_solution(7);
optimal_AS = optimal_solution(8);
optimal_PN = optimal_solution(9);
optimal_PC = optimal_solution(10);
optimal_PO = optimal_solution(11);
optimal_PS = optimal_solution(12);

fprintf('Optimal Shipping Quantities of Dallas-Nashville: %.0f units\n', optimal_DN);
fprintf('Optimal Shipping Quantities of Dallas-Cleveland: %.0f units\n', optimal_DC);
fprintf('Optimal Shipping Quantities of Dallas-Omaha: %.0f units\n', optimal_DO);
fprintf('Optimal Shipping Quantities of Dallas-St. Louis: %.0f units\n', optimal_DS);

fprintf('Optimal Shipping Quantities of Atlanta-Nashville: %.0f units\n', optimal_AN);
fprintf('Optimal Shipping Quantities of Atlanta-Cleveland: %.0f units\n', optimal_AC);
fprintf('Optimal Shipping Quantities of Atlanta-Omaha: %.0f units\n', optimal_AO);
fprintf('Optimal Shipping Quantities of Atlanta-St. Louis: %.0f units\n', optimal_AS);

fprintf('Optimal Shipping Quantities of Pittsburgh-Nashville: %.0f units\n', optimal_PN);
fprintf('Optimal Shipping Quantities of Pittsburgh-Cleveland: %.0f units\n', optimal_PC);
fprintf('Optimal Shipping Quantities of Pittsburgh-Omaha: %.0f units\n', optimal_PO);
fprintf('Optimal Shipping Quantities of Pittsburgh-St. Louis: %.0f units\n', optimal_PS);

fprintf('\nMinimum cost: $%.2f\n', optimal_cost);